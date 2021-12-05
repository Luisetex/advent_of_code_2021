with open('input') as input_file:
    input_readings = input_file.read().splitlines()

gamma_rate = ''
epislon_rate = ''

for bit in range(len(input_readings[0])):
    column = [int(number[bit]) for number in input_readings]
    gamma_rate += (str(max(column, key=column.count)))
    epislon_rate += (str(min(column, key=column.count)))

print(f'A: {int(gamma_rate, 2)*int(epislon_rate, 2)}')

oxygen = input_readings.copy()
co2 = input_readings.copy()

for bit in range(len(input_readings[0])):
    oxygen_column = [int(number[bit]) for number in oxygen]
    co2_column = [int(number[bit]) for number in co2]
    oxygen_count = (oxygen_column.count(0), oxygen_column.count(1))
    most_common = '0' if oxygen_column.count(0) > oxygen_column.count(1) else '1'
    co2_count = (co2_column.count(0), co2_column.count(1))
    least_common = '0' if co2_column.count(0) <= co2_column.count(1) else '1'
    if len(oxygen) > 1:
        oxygen = [input_reading for input_reading in oxygen if input_reading[bit] == most_common]
    if len(co2) > 1:
        co2 = [input_reading for input_reading in co2 if input_reading[bit] == least_common]

print(f'B: {int(oxygen[0], 2)*int(co2[0],2)}')
