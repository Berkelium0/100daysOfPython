from art import logo
import os


def clear():
    os.system('clear')


def add(first, second):
    return first + second


def subtract(first, second):
    return first - second


def multiply(first, second):
    return first * second


def divide(first, second):
    return first / second


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator(first_num, char, sec_num):
    calc = operations[char]
    result = calc(first_num, sec_num)

    print("{:.1f}".format(first_num) + " " + char + " " + "{:.1f}".format(sec_num) + " = " + "{:.1f}".format(result))

    return result


def begin(char, first_num):
    if char == "n":
        first_num = float(input("What is the first number?: "))
        for key in operations:
            print(key)
    char = input("Pick an operation: ")
    sec_num = float(input("What is the next number?: "))
    return calculator(first_num, char, sec_num)


print(logo)
result = begin("n", 0)

while True:
    cont = input("Type 'y' to continue calculating with " + "{:.1f}".format(
        result) + ", or type 'n' to start a new calculation: ")
    if cont == "n":
        clear()
    result = begin(cont, result)
