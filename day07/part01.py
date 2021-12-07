INPUT_PATH = 'input'

with open(INPUT_PATH) as input_file:
    positions = input_file.read().split(',')
    crab_positions = [int(position) for position in positions]

possible_positions = range(max(crab_positions)+1)

costs = list(map(
    lambda possible_position: sum(
        map(lambda crab_position: abs(crab_position-possible_position),
        crab_positions)),
    possible_positions))

print((min(costs)))