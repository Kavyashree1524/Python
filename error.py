#check if a file exists
import os

file = "kavya"

if os.path.exists(file):
    print("file exists")
else:
    print("File does not exists")