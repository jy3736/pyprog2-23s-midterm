#! /usr/bin/env python
# Do not modify this file.  It is used by the autograder.

import unittest
from unittest import mock
from io import StringIO
from random import randint
import os, sys

script_name = sys.argv[0] 
base_name = os.path.basename(script_name)
lab_name = os.path.splitext(base_name)[0].split("_")[-1]
lab_dir = '../../src/' + lab_name

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), lab_dir)))
from main import main

from functools import reduce

def longest(numbers):
    def update_state(state, num):
        curr_len, max_len, prev_num = state
        if num < prev_num:
            curr_len += 1
        else:
            curr_len = 1
        return (curr_len, max(curr_len, max_len), num)

    initial_state = (1, 0, numbers[0])
    _, max_len, _ = reduce(update_state, numbers[1:], initial_state)
    return max_len

class TestMain(unittest.TestCase):
    def test_main(self):
        test_cases = []
        for i in range(10):
            seq = [randint(1, 9) for _ in range(randint(5, 20))]
            test_cases.append(seq)
            expected_result = longest(seq)
            print(f"Test {i+1:2} : {seq} -> {expected_result}")
            with mock.patch('sys.stdin', StringIO(' '.join(map(str, seq)))):
                # redirect input to simulate user input
                with mock.patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                    # redirect output to capture printed result
                    main()

                actual_result = int(mock_stdout.getvalue())
                self.assertEqual(actual_result, expected_result)

if __name__ == '__main__':
    unittest.main()