"""

DIFFICULTY: ELEMENTARY

You are given a positive integer. Your function should calculate the product of the digits excluding any zeroes.
For example: The number given is 123405. The result will be 1*2*3*4*5=120 (don't forget to exclude zeroes).
Input: A positive integer.
Output: The product of the digits as an integer.
Precondition: 0 < number < 106
"""

def checkio(number):
    product = 1
    str_number = str(number)
    for digit in str_number:
        if int(digit) != 0:
            product *= int(digit)
    return product
        

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
