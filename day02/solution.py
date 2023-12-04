import re
import os

dir_path = os.path.dirname(os.path.realpath(__file__))


## Part 1
def is_possible_reveal(
    revelead_blue: int,
    revealed_green: int,
    revelead_red: int,
    total_blue: int,
    total_green: int,
    total_red: int,
) -> bool:
    return (
        (revelead_blue <= total_blue)
        and (revealed_green <= total_green)
        and (revelead_red <= total_red)
    )


def parse_game(line: str) -> list[list]:
    reveals = line.strip("\n").split(": ")[1].split("; ")
    return [re.split(", | ", reveal) for reveal in reveals]


def is_possible_game(
    line: str, total_blue: int, total_green: int, total_red: int
) -> bool:
    game = parse_game(line)
    for reveal in game:
        blue = green = red = 0
        for i in range(len(reveal) // 2):
            if reveal[2 * i + 1] == "blue":
                blue = int(reveal[2 * i])
            elif reveal[2 * i + 1] == "green":
                green = int(reveal[2 * i])
            elif reveal[2 * i + 1] == "red":
                red = int(reveal[2 * i])
        if not is_possible_reveal(blue, green, red, total_blue, total_green, total_red):
            return False
    return True


def solver_part_1(
    input_path: str, total_blue: int, total_green: int, total_red: int
) -> int:
    with open(input_path, "r") as input_file:
        input_lines = input_file.readlines()
    possible_games = map(
        lambda x: is_possible_game(x, total_blue, total_green, total_red), input_lines
    )
    return sum([i + 1 for i, x in enumerate(possible_games) if x])


solution_part_1 = solver_part_1(
    os.path.join(dir_path, "inputs/part1"), total_blue=14, total_green=13, total_red=12
)
print(f"Solution Part 1: {solution_part_1}")


## Part 2
def power_of_game(line: str) -> int:
    game = parse_game(line)
    minimal_blue = 0
    minimal_green = 0
    minimal_red = 0
    for reveal in game:
        for i in range(len(reveal) // 2):
            if reveal[2 * i + 1] == "blue":
                minimal_blue = max(minimal_blue, int(reveal[2 * i]))
            elif reveal[2 * i + 1] == "green":
                minimal_green = max(minimal_green, int(reveal[2 * i]))
            elif reveal[2 * i + 1] == "red":
                minimal_red = max(minimal_red, int(reveal[2 * i]))
    return minimal_blue * minimal_green * minimal_red


def solver_part_2(input_path: str) -> int:
    with open(input_path, "r") as input_file:
        input_lines = input_file.readlines()
    return sum(map(power_of_game, input_lines))


solution_part_2 = solver_part_2(os.path.join(dir_path, "inputs/part1"))
print(f"Solution Part 2: {solution_part_2}")
