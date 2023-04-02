#! /usr/bin/env python
# Do not modify this file.  It is used by the autograder.

import unittest
from unittest.mock import patch
import sys
import os
from random import randint, shuffle, sample
from io import StringIO

script_name = sys.argv[0]
base_name = os.path.basename(script_name)
lab_name = os.path.splitext(base_name)[0].split("_")[-1]
lab_dir = '../../src/' + lab_name

sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), lab_dir)))
from main import main

def can_attack(q1, q2):
    (x1, y1), (x2, y2) = q1, q2
    if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
        return True
    return False


class TestMain(unittest.TestCase):

    def test_main(self):
        data_sets = [
            [(0, 0), (1, 2), (2, 4), (3, 6), (4, 1), (5, 3), (6, 5), (7, 7)],
            [(0, 1), (1, 3), (2, 5), (3, 7), (4, 0), (5, 2), (6, 4), (7, 6)],
            [(0, 2), (1, 7), (2, 3), (3, 6), (4, 0), (5, 5), (6, 1), (7, 4)],
            [(0, 2), (1, 0), (2, 5), (3, 7), (4, 4), (5, 1), (6, 3), (7, 6)],
            [(0, 4), (1, 1), (2, 3), (3, 5), (4, 7), (5, 2), (6, 0), (7, 6)],
            [(0, 0), (1, 2), (2, 4), (3, 6), (4, 1), (5, 7), (6, 5), (7, 3)],
            [(0, 1), (1, 3), (2, 5), (3, 7), (4, 0), (5, 2), (6, 4), (7, 6)],
            [(0, 2), (1, 7), (2, 3), (3, 6), (4, 1), (5, 4), (6, 0), (7, 5)],
            [(0, 6), (1, 1), (2, 5), (3, 2), (4, 0), (5, 3), (6, 7), (7, 4)],
            [(0, 4), (1, 1), (2, 3), (3, 5), (4, 7), (5, 2), (6, 0), (7, 6)],
            [(0, 0), (1, 2), (2, 4), (3, 6), (4, 1), (5, 3), (6, 5), (7, 7)],
            [(0, 1), (1, 3), (2, 5), (3, 7), (4, 0), (5, 2), (6, 4), (7, 6)],
            [(0, 2), (1, 7), (2, 3), (3, 6), (4, 0), (5, 5), (6, 1), (7, 4)],
            [(0, 2), (1, 6), (2, 1), (3, 7), (4, 5), (5, 3), (6, 0), (7, 4)],
            [(0, 3), (1, 6), (2, 2), (3, 7), (4, 1), (5, 4), (6, 0), (7, 5)],
            [(0, 6), (1, 4), (2, 2), (3, 0), (4, 5), (5, 7), (6, 1), (7, 3)],
            [(0, 2), (1, 7), (2, 3), (3, 6), (4, 0), (5, 5), (6, 1), (7, 4)],
            [(0, 2), (1, 0), (2, 5), (3, 7), (4, 4), (5, 1), (6, 3), (7, 6)],
            [(0, 4), (1, 1), (2, 3), (3, 5), (4, 7), (5, 2), (6, 0), (7, 6)],
            [(0, 7), (1, 3), (2, 0), (3, 4), (4, 6), (5, 1), (6, 5), (7, 2)]]

        shuffle(data_sets)
        data_sets = sample(data_sets, 10)

        i = 1
        stdout = sys.stdout
        for queens in data_sets:

            expected_result = "NO"
            for q1 in queens:
                for q2 in queens:
                    if q1 != q2:
                        if can_attack(q1, q2):
                            expected_result = "YES"
                            break
                if expected_result == "YES":
                    break

            # Constructing input string from generated queens
            input_str = ""
            for q in queens:
                input_str += f"{q[0]} {q[1]}\n"

            sys.stdout = stdout
            print(f"Test {i:2} : {queens} -> {expected_result}")
            print(f"{input_str}")
            i += 1
            # Redirecting stdin and stdout to capture input and output
            captured_input = StringIO(input_str)
            captured_output = StringIO()
            sys.stdin = captured_input
            sys.stdout = captured_output

            # Run main() function
            main()

            # Get the output
            output = captured_output.getvalue().strip()
            self.assertEqual(output, expected_result)


if __name__ == '__main__':
    unittest.main()
