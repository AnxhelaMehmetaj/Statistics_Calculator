from operations.population_operations import PopulationOperations
from src.calculator import Calculator


class PopulationCalc(Calculator):

    def __init__(self):
        Calculator.__init__(self)

    def random_sample(self, input, new_list_length):
        self.results.append(PopulationOperations.sample_list(input, new_list_length))
        return self.results[-1]

    def confidence_sample(self, confidence, new_list):
        self.results.append(PopulationOperations.confidence_sample(confidence, new_list))
        return self.results[-1]

    def margin_error(self, input):
        self.results.append(PopulationOperations.margin_error(input))
        return self.results[-1]

    def sample_size(self, input):
        self.results.append(PopulationOperations.sample_size(input))
        return self.results[-1]

    def cochrans(self, input):
        self.results.append(PopulationOperations.cochrans(input))
        return self.results[-1]