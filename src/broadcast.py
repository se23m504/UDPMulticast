import socket
import time

from config import (
    BROADCAST_INTERVAL,
    MULTICAST_IP,
    MULTICAST_PORT,
    SERVICE_IP,
    SERVICE_NAME,
    SERVICE_PORT,
)

message = f"{SERVICE_NAME}:{SERVICE_IP}:{SERVICE_PORT}"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)

try:
    while True:
        sock.sendto(message.encode("utf-8"), (MULTICAST_IP, MULTICAST_PORT))
        print(f"Broadcasting service info: {message}")
        time.sleep(BROADCAST_INTERVAL)
finally:
    sock.close()
