from operations.calc_operations import BasicOperations


class Calculator:
    def __init__(self):
        self.results = []

    def add(self, x, y):
        self.results.append(BasicOperations.addition(x, y))
        return self.results[-1]

    def subtract(self, x, y):
        self.results.append(BasicOperations.subtraction(x, y))
        return self.results[-1]

    def divide(self, x, y):
        self.results.append(BasicOperations.division(x, y))
        return self.results[-1]

    def multiply(self, x, y):
        self.results.append(BasicOperations.multiplication(x, y))
        return self.results[-1]

    def square(self, x):
        self.results.append(BasicOperations.square(x))
        return self.results[-1]

    def squareRoot(self, x):
        self.results.append(BasicOperations.squareRoot(x))
        return self.results[-1]