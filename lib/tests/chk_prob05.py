#! /usr/bin/env python
# Do not modify this file.  It is used by the autograder.

from io import StringIO
from contextlib import redirect_stdout
import unittest
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

class TestMatrixProduct(unittest.TestCase):

    def test_matrix_product(self):

        # Test using 10 sets of random data
        for i in range(10):

            # Generate random data for A, B matrices
            m, n, r = random.randint(1, 5), random.randint(1, 5), random.randint(1, 5)
            A = [[random.randint(0, 9) for _ in range(n)] for _ in range(m)]
            B = [[random.randint(0, 9) for _ in range(r)] for _ in range(n)]
            print(f"Test {i+1:2} : \n{m} {n} {r}")
            [print(' '.join(map(str, row))) for row in A]
            [print(' '.join(map(str, row))) for row in B]
            print()
            # Calculate expected result
            expected_result = [[sum(a * b for a, b in zip(row_a, col_b)) for col_b in zip(*B)] for row_a in A]

            # Capture console output of main() function
            with redirect_stdout(StringIO()) as output:
                sys.stdin = StringIO('{} {} {}\n'.format(m, n, r) + '\n'.join([' '.join(map(str, row)) for row in A]) + '\n' + '\n'.join([' '.join(map(str, row)) for row in B]) + '\n')
                main() # Parse console output to get actual result
            actual_result = [list(map(int, row.split())) for row in output.getvalue().strip().split('\n')]

            # Verify that the expected and actual results are the same
            self.assertEqual(actual_result, expected_result)

if __name__ == '__main__':
    unittest.main()
