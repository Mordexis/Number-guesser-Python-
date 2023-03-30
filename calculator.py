def multiplication():
    result = num1 * num2
    print(num1, "multiplied by", num2, "is equal to", result)

def division():
    result = num1 / num2
    print (num1, "divided by", num2, "is equal to", result)
    
def addition():
    result = num1 + num2
    print (num1, "add", num2, "is equal to", result)
    
def subtraction():
    result = num1 - num2
    print(num1, "minus", num2, "=", result)

def exponential():
    result = num1**num2
    print(num1, "to the power of", num2, "=", result)

"""checker = input("Would you like to calculate? Type No to if you wouldn't.")
if checker.lower == "no" or checker.lower == "stop":
    print ("Alright, Have a good day")
else:
    while checker.lower != "yes":
        num1= float(input("Please enter a number"))
        num2 = float(input("Please enter a second number"))
        Operation = input("Pleas state the operation you'd like to perform")
        if Operation.lower() == "/" or Operation.lower() == "div" or Operation.lower() == "division" or Operation.lower() == "divide":
            division()
        elif Operation.lower() == "*" or Operation.lower() == "multiplication" or Operation.lower() == "times" or Operation.lower() =="mult" or Operation.lower() == "multiply" or Operation.lower == "x":
            multiplication()
        elif Operation.lower() == "+" or Operation.lower() == "addition" or Operation.lower() == "add" or Operation.lower() == "plus":
            addition()
        elif Operation.lower() == "-" or Operation.lower() == "sub" or Operation.lower() == "subtract" or Operation.lower() == "subtraction" or Operation.lower() == "minus":
            subtraction()
        else:
            print ("Error please enter a specified operator.")
        checker = input("Are you finished")
    
        if checker == "yes":
            print("Thanks, please use again")
            break"""
checker = input("Hello, enter any input to get started")
print("This a calculator")
print("It can currently perform 5 functions")
print("Division")
print("Exponents")
print("Multiplication")
print("Subtraction")
print("Addition")
while checker.lower != "yes":
    Operation = input("Pleas state the operation you'd like to perform")
    num1= float(input("Please enter a number"))
    num2 = float(input("Please enter a second number"))
    if Operation.lower() == "/" or Operation.lower() == "div" or Operation.lower() == "division" or Operation.lower() == "divide":
        division()
    elif Operation.lower() == "*" or Operation.lower() == "multiplication" or Operation.lower() == "times" or Operation.lower() =="mult" or Operation.lower() == "multiply" or Operation.lower == "x":
        multiplication()
    elif Operation.lower() == "+" or Operation.lower() == "addition" or Operation.lower() == "add" or Operation.lower() == "plus":
        addition()
    elif Operation.lower() == "-" or Operation.lower() == "sub" or Operation.lower() == "subtract" or Operation.lower() == "subtraction" or Operation.lower() == "minus":
        subtraction()
    elif Operation.lower() == "^" or Operation.lower() == "exponent" or Operation.lower() == "exponents" or Operation.lower() == "exponential" or Operation.lower == "power" or Operation.lower == "powers":
        exponential()
    else:
        print ("Error please enter a specified operator.")
    checker = input("Are you finished")
    
    if checker == "yes":
        print("Thanks, please use this calculator again")
        break
