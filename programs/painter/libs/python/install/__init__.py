import os
import shutil
import winreg

#

install_scripts_dir = os.path.dirname(__file__) + "\\"

for i in range(99):
    install_scripts_current_dir = install_scripts_dir + str(i)

    if(os.path.isdir(install_scripts_current_dir)):
        for file in os.listdir(install_scripts_current_dir):
            current_script_path = install_scripts_current_dir + "\\" + file
            exec(open(current_script_path).read())
