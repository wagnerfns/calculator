# coding:utf-8

import os
from operations import Operations
print("Calculator in python")

print("\nChoice operation ")
exit = 0

while(exit == 0):
    print("1 - Addition\n2 - Subtraction\n3 - Multiplication\n4 - Division\n5 - root\n6 - potentiation")

    operator = int(input("Operator: "))
    value1 = float(input("\nValue 1: "))
    value2 = float(input("Value 2: "))

    operation = Operations(value1, value2) 

    if(operator == 1):
        operation.setAddition()
    elif(operator == 2):
        operation.setSubtraction()
    elif(operator == 3):
        operation.setMultiplication()
    elif(operator == 4):
        operation.setDivision()
    elif(operator == 5):
        operation.setRoot()
    elif(operator == 6):
        operation.setPotentiation()
    
    #os.system('cls' if os.name == 'nt' else 'clear')
    #print("\n" * os.get_terminal_size().lines)

    exit = int(input("\n\nSair da culculadora? - Sim(1) ou não(0): "))



