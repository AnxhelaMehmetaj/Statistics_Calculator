import unittest
from src.randomNumbers import RandomSamples

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.sample = RandomSamples()
        print('')
        print('setUp')

    def tearDown(self):
        if self.sample is not None:
            self.sample = None
        print('')
        print('tearDown')

    def test_random_number(self):
        print("******** Random Number Test **********")
        print("Random Number: ")
        print(self.sample.randNum(0, 100))

    def float_random_number_by_seed(self):
        print(" Random Float Number By Seed Test" )

        first = 0.0
        last = 100.0
        seed = 10
        print(" Random Numbers by seed:", seed)
        randomFloat = self.sample.randNumBySeed(first, last, seed)
        print(randomFloat, self.sample.randNumBySeed(first, last, seed))
        self.assertEqual(randomFloat, self.sample.randNumBySeed(first, last, seed))

    def int_random_number_by_seed(self):
        print("Random Int Number By Seed Test")
        first = 0
        last= 100
        seed = 3
        print("Random Numbers by seed:", seed)
        randomInt = self.sample.randNumBySeed(first, last, seed)
        print(randomInt, self.sample.randNumBySeed(first, last, seed))
        self.assertEqual(randomInt, self.sample.randNumBySeed(first, last, seed))

    def test_random_number_list_int_by_seed(self):
        print("*" * 10 + "Random Number List By Seed " + "*" * 10)
        startVal = 0
        endVal = 50
        seed = self.sample.randNum(0, 10)
        listSize = 12
        print("Random Numbers by seed:", seed)
        randomListInt = self.sample.ranNumBySeedList(startVal, endVal, listSize, seed)
        print(randomListInt, self.sample.ranNumBySeedList(startVal, endVal, listSize, seed))
        self.assertEqual(randomListInt, self.sample.ranNumBySeedList(startVal, endVal,  listSize, seed))

    def test_random_item_from_list(self):
        print("*" * 10 + "Random Item From List Test" + "*" * 10)
        randomList = self.sample.ranNumBySeedList(0, 500, 10, 20)
        print("Testing random item from list")
        randomItemFromList = self.sample.randItemFromList(randomList)
        print("List of Items:")
        print(randomList)
        print("Random Item from list:")
        print(randomItemFromList)

    def test_random_items_from_list(self):
        print("*" * 10 + "Random Items From List Test" + "*" * 10)
        randomList = self.sample.ranNumBySeedList(0, 500, 10, 66)
        numItemsFromList = 7
        print("List of Items:")
        print(randomList)
        print("Random Items from list:")
        print(self.sample.randItemsFromList(randomList, numItemsFromList))

    def test_random_items_from_list_by_seed(self):
        print("*" * 10 + "Random Items From List Test By Seed" + "*" * 10)
        randomList = self.sample.ranNumBySeedList(0, 500, 10, 12)
        numItemsFromList = 7
        seed = 12
        expectedList = self.sample.randItemsBySeedFromList(randomList, numItemsFromList, seed)
        print("List of Items:")
        print(randomList)
        print("Random Items from list:")
        print(expectedList)
        self.assertEqual(expectedList, self.sample.randItemsBySeedFromList(randomList, numItemsFromList, seed))



if __name__ == '__main__':
    unittest.main()