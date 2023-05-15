#Basic
for i in range(0,100,1):
    print (i)
#Multiples of Five
for i in range(5,1000,1):
    if i % 5 ==0:
        print (i)
#Counting The Dojo Way
for num in range(1, 100):
    if num % 10 == 0:
        print("Coding Dojo")
    elif num % 5 == 0:
        print("Coding")
    else:
        print(num)
#Whoa.That Sucker's Huge
sum = 0

for num in range(1, 500000, 2):
    sum += num

print("The sum  is:", sum)
#Countdown By Focus
start_number = 2018

for num in range(start_number, 0, -4):
    print(num)
#Flexible Counter
lowNum = 2
highNum = 9
mult = 3

for num in range(lowNum, highNum + 1):
    if num % mult == 0:
        print(num)


