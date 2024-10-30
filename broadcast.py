import socket
import struct
import time

service_name = "windows.local"
ip_address = "192.168.137.1"
port = 5000
message = f"{service_name}:{ip_address}:{port}"

multicast_group = "224.0.0.251"
multicast_port = 5353

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)

try:
    while True:
        sock.sendto(message.encode("utf-8"), (multicast_group, multicast_port))
        print(f"Broadcasting service info: {message}")
        time.sleep(2)
finally:
    sock.close()