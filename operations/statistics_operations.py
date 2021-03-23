from operations.calc_operations import calcOperations


class StatisticsOperations:
    @staticmethod
    def mean(numbers):
        sum = 0.0
        for number in numbers:
            sum = calcOperations.addition(sum, number)
        return calcOperations.division(sum, len(numbers))

    @staticmethod
    def median(numbers: float):
        numbers = sorted(numbers)
        if len(numbers) % 2 == 1:
            centerIndex = int(calcOperations.division(len(numbers) - 1, 2))
            median = numbers[centerIndex]
        else:
            leftIndex = int(calcOperations.subtraction(calcOperations.division(len(numbers) - 1, 2), 0.5))
            rightIndex = int(calcOperations.addition(calcOperations.division(len(numbers) - 1, 2), 0.5))
            median = calcOperations.division(calcOperations.addition(numbers[leftIndex], numbers[rightIndex]), 2)
        return float(median)

    @staticmethod
    def modes(numbers: list):
        dictionary = {}
        for number in numbers:
            if number in dictionary.keys():
                dictionary[number] += 1
            else:
                dictionary[number] = 1

        repeatednum = 0
        for number in numbers:
            if dictionary[number] > repeatednum:
                repeatednum = dictionary[number]

        modes = []
        for number in dictionary.keys():
            if dictionary[number] == repeatednum:
                modes.append(number)
        return modes

    @staticmethod
    def variance(numbers: list) -> float:
        mean = StatisticsOperations.mean(numbers)
        squaredDifferences = []
        for number in numbers:
            squaredDifferences.append(calcOperations.square(calcOperations.subtraction(mean, number)))
        variance = calcOperations.division(sum(squaredDifferences), len(numbers))
        return variance

    @staticmethod
    def standardDeviation(numbers: list) -> float:
        standardDeviation = calcOperations.squareRoot(StatisticsOperations.variance(numbers))
        return standardDeviation

    @staticmethod
    def zScore(numbers: list) -> list:
        zScores = []
        standardDeviation = StatisticsOperations.standardDeviation(numbers)
        mean = StatisticsOperations.mean(numbers)
        for number in numbers:
            zScores.append(calcOperations.division(calcOperations.subtraction(number, mean), standardDeviation))
        return zScores