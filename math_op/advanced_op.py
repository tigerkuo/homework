import math

def average(nums):
    if not nums:
        raise ValueError("List is empty.")
    return sum(nums) / len(nums)

def power(base, exponent):
    return base ** exponent

def sqrt(num):
    if num < 0:
        raise ValueError("Cannot calculate square root of a negative number.")
    return math.sqrt(num)

def log(num, base=10):
    if num <= 0 or base <= 0:
        raise ValueError("Logarithm input and base must be greater than zero.")
    return math.log(num, base)
