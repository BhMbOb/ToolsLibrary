import os

import pymxs

# loop over all files in the "python/startup/x" folders and run them
for i in range(99):

    startup_folder = os.path.dirname(__file__) + "/" + str(i)
    startup_folder_ms = startup_folder.replace("python", "maxscript")

    # run maxscript files
    if(os.path.isdir(startup_folder_ms)):
        for file in os.listdir(startup_folder_ms):
            print(os.path.join(startup_folder_ms, file))
            if(file.endswith(".ms")):
                file_path = os.path.join(startup_folder_ms, file)
                with open(file_path) as file:
                    file_lines = file.read()
                    pymxs.runtime.execute(file_lines)

        print("Maxscript Startup " + str(i) + " initialized.")

    # run python files
    if(os.path.isdir(startup_folder)):
        for file in os.listdir(startup_folder):
            if(file.endswith(".py")):
                file_path = os.path.join(startup_folder, file)
                exec(open(file_path).read())

        print("Python Startup " + str(i) + " initialized.")
