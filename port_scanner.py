import socket
import threading
import queue
from colorama import init, Fore
import sys

init()

GREEN = Fore.GREEN
RESET = Fore.RESET
GRAY = Fore.LIGHTBLACK_EX

N_THREADS = 200

port_queue = queue.Queue()
print_lock = threading.Lock()

port_services = {
    20: "FTP Data Transfer",
    21: "FTP Control",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    5432: "PostgreSQL",
    6379: "Redis",
    # We can add more 
}

open_ports_found = False

def port_scan(host, port):
    """Scan a port on the specified host."""
    global open_ports_found
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)  # Set timeout
        
        result = s.connect_ex((host, port))
        
        if result == 0:
            service = port_services.get(port, "Unknown Service")
            with print_lock:
                print("[+] {}:{} is open - {}".format(host, port, service))
                open_ports_found = True  # Mark that an open port was found
        
    except Exception as e:
        with print_lock:
            print("[!] Error scanning {}:{} - {}".format(host, port, e))
    finally:
        s.close()

def scan_thread(host):
    """Thread worker function to scan ports."""
    while True:
        port = port_queue.get()
        port_scan(host, port)
        port_queue.task_done()

def main():
    if len(sys.argv) != 3:
        print("Usage: python advanced_port_scanner.py <IP> <Port Range>")
        sys.exit(1)

    target_ip = sys.argv[1]
    port_range = sys.argv[2].split('-')
    
    start_port = int(port_range[0])
    end_port = int(port_range[1])

    print("Scanning target: {}".format(target_ip))
    print("Scanning ports from {} to {}".format(start_port, end_port))

    for _ in range(N_THREADS):
        t = threading.Thread(target=scan_thread, args=(target_ip,))
        t.daemon = True  
        t.start()

    for port in range(start_port, end_port + 1):
        port_queue.put(port)

    port_queue.join()

    if not open_ports_found:
        print("[-] No open ports found on {}".format(target_ip))

if __name__ == "__main__":
    main()