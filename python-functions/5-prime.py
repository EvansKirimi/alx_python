#!/usr/bin/python3

def is_prime(number):
    if number <= 0:
        return False
    elif number / number == 1 and number / 1 == number:
        return True
    else:
        return False 