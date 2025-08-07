import os

a = os.listdir("dir")                   # it print the files including in folder
print(a)

print(os.getcwd())                      # It represent the location of your opened folder

print(os.path.exists("saample.txt"))    # It check wheteher the named folder is present or not

# os.remove("sample1.txt")                # It is used to remove the file 

# os.rmdir("saample.txt")                 # it mainly remove the empty folder 

path = os.path.join("soul_thinks1.txt", "soul_think2.txt", "soul_think3.txt")     # Combine multiple path components into single properly formatted file path
print(path)

# print(os.rename("soul_think1.txt", "soul_thinks1.txt"))    # Rename a file 