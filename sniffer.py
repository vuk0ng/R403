import socket
import struct
import binascii
import sys

try:
    raw_socket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
except socket.error as e:
    sys.exit()

while True:
    packet = raw_socket.recvfrom(65565)
    ethernet_header = packet[0][0:14]
    eth_header = struct.unpack('!6s6s2s', ethernet_header)
    print('Destination :', binascii.hexlify(eth_header[0]))
    print('Source :', binascii.hexlify(eth_header[1]))
    print('Type :', binascii.hexlify(eth_header[2]))
    ip_header = packet[0][14:34]
    ip_hdr = struct.unpack('!12s4s4s', ip_header)
    print('Source IP :', socket.inet_ntoa(ip_hdr[1])) 
    print('Destination IP :', socket.inet_ntoa(ip_hdr[2]))