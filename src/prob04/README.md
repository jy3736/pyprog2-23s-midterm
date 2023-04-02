# 【Problem 4】Determine the Middle Element’s Value and Position

## Objectives

Create a Python program that finds the middle number in a list of odd length with unique numbers. The program should print both the value and index of the middle number in the list. For instance, if the given list is [3, 7, 5, 9, 1], the program should output 5 and 2, where 5 is the middle number and its index is 2.

## Requirements

The Python program should be designed with the assumption that the given list has an odd length and consists of unique numbers. Sorting the list is prohibited as part of the program's requirements. The program's aim is to find the middle number in the given list and print out its corresponding value and index. The output must be in the same format as the example provided, where the value and index are separated by a space.

## Example Usage

```
prob04> python .\\main.py
5 44 56 45 64 89 26 23 51
45 3

prob04> python .\\main.py
67 25 46 44 42 54 59 17 2 20 53
44 3

prob04> python .\\main.py
44 92 65 61 6 80 42 4 2
44 0

```

## Self-testing locally
It's recommended that you self-test your solution before submitting it. You can do this by running the following command in the terminal:

```
python testing.py
```

This script runs the automated tests to verify if your solution is correct or not.

Alternatively, you can run the following command if you have the "make" tool installed:

```
make
```
