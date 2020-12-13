import os

#import tools_library
#import tools_library.filemgr
import tools_library.filemgr


def link(src, dest):
    try:
        tools_library.filemgr.makedir(os.path.dirname(dest))

        if(os.path.isdir(src)):
            if(os.path.islink(dest)):
                os.unlink(dest)
            os.symlink(
                os.path.realpath(src),
                os.path.realpath(dest),
                target_is_directory=True
            )
    except OSError as error:
        if(os.path.isdir(dest)):
            print("[Tools Library][Symlink] Warning: Destination directory already exists!")
        elif(not os.path.isdir(src)):
            print("[Tools Library][Symlink] Warning: Source directory does not exist!")
        else:
            print("[Tools Library][Symlink] Error: Symlink failed!")
            print(error)
    else:
        print("[Tools Library][Symlink] Success: " + dest)
