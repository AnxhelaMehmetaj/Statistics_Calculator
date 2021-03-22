from scipy import stats
from scipy.stats import sem, t
import numpy as np
import random



class PopulationOperations:
    @staticmethod
    def samplesize(input_list):
        # confidence = 0.05
        error = sem(input_list)
        std = stats.gstd(input_list)
        z = 1.96
        n = ((z * std) / error) ** 2
        return int(n)

    @staticmethod
    def confidenceinterval(confidence, sample_list):
        n = len(sample_list)
        avg = np.mean(sample_list)
        std_err = sem(sample_list)
        interval = std_err * t.ppf((1 + confidence) / 2, n - 1)
        low = avg - interval
        high = avg + interval
        return low, high

    @staticmethod
    # The Cochran formula allows you to calculate an ideal sample size given a desired level of precision
    def cochrans(input_list):
        error = sem(input_list)
        std = stats.gstd(input_list)
        z = 1.96
        n = (((z ** 2) * .25) / (error ** 2))
        return int(n)

    @staticmethod
    def marginerror(input_list):
        return sem(input_list)

    @staticmethod
    # Takes a list as input and return a new list with a sample of the original list
    def samplelist(input_list, new_list_length):
        '''if not input_list:
            return "Error: input list was empty" '''
        if new_list_length > len(input_list):
            return "Error: sample list length is bigger than original list"
        return random.sample(input_list, new_list_length)

