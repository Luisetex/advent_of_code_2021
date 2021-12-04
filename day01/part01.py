
from typing import List

class Input:
    value: int
    has_increased: bool
    def __init__(self, value: int):
        self.value = value
        self.has_increased = False

    def __repr__(self):
        return f'Value: {self.value}. Has increased? {self.has_increased}\n'

class Submarine:

    def generate_depth_report(self, report_path: str):
        raw_inputs = self._read_inputs(report_path)
        processed_inputs = self._check_next_increase(raw_inputs)
        print((sum([single_input.has_increased for single_input in processed_inputs])))

    def _read_inputs(self, file_path: str) -> List[Input]:
        with open(file_path, 'r') as f:
            inputs_str = f.read().splitlines()
            return [Input(int(input_str)) for input_str in inputs_str]

    def _check_next_increase(self, inputs: List[Input]) -> List[Input]:
        initial_value = None
        for list_input in inputs:
            if initial_value == None:
                initial_value = list_input
            else:
                list_input.has_increased = list_input.value > initial_value.value
            initial_value = list_input
        return inputs

if __name__ == '__main__':
    submarine = Submarine()
    submarine.generate_depth_report('input')
