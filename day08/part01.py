INPUT_PATH = 'input'

with open(INPUT_PATH) as input_file:
    samples = [sample.split(' | ') for sample in input_file.read().splitlines()]

def is_segment_known(segment):
    length_segment = len(segment)
    return length_segment == 2 or length_segment == 3 or length_segment == 4 or length_segment == 7


output_segments = (map(lambda sample: sample[1].split(' '), samples))
output_segments = [sample[1].strip().split(' ') for sample in samples]
filter_output_segments = [segment for output in output_segments for segment in output if is_segment_known(segment)]
print(len(filter_output_segments))