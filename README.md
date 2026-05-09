# Python Deep Packet Inspection (DPI) Engine

## Overview
This project is a lightweight, efficient **Deep Packet Inspection (DPI)** tool written entirely in Python. It is designed to act as a network traffic filter. It reads a network packet capture (`.pcap`), deeply inspects the raw payload of every TCP/IP packet, identifies specific blocked keywords (like `youtube` or `netflix`), and drops the offending traffic.

All safe, unflagged traffic is automatically saved into a clean `output.pcap` file, which can be analyzed safely in tools like Wireshark.

## How it Works
Unlike a standard firewall that only looks at IP addresses or ports (Layer 3/4), this DPI engine looks at the **Application Layer (Layer 7)**.

1. **Traffic Generation**: The included `generate_test_pcap.py` script generates realistic dummy traffic, including HTTP, DNS, and TLS Server Name Indication (SNI) handshakes mimicking browsing to YouTube, Netflix, Google, Amazon, etc.
2. **Deep Inspection**: `main.py` uses the `scapy` library to iterate through every packet. It decodes the raw binary payload to a UTF-8 string and performs a case-insensitive search for blocked keywords.
3. **Filtering**: If a keyword match is found, the connection is flagged and dropped.
4. **Clean Output**: Packets that pass the inspection are securely written to `output.pcap`.

## File Structure
- `main.py`: The core DPI engine that reads, filters, and writes network packets.
- `generate_test_pcap.py`: Generates the sample `test_dpi.pcap` file with simulated traffic.
- `requirements.txt`: Python dependencies (Scapy).
- `run.bat`: A convenient Windows batch script to automate installation, generation, and analysis.

## Prerequisites
- Python 3.8+ installed on your system.
- Ensure Python is added to your system `PATH`.

## Setup and Execution

### Option 1: One-Click Execution (Windows)
Simply double-click the `run.bat` script. This will automatically:
1. Install Scapy.
2. Generate fresh network traffic.
3. Run the DPI analyzer and output the results.

### Option 2: Manual Execution
Open your terminal and run the following commands:
```bash
# Install dependencies
pip install -r requirements.txt

# Generate the test traffic
python generate_test_pcap.py

# Run the DPI filter
python main.py
```

## Verifying the Output
After running the script, you will see a new `output.pcap` file in the directory. You can open this file using [Wireshark](https://www.wireshark.org/). If you analyze the packets, you will notice that all traces of the blocked keywords have been entirely removed from the network trace!

## Author
Developed by CHARANKUMAR NALLAVENI
