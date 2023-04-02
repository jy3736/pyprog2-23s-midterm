# 【Problem 5】Compute the Product Matrix of Two Matrices

## Objectives

Consider three positive integers m, n, and r. We are given an m x n matrix A with m rows and n columns, and an n x r matrix B with n rows and r columns. To form the product matrix AB, which is an m x r matrix, we compute the dot product of each row of A with each column of B. Specifically, for each (i,k) entry of AB, we compute the sum:

```
        A[i][1]*B[1][k] + A[i][2]*B[2][k] + ... + A[i][n]*B[n][k]

```

Finally, we print the resulting matrix AB.

## Requirements

Write a Python program that takes three positive integers m, n, and r as input. The program should also take two matrices A and B as input, where A is an m x n matrix and B is an n x r matrix. The program should multiply the matrices A and B using the dot product formula and store the result in a matrix AB, which is an m x r matrix. The program should then print the matrix AB in a readable format.

## Example Usage

```
prob05> python .\\main.py
4 2 5
8 8
9 6
3 9
0 0
2 3 8 7 6
6 1 0 4 9
64 32 64 88 120
54 33 72 87 108
60 18 24 57 99
0 0 0 0 0

prob05> python .\\main.py
2 1 4
0
2
7 4 1 1
0 0 0 0
14 8 2 2

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
