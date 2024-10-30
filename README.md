# UDPMulticast

This Python project broadcasts a service on a local network using UDP to enable client devices to discover and connect to it. It is especially useful when DNS is unavailable, or setting up DNS records is not feasible. By listening to UDP multicast messages, client applications (such as a Unity-based HoloLens app) can dynamically discover the service location without needing hardcoded addresses.

## Features

- **Local service discovery**: Allows clients on the same network to find the service by listening to a specific multicast address and port (`224.0.0.251:5353`)
- **Broadcasted service information**: Periodically sends out service details, including IP and port, for clients to pick up and use.
- **Reliable fallback option**: Offers service discovery without relying on DNS, suitable for local networks and ad-hoc setups/networks.

## Why not Zeroconf/mDNS?

Initially, we considered implementing a Zeroconf/mDNS-based discovery solution, as this protocol is widely used for service discovery. However, due to limited support for reliable Zeroconf/mDNS libraries in Unity UWP (targeting HoloLens 2), we opted for a simpler UDP multicast implementation. This "naive" multicast approach fulfills the project's requirements and provides a lightweight, effective solution without the need to implement complex Zeroconf/mDNS protocols from scratch in Unity.

## Prerequisites

- `python >= 3.11`

## Usage

1. Run the script.

```bash
python broadcast.py
```

## How clients receive the service announcement

Clients can listen to the same multicast address and port to receive service information. For instance, in Unity, you could set up a UDP listener on the multicast address, parse the received data, and use it to connect to the service. For debugging purposes, we include a `client.py` that you can run to test that the UDP broadcast is working as expected.

## Limitations

- **Local network only**: The UDP multicast approach is intended for devices on the same local network, and may not work over the internet or in networks that restrict multicast traffic.
- **No authentication**: Broadcasts are open to any listener on the network, so it should only be used in secure, controlled environments.
