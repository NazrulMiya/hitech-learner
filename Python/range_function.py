# range() is a built-in function of python.
# range() function generates the integer numbers between the given start integer to the stop integer, which is generally used to iterate over with for Loop
# syntax : range (start, stop[, step])
# ange() function only works with the integers i.e., whole numbers.


print ('range(5) ', list(range(5))) #n-1
print ('range(10,20) ', list(range(10,20)))
print ('range(10,20, 2) ', list(range(10, 20, 2)))

print ('range(-20, -10, 2) ', list(range(-20, -10, 2)))
print ('range(4,-1,-1) ', list(range(4,-5,-2)))
#Using in For Loop

for i in range(10,20,1):
    if ( i % 2 == 0):
        print(i, ' is Even Number ')
    else:
        print(i, ' is Odd Number ')



    
