#! /usr/bin/env python
# Do not modify this file.  It is used by the autograder.

import unittest
from unittest.mock import patch
import io
import sys
import os 
import random

script_name = sys.argv[0] 
base_name = os.path.basename(script_name)
lab_name = os.path.splitext(base_name)[0].split("_")[-1]
lab_dir = '../../src/' + lab_name

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), lab_dir)))
from main import main

class TestMain(unittest.TestCase):
    def setUp(self):
        self.inputs = []
        self.outputs = []
        for i in range(10):
            nums = [random.randint(-10, 100) for _ in range(5)]
            self.inputs.append('\n'.join(str(num) for num in nums) + '\n')
            largest = max(nums)
            smallest = min(nums)
            self.outputs.append(f"{largest} {smallest}\n")
            print(f"Test {i+1:2} : {nums} -> {largest} {smallest}")

    def test_main(self):
        for i in range(len(self.inputs)):
            sys.stdin = io.StringIO(self.inputs[i])
            captured_output = io.StringIO()
            sys.stdout = captured_output
            main()
            self.assertEqual(captured_output.getvalue(), self.outputs[i])

if __name__ == '__main__':
    unittest.main()
