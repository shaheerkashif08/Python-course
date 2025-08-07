# f = open("shah.txt", "r")
# content = f.read()

# print(content)
# f.close()

with open("shah.txt", "r") as f:
    content = f.read()
    print(content)