from typing import List, Tuple, TypedDict


class NumberCount(TypedDict):
    count_0: int
    count_1: int

class Submarine:

    def generate_report(self, input_path: str):
        diagnostic_raw_data = self._read_diagnostic_input(input_path)
        gamma_rate = self._generate_gamma_rate(diagnostic_raw_data)
        epsilon_rate = self._generate_epsilon_rate(diagnostic_raw_data)
        print(f'Diagnostic Report:\nGamma Rate: {gamma_rate}\nEpsilon Rate: {epsilon_rate}')
        print(f'Integers:\nGamma Rate: {int(gamma_rate, 2)}\nEpsilon Rate: {int(epsilon_rate, 2)}')
        print(f'Multiplied: {int(gamma_rate, 2)*int(epsilon_rate, 2)}')

    def _read_diagnostic_input(self, input_path: str) -> List[str]:
        with open(input_path, 'r') as f:
            diagnostic_raw_data = f.read().splitlines()
            return diagnostic_raw_data

    def _generate_gamma_rate(self, diagnostic_raw_data: List[str]) -> str:
        number_counts = self._count_numbers(diagnostic_raw_data)
        gamma_rate = ''.join(
            [str(self._most_common_number(number_count)) for number_count in number_counts])
        return gamma_rate

    def _generate_epsilon_rate(self, diagnostic_raw_data: List[str]) -> str:
        number_counts = self._count_numbers(diagnostic_raw_data)
        epsilon_rate = ''.join(
            [str(self._least_common_number(number_count)) for number_count in number_counts])
        return epsilon_rate

    def _count_numbers(self, diagnostic_raw_data: List[str]) -> List[NumberCount]:
        positions =  range(len(diagnostic_raw_data[0]))
        counts: List[NumberCount] = [{'count_0': 0, 'count_1': 1} for i in positions]
        for number in diagnostic_raw_data:
            for position in positions:
                if int(number[position]) == 0:
                    counts[position]['count_0'] += 1
                elif int(number[position]) == 1:
                    counts[position]['count_1'] += 1
        return counts

    def _most_common_number(self, number_count: NumberCount):
        return 0 if number_count['count_0'] > number_count['count_1'] else 1

    def _least_common_number(self, number_count: NumberCount):
        return 0 if number_count['count_0'] < number_count['count_1'] else 1

if __name__ == '__main__':
    submarine = Submarine()
    submarine.generate_report('input')
