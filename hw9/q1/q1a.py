from scapy.all import *
from typing import List, Iterable


OPEN = 'open'
CLOSED = 'closed'
FILTERED = 'filtered'


def generate_syn_packets(ip: str, ports: List[int]) -> list:
    """
    Returns a list of TCP SYN packets, to perform a SYN scan on the given
    TCP ports.

    Notes:
    1. Do NOT add any calls of your own to send/receive packets.
    """
    packets = []
    for port in ports:
        packet = IP(dst=ip)/TCP(dport=port, flags='S', seq=1)
        packets.append(packet)
    return packets


def analyze_scan(ip: str, ports: List[int], answered: Iterable, unanswered: Iterable) -> dict:
    """Analyze the results from `sr` of SYN packets.

    This function returns a dictionary from port number (int), to
    'open' / 'closed' / 'filtered' (strings), based on the answered and unanswered
    packets returned from `sr`.

    Notes:
    1. Use the globals OPEN / CLOSED / FILTERED as declared above.
    """
    results = dict()
    for res in answered:
        packet_tcp = (res[1])[TCP]
        if packet_tcp.flags == 'SA':
            results[packet_tcp.sport] = OPEN
        elif packet_tcp.flags == 'RA':
            results[packet_tcp.sport] = CLOSED
    
    for res in unanswered:
        packet_tcp = res[TCP]
        results[packet_tcp.dport] = FILTERED

    return results

def stealth_syn_scan(ip: str, ports: List[int], timeout: int):
    # WARNING: DO NOT MODIFY THIS FUNCTION!
    packets = generate_syn_packets(ip, ports)
    answered, unanswered = sr(packets, timeout=timeout)
    return analyze_scan(ip, ports, answered, unanswered)


def main(argv):
    # WARNING: DO NOT MODIFY THIS FUNCTION!
    if not 3 <= len(argv) <= 4:
        print('USAGE: %s <ip> <ports> [timeout]' % argv[0])
        return 1
    ip = argv[1]
    ports = [int(port) for port in argv[2].split(',')]
    if len(argv) == 4:
        timeout = int(argv[3])
    else:
        timeout = 5
    results = stealth_syn_scan(ip, ports, timeout)
    for port, result in results.items():
        print('port %d is %s' % (port, result))


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
