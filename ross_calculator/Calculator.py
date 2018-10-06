def addition(num1,num2):
    result = num1 + num2
    return result

def subtraction(num1,num2):
    result = num1 - num2
    return result

def multiplication(num1,num2):
    result = num1 * num2
    return result

def division(num1,num2):
    if(num2 == 0):
        result = "Can't divide by 0"
    else:
        result = num1 / num2
    return result

def modulus(num1,num2):
    if(num2 == 0):
        result = "Can't divide by 0"
    else:
        result = num1 % num2
    return result

def menu():
    print("Welcome to the Calculator!")
    print("Type the option you would like.")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")

def calculate():
    menu()
    menuSelect = input("Option: ")
    menuSelect = int(menuSelect)
    inNum1 = int(input("First Number: "))
    inNum2 = int(input("Second Number: "))

    # If menuSelect equals 1, call addition function
    if(menuSelect == 1):
        print("Selected Addition")
        print(addition(inNum1,inNum2))

    # If menuSelect equals 2, call subtraction function
    elif(menuSelect == 2):
        print("Selected Subtraction")
        print(subtraction(inNum1,inNum2))

    # if menuselect equals 3, call Multiplication function
    elif(menuSelect == 3):
        print("Selected Multiplication")
        print(multiplication(inNum1,inNum2))

    # if menuSelect equals 4, call the division function.
    elif(menuSelect == 4):
        print("Selected Division")
        print(division(inNum1,inNum2))
    
    # if menuSelect equals 5, call modulus function
    elif(menuSelect == 5):
        print("Selected Modulus")
        print(modulus(inNum1,inNum2))

    else:
        print("unknown input")

# Run the program
calculate()