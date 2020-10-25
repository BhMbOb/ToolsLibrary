import os

# loop over all files in the "python/startup/x" folders and run them
for i in range(99):

    startup_folder = os.path.dirname(__file__) + "/" + str(i)

    # run python files
    if(os.path.isdir(startup_folder)):
        for file in os.listdir(startup_folder):
            if(file.endswith(".py")):
                file_path = os.path.join(startup_folder, file)
                exec(open(file_path).read())

        print("Python Startup " + str(i) + " initialized.")

print(os.path.dirname(__file__))
