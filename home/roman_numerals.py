"""

DIFFICULTY: MODERATE

Roman numerals come from the ancient Roman numbering system. They are based on specific letters of the alphabet which are combined to signify the sum (or, in some cases, the difference) of their values. The first ten Roman numerals are:
I, II, III, IV, V, VI, VII, VIII, IX, and X.
The Roman numeral system is decimal based but not directly positional and does not include a zero. Roman numerals are based on combinations of these seven symbols:
Symbol Value
I 1 (unus)
V 5 (quinque)
X 10 (decem)
L 50 (quinquaginta)
C 100 (centum)
D 500 (quingenti)
M 1,000 (mille)
More additional information about roman numerals can be found on the Wikipedia article.
For this task, you should return a roman numeral using the specified integer value ranging from 1 to 3999.
Input: A number as an integer.
Output: The Roman numeral as a string.
Precondition: 0 < number < 4000
"""

def checkio(data):

    """
    I 1 (unus)
    V 5 (quinque)
    X 10 (decem)
    L 50 (quinquaginta)
    C 100 (centum)
    D 500 (quingenti)
    M 1,000 (mille)
    """
    
    num_list = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    let_list =["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    mod = 0
    int_div = 0
    fin_str = ""
    index = 0
        
    for num in num_list:   
        int_div = data // num
        data = data % num
        fin_str = fin_str + let_list[index] * int_div           
        index += 1
    return fin_str  
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
