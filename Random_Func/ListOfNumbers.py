from Random_Func.NumberBySeed import NumberBySeed


class randListOfNum(NumberBySeed):
    def __init__(self, start, end, n, seed):
        super().__init__(start, end, seed)
        self.n = n
        self.resultList = []
        self.outputList()

    def outputList(self):
        for i in range(self.n):
            super().generateValue()
            self.resultList.append(super().getResult())

    def getResult(self):
        return self.resultList