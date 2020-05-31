import socketserver
import threading
from multiprocessing import Process


class TcpHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        data = self.request.recv(1024).decode('utf-8')
        print(str(data))
        self.request.sendall(data.upper().encode('utf-8'))


class TcpServer:

    def __init__(self, port):
        self.server = socketserver.TCPServer(('', port), TcpHandler)

    def run(self):
        threading.Thread(target=self.server.serve_forever).start()




