import os

dir_path = os.path.dirname(os.path.realpath(__file__))


## Part 1
def calibration_value(line: str) -> int:
    numeric_values = list(map(str.isnumeric, line))
    first_digit = line[numeric_values.index(True)]
    last_digit = line[::-1][numeric_values[::-1].index(True)]
    return int(first_digit + last_digit)


def solver_part_1(input_path: str) -> int:
    with open(input_path, "r") as input_file:
        input_lines = input_file.readlines()
    return sum(map(calibration_value, input_lines))


solution_part_1 = solver_part_1(os.path.join(dir_path, "inputs/part1"))
print(f"Solution Part 1: {solution_part_1}")


## Part 2
def calibration_value_with_spelling(line: str) -> int:
    digit_dictionary = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    # First digit
    first_digit = None
    for i, character in enumerate(line):
        if character.isnumeric():
            first_digit = character
        else:
            for spelling, digit in digit_dictionary.items():
                if line[i:].startswith(spelling):
                    first_digit = digit
        if first_digit:
            break

    # Last digit
    reversed_line = line[::-1]
    last_digit = None
    for i, character in enumerate(reversed_line):
        if character.isnumeric():
            last_digit = character
        else:
            for spelling, digit in digit_dictionary.items():
                if reversed_line[i:].startswith(spelling[::-1]):
                    last_digit = digit
        if last_digit:
            break

    return int(first_digit + last_digit)


def solver_part_2(input_path: str) -> int:
    with open(input_path, "r") as input_file:
        input_lines = input_file.readlines()
    return sum(map(calibration_value_with_spelling, input_lines))


solution_part_2 = solver_part_2(os.path.join(dir_path, "inputs/part1"))
print(f"Solution Part 2: {solution_part_2}")
