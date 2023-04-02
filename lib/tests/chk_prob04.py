#! /usr/bin/env python
# Do not modify this file.  It is used by the autograder.

import unittest
from unittest import mock
from io import StringIO
import sys
import os 
from random import sample, randint

script_name = sys.argv[0] 
base_name = os.path.basename(script_name)
lab_name = os.path.splitext(base_name)[0].split("_")[-1]
lab_dir = '../../src/' + lab_name

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), lab_dir)))
from main import main

import io
import unittest
import sys
from unittest.mock import patch

def middle(L):
    for i in range(len(L)):
        cnt = 0
        for j in range(len(L)):
            if L[i] > L[j]:
                cnt += 1   
        if cnt == len(L) // 2:
            return f"{L[i]} {i}"

class TestMain(unittest.TestCase):
    
    def test_main(self):
        for i in range(1,11):
            seq = sample(range(1,100),randint(1,5)*2+1)
            expected_result = middle(seq)
            print(f'Test {i:2} : {" ".join(map(str, seq))} -> {expected_result}')
            with mock.patch('sys.stdin', StringIO(' '.join(map(str, seq)))):
                # redirect input to simulate user input
                with mock.patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                    # redirect output to capture printed result
                    main()

                actual_result = mock_stdout.getvalue().strip()
                self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()