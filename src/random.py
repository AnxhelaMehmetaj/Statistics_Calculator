import random
from random_functions import ItemFromList, ItemFromListBySeed, ItemsFromList, ItemsFromListBySeed, ListOfNum, RandomNumber, RandomNumberBySeed

class RandomGenerators:
    # Generate a random number without a seed between a range of two numbers - Both Integer and Decimal
    def RandomNumber (self, start, end):
        return RandomNumber.randomNumber(start, end).getResult()


    # Generate a random number with a seed between a range of two numbers - Both Integer and Decimal

    def randNumBySeed (self, start, end, seed):
        return RandomNumberBySeed.randomNumberBySeed(start, end, seed).getResult()

    # Generate a list of N random numbers with a seed and between a range of numbers - Both Integer and Decimal

    def ranNumBySeedList (self, start, end, n, seed):
        return ListOfNum.randomListOfNum(start, end, n, seed).getResult()

    # A random item from a list
    def random_ItemFromList(self, array):
        return ItemFromList.Random(array).getValue()

    # Set a seed and randomly select the same value from a list
    def random_ItemFromListBySeed(self, array, seed):
        return ItemFromListBySeed.randomItemsFromList(array, seed).getValue()

    # Select N number of items from a list without a seed

    def randomItemsFromList(self, array, n):
        return ItemsFromList.random_ItemsFromList(array, n).getValue()

    # Select N number of items from a list with a seed
    def randItemsBySeedFromList(self, array, n, seed):
        return ItemsFromListBySeed.randomItemsFromListBySeed(array, n, seed).getValue()