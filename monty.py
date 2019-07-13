from random import randint


def dieroll():
    res = randint(1,6)
    return res

def dierolls():
    a = 0
    rolls = []
    while a < 4:
        a = a + 1
        roll = dieroll()
        rolls.append(roll)
    rolls.remove(min(rolls))
    return rolls

def sumpoints(roll):
    summ = 0
    for number in roll:
        summ = summ + number
    return summ

def roll():
    res = sumpoints(dierolls())
    return res

def second_option():
    a = 0
    seven = []
    while a < 7:
        a = a + 1
        res = roll()
        seven.append(res)
        if a == 7:
            if max(seven) < 15:
                a = 0
                seven = []
                continue
    seven.remove(min(seven))
    return seven

def third_option():
    a = 0
    six = []
    while a < 6:
        a = a + 1
        res = roll()
        six.append(res)
        if a == 6:
            if max(six) < 15:
                a = 0
                six = []
                continue
            else:
                firstmax = max(six)
                six.remove(firstmax)
                if max(six) < 15:
                    a = 0
                    six = []
                else:
                    six.append(firstmax)
                    return six

def sumscores(scores):
    res = 0
    for score in scores:
        res = res + score
    return res

# iterations
iterations = 50000
a = 0
secondsum = 0
thirdsum = 0
while a < iterations:
    a = a + 1
    second = sumscores(second_option())
    third = sumscores(third_option())
    secondsum = secondsum + second
    thirdsum = thirdsum + third
secondav = secondsum / iterations
thirdav = thirdsum / iterations

print(secondav)
print(thirdav)
print(secondav - thirdav)

        
