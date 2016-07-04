summ = 0
for x in range (1000):
    if (x % 5 ==0) or (x % 3 == 0):
        summ += x

print summ

# better using list comp
# sum([x for x in range(1000) if x % 3== 0 or x % 5== 0])
