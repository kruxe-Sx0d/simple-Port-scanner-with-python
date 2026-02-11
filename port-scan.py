import pyfiglet
import socket
import sys
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed

BANNER = pyfiglet.figlet_format("PORT SCANNER")
print(BANNER)

if len(sys.argv) != 2:
    print("Usage: python3 scanner.py <target>")
    sys.exit(1)

target = socket.gethostbyname(sys.argv[1])

print("-" * 60)
print(f"Target: {target}")
print(f"Start Time: {datetime.now()}")
print("-" * 60)

open_ports = []

def scan_port(port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            result = s.connect_ex((target, port))
            if result == 0:
                return port
    except:
        pass
    return None

try:
    with ThreadPoolExecutor(max_workers=200) as executor:
        futures = [executor.submit(scan_port, port) for port in range(1, 65535)]
        
        for f in as_completed(futures):
            port = f.result()
            if port:
                print(f"[+] Port {port} is OPEN")
                open_ports.append(port)

except KeyboardInterrupt:
    print("\nScan aborted by user.")
    sys.exit()

except socket.gaierror:
    print("Invalid hostname.")
    sys.exit()

except socket.error:
    print("Connection error.")
    sys.exit()

print("-" * 60)
print("Scan complete.")
if open_ports:
    print("Open Ports:")
    for p in open_ports:
        print(f" - {p}")
else:
    print("No open ports found.")
print("-" * 60)
