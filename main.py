from operations import Operations
print("Calculator in python")

print("\nChoice operation ")
exit = 0

while(exit == 0):
    print("1 - Addition\n2 - Subtraction\n3 - Multiplication\n4 - Division\n")

    operator = int(input("Operator: \n"))
    value1 = float(input("Value 1: "))
    value2 = float(input("Value 2: "))

    operation = Operations(value1, value2) 

    if(operator == 1):
        operation.addition()
    elif(operator == 2):
        operation.subtraction()
    elif(operator == 3):
        operation.multiplication()
    elif(operator == 4):
        operation.division()


    exit = int(input("Sair da culculadora? - Sim(1) ou não(0): "))



