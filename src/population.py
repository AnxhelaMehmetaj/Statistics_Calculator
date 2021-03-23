
from operations.population_operations import PopulationOperations
from src.calculator import Calculator


class Population_Sampling_Calculator(Calculator):

    def __init__(self):
        Calculator.__init__(self)

    def random_sampling(self, input_list, new_list_length):
        self.results.append(PopulationOperations.samplelist(input_list, new_list_length))
        return self.results[-1]

    def confidence_interval_for_sample(self, confidence, sample_list):
        self.results.append(PopulationOperations.confidenceinterval(confidence

                                                                    , sample_list))
        return self.results[-1]

    def margin_error(self, input_list):
        self.results.append(PopulationOperations.marginerror(input_list))
        return self.results[-1]

    def sample_size(self, input_list):
        self.results.append(PopulationOperations.samplesize(input_list))
        return self.results[-1]

    def cochrans(self, input_list):
        self.results.append(PopulationOperations.cochrans(input_list))
        return self.results[-1]