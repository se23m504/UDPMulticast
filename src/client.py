import socket
import struct

from config import MULTICAST_IP, MULTICAST_PORT

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(("", MULTICAST_PORT))

group = socket.inet_aton(MULTICAST_IP)
mreq = struct.pack("4sL", group, socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

print(f"Listening for messages on {MULTICAST_IP}:{MULTICAST_PORT}")

while True:
    data, addr = sock.recvfrom(1024)
    print(f"Received message: {data.decode()} from {addr}")
