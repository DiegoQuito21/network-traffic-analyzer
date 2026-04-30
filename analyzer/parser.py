from scapy.all import IP, TCP, UDP, ICMP
from rich import print as rprint


port_scan_tracker = {}
PORT_SCAN_THRESHOLD = 10 

counts = {
    "TCP": 0,
    "UDP": 0,
    "ICMP": 0,
    "OTHER": 0
    }



def parse_packet(packet):
    result = {
        "protocol": "OTHER",
        "src" : "unknown",
        "dst" : "unknown",
        "sport" : None,
        "dport" : None,
        "info": ""
    }

    if IP in packet:
        result["src"] = packet[IP].src
        result["dst"] = packet[IP].dst
    
    if TCP in packet:
        result["protocol"] = "TCP"
        result["sport"] = packet[TCP].sport
        result["dport"] = packet[TCP].dport

    if UDP in packet:
        result["protocol"] = "UDP"
        result["sport"] = packet[UDP].sport
        result["dport"] = packet [UDP].dport
    
    if ICMP in packet:
        result["protocol"] = "ICMP"
        result["sport"] = None
        result["dport"] =None 

    counts[result["protocol"]] += 1
    if result["src"] != "unknown" and result["dport"] is not None:
        src = result["src"]
        dport = result["dport"]

    
    
        if src not in port_scan_tracker:
            port_scan_tracker[src] = set()
        port_scan_tracker[src].add(dport)

        if len(port_scan_tracker[src]) > PORT_SCAN_THRESHOLD:
            rprint(f"[red][WARNING] Possible port scan detected from {src}![/red]")
    return result 



    