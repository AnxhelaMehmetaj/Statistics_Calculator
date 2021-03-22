from random_functions.RandomNumberBySeed import randomNumberBySeed


class randomListOfNum(randomNumberBySeed):
    def __init__(self, start, end, n, seed):
        super().__init__(start, end, seed)
        self.n = n
        self.result = []
        self.generateListResult()

    def generateListResult(self):
        for i in range(self.n):
            super().generateResult()
            self.result.append(super().getResult())

    def getResult(self):
        return self.result