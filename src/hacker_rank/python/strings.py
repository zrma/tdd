from typing import Sequence, List
from re import findall
import textwrap


def swap_case(s: str) -> str:
    def change(c: str) -> str:
        if not c.isalpha():
            return c
        if c.isupper():
            return c.lower()
        return c.upper()

    return ''.join(map(change, s))


def split_and_join(s: str) -> Sequence[str]:
    return s.replace(' ', '-')


def what_s_your_name(a: str, b: str):
    print(f"Hello {a} {b}! You just delved into python.")


def mutations(s: str, pos: int, c: str) -> str:
    return "".join((s[:pos], c, s[pos + 1:]))


def count_substring(string: str, sub_string: str) -> int:
    return len(findall(f"(?={sub_string})", string))


def validate_string(s: str):
    print(any((x for x in s if x.isalnum())))
    print(any((x for x in s if x.isalpha())))
    print(any((x for x in s if x.isdigit())))
    print(any((x for x in s if x.islower())))
    print(any((x for x in s if x.isupper())))


def text_alignment(thickness: int, c: str):
    print()

    # Top Cone
    for i in range(thickness):
        print((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))

    # Top Pillars
    for i in range(thickness + 1):
        print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

    # Middle Belt
    for i in range((thickness + 1) // 2):
        print((c * thickness * 5).center(thickness * 6))

        # Bottom Pillars
    for i in range(thickness + 1):
        print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

        # Bottom Cone
    for i in range(thickness):
        print(((c * (thickness - i - 1)).rjust(thickness) + c +
               (c * (thickness - i - 1)).ljust(thickness)).rjust(thickness * 6))


def wrap(string: str, max_width: int) -> str:
    return "\n".join(textwrap.wrap(string, max_width))


def designer_door_mat(n: int, m: int):
    output: List[List[str]] = [["-" for _ in range(m)] for _ in range(n)]
    output[n // 2] = list("WELCOME".center(m, "-"))

    def point(pos_x: int, pos_y: int):
        output[pos_y][pos_x - 1] = '.'
        output[pos_y][pos_x] = '|'
        output[pos_y][pos_x + 1] = '.'

    center = m // 2
    for y in range(n):
        if y == n // 2:
            continue
        for offset in range(n // 2 - abs(n // 2 - y) + 1):
            point(center + offset * 3, y)
            point(center - offset * 3, y)

    for row in output:
        print(''.join(row))
