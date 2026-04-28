from scapy.all import sniff 
from .parser import parse_packet 
from .display import display_packet , display_summary

def start_capture(packet_count = 1000):
    def handle_packet(packet):
        parsed = parse_packet(packet)
        display_packet(parsed)
    
    print(f"packet capture starting")
    sniff(count = packet_count , store = False , prn = handle_packet)
    display_summary()
   


 