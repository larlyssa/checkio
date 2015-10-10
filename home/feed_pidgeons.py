"""

DIFFICULTY: MODERATE

I start to feed one of the pigeons. A minute later two more fly by and a minute after that another 3. Then 4, and so on (Ex: 1+2+3+4+...). One portion of food lasts a pigeon for a minute, but in case there's not enough food for all the birds, the pigeons who arrived first ate first. Pigeons are hungry animals and eat without knowing when to stop. If I have N portions of bird feed, how many pigeons will be fed with at least one portion of wheat?
pigeons
Input: A quantity of portions wheat as a positive integer.
Output: The number of fed pigeons as an integer.
Precondition: 0 < N < 105.
"""

def checkio(bird_feed):
    
    nbirds = 1
    increment = 2
    birds = [0]
    count = 0
    count1 = 0
    total_fed = 0
    while bird_feed > 0:
        if bird_feed >= nbirds:
            birds = [x + 1 for x in birds]
            bird_feed -= len(birds)
        else:
            while count1 < len(birds) and bird_feed > 0:
                birds[count1] += 1
                bird_feed -= 1
                count1 += 1
        while count < increment:
            count += 1
            birds.append(0)
        count = 0
        nbirds += increment
        increment += 1
        
        
    for bird in birds:
        if bird > 0:
            total_fed += 1
    return total_fed
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(1) == 1, "1st example"
    assert checkio(2) == 1, "2nd example"
    assert checkio(5) == 3, "3rd example"
    assert checkio(10) == 6, "4th example"
