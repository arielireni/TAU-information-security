from scapy.all import *


def on_packet(packet):
    """Implement this to send a SYN ACK packet for every SYN.

    Notes:
    1. Use *ONLY* the `send` function from scapy to send the packet!
    """
    # If there is no TCP\IP layer
    try:
        if packet[TCP].flags == 'S':
            tcp = packet[TCP]
            ip = packet[IP]
            sa_packet = IP(dst=ip.src)/TCP(flags='SA', sport=tcp.dport, dport=tcp.sport, seq=tcp.ack, ack=tcp.seq+1)
            # send the SA packet
            send(sa_packet)

    except:
        return

def main(argv):
    # WARNING: DO NOT MODIFY THIS FUNCTION!
    sniff(prn=on_packet)


if __name__ == '__main__':
    # WARNING: DO NOT MODIFY THIS FUNCTION!
    import sys
    sys.exit(main(sys.argv))
