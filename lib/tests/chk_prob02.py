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

sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), lab_dir)))
from main import main

class TestMainFunction(unittest.TestCase):

    def chk_prime(self, n):
        """Checks if a given number is prime or not."""
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def test_main(self):
        # Test 10 sets of random inputs
        stdout = sys.stdout
        for i in range(10):
            # Generate random values for a and b
            a = random.randint(1, 100)
            b = random.randint(a, a+50)
            # Calculate the expected output
            expected_output = ' '.join(
                str(num) for num in range(a, b+1) if self.chk_prime(num))
            sys.stdout = stdout
            print(f'Test {i+1:2} : [{a}, {b}] -> {expected_output}')

            # Redirect stdout to a StringIO object to capture output
            captured_output = io.StringIO()
            sys.stdin = io.StringIO(f"{a}\n{b}\n")
            sys.stdout = captured_output

            # Call the main function with the random inputs
            main()

            # Get the printed output as a string
            printed_output = captured_output.getvalue().strip()

            # Check if the printed output matches the expected output
            self.assertEqual(printed_output, expected_output)


if __name__ == '__main__':
    unittest.main()
