class Operations:
    def __init__(self, value1, value2): 
        self.value1 = value1
        self.value2 = value2
        #self.operation = operation
    

    def addition(self):
        print("result: {}".format(self.value1 + self.value2))

    def subtraction(self):
        print("result: {}".format(self.value1 - self.value2))

    def multiplication(self):
        print("result: {}".format(self.value1 * self.value2))

    def division(self):
        print("result: {}".format(self.value1 / self.value2))