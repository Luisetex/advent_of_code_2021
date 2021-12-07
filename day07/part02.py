INPUT_PATH = 'input'

with open(INPUT_PATH) as input_file:
    positions = input_file.read().split(',')
    crab_positions = [int(position) for position in positions]

possible_positions = range(max(crab_positions)+1)

"""
The cost of the fuel increases by one in each step -> Arithmetic progression
Sum of members in a finite arithmetic progression: Sn = (n/2) * (a1+an)
Notation:
    a1: first element (1)
    an: last element ( abs(crab_position-possible_position) )
    d: difference between two consecutive elements a(n-1) and a(n)
    n: number of "steps" to get from a1 to an. As d = 1, n = an
For more info: https://en.wikipedia.org/wiki/Arithmetic_progression
"""

costs = list(map(
    lambda possible_position: sum(
        map(lambda crab_position: (1+abs(crab_position-possible_position)) * abs(crab_position-possible_position) / 2,
        crab_positions)),
    possible_positions))

print((min(costs)))
