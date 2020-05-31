import socket


# sends a packet and waits for a response
# this means the server has to respond with something, so we will make a null packet for this reason
import struct

from networking.packets import packet


def send_packet(pack, ip, port) -> str:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
    print(pack)
    s.send(pack.encode('utf-8'))
    # receive and reconstruct a possibly large message
    data = recv_msg(s).decode('utf-8')
    print(data)
    return data


def recv_msg(sock):
    # Read message length and unpack it into an integer
    raw_msglen = recvall(sock, 4)
    if not raw_msglen:
        return None
    msglen = struct.unpack('>I', raw_msglen)[0]
    # Read the message data
    return recvall(sock, msglen)


def recvall(sock, n):
    # Helper function to recv n bytes or return None if EOF is hit
    data = bytearray()
    while len(data) < n:
        packet = sock.recv(n - len(data))
        if not packet:
            return None
        data.extend(packet)
    return data
