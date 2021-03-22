import random
from random_functions.ItemsFromList import random_ItemsFromList


class randomItemsFromListBySeed(random_ItemsFromList):
    def __init__(self, array, n, seed):
        super().__init__(array, n)
        self.seed = seed
        random.seed(self.seed)
        super().generatedResult()