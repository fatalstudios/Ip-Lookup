import socket
import time
import sys

ascii_art = r""""
$$$$$$\ $$$$$$$\         $$$$$$\   $$$$$$\   $$$$$$\  $$\   $$\ $$\   $$\ $$$$$$$$\ $$$$$$$\  
\_$$  _|$$  __$$\       $$  __$$\ $$  __$$\ $$  __$$\ $$$\  $$ |$$$\  $$ |$$  _____|$$  __$$\ 
  $$ |  $$ |  $$ |      $$ /  \__|$$ /  \__|$$ /  $$ |$$$$\ $$ |$$$$\ $$ |$$ |      $$ |  $$ |
  $$ |  $$$$$$$  |      \$$$$$$\  $$ |      $$$$$$$$ |$$ $$\$$ |$$ $$\$$ |$$$$$\    $$$$$$$  |
  $$ |  $$  ____/        \____$$\ $$ |      $$  __$$ |$$ \$$$$ |$$ \$$$$ |$$  __|   $$  __$$< 
  $$ |  $$ |            $$\   $$ |$$ |  $$\ $$ |  $$ |$$ |\$$$ |$$ |\$$$ |$$ |      $$ |  $$ |
$$$$$$\ $$ |            \$$$$$$  |\$$$$$$  |$$ |  $$ |$$ | \$$ |$$ | \$$ |$$$$$$$$\ $$ |  $$ |
\______|\__|             \______/  \______/ \__|  \__|\__|  \__|\__|  \__|\________|\__|  \__|
"""

def slow_print(text, delay=0.05):
    for line in text.splitlines():
        print(line)
        time.sleep(delay)

def scan_ports(target, start_port=1, end_port=1024):
    print(f"\nScanning {target} for open ports from {start_port} to {end_port}...\n")
    open_ports = []
    
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)  # Timeout for the connection attempt
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port}: OPEN")
            open_ports.append(port)
        sock.close()
    
    if not open_ports:
        print("No open ports found.")
    else:
        print(f"\nOpen ports: {open_ports}")

if __name__ == "__main__":
    slow_print(ascii_art, delay=0.1)
    target_ip = input("\nEnter target IP or hostname: ")
    scan_ports(target_ip)
