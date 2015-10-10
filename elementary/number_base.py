"""

DIFFICULTY: SIMPLE

Do you remember the radix and Numeral systems from math class? Let's practice with it.
You are given a positive number as a string along with the radix for it. Your function should convert it into decimal form. The radix is less than 37 and greater than 1. The task uses digits and the letters A-Z for the strings.
Watch out for cases when the number cannot be converted. For example: "1A" cannot be converted with radix 9. For these cases your function should return -1.
Input: Two arguments. A number as string and a radix as an integer.
Output: The converted number as an integer.
Precondition: 
re.match("\A[A-Z0-9]\Z", str_number)
0 < len(str_number) ≤ 10
2 ≤ radix ≤ 36
"""

def checkio(str_number, radix):
    dictionary = {
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15,
        'G': 16,
        'H': 17,
        'I': 18,
        'J': 19,
        'K': 20,
        'L': 21,
        'M': 22,
        'N': 23,
        'O': 24,
        'P': 25,
        'Q': 26,
        'R': 27,
        'S': 28,
        'T': 29,
        'U': 30,
        'V': 31,
        'W': 32,
        'X': 33,
        'Y': 34,
        'Z': 35
        }
    counter = len(str_number) - 1
    value = 0
    for digit in str_number:
        if digit in "1234567890" and int(digit) >= radix:
            return -1
        elif digit in "1234567890":
            value += int(digit) * (radix ** counter)
            counter -= 1
        if digit in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" and dictionary[digit] >= radix:
            return -1
        elif digit in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            value += dictionary[digit] * (radix ** counter)
            counter -= 1
    return value
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("AF", 16) == 175, "Hex"
    assert checkio("101", 2) == 5, "Bin"
    assert checkio("101", 5) == 26, "5 base"
    assert checkio("Z", 36) == 35, "Z base"
    assert checkio("AB", 10) == -1, "B > A > 10"
