# Basic Python For loop
# for y in range (0, 100):
#     pass

#1 Print all integers from 0 to 150.
# y = 0
# for y in range (0, 151):
#     print (y)

#2 Print all the multiples of 5 from 5 to 1,000
# y = 0
# for y in range (5, 1001, 5):
#     print (y)

#3 Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
# y = 0
# for y in range (1, 101):
#     if (y % 10 == 0):
#         print("Coding Dojo")
#     elif (y % 5 == 0):
#         print ("Coding")
#     else: 
#         print(y)
    
#4 Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
# num = 1
# sum= 0
# for y in range (1, 500001):
#     if (y % 2 != 0):
#         sum = sum + num
# print(sum)

#5 Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.

# for i in range (2018, 0, -4):
#         print(i)

#6 Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum 
# and going through highNum, print only the integers that are a multiple of mult. 
# For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 
# (on successive lines)

# lowNum = 2
# highNum = 9
# mult = 3
# odds = 0

# for odds in range (3, 11, 3):
#     if (odds % 3 == 0):
#         print(odds)
