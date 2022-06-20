import scapy.all as S
import urllib.parse as urlparse
from typing import Tuple

WEBSITE = 'infosec.cs.tau.ac.il'


def parse_packet(packet) -> Tuple[str]:
    """
    If the given packet is a login request to the course website, return the
    username and password as a tuple => ('123456789', 'opensesame'). Otherwise,
    return None.

    Notes:
    1. You can assume the entire HTTP request fits within one packet, and that
       both the username and password are non-empty for login requests (if any
       of the above assumptions fails, it's OK if you don't extract the
       user/password - but you must still NOT crash).
    2. Filter the course website using the `WEBSITE` constant from above. DO NOT
       use the server IP for the filtering (as our domain may point to different
       IPs later and your code should be reliable).
    3. Make sure you return a tuple, not a list.
    """
    # NOTE: I used this resource as a reference: https://stackoverflow.com/questions/39090366/how-to-parse-raw-http-request-in-python-3

    # get the raw data if exists and split by lines
    try:
        packet_lst = packet[S.Raw].load.decode('latin-1').split('\r\n')
    except:
        return

    password, username = '',''
    for i in range(1, len(packet_lst)):
        # try to split current data by ':'
        if i < len(packet_lst)-1:
            try:
                curr_data = packet_lst[i].split(':')
                # verify course website
                if curr_data[0] == 'Host' and curr_data[1].find(WEBSITE) == -1:
                    return
            except:
                if packet_lst[i] != '':
                    return

        # last value in the list, should contain usename & password
        else:
            curr_data = packet_lst[i].split('&')
            # loop over these values
            for j in range(len(curr_data)):
                try:
                    values = curr_data[j].split('=')
                    # use urlparse for the data to include all characters
                    if values[0] == 'username':
                        username = urlparse.unquote(values[1])
                    elif values[0] == 'password':
                        password = urlparse.unquote(values[1])
                except:
                    return

    return password, username
                        


def packet_filter(packet) -> bool:
    """
    Filter to keep only HTTP traffic (port 80) from any HTTP client to any
    HTTP server (not just the course website). This function should return
    `True` for packets that match the above rule, and `False` for all other
    packets.

    Notes:
    1. We are only keeping HTTP, while dropping HTTPS
    2. Traffic from the server back to the client should not be kept
    """
    try:
        return packet[S.TCP].dport == 80
    except:
        return False


def main(args):
    # WARNING: DO NOT EDIT THIS FUNCTION!
    if '--help' in args:
        print('Usage: %s [<path/to/recording.pcapng>]' % args[0])

    elif len(args) < 2:
        # Sniff packets and apply our logic.
        S.sniff(lfilter=packet_filter, prn=parse_packet)

    else:
        # Else read the packets from a file and apply the same logic.
        for packet in S.rdpcap(args[1]):
            if packet_filter(packet):
                print(parse_packet(packet))


if __name__ == '__main__':
    import sys
    main(sys.argv)
