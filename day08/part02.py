INPUT_PATH = 'input'

with open(INPUT_PATH) as input_file:
    samples = [sample.split(' | ') for sample in input_file.read().splitlines()]

def build_decoder(input_1, input_4, input_7, input_8, inputs_with_5, inputs_with_6):
    decoder = {}
    decoder[input_1] = '1'
    decoder[input_4] = '4'
    decoder[input_7] = '7'
    decoder[input_8] = '8'
    for input_with_5 in inputs_with_5:
        if all([letter in input_with_5 for letter in input_1]):
            decoder[input_with_5] = '3'
        elif sum([letter in input_with_5 for letter in input_4]) == 3:
            decoder[input_with_5] = '5'
        else:
            decoder[input_with_5] = '2'
    for input_with_6 in inputs_with_6:
        if all([letter in input_with_6 for letter in input_4]):
            decoder[input_with_6] = '9'
        elif sum([letter in input_with_6 for letter in input_1]) == 1:
            decoder[input_with_6] = '6'
        else:
            decoder[input_with_6] = '0'
    return decoder

def check_key(decoding_key, output):
    return all([letter in decoding_key and len(output) == len(decoding_key) for letter in output])

decoded_values = []

for sample in samples:
    input_signals, outputs  = [sample[0].split(' '), sample[1].split(' ')]
    input_1 = next(filter(lambda i: len(i) == 2, input_signals))
    input_4 = next(filter(lambda i: len(i) == 4, input_signals))
    input_7 = next(filter(lambda i: len(i) == 3, input_signals))
    input_8 = next(filter(lambda i: len(i) == 7, input_signals))
    inputs_with_5 = list(filter(lambda i: len(i) == 5, input_signals))
    inputs_with_6 = list(filter(lambda i: len(i) == 6, input_signals))
    decoder = build_decoder(input_1, input_4, input_7, input_8, inputs_with_5, inputs_with_6)
    decoded_output = ''
    for output in outputs:
        decoding_key = [decoding_key for decoding_key in list(decoder) if check_key(decoding_key, output)][0]
        decoded_output += decoder[decoding_key]
    decoded_values.append(int(decoded_output))

print(sum(decoded_values))