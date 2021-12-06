from functools import reduce

INPUT_PATH = 'input'

SLIDING_WINDOW = 3

with open(INPUT_PATH) as input_file:
    data = list(map(lambda x: int(x), input_file.read().splitlines()))

print(
    reduce(lambda x, y: x+y,
        map(lambda x: data[x] < data[x+1] if x+1 < len(data) else 0, range(len(data))),
    0)
)

print(
    reduce(lambda x,y: x+y,
        map(lambda x: reduce(lambda x, y: x+y, data[x:x+3],0) < reduce(lambda x, y: x+y, data[x+1:x+1+SLIDING_WINDOW],0), range(len(data))),
    0)
)
