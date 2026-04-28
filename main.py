import argparse
from analyzer import start_capture

parser = argparse.ArgumentParser(description="Network Traffic Analyzer")
parser.add_argument("--filter", type = str, help= "Filter by protocol TCP, UDP , ICMP")
args = parser.parse_args()

if __name__ =="__main__":
    start_capture(filter_protocol = args.filter)
    


    
