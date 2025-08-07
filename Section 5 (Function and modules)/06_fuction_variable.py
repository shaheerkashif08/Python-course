def sum(a,b):
    c = a+b  # a and b are local variales
    z = 1  # it create a local variable which will destroyed after the funcion return
    return c

def greet():
    z = 32  # z is a local variable
    print("Hello")

    
z = 6
print(sum(4,5))
print(z)  # z is a global variable