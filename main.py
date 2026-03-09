import art
from email.policy import default


def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def divide(n1, n2):
    return n1 / n2

def multiply(n1, n2):
    return n1 * n2



calculation = {"+": add, "-":subtract, "/": divide, "*":multiply}


def calculator():
    active = True
    print(art.logo)
    first_number = input("What is the first number? ")

    while active:
        for symbol in calculation:
            print (symbol)
        operation = input("What is the operation? " )
        second_number = input("What is the second number? ")
        result = calculation[operation](int(first_number), int(second_number))
        print(f"The result for {first_number} {operation} {second_number} is {result}.")
        continue_to_calculate = input ("Do you wish to continue calculating with the previous result? Type 'yes' if so - or 'no' if you wish to start anew.")
        while continue_to_calculate == "yes":
            """this is code"""
            first_number = result
            operation = input("What is the operation? ")
            second_number = input("What is the second number? ")
            result = calculation[operation](int(first_number), int(second_number))
            print(f"The result for {first_number} {operation} {second_number} is {result}.")
            continue_to_calculate = input(
                "Do you wish to continue calculating with the previous result? Type 'yes' if so - or 'no' if you wish to start anew.")


        else:
            active = False
            print("\n" * 30)
            calculator()

calculator()

"""continue_to_calculate == 'no'
first_number = input("What is the first number? ")
operation = input("What is the operation? ")
second_number = input("What is the second number? ")
result = calculation[operation](int(first_number), int(second_number))
print(f"The result for {first_number} {operation} {second_number} is {result}.")

continue_to_calculate = input("Do you wish to continue calculating with the previous result? Type 'yes' if so - or 'no' if you wish to start anew.")



if continue_to_calculate == "yes":
#this is code
first_number = result
operation = input("What is the operation? ")
second_number = input("What is the second number? ")
result = calculation[operation](int(first_number), int(second_number))
print(f"The result for {first_number} {operation} {second_number} is {result}.")

else:
#continue_to_calculate == 'no'
first_number = input("What is the first number? ")
for symbol in operation:
    print (symbol)
operation = input("What is the operation? ")
second_number = input("What is the second number? ")
result = calculation[operation](float(first_number), float(second_number))
print(f"The result for {first_number} {operation} {second_number} is {result}.")"""



