# 【Problem 2】Printing Prime Numbers in [A,B]

## Objectives

To print prime numbers in [A,B], check each integer in that range for divisibility by numbers from 2 to its square root. If none divides it, it is prime. A prime number is a natural number >1 with only two positive factors: 1 and itself.

## Requirements

The program should be designed to find and print all prime numbers within a given range. Two functions, is_prime and main, should be implemented. The is_prime function should accept a single integer parameter, n, and return True if n is a prime number; otherwise, it should return False. The main function should accept two integer parameters, a and b, representing the range of numbers to check for primes. It should then iterate through each number in the range, calling the is_prime function on each one. 

## Example Usage

```
PS prob02> echo 1 10 | python .\\main.py
2 3 5 7

PS prob02> echo 50 100 | python .\\main.py
53 59 61 67 71 73 79 83 89 97

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
