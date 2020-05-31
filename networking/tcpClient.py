import socket


# sends a packet and waits for a response
# this means the server has to respond with something, so we will make a null packet for this reason
def send_packet(packet, ip, port) -> str:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
    print(packet)
    s.send(packet.encode('utf-8'))
    # maybe the response is longer than this, so we may need to come up with a way of receiving more data on the
    # client end
    data = s.recv(1024).decode('utf-8')
    print(str(data))
    return str(data)
