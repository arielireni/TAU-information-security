import socket
import math
from scapy.all import *

SRC_PORT = 65000


def send_message(ip: str, port: int):
    """Send a *hidden* message to the given ip + port.

    Julia expects the message to be hidden in the TCP metadata, so re-implement
    this function accordingly.

    Notes:
    1. Use `SRC_PORT` as part of your implementation.
    """
    plaintext = 'I love you'
    text_bits = ''.join(format(ord(i), '08b') for i in plaintext)
    
    # divide and round up
    needed_packets = math.ceil(len(text_bits) / 3)
    for i in range(needed_packets):
        # slice the next 3 bits and convert it to int
        curr_triple = text_bits[3*i:3*i+3]

        # if the last one is not a triple, pad with zeros
        if i == needed_packets-1 and len(curr_triple) != 3:
            curr_triple += '0'*(3-len(curr_triple))
        packet_data = int(curr_triple)    
        
        # use serial SEQ number and total number of triples in ACK
        packet = IP(dst=ip) / TCP(flags='SA', sport=SRC_PORT, dport=port, seq=i, ack=needed_packets, reserved=packet_data)
        send(packet)


def main():
    # WARNING: DO NOT MODIFY THIS FUNCTION!
    send_message('127.0.0.1', 1984)


if __name__ == '__main__':
    main()
