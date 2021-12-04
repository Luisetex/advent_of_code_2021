from typing import List


class Input:
    value: int
    has_increased: bool
    def __init__(self, value: int):
        self.value = value
        self.has_increased = False
        self.sliding_window = 0

    def __repr__(self):
        return f'Value: {self.value}. Has increased? {self.has_increased}\n'

def read_inputs(file_path: str) -> List[Input]:
    with open(file_path, 'r') as f:
        inputs_str = f.read().splitlines()
        return [Input(int(input_str)) for input_str in inputs_str]

def sliding_window_sum(inputs: List[Input], list_index: int, window_size: int = 3) -> int:
    return sum([single_input.value for single_input in inputs[list_index:list_index+window_size]])

def check_next_increase(inputs: List[Input]) -> List[Input]:
    initial_value = None
    for list_input in inputs:
        if initial_value == None:
            initial_value = list_input
        else:
            list_input.has_increased = list_input.sliding_window > initial_value.sliding_window
        initial_value = list_input
    return inputs

def compute_sliding_window(inputs: List[Input]) -> List[Input]:
    for index, single_input in enumerate(inputs):
        single_input.sliding_window = sliding_window_sum(inputs, index, 3)
    return check_next_increase(inputs)

if __name__ == '__main__':
    inputs = read_inputs('input')
    inputs = compute_sliding_window(inputs)
    print(inputs)
    print(sum([single_input.has_increased for single_input in inputs]))
