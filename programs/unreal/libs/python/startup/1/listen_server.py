"""
Listen server bound to the unreal slate tick used to recieve commands from external python instances
"""

import unreal
import socket
import select
import sys

import tools_library.programs.unreal
import tools_library.utilities.listen_server


listen_port = tools_library.programs.unreal.listen_port()
listen_server = tools_library.utilities.listen_server.ListenServer(listen_port)


def slate_tick(delta_seconds):
    """Function bound to unreal's slate tick"""
    listen_server.tick()

def engine_shutdown():
    """Called when unreal shuts down"""
    unreal.unregister_slate_post_tick_callback(slate_tick_handle)
    unreal.unregister_python_shutdown_callback(engine_shutdown_handle)


slate_tick_handle = unreal.register_slate_post_tick_callback(slate_tick)
engine_shutdown_handle = unreal.register_python_shutdown_callback(engine_shutdown)
