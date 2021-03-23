import random


class ItemFromList:
    def __init__(self, array):
        self.array = array
        self.output = None
        random.seed()
        self.randomSample()

    def randomSample(self):
        if not isinstance(self.array, list):
            self.output = "ERROR"
        else:
            self.output = random.choice(self.array)

    def getValue(self):
        return self.output