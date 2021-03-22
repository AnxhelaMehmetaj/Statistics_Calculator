import random
from random_functions.RandomNumber import randomNumber


class randomNumberBySeed(randomNumber):
    def __init__(self, start, end, seed):
        super().__init__(start, end)
        random.seed(seed)
        super(randomNumberBySeed, self).generateValue()