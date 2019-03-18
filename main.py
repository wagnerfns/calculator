# coding:utf-8
import os
from operations import Operations

print("Calculator in python")

print("\nChoice operation ")
exit = 0

while(exit == 0):
    print("1 - Addition\n2 - Subtraction\n3 - Multiplication\n4 - Division\n5 - root\n6 - potentiation\n7 - Mean")

    operator = int(input("Operator: "))
    

    if(operator == 1):
        value1 = float(input("Value 1: "))
        value2 = float(input("Value 2: "))

        operation = Operations(value1, value2)
        result = operation.setAddition()
        print("result: {}".format(result))
    elif(operator == 2):
        value1 = float(input("Value 1: "))
        value2 = float(input("Value 2: "))

        operation = Operations(value1, value2)
        result = operation.setSubtraction()
        print("result: {}".format(result))
    elif(operator == 3):
        value1 = float(input("Value 1: "))
        value2 = float(input("Value 2: "))

        operation = Operations(value1, value2)
        result = operation.setMultiplication()
        print("result: {}".format(result))
    elif(operator == 4):
        value1 = float(input("Value 1: "))
        value2 = float(input("Value 2: "))

        operation = Operations(value1, value2)
        result = operation.setDivision()
        print("result: {}".format(result))
    elif(operator == 5):
        value1 = float(input("Value 1: "))
        value2 = float(input("Value 2: "))

        operation = Operations(value1, value2)
        result = operation.setRoot()
        print("result: {}".format(result))
    elif(operator == 6):
        value1 = float(input("Value 1: "))
        value2 = float(input("Value 2: "))

        operation = Operations(value1, value2)
        result = operation.setPotentiation()
        print("result: {}".format(result))
    elif(operator == 7):
        print("separate by ',' the values")
        value1 = [float(x)for x in raw_input("\nValue 1: ").split(',')]
        operation = Operations(value1, False)
        result = operation.avg()
        print("result: {}".format(result))

    #os.system('cls' if os.name == 'nt' else 'clear')
    #print("\n" * os.get_terminal_size().lines)

    exit = int(input("\n\nSair da culculadora? - Sim(1) ou não(0): "))



