"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""
import math

def primes(number_of_primes):
    list = []

    if number_of_primes <= 0:
        raise ValueError("invalid parameter")

    loops = number_of_primes

    next_number = 2
    while loops > 0:
        if is_prime(next_number):
            list.append(next_number)
            loops -= 1

        next_number += 1

    return list


def is_prime(number):
    for divisor in range(2, number):
        if number % divisor == 0:
            return False
    return True


print(primes(2))