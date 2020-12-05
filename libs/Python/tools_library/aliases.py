import sys

# TODO: Fix for Py2 - replace when Unreal is on Py3
if(sys.version_info >= (3, 0)):
    import winreg
else:
    import _winreg as winreg