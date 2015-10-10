"""

DIFFICULTY: SIMPLE

Stephen's speech module is broken. This module is responsible for his number pronunciation. He has to click to input all of the numerical digits in a figure, so when there are big numbers it can take him a long time. Help the robot to speak properly and increase his number processing speed by writing a new speech module for him. All the words in the string must be separated by exactly one space character. Be careful with spaces -- it's hard to see if you place two spaces instead one.
Input: A number as an integer.
Output: The string representation of the number as a string.
How it is used: This concept may be useful for the speech synthesis software or automatic reports systems. This system can also be used when writing a chatbot by assigning words or phrases numerical values and having a system retrieve responses based on those values.
Precondition: 0 < number < 1000
"""

FIRST_TEN = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine"
             }
SECOND_TEN = {
    "10": "ten",
    "11": "eleven",
    "12": "twelve",
    "13": "thirteen",
    "14": "fourteen",
    "15": "fifteen",
    "16": "sixteen",
    "17": "seventeen",
    "18": "eighteen",
    "19": "nineteen"
    }
OTHER_TENS = {
    "20": "twenty",
    "30": "thirty",
    "40": "forty",
    "50": "fifty",
    "60": "sixty",
    "70": "seventy",
    "80": "eighty",
    "90": "ninety"
    }
HUNDRED = "hundred"

def checkio(number):
    STR_NUM = str(number)
    LENGTH = len(STR_NUM)
    huns_dig = 0
    tens_dig = 0
    ones_dig = 0
    two_dig = 0
    final_str = ""
    
    if LENGTH == 1:
        final_str = FIRST_TEN[STR_NUM]
    
    if LENGTH == 2:
        if STR_NUM in SECOND_TEN:
            return SECOND_TEN[STR_NUM]
        else:
            tens_dig = number // 10 * 10
            ones_dig = number % 10
            final_str = OTHER_TENS[str(tens_dig)]
            if ones_dig != 0:
                final_str = final_str + " " + FIRST_TEN[str(ones_dig)]
    
    if LENGTH == 3:
        
        huns_dig = number // 100
        two_dig = number % 100
        tens_dig = number % 100 // 10 * 10
        ones_dig = number % 10
        
        final_str = FIRST_TEN[str(huns_dig)] + " " + HUNDRED
        
        if str(two_dig) in SECOND_TEN:
            final_str = final_str + " " + SECOND_TEN[str(two_dig)]
            
        if tens_dig != 0 and str(two_dig) not in SECOND_TEN:
            final_str = final_str + " " + OTHER_TENS[str(tens_dig)]
            
        if ones_dig != 0 and str(two_dig) not in SECOND_TEN:
                final_str = final_str + " " + FIRST_TEN[str(ones_dig)]
    return final_str
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
