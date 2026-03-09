from art import logo
from email.policy import default


def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def divide(n1, n2):
    return n1 / n2

def multiply(n1, n2):
    return n1 * n2

active = True

calculation = {"+": add, "-":subtract, "/": divide, "*":multiply}

print (logo)
while active:
    first_number = input("What is the first number? ")
    operation = input("What is the operation? " )
    second_number = input("What is the second number? ")
    result = calculation[operation](int(first_number), int(second_number))
    print (f"The result is {result}.")
    continue_to_calculate = input ("Do you wish to continue calculating with the previous result? Type 'yes' if so - or 'no' if you wish to start anew.")
    if continue_to_calculate == "yes":
        """this is code"""
        first_number = result
        operation = input("What is the operation? ")
        second_number = input("What is the second number? ")
        result = calculation[operation](int(first_number), int(second_number))
        print(f"The result is {result}.")
    else:
        """continue_to_calculate == 'no'"""
        first_number = input("What is the first number? ")
        operation = input("What is the operation? ")
        second_number = input("What is the second number? ")
        result = calculation[operation](int(first_number), int(second_number))
        print(f"The result is {result}.")
        continue_to_calculate = input(
            "Do you wish to continue calculating with the previous result? Type 'yes' if so - or 'no' if you wish to start anew.")
        if continue_to_calculate == "yes":
            """this is code"""
            first_number = result
            operation = input("What is the operation? ")
            second_number = input("What is the second number? ")
            result = calculation[operation](int(first_number), int(second_number))
            print(f"The result is {result}.")
        else:
            """continue_to_calculate == 'no'"""
            first_number = input("What is the first number? ")
            operation = input("What is the operation? ")
            second_number = input("What is the second number? ")
            result = calculation[operation](int(first_number), int(second_number))
            print(f"The result is {result}.")






