from scapy.all import rdpcap, wrpcap, IP, TCP, Raw

def analyze_pcap(pcap_file):
    try:
        print(f"Reading {pcap_file}...")
        packets = rdpcap(pcap_file)
        print(f"Loaded {len(packets)} packets from {pcap_file}")
    except FileNotFoundError:
        print(f"Error: File '{pcap_file}' not found.")
        return
    except Exception as e:
         print(f"Error reading pcap: {e}")
         return

    match_count = 0
    forwarded_packets = []
    
    for pkt in packets:
        is_blocked = False
        # Check for IP and TCP layers
        if IP in pkt and TCP in pkt:
            # Check if there is a Raw payload
            if Raw in pkt:
                try:
                    # Extract the raw payload
                    payload = pkt[Raw].load.decode('utf-8', errors='ignore')
                    
                    # Perform simple DPI: look for specific keywords
                    payload_lower = payload.lower()
                    if 'youtube' in payload_lower or 'netflix' in payload_lower:
                        is_blocked = True
                        src_ip = pkt[IP].src
                        dst_ip = pkt[IP].dst
                        src_port = pkt[TCP].sport
                        dst_port = pkt[TCP].dport
                        
                        print("-" * 40)
                        print(f"Match found in packet! Blocking...")
                        print(f"Source: {src_ip}:{src_port} -> Destination: {dst_ip}:{dst_port}")
                        
                        if 'youtube' in payload_lower:
                            print("Keyword: YouTube")
                        if 'netflix' in payload_lower:
                            print("Keyword: Netflix")
                        match_count += 1
                except Exception:
                    # Handle any parsing errors gracefully
                    pass
        
        if not is_blocked:
            forwarded_packets.append(pkt)
    
    print("-" * 40)
    print(f"Analysis complete. Blocked {match_count} packets.")
    
    output_filename = "output.pcap"
    print(f"Writing {len(forwarded_packets)} forwarded packets to {output_filename}...")
    wrpcap(output_filename, forwarded_packets)
    print("Done.")

if __name__ == "__main__":
    pcap_filename = "test_dpi.pcap"
    analyze_pcap(pcap_filename)
