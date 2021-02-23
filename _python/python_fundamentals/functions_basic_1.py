# functions basic 1

# 1
# def a():
#     return 5
# print(a())
# print(a(5))
# output: 5

# 2
# def a():
#     return 5
# print(a()+a())
#    (a(5)+a(5))
#        5+5 = 10

# output: 10

# 3
# def a():
#     return 5
#     return 10
# print(a())
# it will only print what is returned in the function
# there are no arguments in the function call and no parameters
# set in the function for the arguments to pass through.

# 4
# def a():
#     return 5
# print(10)
# # print 10 because it was told to print to the console first
# print(a())
# print 5 because 5 was set as the return value thus the output will be
# 10,5

# output: 10,5

# 5

# def a():
#     print(5)
# x = a()
# # function call but no argument passed to def a() so nothing to output
# print(x)
# # will print 5

# output: 5

# #6

# def a(b,c):
#     print(b+c)
# print(a(1,2) + a(2,3))

# output: 3, 5, 8

# 7

# def a(b,c):
#     return str(b)+str(c)
#     # concatination will occur here. str(2)+str(5)turns the int
#     # into a string and merges them together
# print(a(2,5))

# output: 25

# 8

# def a():
#     b = 100
#     print(b)

#     if b < 10:
#         return 5

#     else:
#         return 10
#     return 7
# print(a())

# output: 100, 10

# 9

# def a(b,c):
#     if b<c:
#         return 7
#     else:
#         return 14
#     return 3
# print(a(2,3))
# print(a(5,3))
# print(a(2,3) + a(5,3))

# output: 7,14,21

# 10

# def a(b,c):
#     return b+c
#     return 10
# print(a(3,5))

# output: 8

# 11

# b = 500
# print(b)

# def a():
#     b = 300
#     print(b)
# print(b)
# a()
# print(b)

# output: 500

# 12

# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
#     return b
# print(b)
# a()
# print(b)

# # output: 500, 500, 300, 500

# 13

# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
#     return b
# print(b)
# b=a()
# print(b)

# output:

# 14

def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()

# output: 1,3,2

# 15

def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)

# output: 1,3,2,1,3,5,10




