import unittest
from src.calculator import Calculator
from CSV_Reader.CSVReader import readCSV


class TestCalculator(unittest.TestCase):
    calculator = None

    @classmethod
    def setUpClass(cls):
        print('')
        print('setUpClass')


    @classmethod
    def tearDownClass(cls):
        print('')
        print('tearDownClass')


    def setUp(self):
        self.calculator = Calculator()
        print('')
        print('setUp')

    # execute after every tests case function run.
    def tearDown(self):
        # release the Calculator object.
        if self.calculator is not None:
            self.calculator = None
        print('')
        print('tearDown')

    # below are function that tests Calculator class's plus, minus, multiple and divide functions.
    def testInstantiateCalculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def testAddition(self):
        rows = readCSV("tests/test_cases/Addition.csv")
        for row in rows:
            result = float(row["Result"])
            x = float(row["Value 1"])
            y = float(row["Value 2"])
            self.assertEqual(self.calculator.add(x, y), result)

    def testSubtraction(self):
        rows = readCSV("tests/test_cases/Subtraction.csv")
        for row in rows:
            result = float(row["Result"])
            y = float(row["Value 1"])
            x = float(row["Value 2"])
            self.assertEqual(self.calculator.subtract(x, y), result)

    def testDivision(self):
        self.assertRaises(ZeroDivisionError, self.calculator.divide, 1, 0)
        rows = readCSV("tests/test_cases/Division.csv")
        for row in rows:
            result = float(row["Result"])
            y = float(row["Value 1"])
            x = float(row["Value 2"])
            self.assertAlmostEqual(self.calculator.divide(x, y), result)

    def testMultiplication(self):
        rows = readCSV("tests/test_cases/Multiplication.csv")
        for row in rows:
            result = float(row["Result"])
            x = float(row["Value 1"])
            y = float(row["Value 2"])
            self.assertAlmostEqual(self.calculator.multiply(x, y), result)

    def testSquare(self):
        rows = readCSV("tests/test_cases/Square.csv")
        for row in rows:
            result = float(row["Result"])
            x = float(row["Value 1"])
            self.assertAlmostEqual(self.calculator.square(x), result)

    def testSquareRoot(self):
        rows = readCSV("tests/test_cases/SquareRoot.csv")
        for row in rows:
            result = float(row["Result"])
            x = float(row["Value 1"])
            self.assertAlmostEqual(self.calculator.squareRoot(x), result)

    def testResultProperty(self):
        self.calculator.results.clear()
        self.assertEqual(self.calculator.results, [])


if __name__ == "__main__":
    unittest.main()


