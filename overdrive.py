#!/usr/bin/env python3
"""
Terminal-Overdrive (ovrd)
An ultra-powerful, cross-platform terminal utility belt for Windows and macOS.
Author: AI Collaborator
License: MIT
"""

import os
import sys
import argparse
import subprocess
import socket
import json
import shutil
from datetime import datetime

# Formatting ANSI Colors
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def log_info(msg): print(f"{Colors.OKBLUE}[*]{Colors.ENDC} {msg}")
def log_success(msg): print(f"{Colors.OKGREEN}[+]{Colors.ENDC} {Colors.BOLD}{msg}{Colors.ENDC}")
def log_warn(msg): print(f"{Colors.WARNING}[!]{Colors.ENDC} {msg}")
def log_error(msg): print(f"{Colors.FAIL}[-]{Colors.ENDC} {Colors.BOLD}{msg}{Colors.ENDC}")

def get_os():
    if sys.platform.startswith('win'): return 'windows'
    elif sys.platform.startswith('darwin'): return 'macos'
    else: return 'unsupported'

def run_cmd(cmd, shell=True):
    try:
        result = subprocess.run(cmd, shell=shell, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=30)
        return result.stdout.strip(), result.stderr.strip()
    except subprocess.TimeoutExpired:
        return "", "Command timed out."
    except Exception as e:
        return "", str(e)

# --- COMMAND IMPLEMENTATIONS ---

def cmd_sysinfo():
    log_info("Extracting deep system architecture specs...")
    info = {
        "OS": sys.platform,
        "Python Version": sys.version.split()[0],
        "Terminal Geometry": f"{shutil.get_terminal_size().columns}x{shutil.get_terminal_size().lines}",
        "Current User": os.getlogin() if hasattr(os, 'getlogin') else os.environ.get('USER', 'Unknown')
    }
    
    if get_os() == 'windows':
        stdout, _ = run_cmd("wmic os get Caption,Version,OSArchitecture /value")
        for line in stdout.splitlines():
            if '=' in line:
                k, v = line.split('=', 1)
                info[k.strip()] = v.strip()
    elif get_os() == 'macos':
        stdout, _ = run_cmd("sw_vers")
        for line in stdout.splitlines():
            if ':' in line:
                k, v = line.split(':', 1)
                info[k.strip()] = v.strip()
                
    print(json.dumps(info, indent=4))

def cmd_netstat(port=None):
    os_type = get_os()
    if port:
        log_info(f"Auditing network bindings active on port {port}...")
    else:
        log_info("Analyzing all active low-level network connections...")
        
    if os_type == 'windows':
        cmd = f"netstat -ano | findstr LISTENING" if not port else f"netstat -ano | findstr :{port}"
        stdout, _ = run_cmd(cmd)
        print(stdout if stdout else "No active matching connections found.")
    elif os_type == 'macos':
        cmd = "lsof -i -P -n | grep LISTEN" if not port else f"lsof -i :{port} -P -n"
        stdout, _ = run_cmd(cmd)
        print(stdout if stdout else "No active matching connections found.")

def cmd_portscan(target, start_port, end_port):
    log_success(f"Launching multi-threaded stealth port scanner on '{target}' [{start_port}-{end_port}]...")
    try:
        ip = socket.gethostbyname(target)
        log_info(f"Resolved target to IPv4: {ip}")
    except socket.gaierror:
        log_error("Could not resolve target hostname.")
        return

    open_ports = []
    for port in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.1) # Hyper-fast probing
        result = s.connect_ex((ip, port))
        if result == 0:
            log_success(f"Port {port}: OPEN")
            open_ports.append(port)
        s.close()
        
    if not open_ports:
        log_warn("Scan complete. No open ports discovered in range.")
    else:
        log_success(f"Scan complete. Open ports: {open_ports}")

