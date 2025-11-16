while True:      
    operator = input("Please Enter the Operator (+, -, *, /+)")
    number1 = input("Please Enter the first Number: ")
    number2= input("Please Enter the Second Number: ")

    while True:
            if number1.isdigit() & number2.isdigit():
                number1= float(number1)
                number2= float(number2)
                break
            else:
                print("Please Enter only numbers")


    if operator == "+":
        print(f"The addition of two numbers is {number1+number2}")
    elif operator == "-":
        print(f"The subtraction of two numbers is {number1-number2}")
    elif operator == "*":
        print(f"The multiplication of two numbers is {number1*number2}")
    elif operator == "/":
        print(f"The division of two numbers is {number1/number2}")
    else:
        print(f"{operator} is invalid operator")


