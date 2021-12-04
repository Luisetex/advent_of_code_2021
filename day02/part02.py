import re
from typing import List, TypedDict


COMMAND_PATTERN = re.compile(r'([a-z]+) (\d+)')

class Command(TypedDict):
    verb: str
    steps: int

class Submarine:
    position_x: int
    position_y: int
    aim: int

    def __init__(self, position_x: int = 0, position_y: int = 0, aim: int = 0):
        self.position_x = position_x
        self.position_y = position_y
        self.aim = aim

    def __repr__(self) -> str:
        return f'Current positions:\nX = {self.position_x}\nY = {self.position_y}\n'\
            f'Aim = {self.aim}\n'\
            f'Multipled result = {self.position_x*self.position_y}'

    def _move_x(self, steps:int):
        self.position_x += steps

    def _move_y(self, steps:int):
        self.position_y += steps

    def _move_aim(self, steps: int):
        self.aim += steps

    def execute_command(self, command: Command):
        verb = command['verb']
        if verb == 'forward':
            self._move_x(command['steps'])
            self._move_y(self.aim * command['steps'])
        if verb == 'down':
            self._move_aim(command['steps'])
        if verb == 'up':
            self._move_aim(-command['steps'])


def read_commands_str(file_path: str) -> List[str]:
    with open(file_path, 'r') as f:
        commands = f.read().splitlines()
        return commands

def parse_command(command_str: str) -> Command:
    match = COMMAND_PATTERN.search(command_str)
    if match:
        if len(match.groups()) == 2:
            return { 'verb': match.group(1), 'steps': int(match.group(2)) }
        else:
            raise Exception
    raise Exception

if __name__ == '__main__':
    submarine = Submarine()

    commands_str = read_commands_str('input')
    commands = [parse_command(command_str) for command_str in commands_str]

    for command in commands:
        submarine.execute_command(command)

    print(submarine)
