# ⚡ Terminal-Overdrive (`ovrd`)

`Terminal-Overdrive` is a lightweight, zero-dependency, ultra-powerful command-line utility belt engineered to bypass standard OS abstractions and unlock direct power-user capabilities on **Windows** and **macOS**. 

Written entirely in native Python, it wraps complex system-level execution strings, asynchronous probing routines, and diagnostic tools into a single, unified, easy-to-trigger CLI engine.

---

## 🚀 Superpowers (Core Module Index)

| Command Component | Target System Matrix | Threat Level / Impact | Description |
| :--- | :---: | :---: | :--- |
| `sysinfo` | Windows / macOS | 🟢 Low | Exposes low-level hardware profiles, terminal geometry matrix, and build telemetry without menu navigation. |
| `netstat` | Windows / macOS | 🟡 Medium | Instantly tracks what processes are quietly listening on local network sockets, or isolates specific ports instantly. |
| `portscan` | Cross-Platform | 🟡 Medium | Launches a low-latency socket crawler to audit target endpoints and uncover exposed entry pathways. |
| `purge` | Windows / macOS | 🔴 High | Completely bypasses the operating system's safety bins to obliterate locked directories or files directly from physical blocks. |
| `kill` | Windows / macOS | 🔴 High | Executes an unyielding tree termination payload against sticky apps using partial matching strings or explicit PIDs. |
| `dnsflush` | Windows / macOS | 🟢 Low | Nukes local network resolver lookup registries and forces real-time propagation sweeps. |

---

## 🛠️ Installation & Activation

Since `ovrd` relies strictly on native Python APIs, installation requires zero third-party pip dependencies.

### 1. Save the Engine Blueprint
Download or create a script file named `overdrive.py` containing the core execution code.

### 2. Grant POSIX Execution Access (macOS / Linux Only)
Before driving the engine inside Unix terminals, authorize shell mapping rights:
```bash
chmod +x overdrive.py
```

### 3. Establish a System-Wide Alias Shortcut (Optional)
To invoke god-mode actions instantly from anywhere inside your file system architecture:

*   **macOS (`~/.zshrc` or `~/.bash_profile`):**
    ```bash
    alias ovrd="python3 /absolute/path/to/overdrive.py"
    ```
*   **Windows PowerShell (`$PROFILE`):**
    ```powershell
    Set-Alias -Name ovrd -Value "C:\Absolute\Path\To\overdrive.py"
    ```

---

## 📖 Tactical Usage Guide

Run the base help utility to display the interactive capabilities parameter guide:
```bash
python3 overdrive.py --help
```

### ⚡ 1. Deep System Diagnostics Check
Expose hardware parameters, environment geometry data, and runtime profiles instantly.
```bash
python3 overdrive.py sysinfo
```

### 📡 2. Socket Tracking & Port Interception
Find out exactly what malicious application or hidden local daemon is currently hijacking Port `8080` right now.
```bash
python3 overdrive.py netstat --port 8080
```

### 🔍 3. Asynchronous Multi-Threaded Port Scanner
Map out network endpoints or localized microservices to check for vulnerable ingress pathways.
```bash
python3 overdrive.py portscan 192.168.1.1 --start 20 --end 443
```

### 💀 4. Aggressive Process Tree Annihilation
Bypass Windows Task Manager restrictions or stubborn macOS application hangs. Provide either a partial string name or an exact Process Identification ID.
```bash
python3 overdrive.py kill chrome
python3 overdrive.py kill 4821
```

### ☣️ 5. Forced File System Erasure
Shred an locked node directory tree or unyielding system lockouts completely, directly bypassing garbage collection cycles.
```bash
python3 overdrive.py purge ./corrupted_cache_folder/
```

### 🌐 6. Instant Network DNS Flush
Instantly rebuild and clean messy caching tables when modern network redirects or development endpoints fail to resolve properly.
```bash
python3 overdrive.py dnsflush
```

---

## ⚠️ Safety Protocols & Disclaimer

**CRITICAL WARNING:** This suite contains industrial-grade manipulation routines (`purge`, `kill`). Executing operations with elevated admin credentials (`sudo` / `Run as Administrator`) grants the utility unmitigated physical execution capabilities. The creators hold zero accountability for accidental production data deletion, crashed application workflows, or hardware disruption. **Verify your variables before executing commands.**

---
Distributed via the **MIT License**. Build, modify, and optimize responsibly.
