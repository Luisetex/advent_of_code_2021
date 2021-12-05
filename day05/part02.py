import re
from typing import List, Tuple

REGEX_NUMBERS = r'\d+'
compiled_pattern = re.compile(REGEX_NUMBERS)

class Board:
    matrix: List[List[int]]

    def __repr__(self):
        string = ''
        for row in self.matrix:
            for number in row:
                string += f'{number} '
            string +='\n'
        return string

    def __init__(self, readings: List[List[str]]):
       max_x = max([coordinate for sublist in [(int(reading[0]), int(reading[3])) for reading in readings] for coordinate in sublist])+1
       max_y = max([coordinate for sublist in [(int(reading[1]), int(reading[2])) for reading in readings] for coordinate in sublist])+1
       self.matrix = [[0 for col in range(max_y)] for row in range(max_x)]

    def get_dimension(self):
        dim_x = len(self.matrix)
        dim_y = len(self.matrix[0])
        return dim_x, dim_y

    def _get_consecutive_points(self, point_a:int, point_b: int):
        return range(point_a, point_b+1) if point_a < point_b else range(point_a, point_b-1, -1)

    def get_line_points(self, reading: List[str]) -> List[Tuple[int, int]]:
        reading_int = [int(point) for point in reading]
        points: List[Tuple[int, int]] = [(0,0)]
        if reading_int[0] == reading_int[2]:
            x_pos = reading_int[0]
            points_y = self._get_consecutive_points(reading_int[1], reading_int[3])
            points = [(x,y) for x, y in zip([x_pos]*len(points_y), points_y)]
        elif reading_int[1] == reading_int[3]:
            y_pos = reading_int[1]
            points_x = self._get_consecutive_points(reading_int[0], reading_int[2])
            points = [(x,y) for x, y in zip(points_x, [y_pos]*len(points_x))]
        else:
            points_x = self._get_consecutive_points(reading_int[0], reading_int[2])
            points_y = self._get_consecutive_points(reading_int[1], reading_int[3])
            points = [(x,y) for x, y in zip(points_x, points_y)]
        return points

    def mark_point(self, points: List[Tuple[int, int]]):
        for point in points:
            x_pos, y_pos = point
            self.matrix[y_pos][x_pos] += 1

    def process_readings(self, readings: List[List[str]]):
        for reading in readings:
            line_points = self.get_line_points(reading)
            self.mark_point(line_points)

    def dangerous_count(self) -> int:
        return len([point for row in self.matrix for point in row if point > 1])


def read_input(input_path: str) -> List[List[str]]:
    with open(input_path, 'r') as input_file:
        lines = input_file.read().splitlines()
        readings_str = [compiled_pattern.findall(line) for line in lines]
    return readings_str

def is_diagonal(reading: List[str]) -> bool:
    return reading[0] != reading[2] and reading[1] != reading[3]


if __name__ == '__main__':
    readings = read_input('input')

    board = Board(readings)
    board.process_readings(readings)
    print(board.dangerous_count())
