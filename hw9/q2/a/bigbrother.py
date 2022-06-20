from scapy.all import *


LOVE = 'love'
unpersons = set()


def spy(packet):
    """Check for love packets.

    For each packet containing the word 'love', add the sender's IP to the
    `unpersons` set.

    Notes:
    1. Use the global LOVE as declared above.
    """
    # TODO: IMPLEMENT THIS FUNCTION
    try:
        packet_content = packet[Raw].load.decode('latin-1')
        if LOVE in packet_content:
            sender = packet[IP].src
            unpersons.add(sender)
    except:
        return

def main():
    # WARNING: DO NOT MODIFY THIS FUNCTION!
    sniff(iface=get_if_list(), prn=spy)


if __name__ == '__main__':
    main()
