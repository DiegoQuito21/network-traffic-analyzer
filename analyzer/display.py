from rich import print as rprint

def display_packet(parsed):
    protocol = parsed["protocol"]
    src = parsed["src"]
    dst = parsed["dst"]
    sport = parsed["sport"]
    dport = parsed["dport"]

    if protocol == "TCP":
        rprint(f"[green][TCP] {src}:{sport}→ {dst}:{dport}[/green]")

    elif protocol == "UDP":
        rprint(f"[yellow][UDP] {src}:{sport}→ {dst}:{dport}[/yellow] ")

    elif protocol == "ICMP":
       rprint(f"[blue][ICMP] {src} → {dst}[/blue]")

    else:
        rprint(f"[dim][OTHER][/dim]")

    
    
