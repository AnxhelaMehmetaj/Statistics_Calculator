from operations.statistics_operations import StatisticsOperations
from src.calculator import Calculator


class StatisticsCalculator(Calculator):

    def __init__(self):
        Calculator.__init__(self)

    def mean(self, inputnumbers: list) -> float:
        self.results.append(StatisticsOperations.mean(inputnumbers))
        return self.results[-1]

    def median(self, inputnumbers:float):
        self.results.append(StatisticsOperations.median(inputnumbers))
        return self.results[-1]



    def variance(self, inputnumbers: list) -> float:
        self.results.append(StatisticsOperations.variance(inputnumbers))
        return self.results[-1]

    def standardDeviation(self, inputnumbers: list) -> float:
        self.results.append(StatisticsOperations.standardDeviation(inputnumbers))
        return self.results[-1]

    def zScores(self, inputnumbers: list) -> list:
        self.results.append(StatisticsOperations.zScore(inputnumbers))
        return self.results[-1]