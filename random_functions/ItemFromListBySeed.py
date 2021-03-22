import random
from random_functions.ItemFromList import random


class randomItemsFromList(random):
    def __init__(self, array, seed):
        super().__init__(array)
        self.items = []
        random.seed(seed)
        super().generateResult()