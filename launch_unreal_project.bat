0<0# : ^
''' 
@echo off
echo batch code
"bin/python 3.7/python.exe" "%~f0" %*
exit /b 0
'''

import tools_library.programs.unreal
tools_library.programs.unreal.launch_unreal_project()