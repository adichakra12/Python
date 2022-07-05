for i in range(151):
    print(i)

for i in range(5, 1001, 5):
    print(i)

for i in range (1,101):
    if (i%5 == 0 and i%10 != 0):
        print("Coding")
    if (i%10 == 0):
        print("Coding Dojo")
    if (i%5 != 0):
        print(i)

sum = 0

for i in range (0,500001):

    if(i%2 != 0):
        sum += i

print(sum)

for i in range (2018, 0, -4):
    print(i)



lowNum = 2
highNum = 20
mult = 2

for i in range (lowNum, highNum + 1):
    if (i % mult == 0):
        print(i)
    else:
        continue    
