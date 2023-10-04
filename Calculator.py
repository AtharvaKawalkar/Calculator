import Calculator_art
import os

clear = lambda: os.system('cls')

#Add
def add(n1, n2):
    return n1 + n2

#Subtract
def subtract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

def calculator():
    clear()
    print(Calculator_art.logo)
    should_continue = True

    num1 = float(input("What's the first number? : " ))
    for symbol in operations:
        print(symbol)
    
    while should_continue:
        operation_symbol = input("Pick an operation : ")
        num2 = float(input("What's the next number? : " ))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        user_response = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start new calculation : ")
        if(user_response == 'y'):
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()