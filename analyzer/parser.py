from scapy.all import IP, TCP, UDP, ICMP

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

    return result 
