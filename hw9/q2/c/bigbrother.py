import math
from scapy.all import *


LOVE = 'love'
unpersons = set()


def spy(packet):
    """Check for love packets and encrypted packets.

    For each packet containing the word 'love', or a packed which is encrypted,
    add the sender's IP to the `unpersons` set.

    Notes:
    1. Use the global LOVE as declared above.
    """
    # same as done in part (a)
    try:
        packet_content = packet[Raw].load.decode('latin-1')
        # calculate entropy
        entropy_val = shannon_entropy(packet_content)
        if LOVE in packet_content or entropy_val > 3.0:
            sender = packet[IP].src
            unpersons.add(sender)
    except:
        return


def shannon_entropy(string: str) -> float:
    # WARNING: DO NOT MODIFY THIS FUNCTION!
    distribution = [float(string.count(c)) / len(string)
                    for c in set(string)]
    return -sum(p * math.log(p) / math.log(2.0) for p in distribution)


def main():
    # WARNING: DO NOT MODIFY THIS FUNCTION!
    sniff(iface=get_if_list(), prn=spy)


if __name__ == '__main__':
    main()
