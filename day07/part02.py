INPUT_PATH = 'input'

with open(INPUT_PATH) as input_file:
    positions = input_file.read().split(',')
    crab_positions = [int(position) for position in positions]

possible_positions = range(max(crab_positions)+1)

# each step costs one more fuel: arithmetic progression

costs = list(map(
    lambda possible_position: sum(
        map(lambda crab_position: (1+abs(crab_position-possible_position)) * abs(crab_position-possible_position) / 2,
        crab_positions)),
    possible_positions))

print((min(costs)))
