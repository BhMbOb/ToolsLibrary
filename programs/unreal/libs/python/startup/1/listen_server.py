import unreal
import subprocess

#print(unreal.get_editor_subsystem(unreal.EditorSubsystem))

is_quit = False


def test_tick(value):
    if not(is_quit):
        pass
    else:
        unreal.unregister_slate_post_tick_callback(tick_handle)


def shutdown():
    is_quit = True
    subprocess.Popen('explorer "C:\\"')
    unreal.unregister_python_shutdown_callback(shutdown_handle)


tick_handle = unreal.register_slate_post_tick_callback(test_tick)
shutdown_handle = unreal.register_python_shutdown_callback(shutdown)