# Port Scanner

A fast and lightweight Python-based port scanner that checks all ports (1–65535) on a target host.  
Built with multithreading for high performance and designed for security testing and research purposes only.

## Features

- Scans all ports on a target (1–65535)
- Multithreaded for significantly faster scan times
- Clean and readable output
- Error handling for common network issues
- ASCII banner using `pyfiglet`

## Usage

### 1. Install Dependencies

```bash
pip install pyfiglet
```
### 2. Run the Scanner
```bash
python3 scanner.py <target>
```

#### Example:
```bash
python3 scanner.py example.com
```

### 3. Sample Output
```bash
PORT SCANNER (ASCII ART)

------------------------------------------------------------
Target: 93.184.216.34
Start Time: 2026-02-11 12:00:00
------------------------------------------------------------
[+] Port 80 is OPEN
[+] Port 443 is OPEN
...
------------------------------------------------------------
Scan complete.
Open Ports:
 - 80
 - 443
------------------------------------------------------------
```
### Code Overview
- Uses *ThreadPoolExecutor* for concurrent port scanning

- Automatically resolves domain names to IPv4 addresses

- Gracefully handles timeouts, invalid hosts, and user interruptions

### Disclaimer

This tool is intended only for educational purposes and authorized security testing.
Do not scan systems without explicit permission. The author is not responsible for any misuse.

### License

This project is released under the MIT License.