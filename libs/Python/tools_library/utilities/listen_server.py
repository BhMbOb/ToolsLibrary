"""
Utility function/class for setting up a basic non-blocking listen server
"""

import sys
import os
import socket
import select

class ListenServer(object):
    def __init__(self, port):
        self.port = port

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind(("localhost", port))
        self.server_socket.listen(5)
        self.server_socket.setblocking(0)
        self.read_list = [self.server_socket]

        # we must send an initial command else the server will block the program until the first connection
        init_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        init_client.connect(("localhost", port))
        init_client.send(str("").encode("utf-8"))
        init_client.setblocking(0)
        init_client.close()

    def tick(self):
        readable, writable, errored = select.select(self.read_list, [], [])
        for s in readable:
            if(s is self.server_socket):
                client_socket, address = self.server_socket.accept()
                self.read_list.append(client_socket)
            else:
                # NOTE: We may need to up the size if we end up sending large scripts to run
                data = (s.recv(1024)).decode("utf-8")
                if(data):
                    try:
                        exec(data)
                    except:
                        pass

    def close(self):
        self.server_socket.close()