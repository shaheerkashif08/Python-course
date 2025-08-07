numbers = [1, 2, 3, 4, 5, 15, 21]

# def square(x):
#     return x*x   or else we can use lambda 

new = list(map(lambda x: x*x , numbers))
print(new)