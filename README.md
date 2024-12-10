# IP Port Scanner
## Overview
The IP Port Scanner is a tool designed to scan and identify open ports on a given IP address or range of IP addresses. This scanner helps to detect the availability of network services on a target system by checking the status of various ports commonly used by protocols such as HTTP, FTP, SSH, and more. It's a valuable utility for network administrators, security professionals, and anyone interested in assessing network security.

## Features
Scan a Single IP or IP Range: Allows scanning of individual IP addresses or a range of IPs.
Port Selection: Supports scanning specific ports or a range of ports to identify open services.
Fast and Efficient: Performs the scan quickly and provides results with minimal delay.
Customizable: Easily modify parameters like timeouts, port ranges, and scanning methods.
Simple Output: Displays clear results showing open, closed, and filtered ports for each target.
## Installation
Clone the repository:

>```git clone https://github.com/evolexinc/ip-port-scanner.git```<br/>

Install dependencies (if any):

bash
Copy code
pip install -r requirements.txt
Run the script:

bash
Copy code
```>python3 port_scanner.py --target <IP_ADDRESS> --ports <PORT_RANGE>```
Usage
To scan a single IP address for open ports:

bash
Copy code
>```python port_scanner.py --target 192.168.1.1```
To scan a specific range of ports:

bash
Copy code
>```python port_scanner.py --target 192.168.1.1 --ports 80-100```
Contributing
Feel free to fork the repository, submit issues, or create pull requests. All contributions are welcome!

Feel free to adjust the script name (port_scanner.py) and other details based on your project.