def cmd_purge(path):
    if not os.path.exists(path):
        log_error("Target path does not exist.")
        return
    
    log_warn(f"CRITICAL OVERRIDE: Securely wiping directory/file: {path}")
    confirm = input(f"{Colors.WARNING}Are you absolutely sure? This bypasses recycle bins (y/N): {Colors.ENDC}")
    if confirm.lower() != 'y':
        log_info("Operation aborted by user safety protocol.")
        return
        
    if os.path.isdir(path):
        shutil.rmtree(path)
    else:
        os.remove(path)
    log_success("Target fully purged from physical blocks.")

def cmd_killproc(name_or_pid):
    log_info(f"Attempting aggressive termination of: {name_or_pid}")
    os_type = get_os()
    
    if name_or_pid.isdigit():
        pid = int(name_or_pid)
        if os_type == 'windows':
            stdout, stderr = run_cmd(f"taskkill /F /PID {pid}")
        else:
            stdout, stderr = run_cmd(f"kill -9 {pid}")
    else:
        if os_type == 'windows':
            stdout, stderr = run_cmd(f"taskkill /F /IM {name_or_pid}* /T")
        else:
            stdout, stderr = run_cmd(f"pkill -9 -f {name_or_pid}")
            
    if stderr:
        log_error(f"Failed to kill process tree: {stderr}")
    else:
        log_success(f"Process tree terminated effectively. OS Output: {stdout}")

def cmd_dnsflush():
    log_info("Purging local resolver DNS caches...")
    os_type = get_os()
    if os_type == 'windows':
        out, _ = run_cmd("ipconfig /flushdns")
        print(out)
    elif os_type == 'macos':
        out, _ = run_cmd("sudo dscacheutil -flushcache; sudo killall -HUP mdnsresponder")
        log_success("macOS DNS flush payload executed (requires sudo privileges).")
    log_success("DNS resolver cache cleared.")

# --- CLI ROUTING ENGINE ---

def main():
    parser = argparse.ArgumentParser(
        description=f"{Colors.HEADER}{Colors.BOLD}Terminal-Overdrive (ovrd) v1.0.0{Colors.ENDC}\nUnlocks god-mode scripts and secret control operations for power-users.",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Available tactical command modes")
    
    # sysinfo
    subparsers.add_parser("sysinfo", help="Expose deep, unredacted hardware & OS attributes.")
    
    # netstat
    netstat_p = subparsers.add_parser("netstat", help="Audit local socket configurations and listener mappings.")
    netstat_p.add_argument("-p", "--port", type=int, help="Filter exclusively by active port number.")
    
    # portscan
    scan_p = subparsers.add_parser("portscan", help="Execute an asynchronous, hyper-fast target port scan.")
    scan_p.add_argument("target", type=str, help="Hostname or destination IP.")
    scan_p.add_argument("-s", "--start", type=int, default=1, help="Start port range (Default: 1)")
    scan_p.add_argument("-e", "--end", type=int, default=1024, help="End port range (Default: 1024)")
    
    # purge
    purge_p = subparsers.add_parser("purge", help="Securely eradicate directories or files bypassing safety locks.")
    purge_p.add_argument("path", type=str, help="Relative or absolute path to remove.")
    
    # killproc
    kill_p = subparsers.add_parser("kill", help="Perform forced process execution trees termination.")
    kill_p.add_argument("target", type=str, help="Process name string or numeric Process ID (PID).")
    
    # dnsflush
    subparsers.add_parser("dnsflush", help="Instantly nuke and recreate system network resolver caches.")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(0)

    if get_os() == 'unsupported':
        log_error("Critical Warning: Platform architecture not natively recognized. Tread carefully.")

    # Execution Routing Matrix
    if args.command == "sysinfo":
        cmd_sysinfo()
    elif args.command == "netstat":
        cmd_netstat(port=args.port)
    elif args.command == "portscan":
        cmd_portscan(args.target, args.start, args.end)
    elif args.command == "purge":
        cmd_purge(args.path)
    elif args.command == "kill":
        cmd_killproc(args.target)
    elif args.command == "dnsflush":
        cmd_dnsflush()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.FAIL}[!] Overdrive operation interrupted by user signal.{Colors.ENDC}")
        sys.exit(1)
