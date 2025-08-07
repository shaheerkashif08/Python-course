a = int(input("Enter 1rst number: "))
b = int(input("Enter 2nd number: "))

try:
    print(a/b)

except Exception as e:
    print(e)

finally:
    print("This is always executed! ")