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
    if (num2 == 0):
        result = "Cant't divide by 0"
    else:
        result = num1 / num2

    return result

def modulus (num1,num2):

    if (num2 == 0):
        result = "Cant't modulus by 0"
    else:
        result = num1 % num2

    return result


def menu():
    print("Welcome to the Calculator!")
    print("Type the option you would like")
    print("1 Addition")
    print("2 Subtraction")
    print("3 Multiplication")
    print("4 Division")
    print("5 Modulus")


def calculate():
    menu ()
    menuSelect = input ("Option: ")
    menuSelect = int(menuSelect)
    inNum1 = int(input("First Number: "))
    inNum2 = int(input("Second Number: "))
    
    if (menuSelect == 1):
        print("Selected Addition")
        print (addition(inNum1,inNum2))
    elif (menuSelect == 2):
        print("Selected Subtraction")
        print (subtraction(inNum1,inNum2))
    elif (menuSelect == 3):
        print("Selected Multiplication")
        print (multiplication(inNum1,inNum2))
    elif (menuSelect == 4):
        print("Selected Division")
        print (division(inNum1,inNum2))
    elif (menuSelect == 5):
        print("Selected Modulus")
        print (modulus(inNum1,inNum2))
    else:
        print ("Unknown input")

#run programe
calculate()



#print (addition(5,5))
#print (subtraction(10,5))
#print (multiplication(20,5))
#print (division(100,2))
#print (division(100,0))



