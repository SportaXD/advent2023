import os
import re

dir_path = os.path.dirname(os.path.realpath(__file__))


## Part 1
def has_adjacent_symbol(table: list[str], i: int, j_start: int, j_end: int) -> bool:
    height, width = len(table), len(table[0]) - 1
    adjacent_characters = ""
    if i > 0:
        adjacent_characters += table[i - 1][max(0, j_start - 1) : min(width, j_end + 1)]
    if i < height - 1:
        adjacent_characters += table[i + 1][max(0, j_start - 1) : min(width, j_end + 1)]
    if j_start > 0:
        adjacent_characters += table[i][j_start - 1]
    if j_end < width:
        adjacent_characters += table[i][j_end]
    adjacent_characters = adjacent_characters.strip("0|1|2|3|4|5|6|7|8|9|.|\n")
    return adjacent_characters != ""


def solver_part_1(input_path: str) -> int:
    with open(input_path, "r") as input_file:
        input_lines = input_file.readlines()
    parts = []
    j_start = -1
    for i, line in enumerate(input_lines):
        for j, char in enumerate(line):
            if char.isnumeric():
                if j_start == -1:
                    j_start = j
            else:
                if j_start != -1:
                    if has_adjacent_symbol(input_lines, i, j_start, j):
                        parts.append(int(line[j_start:j]))
                    j_start = -1
    return sum(parts)


solution_part_1 = solver_part_1(os.path.join(dir_path, "inputs/part1"))
print(f"Solution Part 1: {solution_part_1}")


## Part 2
def find_adjacent_stars(
    table: list[str], i: int, j_start: int, j_end: int
) -> list[(int, int)]:
    height, width = len(table), len(table[0]) - 1
    adjacent_stars = []
    if i > 0:
        adjacent_stars += [
            (i - 1, max(0, j_start - 1) + k.start())
            for k in re.finditer(
                "\*", table[i - 1][max(0, j_start - 1) : min(width, j_end + 1)]
            )
        ]

    if i < height - 1:
        adjacent_stars += [
            (i + 1, max(0, j_start - 1) + k.start())
            for k in re.finditer(
                "\*", table[i + 1][max(0, j_start - 1) : min(width, j_end + 1)]
            )
        ]

    if j_start > 0 and table[i][j_start - 1] == "*":
        adjacent_stars.append((i, j_start - 1))
    if j_end < width and table[i][j_end] == "*":
        adjacent_stars.append((i, j_end))
    return adjacent_stars


def solver_part_2(input_path: str) -> int:
    with open(input_path, "r") as input_file:
        input_lines = input_file.readlines()
    stars = {}
    j_start = -1
    for i, line in enumerate(input_lines):
        for j, char in enumerate(line):
            if char.isnumeric():
                if j_start == -1:
                    j_start = j
            else:
                if j_start != -1:
                    value = int(line[j_start:j])
                    for star_indices in find_adjacent_stars(input_lines, i, j_start, j):
                        if star_indices in stars.keys():
                            stars[star_indices].append(value)
                        else:
                            stars[star_indices] = [value]
                    j_start = -1
    return sum([v[0] * v[1] for _, v in stars.items() if len(v) == 2])


solution_part_2 = solver_part_2(os.path.join(dir_path, "inputs/part1"))
print(f"Solution Part 2: {solution_part_2}")
