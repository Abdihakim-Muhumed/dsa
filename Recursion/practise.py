
#  Created by Abdihakim Muhumed.
# Copyright c 2022 Abdihakim. All rights reserved.

#find sum of digit of a positive integer number using recursion.

from cmath import exp
from re import A


def sumOfDigits(n):
    assert n>0 and int(n), "The number should be a positive integer"
    if n == 0:#base case
        return 0
    else:
        return int(n%10) + sumOfDigits(int(n/10)) #recursive case

#2. How to calculate power of a number using recursion
def power(base, exp):
    assert int(exp) == exp, "The exponent must be an integer only."
    if exp ==0:
        return 1
    elif exp < 0:
        return 1/base * power(base, exp-1)
    else:
        return base * power(base, exp-1)

# 3. How to find GCD (Greatest Common Divisor) of two numbers usin recursion
def gcd(a, b):
    assert int(a) == a  and int(b) == b, "The numbers must be an integer only."
    if a < 0:
        a = -1 * a
    if b < 0:
        b = -1 * b
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
    
# 4. Convert a number from Decimal to Binary using recursion
def decimalToBinary(n):
    if n == 0:
        return 0
    else:
        return n%2 + 10 * decimalToBinary(int(n/2))
#print(sumOfDigits(44))
#print(power(2,4))
#print(gcd(48,18))
print(decimalToBinary(10))
