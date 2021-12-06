from itertools import count
from typing import List

def read_input(path: str) -> List[int]:
    with open(path, 'r') as input_file:
        lanternfishes = [(int(cycle)) for cycle in input_file.read().split(',')]
    return lanternfishes

lanternfishes = read_input('input')
possible_states = 9
count_fishes_per_state = [0] * possible_states

for fish_days in lanternfishes:
    count_fishes_per_state[fish_days] += 1

for day in range(256):
    newborns = count_fishes_per_state[0]
    for index in range(len(count_fishes_per_state)):
        if index != 0:
            count_fishes_per_state[index-1] += count_fishes_per_state[index]
            count_fishes_per_state[index] = 0
    count_fishes_per_state[8] = newborns
    count_fishes_per_state[6] += newborns
    count_fishes_per_state[0] -= newborns
print(sum(count_fishes_per_state))
