# network-traffic-analyzer
A dual-implementation network traffic analyzer built in **Python** and **C++**. Both versions capture packets at the kernel level, parse protocol headers (Ethernet, IP, TCP, UDP, ICMP), and display real-time statistics in the terminal.
Built as a hands-on cybersecurity project to explore low-level networking, packet dissection, and systems programming.

## Implementations

| | Python | C++ |
|---|---|---|
| **Stack** | Python 3 · Scapy · Rich · Matplotlib | C++20 · libpcap · FTXUI |
| **Display** | Live terminal via Rich | Interactive TUI via FTXUI |
| **Threading** | Producer-consumer model | Mutex-protected stats engine |
| **Filters** | BPF filter builder | BPF via libpcap |
| **Export** | Matplotlib chart export | 

## Features

- Live packet capture on any network interface
- Protocol breakdown — TCP, UDP, ICMP, and more
- Top source/destination IP tracking
- Bytes and packet rate statistics
- BPF filter support for targeted capture
- Chart export for post-session analysis (Python)
- Interactive TUI with real-time updates (C++)

## Requirements

Both implementations require **root** or `CAP_NET_RAW` capability for raw packet access.

### Python
- Python 3.10+
- Scapy
- Rich
- Matplotlib

### C++
- C++20 compiler
- libpcap
- FTXUI
- CMake + just

## Status
🚧 In progress — Python implementation first, C++ coming soon.

## Project Structure
```
network-traffic-analyzer/
├── python/
│   ├── main.py
│   ├── capture.py
│   ├── parser.py
│   ├── stats.py
│   └── display.py
├── cpp/
│   ├── src/
│   ├── CMakeLists.txt
│   └── install.sh
└── README.md
```

## Learning Goals

- Kernel-level packet capture with libpcap and Scapy
- Manual protocol header parsing from raw bytes
- Multithreaded producer-consumer architecture
- Real-time terminal UI rendering
- BPF (Berkeley Packet Filter) usage

