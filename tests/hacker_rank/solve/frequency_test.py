import unittest
from collections import namedtuple
from typing import List

from src.hacker_rank.solve.frequency import frequency

TestCase = namedtuple("TestCase", "input expected desc")


class TestFrequency(unittest.TestCase):
    def setUp(self):
        pass

    def test_frequency(self):
        cases: List[TestCase] = [
            TestCase(input="1226#24#",
                     expected="1 1 0 0 0 0 0 0 0 0 0 0 0 "
                              "0 0 0 0 0 0 0 0 0 0 1 0 1",
                     desc="# 처리 실패"),
            TestCase(input="1(2)23(3)",
                     expected="2 1 3 0 0 0 0 0 0 0 0 0 0 "
                              "0 0 0 0 0 0 0 0 0 0 0 0 0",
                     desc="괄호 처리 실패"),
            TestCase(input="2110#(2)",
                     expected="1 1 0 0 0 0 0 0 0 2 0 0 0 "
                              "0 0 0 0 0 0 0 0 0 0 0 0 0",
                     desc="# + 괄호 처리 실패"),
            TestCase(input="23#(2)24#25#26#23#(3)",
                     expected='0 0 0 0 0 0 0 0 0 0 0 0 0 '
                              '0 0 0 0 0 0 0 0 0 5 1 1 1',
                     desc="복잡한 형태의 # + 괄호 중복 복합 처리 실패"),
        ]

        for case in cases:
            self.assertEqual(
                ' '.join([str(s) for s in frequency(case.input)]),
                case.expected,
                case.desc
            )