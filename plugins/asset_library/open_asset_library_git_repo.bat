0<0# : ^
''' 
@echo off
echo batch code
"../../bin/python 3.7/python.exe" "%~f0" %*
exit /b 0
'''

import os
import tools_library
tools_library.run_file(os.path.join(tools_library.path(), "plugins\\asset_library\\programs\\python\\scripts\\open_asset_library_git_repo.py"))