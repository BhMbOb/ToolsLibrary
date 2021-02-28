import sys
import os
import socket
import select
import contextlib


def is_free(port):
    """Returns whether a port is free\n
    :param <int:port> Port index\n
    :return <bool:free> True if free, false if not\n
    """
    test_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    loc = ("localhost", port)
    output = test_socket.connect_ex(loc) is not 0
    test_socket.close()
    return output


class ListenServer(object):
    """Creates a simple non-blocking listen server"""
    def __init__(self, port):
        self.port = port

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind(("localhost", port))
        self.server_socket.listen(0)
        self.server_socket.setblocking(0)
        self.read_list = [self.server_socket]


        # Temporarily stops the "ConnectionRefusedError" from displaying in the logs
        # sending an empty command is only a workaround to stop blocking on the listen server
        # and if the connection fails then we get around the initial blocking anyway
        # we must send an initial command else the server will block the program until the first connection
        null = open(os.devnull, "wb")
        with contextlib.redirect_stderr(null):
            init_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            init_client.connect(("localhost", port))
            init_client.send(str("").encode("utf-8"))
            init_client.setblocking(0)
            init_client.close()
            self.initialized = True
    
    def tick(self):
        """Update the listen server and check for calls"""
        if(self.initialized):
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
        """Close the listen server"""
        self.server_socket.close()
