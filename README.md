# Network Traffic Analyzer

A real-time network packet capture and analysis tool built in Python. 
Captures live traffic at the network level, parses protocol headers, 
detects suspicious activity, and exports results for further analysis.

Built as a hands-on cybersecurity project to explore low-level networking, 
packet dissection, and threat detection.

## Features

- Live packet capture at the network interface level
- Protocol parsing — TCP, UDP, ICMP, and other traffic
- Color-coded real-time terminal display
- Protocol filter flag for targeted capture
- Port scan detection with configurable threshold
- Capture summary with protocol breakdown and percentages
- JSON export of capture results

## Tech Stack

- Python 3
- Scapy — packet capture and parsing
- Rich — color-coded terminal output
- argparse — CLI flag handling

## Requirements

- Python 3.10+
- Root or sudo privileges (required for raw packet access)
- macOS or Linux

## Installation

```bash
git clone https://github.com/DiegoQuito21/network-traffic-analyzer
cd network-traffic-analyzer
pip3 install -r requirements.txt
```

## Usage

Capture 1000 packets (default):
```bash
sudo python3 main.py
```

Filter by protocol:
```bash
sudo python3 main.py --filter TCP
sudo python3 main.py --filter UDP
sudo python3 main.py --filter ICMP
```

## Output

Live terminal output with color coding:
- Green — TCP
- Yellow — UDP  
- Blue — ICMP
- Dim — Other

Capture summary printed after session ends.
Results exported to `capture_results.json`.

## Port Scan Detection

The analyzer tracks unique destination ports per source IP.
If a single IP hits more than 10 different ports, a warning is triggered:
[WARNING] Possible port scan detected from 192.168.1.x!
The threshold is configurable in `analyzer/parser.py`.

## Project Structure
network-traffic-analyzer/
│
├── main.py
├── requirements.txt
│
└── analyzer/
├── init.py
├── capture.py
├── parser.py
└── display.py

## Learning Goals

- Network packet capture with Scapy
- Protocol header parsing — Ethernet, IP, TCP, UDP, ICMP
- Modular Python architecture
- Real-time terminal UI with Rich
- Basic threat detection logic

- ## Motivation

I built this project to deepen my understanding of how network 
traffic works at a low level. Coming from a cybersecurity focus, 
I wanted to see firsthand how tools like Wireshark detect and 
classify packets, and build my own version from scratch.
