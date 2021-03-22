from operations.basic_operations import BasicOperations


class StatisticsOperations:
    @staticmethod
    def mean(numbers):
        sum = 0.0
        for number in numbers:
            sum = BasicOperations.addition(sum, number)
        return BasicOperations.division(sum, len(numbers))

    @staticmethod
    def median(numbers:float):
        numbers = sorted(numbers)
        if len(numbers) % 2 == 1:
            middleIndex = int(BasicOperations.division(len(numbers) - 1, 2))
            median = numbers[middleIndex]
        else:
            firstMiddleIndex = int(BasicOperations.subtraction(BasicOperations.division(len(numbers) - 1, 2), 0.5))
            secondMiddleIndex = int(BasicOperations.addition(BasicOperations.division(len(numbers) - 1, 2), 0.5))
            median = BasicOperations.division(BasicOperations.addition(numbers[firstMiddleIndex], numbers[secondMiddleIndex]), 2)
        return float(median)

    @staticmethod
    def modes(numbers):
        dictionary = {}
        for number in numbers:
            if number in dictionary.keys():
                dictionary[number] += 1
            else:
                dictionary[number] = 1

        max_repeated = 0
        for number in numbers:
            if dictionary[number] > max_repeated:
                max_repeated = dictionary[number]

        modes = []
        for number in dictionary.keys():
            if dictionary[number] == max_repeated:
                modes.append(number)
        return modes

    @staticmethod
    def variance(numbers):
        mean = StatisticsOperations.mean(numbers)
        Differences = []
        for number in numbers:
            Differences.append(BasicOperations.square(BasicOperations.subtraction(mean, number)))
        variance = BasicOperations.division(sum(Differences), len(numbers))
        return variance

    @staticmethod
    def standardDeviation(numbers):
        standardDeviation = BasicOperations.squareRoot(StatisticsOperations.variance(numbers))
        return standardDeviation

    @staticmethod
    def zScore(numbers: list) -> list:
        zScores = []
        standardDeviation = StatisticsOperations.standardDeviation(numbers)
        mean = StatisticsOperations.mean(numbers)
        for number in numbers:
            zScores.append(BasicOperations.division(BasicOperations.subtraction(number, mean), standardDeviation))
        return zScores