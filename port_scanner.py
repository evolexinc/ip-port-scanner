''' Use It for Education Purpose only 
copyright 2024 Evolex Inc. '''
import socket

def scan_port(ip, port):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.settimeout(1)
	result = sock.connect_ex((ip, port))
	sock.close()
	return result == 0
target_ip =input("Enter IP Address:")
for port in range(1, 1025):
	if scan_port(target_ip, port):
		print(f"https://{target_ip}:{port} is open")

