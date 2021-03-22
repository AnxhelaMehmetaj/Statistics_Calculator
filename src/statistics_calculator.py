from operations.statistics_operations import StatisticsOperations
from src.calculator import Calculator


class StatisticsCalculator(Calculator):

    def __init__(self):
        Calculator.__init__(self)

    def mean(self, input_list):
        self.results.append(StatisticsOperations.mean(input_list))
        return self.results[-1]

    def median(self, input_list):
        self.results.append(StatisticsOperations.median(input_list))
        return self.results[-1]

    def modes(self, input_list):
        self.results.append(StatisticsOperations.modes(input_list))
        return self.results[-1]

    def variance(self, input_list):
        self.results.append(StatisticsOperations.variance(input_list))
        return self.results[-1]

    def standardDeviation(self, input_list):
        self.results.append(StatisticsOperations.standardDeviation(input_list))
        return self.results[-1]

    def zScores(self, input_list):
        self.results.append(StatisticsOperations.zScore(input_list))
        return self.results[-1]