import socket
from scapy.all import *

SRC_PORT = 65000

bits = list()

def receive_message(port: int) -> str:
    """Receive *hidden* messages on the given TCP port.

    As Winston sends messages encoded over the TCP metadata, re-implement this
    function so to be able to receive the messages correctly.

    Notes:
    1. Use `SRC_PORT` as part of your implementation.
    """
    # sniff packets
    sniff(prn=parse_packet, stop_filter=(lambda x: len(bits) == x[TCP].ack), iface=get_if_list())

    # decrypt the data
    data_bits = ""
    for i in range(len(bits)):
        data_bits += '0' * (3 - len("{0:b}".format(bits[i]))) + "{0:b}".format(bits[i])
    
    # convert the bits back to string
    data_str = ''
    for i in range(0, len(data_bits), 8):
        data_tmp = data_bits[i:i+8]
        data_dec = int(data_tmp, 2)
        data_str += chr(data_dec)
    
    return data_str


def parse_packet(packet):
    try:
        if packet[TCP].sport == SRC_PORT and len(bits) == packet[TCP].seq:
                bits.append(packet[TCP].reserved)

    except:
        return
    

def main():
    # WARNING: DO NOT MODIFY THIS FUNCTION!
    message = receive_message(1984)
    print('received: %s' % message)


if __name__ == '__main__':
    main()
