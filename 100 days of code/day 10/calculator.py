from art import logo
import os

clear = lambda: os.system('cls')

def add(num1, num2):
  return num1 + num2

def subtract(num1, num2):
  return num1 - num2

def multiple(num1, num2):
  return num1 * num2

def divide(num1, num2):
  return num1 / num2

operations = {
  '+': add, 
  '-': subtract, 
  '*': multiple, 
  '/': divide
  }


def calculator():
  print(logo)

  num1 = float(input("What is the first number?: "))
  for operation in operations:
    print(operation)

  should_continue = True

  while should_continue:

    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What is the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation: ") == "y":
      num1 = answer
    else:
      should_continue = False
      clear()
      calculator()

calculator()