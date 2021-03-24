from scipy import stats
from scipy.stats import sem, t
import numpy as np
import random


class PopulationOperations:
    @staticmethod
    def cochrans(input):
        err = sem(input)
        std = stats.gstd(input)
        z = 1.96
        n = (((z ** 2) * .25) / (err ** 2))
        return int(n)

    @staticmethod
    def confidence_sample(confidence, sample_list):
        average = np.median(sample_list)
        std_err = sem(sample_list)
        interval = std_err * t.ppf((1 + confidence) / 2, len(sample_list) - 1)
        low = average - interval
        high = average + interval
        return low, high

    @staticmethod
    def margin_error(input_list):
        return sem(input_list)

    @staticmethod
    def sample_list(input, new_list):
        return random.sample(input, new_list)

    @staticmethod
    def sample_size(input):
        error = sem(input)
        std = stats.gstd(input)
        z = 1.96
        n = ((z * std) / error) ** 2
        return int(n)
