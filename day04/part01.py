import re
from typing import List, Tuple

REGEX_NUMBERS = r'\d+'
compiled_pattern = re.compile(REGEX_NUMBERS)

class bold_color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

class BingoCell:
    number: int
    has_appeared: bool
    def __init__(self, number: int):
        self.number = number
        self.has_appeared = False

    def __str__(self) -> str:
        return f'{bold_color.GREEN}{self.number}{bold_color.END}' if self.has_appeared else f'{self.number}'

    def check_drawn_number(self, drawn_number: int):
        if not self.has_appeared and self.number == drawn_number:
            self.has_appeared = True


BingoMatrix = List[List[BingoCell]]

class BingoCard:
    matrix: BingoMatrix
    matrix_dimensions: Tuple[int, int]
    complete_rows: int
    complete_columns: int

    def __init__(self, matrix: BingoMatrix):
        self.matrix = matrix
        self.matrix_dimensions = self._get_matrix_dimensions()
        self.complete_rows = 0
        self.complete_columns = 0

    def __repr__(self) -> str:
        matrix_representation = ''
        for row in self.matrix:
            for matrix_cell in row:
                number_repr = str(matrix_cell)
                matrix_representation += f'{number_repr} '
            matrix_representation += '\n'
        matrix_representation += '\n'
        return matrix_representation

    def _get_matrix_dimensions(self) -> Tuple[int, int]:
        rows = len(self.matrix)
        columns = len(self.matrix[0])
        return (rows, columns)

    def _get_matrix_row_x(self, row_number: int) -> List[BingoCell]:
        return self.matrix[row_number]

    def _get_matrix_column_x(self, column_number: int) -> List[BingoCell]:
        column: List[BingoCell] = []
        for row in self.matrix:
            column.append(row[column_number])
        return column

    def check_number(self, drawn_number: int):
        for row in self.matrix:
            for bingo_cell in row:
                bingo_cell.check_drawn_number(drawn_number)

    def check_rows(self):
        for matrix_row in self.matrix:
            correct_numbers = sum([matrix_cell.has_appeared for matrix_cell in matrix_row])
            self.complete_rows += correct_numbers == self.matrix_dimensions[1]

    def check_columns(self):
        for column_number in range(self.matrix_dimensions[1]):
            correct_numbers = sum(
                [matrix_cell.has_appeared for matrix_cell in self._get_matrix_column_x(column_number)]
            )
            self.complete_columns += correct_numbers == self.matrix_dimensions[0]

    def has_won(self) -> bool:
        return self.complete_rows > 0 or self.complete_columns > 0

    def sum_unmarked_numbers(self) -> int:
        return sum([matrix_cell.number for matrix_row in self.matrix for matrix_cell in matrix_row if not matrix_cell.has_appeared])


def read_bingo_input(input_path: str) -> Tuple[List[int], List[BingoCard]]:
    with open(input_path, 'r') as bingo_input:
        bingo_lines = bingo_input.read().splitlines()
    numbers_drawn = [int(number) for number in bingo_lines[0].split(',')]
    bingo_cards: List[BingoCard] = []
    matrix = []
    for index, line in enumerate(bingo_lines[2:]):
        if line == '' or index == len(bingo_lines[2:])-1:
            bingo_cards.append(BingoCard(matrix))
            matrix = []
        else:
            matrix.append([BingoCell(int(number)) for number in compiled_pattern.findall(line)])

    return numbers_drawn, bingo_cards

if __name__ == '__main__':
    drawn_numbers, bingo_cards = read_bingo_input('input')
    print(drawn_numbers)
    winner_card = None
    last_drawn_number = -1
    for drawn_number in drawn_numbers:
        print(f'Drawn Number: {drawn_number}')
        for bingo_card in bingo_cards:
            bingo_card.check_number(drawn_number)
            bingo_card.check_columns()
            bingo_card.check_rows()
            if bingo_card.has_won():
                winner_card = bingo_card
                last_drawn_number = drawn_number
                break
        if winner_card:
            break
    print(winner_card)
    unmarked_numbers_sum = winner_card.sum_unmarked_numbers()
    final_multiplication = unmarked_numbers_sum*last_drawn_number
    print(f'Unmarked Numbers Sum: {unmarked_numbers_sum}')
    print(f'Final multiplication: {final_multiplication}')
