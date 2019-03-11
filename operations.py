import math

class Operations:
    def __init__(self, value1, value2): 
        self.value1 = value1
        self.value2 = value2    

    def setAddition(self):
        print("result: {}".format(self.value1 + self.value2))
        return(self.value1 + self.value2)

    def setSubtraction(self):
        print("result: {}".format(self.value1 - self.value2))
        return(self.value1 - self.value2)

    def setMultiplication(self):
        print("result: {}".format(self.value1 * self.value2))
        return(self.value1 * self.value2)

    def setDivision(self):
        print("result: {}".format(self.value1 / self.value2))
        return(self.value1 / self.value2)

    def setRoot(self):
        print("Result: {}".format(math.sqrt(self.value1)))
        return(math.sqrt(self.value1))
        
    def setPotentiation(self):
        print("Result: {}".format(self.value1 ** 2))
        return(self.value1 ** 2)