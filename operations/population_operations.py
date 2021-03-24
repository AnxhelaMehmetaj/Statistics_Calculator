from scipy import stats
from scipy.stats import sem, t
import numpy as np
import random


class PopulationOperations:
    @staticmethod
    def cochrans(input_list):
        err = sem(input_list)
        std = stats.gstd(input_list)
        z = 1.96
        n = (((z ** 2) * .25) / (err ** 2))
        return int(n)

    @staticmethod
    def confidence_sample(confidence, sample_list):
        length = len(sample_list)
        average = np.median(sample_list)
        std_error = sem(sample_list)
        interval = std_error * t.ppf((1 + confidence) / 2, length - 1)
        low = average - interval
        high = average + interval
        return low, high

    @staticmethod
    def margin_error(input_list):
        return sem(input_list)

    @staticmethod
    def sample_list(input_list, new_list_length):
        return random.sample(input_list, new_list_length)

    @staticmethod
    def sample_size(input_list):
        error = sem(input_list)
        std = stats.gstd(input_list)
        z = 1.96
        n = ((z * std) / error) ** 2
        return int(n)
