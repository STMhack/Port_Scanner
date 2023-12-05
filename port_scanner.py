import socket
import threading
import os


def scan_port(host, port):
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Set a timeout for the connection attempt
        sock.settimeout(1)
        
        # Attempt to connect to the target host and port
        sock.connect((host, port))
        
        # Print if the connection was successful
        print('\033[1m')
        print(f"\n\033[31mPort \033[32m{port}\033[31m is open\033[32m ✓")
        
    except socket.error:
        pass  # Port is closed, do nothing
    finally:
        # Close the socket
        sock.close()

def port_scanner(host, ports):
    # Create a list to store threads
    threads = []

    # Create threads for each port scan
    for port in ports:
        thread = threading.Thread(target=scan_port, args=(host, port))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    # Specify the target host and range of ports to scan
    print('\033[1m')
    os.system('pyfiglet Port Scanner | lolcat')
    print('\n')
    print('\033[1m\033[36m~'*70)
    print('\n')
    
    target_host=input('\033[1m\033[31m[\033[33m+\033[31m]\033[32m Enter Target Host: \033[33m')
    print('\n')
    target_ports = range(0, 50000)  # Scan ports 1 to 1024
    # Perform the port scan
    port_scanner(target_host, target_ports)
    print('\n')
    print('\033[1m\033[36m~'*70)
