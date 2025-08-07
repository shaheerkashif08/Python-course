try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print("What kind of operation You want to do Here\nPress + for Addition \nPress - for substraction \nPress * for multiplication\nPress / for division\nPress ^ for exponentiation")

    opr = input("Enter the operation: ")
    match opr:
        case "+":
            print(f"The result is: {a+b}") 
        case "-":
            print(f"The result is: {a-b}")
        case "*":
            print(f"The result is: {a*b}")
        case "/":
            print(f"The result is: {a/b}")
        case "^":
            print(f"The result is: {a**b}") 
        case "default":
            print("Invalid Operation case")

except Exception as e:
    print("Invalid number!")