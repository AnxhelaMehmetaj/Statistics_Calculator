from random_functions.ItemFromList import random


class random_ItemsFromList(random):
    def __init__(self, array, n):
        super().__init__(array)
        self.result = []
        self.n = n
        self.generateResult()

    def generateResult(self):
        for i in range(self.n):
            super().generateResult()
            # want to append randomly chosen value from
            # array and remove that value from the
            # list so we don't choose it again
            self.result.append(super().getValue())
            self.array.remove(super().getValue())


    def getValue(self):
        return self.result