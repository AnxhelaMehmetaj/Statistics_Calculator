import random

class Random:
    def __init__(self, arr):
        self.arr = arr
        self.output = None
        random.seed()
        self.generatedChoice()

    def generatedChoice(self):
        if isinstance(self.arr, list):
            self.result = random.choice(self.arr)

    def getValue(self):
        return self.result