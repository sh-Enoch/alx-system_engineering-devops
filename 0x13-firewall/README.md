Network Security Toolkit - Firewall
This project provides a user-space, stateful firewall for Linux operating systems.

Description
This stateful firewall allows you to define rules that control incoming and outgoing network traffic based on various criteria, including source and destination IP addresses, ports, and protocols. It monitors active connections and allows or denies packets based on established rules. The firewall also logs information about blocked traffic for monitoring purposes.

Features
Stateful Packet Filtering: Tracks connections and allows/denies packets based on established rules and connection state.
Rule Management: Create, edit, and delete rules to control traffic flow.
Protocol Support: Supports common protocols like TCP, UDP, and ICMP.
IP/Port Filtering: Define rules based on source and destination IP addresses and ports.
Logging: Logs information about blocked packets for analysis.
Command-Line Interface (CLI): Manage the firewall through a user-friendly CLI.
Dependencies
libnetfilter_queue: Required for packet filtering capabilities.
libcap: Optional, provides additional capabilities for advanced users (requires root privileges).
Installation:

Ensure you have the required dependencies installed (libnetfilter_queue). Refer to your distribution's package manager for installation instructions.
Clone this repository: git clone https://your-repo-link.git
Compile the project: make
To run the firewall (requires root privileges): sudo ./firewall
Note: Running the firewall with root privileges allows it to modify system rules. Exercise caution and understand the implications before running the program.

Usage
Rule Management:

Rules are defined in a text file (firewall.rules).
Each rule specifies a direction (inbound/outbound), protocol, source and destination IP addresses (optional), source and destination ports (optional), and an action (ALLOW/DENY).
See firewall.rules for an example format.
Logging:

The firewall logs information about blocked packets to firewall.log.
The log file contains details like timestamps, source/destination IP addresses, ports, protocols, and the reason for blocking.
Examples:

Allow all traffic on port 80 (HTTP):
ALLOW TCP any any *:80
Deny all SSH traffic from a specific IP address:
DENY TCP 192.168.1.10 any 22:22
