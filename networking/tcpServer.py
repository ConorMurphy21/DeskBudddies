import socketserver
import struct
import threading
from multiprocessing import Process


class TcpHandler(socketserver.BaseRequestHandler):
    response = """
        Hi, guy!
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        data = self.request.recv(1024).decode('utf-8')
        print(str(data))
        data = self.response.encode('utf-8')
        msg = struct.pack('>I', len(data)) + data
        self.request.sendall(msg)


class TcpServer:

    def __init__(self, port):
        self.server = socketserver.TCPServer(('', port), TcpHandler)

    def run(self):
        threading.Thread(target=self.server.serve_forever).start()




