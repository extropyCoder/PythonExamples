summ = 0
lastTerm = 1
lastTerm2 = 0
currentValue = 1
while currentValue < 4000000:
    currentValue =  lastTerm + lastTerm2
    if (currentValue % 2 ==0) :
        summ += currentValue

    lastTerm2 = lastTerm
    lastTerm = currentValue
    #print currentValue
    #print summ
print summ
