import unittest
import random

from src.population_calc import PopulationCalc

seedNum = 50  # KEEP AT 50 because values are checked against this seed
random.seed(seedNum)
original_list = []
for x in range(50):
    original_list.append(float(random.randint(40, 50)))


class SamplingTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calc_obj = PopulationCalc()

    def testInstantiateCalculator(self):
        self.assertIsInstance(self.calc_obj, PopulationCalc)

    def test_random_sample(self):
        print("******test_random_sampling******")
        sample_list = self.calc_obj.random_sample(original_list, 8)
        print("Random Sample List")
        print(sample_list, "\n")
        self.assertEqual(sample_list, [49.0, 44.0, 42.0, 46.0, 43.0, 47.0, 50.0, 49.0])




    def test_margin_error(self):
        print("******test_margin_error******")
        res = self.calc_obj.margin_error(original_list)
        print("Margin of Error:", res, "\n")
        self.assertEqual(res, 0.41797373220852824)

    def test_sample_size(self):
        print("******test_sample_size******")
        res = self.calc_obj.sample_size(original_list)
        print("Sample Size:", res, "\n")
        self.assertEqual(res, 25)

    def test_cochrans(self):
        print("******test_cochrans******")
        res = self.calc_obj.cochrans(original_list)
        print("Cochrans' Sample Size:", res, "\n")
        self.assertEqual(res, 5)

    def testResultProperty(self):
        self.calc_obj.results.clear()
        self.assertEqual(self.calc_obj.results, [])


if __name__ == '__main__':
    unittest.main()