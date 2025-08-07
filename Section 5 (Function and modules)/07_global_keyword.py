def sum(a, b):
    print("Hey i am sum of two number: ")
    c = a + b
    global z  # instruct the python interpreter to modify the z
    z = 1
    return c

z = 5
print(sum(4,6))
print(z)