class Calculator:
    def __init__(self, value1, value2):  # initialising calculator with 2 values
        self.value1 = value1
        self.value2 = value2

    def adder(self):
        result = self.value1 + self.value2  # adding the 2 values
        return result

    def subtractor(self):
        result = self.value1 - self.value2  # subtracting value 2 from value 1
        return result

    def multiplier(self):
        result = self.value1 * self.value2  # multiplying the 2 values
        return result

    def divider(self):
        result = self.value1 / self.value2  # dividing value 1 by value 2
        return result

    def clear(self):
        self.value1 = 0
        self.value2 = 0
        return self.value1, self.value2


input1 = int(input('Enter 1st number: '))
input2 = int(input('Enter 2nd number: '))

calculatorObj = Calculator(input1, input2)

print("Result of adder() method with input values " + str(input1) + " and " + str(input2) + " is " + str(
    calculatorObj.adder()))
print("Result of subtractor() method with input values " + str(input1) + " and " + str(input2) + " is " + str(
    calculatorObj.subtractor()))
print("Result of multiplier() method with input values " + str(input1) + " and " + str(input2) + " is " + str(
    calculatorObj.multiplier()))
print("Result of divider() method with input values " + str(input1) + " and " + str(input2) + " is " + str(
    calculatorObj.divider()))
print("Result of clear() method with input values " + str(input1) + " and " + str(input2) + " is " + str(
    calculatorObj.clear()))
