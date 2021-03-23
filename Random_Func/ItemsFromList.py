from Random_Func.ItemFromList import ItemFromList


class ItemsFromList(ItemFromList):
    def __init__(self, array, num):
        super().__init__(array)
        self.items = []
        self.num = num
        self.generateChoices()

    def generateChoices(self):
        if self.num > len(self.array):
            self.items = "ERROR"
        else:
            for i in range(self.num):
                super().randomSample()
                self.items.append(super().getValue())
                self.array.remove(super().getValue())

    def getValue(self):
        return self.items