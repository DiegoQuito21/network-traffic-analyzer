from rich import print as rprint
from rich.console import Console
from .parser import counts
import json


console = Console()


def display_packet(parsed):
    protocol = parsed["protocol"]
    src = parsed["src"]
    dst = parsed["dst"]
    sport = parsed["sport"]
    dport = parsed["dport"]

    if protocol == "TCP":
        rprint(f"[green][TCP] {src}:{sport} → {dst}:{dport}[/green]")

    elif protocol == "UDP":
        rprint(f"[yellow][UDP] {src}:{sport} → {dst}:{dport}[/yellow]")

    elif protocol == "ICMP":
        rprint(f"[blue][ICMP] {src} → {dst}[/blue]")

    else:
        rprint(f"[dim][OTHER][/dim]")


def display_summary():
    total = sum(counts.values())

    if total == 0:
        rprint("No packets captured")
        return

    console.rule("Capture Summary")
    rprint(f"  Total packets: {total}")

    for protocol, count in counts.items():
        pct = (count / total) * 100
        rprint(f"  {protocol}: {count} ({pct:.1f}%)")

    console.rule()

def export_json():
    total = sum(counts.values())

    data = { 
        "total_packets": total, 
        "summary": counts 
    }
    with open ("capture_results.json", "w") as f:
        json.dump(data, f , indent = 4)
    rprint("[green]Results saved to captured_results.json[/green]")


              
              
        

    
    
        

        

    

