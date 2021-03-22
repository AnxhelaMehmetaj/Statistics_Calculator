import unittest
from src.random import RandomGenerators

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.randGenerator = RandomGenerators()
        print('')
        print('setUp')

    # execute after every tests case function run.
    def tearDown(self):
        # release the Calculator object.
        if self.randGenerator is not None:
            self.randGenerator = None
        print('')
        print('tearDown')

    def test_random_number(self):
        print("*"*10+"Random Number Test"+"*"*10)
        print("Random Number: ")
        print(self.randGenerator.randNum(0,100))

    def test_random_number_by_seed_float(self):
        print("*" * 10 + "Random Float Number By Seed Test" + "*" * 10)
        #print(self.randGenerator.randInt(0, 100, 2))
        startVal = 0.0
        endVal = 100.0
        seed = 10
        print("Testing Random Numbers by seed:", seed)
        randomFloat = self.randGenerator.randNumBySeed(startVal, endVal, seed)
        print(randomFloat, self.randGenerator.randNumBySeed(startVal, endVal, seed))
        self.assertEqual(randomFloat, self.randGenerator.randNumBySeed(startVal, endVal, seed))

    def test_random_number_by_seed_int(self):
        print("*" * 10 + "Random Int Number By Seed Test" + "*" * 10)
        #print(self.randGenerator.randInt(0, 100, 2))
        startVal = 0
        endVal = 100
        seed = 3
        print("Testing Random Numbers by seed:", seed)
        randomInt = self.randGenerator.randNumBySeed(startVal, endVal, seed)
        print(randomInt, self.randGenerator.randNumBySeed(startVal, endVal, seed))
        self.assertEqual(randomInt, self.randGenerator.randNumBySeed(startVal, endVal, seed))

    def test_random_number_list_int_by_seed(self):
        print("*" * 10 + "Random Number List By Seed Test" + "*" * 10)
        startVal = 0
        endVal = 50
        seed = self.randGenerator.randNum(0, 10)
        listSize = 12
        print("Testing Random Numbers by seed:", seed)
        randomListInt = self.randGenerator.ranNumBySeedList(startVal, endVal, listSize, seed)
        print(randomListInt, self.randGenerator.ranNumBySeedList(startVal, endVal, listSize, seed))
        self.assertEqual(randomListInt, self.randGenerator.ranNumBySeedList(startVal, endVal,  listSize, seed))

    def test_random_item_from_list(self):
        print("*" * 10 + "Random Item From List Test" + "*" * 10)
        randomList = self.randGenerator.ranNumBySeedList(0, 500, 10, 20)
        print("Testing random item from list")
        randomItemFromList = self.randGenerator.randItemFromList(randomList)
        print("List of Items:")
        print(randomList)
        print("Random Item from list:")
        print(randomItemFromList)

    def test_random_items_from_list(self):
        print("*" * 10 + "Random Items From List Test" + "*" * 10)
        randomList = self.randGenerator.ranNumBySeedList(0, 500, 10, 66)
        numItemsFromList = 7
        print("List of Items:")
        print(randomList)
        print("Random Items from list:")
        print(self.randGenerator.randItemsFromList(randomList, numItemsFromList))

    def test_random_items_from_list_by_seed(self):
        print("*" * 10 + "Random Items From List Test By Seed" + "*" * 10)
        randomList = self.randGenerator.ranNumBySeedList(0, 500, 10, 12)
        numItemsFromList = 7
        seed = 12
        expectedList = self.randGenerator.randItemsBySeedFromList(randomList, numItemsFromList, seed)
        print("List of Items:")
        print(randomList)
        print("Random Items from list:")
        print(expectedList)
        self.assertEqual(expectedList, self.randGenerator.randItemsBySeedFromList(randomList, numItemsFromList, seed))



if __name__ == '__main__':
    unittest.main()