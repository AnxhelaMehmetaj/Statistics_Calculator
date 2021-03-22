import random


class randomNumber:
    def __init__(self, start, end):
        random.seed()
        self.start = start
        self.end = end
        self.result = None
        self.generateResult()

    def generateResult(self):
        if (type(self.start) is int) & (type(self.end) is int):
            self.result= random.randint(self.start, self.end)
        elif (type(self.start) is float) & (type(self.end) is float):
            self.result = random.uniform(self.start, self.end)
        else:
            self.result = "ERROR: Both value are either not the same type"

    def getResult(self):
        return self.result