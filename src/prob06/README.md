# 【Problem 6】Eight Queens on a Chessboard are not Threatened

## Objectives

Eight queens can be placed on an 8x8 chessboard so that they do not attack each other. Given the positions of eight queens on a chessboard, determine if any two queens can attack each other in the next move. Print "YES" if there is a possible attack, otherwise print "NO". Input eight pairs of coordinates, one per line, representing the positions of the queens on the standard chessboard with rows and columns numbered starting from 1.

## Requirements

The input consist of eight sets of coordinates, where each set is made up of two integers (x and y) separated by a space. The values of x and y should be whole numbers between 0 and 7. Each set of coordinates should be provided on a single line of input.

## Example Usage

```
prob06> python .\\main.py
0 1
1 3
2 5
3 7
4 0
5 2
6 4
7 6
YES

prob06> python .\\main.py
0 4
1 1
2 3
3 5
4 7
5 2
6 0
7 6
NO

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
