import unittest
import statistics
import random
from scipy.stats import zscore as scipy_zscore
from src.statistics_calculator import StatisticsCalculator


class TestCases(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = StatisticsCalculator()

    def testInstantiateCalculator(self):
        self.assertIsInstance(self.calculator, StatisticsCalculator)

    def testMean(self):
        RandomList = []
        for i in range(0, 100000):
            RandomNumber = random.randint(0, 1000)
            RandomList.append(RandomNumber)
        expectedValue = statistics.mean(RandomList)
        actualValue = self.calculator.mean(RandomList)
        self.assertEqual(expectedValue, actualValue)

    def testMedian(self):
        RandomList = []
        for i in range(0, 100000):
            RandomNumber = random.randint(0, 1000)
            RandomList.append(RandomNumber)
        expectedValue = statistics.median(RandomList)
        actualValue = self.calculator.median(RandomList)
        self.assertEqual(expectedValue, actualValue)

    def testMode(self):
        RandomList = []
        for i in range(0, 100000):
            RandomNumber = random.randint(0, 1000)
            RandomList.append(RandomNumber)
        expectedValue = statistics.multimode(RandomList)
        actualValue = self.calculator.modes(RandomList)
        self.assertEqual(expectedValue, actualValue)

    def testVariance(self):
        RandomList = []
        for i in range(0, 100000):
            RandomNumber = random.randint(0, 1000)
            RandomList.append(RandomNumber)
        expectedValue = statistics.pvariance(RandomList)
        actualValue = self.calculator.variance(RandomList)
        self.assertAlmostEqual(expectedValue, actualValue)

    def testStandardDeviation(self):
        RandomList = []
        for i in range(0, 100000):
            RandomNumber = random.randint(0, 1000)
            RandomList.append(RandomNumber)
        expectedValue = statistics.pstdev(RandomList)
        actualValue = self.calculator.standardDeviation(RandomList)
        self.assertAlmostEqual(expectedValue, actualValue)

    def testZScore(self):
        RandomList = []
        for i in range(0, 100000):
            RandomNumber = random.randint(0, 1000)
            RandomList.append(RandomNumber)
        expectedValues = scipy_zscore(RandomList)
        actualValues = self.calculator.zScores(RandomList)
        self.assertEqual(expectedValues.size, len(actualValues))
        for i in range(0, expectedValues.size):
            self.assertAlmostEqual(expectedValues[i], actualValues[i])

    def testResultProperty(self):
        self.calculator.results.clear()
        self.assertEqual(self.calculator.results, [])


if __name__ == "__main__":
    unittest.main()