import unreal
import socket
import select
import sys

import tools_library.programs.unreal


# only set up the listen server if we are the only instance of UE4 running
listen_port = tools_library.programs.unreal.listen_port()
if(socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect_ex(("localhost", listen_port)) == 0):

    # initialize listen server
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', listen_port))
    server_socket.listen(5)
    server_socket.setblocking(0)

    # send single request as client else UE4 is locked until the first request
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', listen_port))
    client_socket.send(str("").encode("utf-8"))
    client_socket.setblocking(0)
    client_socket.close()

    read_list = [server_socket]


    def slate_tick(delta_seconds):
        readable, writable, errored = select.select(read_list, [], [])
        for s in readable:
            if s is server_socket:
                client_socket, address = server_socket.accept()
                read_list.append(client_socket)
            else:
                data = (s.recv(1024)).decode("utf-8")
                if(data):
                    try:
                        exec(data)
                    except:
                        pass


    def engine_shutdown():
        unreal.unregister_slate_post_tick_callback(slate_tick_handle)
        unreal.unregister_python_shutdown_callback(engine_shutdown_handle)


    slate_tick_handle = unreal.register_slate_post_tick_callback(slate_tick)
    engine_shutdown_handle = unreal.register_python_shutdown_callback(engine_shutdown)

else:
    print("[Tools Library] Listen server already running in another unreal instance!")
