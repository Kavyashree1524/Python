import os #accesing anthing from the system need to use this module

print(os.listdir())
file_other_than_py = [f for f in os.listdir() if not f.endswith('py')] # elements in the list of dir in the current directory and its not end with py store those in the list
print(file_other_than_py)