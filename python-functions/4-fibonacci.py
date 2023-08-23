#!/usr/bin/python3

def fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [0, 1]
    sequence = [0, 1]

    for i in range(2, n):
        fib = sequence[-1] + sequence[-2]
        sequence.append(fib)
    
    return sequence