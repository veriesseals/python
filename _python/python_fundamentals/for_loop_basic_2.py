# 1) Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
#    Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]

# assigned an array to varaible biggieSmall
biggieSmalls = [-1, 3, 5, -5]

# created loop to  loop though the list
for y in range (0, 4):
    # created condition that allows the loop to check the variables
    # for all the positive numbers greater than 0 inside the list
    if( biggieSmalls[y] > 0):
        #replace what is postive inside the biggieSmalls[y] list with the string "big" 
        biggieSmalls[y] = "big"      
# print (biggieSmalls)

# 2) Count Positives - Given a list of numbers, create a function to replace the last value 
#    with the number of positive values. (Note that zero is not considered to be a positive number).

# assigned an array to varaible negToPos
#            0 1 2 3
negToPos = [-1,1,1,1]

posResult = 0 
# created loop to  loop though the list
for y in range (0,len(negToPos)):
    #create a condition that counts all positive numbers from 0
    if (negToPos[y] > 0):
        posResult += 1 # increasing the counter for the positive result
        
lastVal = len(negToPos)-1 # created a pointer to the last value
negToPos[lastVal]= posResult # took the last value and called on the desired array
# print (negToPos)

# 3)Sum Total - Create a function that takes a list and returns the sum of all the values in the list.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7


og_List = [1,2,3,4]

sum = 0
newSum = []

def sum_total(sum):
    for y in og_List:
        sum += y
        y = newSum
        return newSum


print (sum_total(og_List))






