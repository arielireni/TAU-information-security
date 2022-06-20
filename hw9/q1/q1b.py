import time
import os
from scapy.all import *


WINDOW = 60
MAX_ATTEMPTS = 15


# Initialize your data structures here
# TODO: Initialize your data structures
syn_records = dict()

blocked = set()  # We keep blocked IPs in this set


def on_packet(packet):
    """This function will be called for each packet.

    Use this function to analyze how many packets were sent from the sender
    during the last window, and if needed, call the 'block(ip)' function to
    block the sender.

    Notes:
    1. You must call block(ip) to do the blocking.
    2. The number of SYN packets is checked in a sliding window.
    3. Your implementation should be able to efficiently handle multiple IPs.
    """
    # If there is no TCP\IP layer
    try:
        if packet[TCP].flags == 'S':
            ip = packet[IP].src
            if ip in syn_records:
                curr_packets = syn_records[ip]
                curr_packets.append(packet)

                # clean previous packets if needed
                while packet.time - curr_packets[0].time > WINDOW:
                    curr_packets.pop(0)
            
                if len(curr_packets) > MAX_ATTEMPTS:
                    block(ip)
                    syn_records.pop(ip)
                else:
                    syn_records[ip] = curr_packets
            else:
                syn_records[ip] = list(packet)
    except:
        return

def generate_block_command(ip: str) -> str:
    """Generate a command that when executed in the shell, blocks this IP.

    The blocking will be based on `iptables` and must drop all incoming traffic
    from the specified IP."""
    # pass ip as source using -s flag
    command = "sudo iptables -A INPUT -s %s -j DROP" % (ip)
    return command

def block(ip):
    # WARNING: DO NOT MODIFY THIS FUNCTION!
    os.system(generate_block_command(ip))
    blocked.add(ip)


def is_blocked(ip):
    # WARNING: DO NOT MODIFY THIS FUNCTION!
    return ip in blocked


def main():
    # WARNING: DO NOT MODIFY THIS FUNCTION!
    sniff(prn=on_packet)


if __name__ == '__main__':
    main()
