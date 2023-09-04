"""
CMPS 6100  Lab 1
Author: Tiancheng.Xu
"""

### the only imports needed are here
import math
import time
###

def is_divisible_by(num, i):
    if num % i==0:
       return True
    else:
       return False


def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    i = 2
    while i < num:
        if num % i == 0:
            return False
        i =i + 1
    return True

def generate_primes(upper_bound):
    i = 2
    while i <= upper_bound:
        if is_prime(i) == True:
            print(i)
        i = i + 1


def count_primes(upper_bound):
    i = 2
    counter = 0
    while i <= upper_bound:
        if is_prime(i) == True:
            counter = counter + 1
        i = i + 1
    return counter


def generate_twin_primes(upper_bound):
    i = 1
    if  upper_bound < 6:
        print("({},{})".format(3,5))
    print("({},{})".format(3,5))
    while 6 * i <= upper_bound:
          if is_prime(6 * i + 1) == True and is_prime(6 * i - 1) == True:
             print("({},{})".format(6 * i - 1,6 * i + 1))
          i = i + 1

    

def count_twin_primes(upper_bound):
    i = 1
    counter = 1
    if  upper_bound < 6:
        return counter
    while 6 * i <= upper_bound:
          if is_prime(6 * i + 1) == True and is_prime(6 * i - 1) == True:
             counter = counter + 1
          i = i + 1
    return counter

#########    #########
### Test Functions ###
#########    #########

# You can run them on the terminal.
# The command:
#
# pytest main.py::test_is_divisible_by
#
# Will run the test_is_divisible_by test function.

def test_is_divisible_by():
    assert is_divisible_by(2, 2) == True
    assert is_divisible_by(3, 2) == False
    assert is_divisible_by(47, 7) == False

def test_is_prime():
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 241, 461, 701, 881, 883, 997]
    for prime in primes:
        assert is_prime(prime) == True
    composites = [4, 6, 8, 9, 10, 25, 30, 36, 39, 49, 60, 64, 121]
    for composite in composites:
        assert is_prime(composite) == False

def test_count_primes():
    assert count_primes(10) == 4
    assert count_primes(100) == 25
    assert count_primes(1000) == 168
    assert count_primes(10000) == 1229

def test_count_twin_primes():
    assert count_twin_primes(10) == 2
    # The two pairs less than 10 are (3,5) and (5,7)
    assert count_twin_primes(100) == 8
    assert count_twin_primes(1000) == 35
    assert count_twin_primes(10000) == 205

start = time.time()
generate_twin_primes(1000)
end = time.time()
elasped_time_ms = (end - start) * 1000
print("Elapsed Time: {:.2f} milliseconds".format(elasped_time_ms))
