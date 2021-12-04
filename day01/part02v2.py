from typing import List



class Input:
    value: int
    has_increased: bool
    sliding_window_sum: int

    def __init__(self, value: int):
        self.value = value
        self.has_increased = False
        self.sliding_window_sum = 0

    def __repr__(self):
        return f'Value: {self.value}. Has increased? {self.has_increased}\n'

class Submarine:

    def generate_depth_report(self, report_path: str):
        inputs = self._read_inputs(report_path)
        for index, single_input in enumerate(inputs):
            single_input.sliding_window_sum = self._sum_sliding_window(inputs, index, 3)
        processed_inputs = self._check_next_increase(inputs)
        print((sum([single_input.has_increased for single_input in processed_inputs])))

    def _read_inputs(self, file_path: str) -> List[Input]:
        with open(file_path, 'r') as f:
            inputs_str = f.read().splitlines()
            return [Input(int(input_str)) for input_str in inputs_str]

    def _sum_sliding_window(self,
        inputs: List[Input],
        list_index: int,
        window_size: int = 3
        ) -> int:
        return sum(
            [single_input.value for single_input in inputs[
                list_index:list_index+window_size]])

    def _check_next_increase(self, processed_inputs: List[Input]) -> List[Input]:
        initial_value = None
        for list_input in processed_inputs:
            if initial_value == None:
                initial_value = list_input
            else:
                list_input.has_increased =\
                    list_input.sliding_window_sum > initial_value.sliding_window_sum
            initial_value = list_input
        return processed_inputs

if __name__ == '__main__':
    submarine = Submarine()
    submarine.generate_depth_report('input')
