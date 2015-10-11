"""

DIFFICULTY: SIMPLE

Help Stephen to create a module for converting a normal time string to a morse time string. As you can see in the illustration, a gray circle means on, while a white circle means off. Every digit in the time string contains a different number of slots. The first digit for the hours has a length of 2 while the second digit for the hour has a length of 4. The first digits for the minutes and seconds have a length of 3 while the second digits for the minutes and seconds have a length of 4. Every digit in the time is converted to binary representation. You will convert every on (or 1) signal to dash ("-") and every off (or 0) signal to dot (".").
source: Wikipedia example
An time string could be in the follow formats: "hh:mm:ss", "h:m:s" or "hh:m:ss". The "missing" digits are zeroes. For example, "1:2:3" is the same as "01:02:03".
The result will be a morse time string with specific format:
"h h : m m : s s"
where each digits represented as sequence of "." and "-"

Input: A normal time string as a string (unicode).
Output: The morse time string as a string.

Precondition: 
time_string contains correct time.
"""

def checkio(time_string):
    
    #creates empty lists that will be the slots
    slots = [ [0, 0],  [0, 0, 0, 0], [0, 0, 0], [0, 0, 0, 0], [0, 0, 0], [0, 0, 0, 0] ]
    output = ""
    
    #creates the list that will act as the values of the slots
    vals = [8, 4, 2, 1]
    starting_point = 0
    
    #converts the time_string into something more usable
    time_list = time_string.split(":")
    for i in range(0, 3):
        if len(time_list[i]) == 1:
            time_list[i] = "0" + time_list[i]
        time_list[i] = list(time_list[i])
        for j in range(0, 2):
            time_list[i][j] = int(time_list[i][j])
    time_list = [item for sublist in time_list for item in sublist]
  
    for i in range(6):
        if len(slots[i]) == 4:
            starting_point = 0
        elif len(slots[i]) == 3:
            starting_point = 1
        elif len(slots[i]) == 2:
            starting_point = 2
        for j in range(starting_point, 4):
            if time_list[i] >= vals[j]:
                output += "-"
                time_list[i] -= vals[j]
            else:
                output += "."
        if i != 5:
            output += " "
        if i == 1 or i == 3:
            output += ": "
    return output
    
    return slots
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("10:37:49") == ".- .... : .-- .--- : -.. -..-", "First Test"
    assert checkio("21:34:56") == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
    assert checkio("00:1:02") == ".. .... : ... ...- : ... ..-.", "Third Test"
    assert checkio("23:59:59") == "-. ..-- : -.- -..- : -.- -..-", "Fourth Test"

