# while True:
#     try:
#         a = int(input("Enter he 1rst number: "))
#         b = int(input("Enter he 2nd number: "))
#         print(f"The division is {a/b}")

#     except ValueError:
#         print("Please don't perform bad typecast")

#     except ZeroDivisionError:
#         print("Don't divide a number by zero")
#     except Exception as e:
#         print("Syntax Error occured!!wyw", e)

a = int(input("Enter 1rst number: "))
b = int(input("Enter 2nd number: "))

if b == 0:
    raise ValueError("Please don't divide by zero")

print(f"The division of a and b is {a/b}")