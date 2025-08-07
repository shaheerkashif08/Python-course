def average(a, b, c):
    avg = (a+b+c)/3
    # print(f"The average of three numbers are {avg}")
    return avg

a = float(input("Enter First number: "))
b = float(input("Enter Second number: "))
c = float(input("Enter Third number: "))
d = average(a, b, c)
print(d)