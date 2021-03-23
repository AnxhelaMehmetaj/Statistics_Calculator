import random


class randomChoice:
    def __init__(self, start, end):
        random.seed()
        self.start = start
        self.end = end
        self.output = None
        self.generateValue()

    def generateValue(self):
        if (type(self.start) is int) & (type(self.end) is int):
            self.output = random.randint(self.start, self.end)
        # If type of start and end is float
        elif (type(self.start) is float) & (type(self.end) is float):
            self.output = random.uniform(self.start, self.end)
        else:
            self.output = "ERROR: Both value are either not the same type or wrong type "

    def getResult(self):
        return self.output