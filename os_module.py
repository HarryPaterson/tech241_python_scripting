# Using os to do things

import os

# Echo to the terminal
# os.system('echo "Hello world!"')

# make and change directories

# create a directory


# Directory name
directory = "test_dir"

# Parent directory
parent_dir = "C:/Users/User"

# Path
path = os.path.join(parent_dir, directory)

# os.mkdir(path)

# Putting a new file in the new dir

filename = "testfile.txt"
filepath = os.path.join(path, filename)

with open(filepath, "w") as file1:
    toFile = "Contents of file is wrriten here"
    file1.write(toFile)

print("File " + filename + " created in " + directory + " folder")

