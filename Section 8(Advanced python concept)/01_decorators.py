# Decorator is a function that takes a function, it creates a new function inside its body (wrapper). Then it returns to a new function

def decorators(func):
    def wrapper():
        print("I am here to execute a function...")
        func()
        print("I have executed the function...")
    return wrapper
    
@decorators
def say_hello():
    print("Hello Boy!!")

say_hello()
# f = decorators(say_hello)
# f()