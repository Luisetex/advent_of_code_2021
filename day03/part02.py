from typing import List, Tuple, TypedDict


class NumberCount(TypedDict):
    count_0: int
    count_1: int

class Submarine:

    def generate_report(self, input_path: str):
        diagnostic_raw_data = self._read_diagnostic_input(input_path)
        number_counts = self._count_numbers(diagnostic_raw_data)
        gamma_rate = self._generate_gamma_rate(number_counts)
        epsilon_rate = self._generate_epsilon_rate(number_counts)
        oxygen_generator_rate = self._generate_oxygen_generator_rate(diagnostic_raw_data)
        co2_scrubber_rate = self._generate_co2_scrubber_rate(diagnostic_raw_data)

        print(f'Diagnostic Report:\nGamma Rate: {gamma_rate}\nEpsilon Rate: {epsilon_rate}')
        print(f'Integers:\nGamma Rate: {gamma_rate}\nEpsilon Rate: {epsilon_rate}')
        print(f'Multiplied: {int(gamma_rate, 2)*int(epsilon_rate, 2)}')
        print(f'Oxygen Generator Rate: {oxygen_generator_rate}')
        print(f'CO2 Scrubber Rate: {co2_scrubber_rate}')
        print(f'Multiplied: {int(oxygen_generator_rate, 2)*int(co2_scrubber_rate, 2)}')


    def _read_diagnostic_input(self, input_path: str) -> List[str]:
        with open(input_path, 'r') as f:
            diagnostic_raw_data = f.read().splitlines()
            return diagnostic_raw_data

    def _generate_gamma_rate(self, number_counts: List[NumberCount]) -> str:
        gamma_rate = ''.join(
            [str(self._most_common_number(number_count)) for number_count in number_counts])
        return gamma_rate

    def _generate_epsilon_rate(self, number_counts: List[NumberCount]) -> str:
        epsilon_rate = ''.join(
            [str(self._least_common_number(number_count)) for number_count in number_counts])
        return epsilon_rate

    def _generate_oxygen_generator_rate(self,
    diagnostic_raw_data: List[str]) -> str:
        possible_numbers: List[str] = diagnostic_raw_data.copy()
        for bit_position in range(len(possible_numbers[0])):
            number_counts = self._count_numbers(possible_numbers)
            most_common_number = self._most_common_number(number_counts[bit_position])
            most_common_number_count = number_counts[bit_position]['count_0'] if most_common_number == 0 else number_counts[bit_position]['count_1']
            possible_numbers = self._filter_numbers_with_bit(
                possible_numbers, bit_position, most_common_number, most_common_number_count)

        return possible_numbers[0]

    def _generate_co2_scrubber_rate(self,
    diagnostic_raw_data: List[str]) -> str:
        possible_numbers: List[str] = diagnostic_raw_data.copy()
        for bit in range(len(possible_numbers[0])):
            if len(possible_numbers) == 1:
                break
            number_counts = self._count_numbers(possible_numbers)
            least_common_number = self._least_common_number(number_counts[bit])
            least_common_number_count = number_counts[bit]['count_0'] if least_common_number == 0 else number_counts[bit]['count_1']
            possible_numbers = self._filter_numbers_with_bit(
                possible_numbers, bit, least_common_number, least_common_number_count)

        return possible_numbers[0]

    def _count_numbers(self, diagnostic_raw_data: List[str]) -> List[NumberCount]:
        positions =  range(len(diagnostic_raw_data[0]))
        counts: List[NumberCount] = [{'count_0': 0, 'count_1': 0} for _ in positions]
        for number in diagnostic_raw_data:
            for position in positions:
                if int(number[position]) == 0:
                    counts[position]['count_0'] += 1
                elif int(number[position]) == 1:
                    counts[position]['count_1'] += 1
        return counts

    def _filter_numbers_with_bit(self, possible_numbers: List[str], reference_bit_position: int, reference_value: int, total: int):
        filtered_numbers: List[str] = []
        for number in possible_numbers:
            if len(filtered_numbers) >= total:
                break
            if number[reference_bit_position] == str(reference_value):
                filtered_numbers.append(number)
        return filtered_numbers


    def _most_common_number(self, number_count: NumberCount) -> int:
        return 0 if number_count['count_0'] > number_count['count_1'] else 1

    def _least_common_number(self, number_count: NumberCount):
        return 0 if number_count['count_0'] <= number_count['count_1'] else 1


if __name__ == '__main__':
    submarine = Submarine()
    submarine.generate_report('input')
