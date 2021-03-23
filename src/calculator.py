from operations.calc_operations import calcOperations


class Calculator:
    def __init__(self):
        self.results = []

    def add(self, x, y):
        self.results.append(calcOperations.addition(x, y))
        return self.results[-1]

    def subtract(self, x, y):
        self.results.append(calcOperations.subtraction(x, y))
        return self.results[-1]

    def divide(self, x, y):
        self.results.append(calcOperations.division(x, y))
        return self.results[-1]

    def multiply(self, x, y):
        self.results.append(calcOperations.multiplication(x, y))
        return self.results[-1]

    def square(self, x):
        self.results.append(calcOperations.square(x))
        return self.results[-1]

    def squareRoot(self, x):
        self.results.append(calcOperations.squareRoot(x))
        return self.results[-1]