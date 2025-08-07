square = lambda x: x*x
sum = lambda x,y: x+y
print(square(4))
print(sum(3,7))

num = [1,2,3,4]
squared = list(map(lambda x: x**2, num))
print(squared)