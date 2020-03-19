# A set object is an unordered collection of distinct hashable objects
''' Hashable Object: An object is hashable if it has a hash value which never changes during its lifetime
    (it needs a __hash__() method), and can be compared to other objects (it needs an __eq__() method). Hashable objects which compare equal must have the same hash value.
    Hashability makes an object usable as a dictionary key and a set member, because these data structures use the hash value internally.'''
# Most of Python’s immutable built-in objects are hashable
# Mutable Data Types such as List, Dictionary are not hashable.
# the order of elements in a set is undefined
# Set Type is mutable means we can add or remove elements from set.
# set is created using {}
# set is mutable but individual elements ins set are immutable

# Creating Set
s = {1,2,5,5,3,4,4,4}
print('set contains unique elements ', s)

s = {1,'One',1.1}
print('Set with mixed type values ', s)

empty_set = set()
empty_set = {}
print('empty set ', empty_set)

# String to Set
string_to_set = set('Quarrel')
print('string_to_set ', string_to_set)

# List to Set
list_to_set = set([10,50,50,40,30,30,20])
print('list_to_set ', list_to_set)

# Adding Elements into Set
new_set = {10,20,40,30,10}
new_set.add(50)
print('after adding new element ', new_set)

# Removing Element
new_set.discard(20)
print('after discarding element ', new_set)

new_set.discard(25)
print('after discarding non existing element , discard does not throw error')

#new_set.remove(25)# Will throw an error if the element does not exist

new_set.clear()
print('After Removing all elements ', new_set)

# del new_set


new_set = {10,20,40,30,10}
print('\nCheck if an element exist in Set ' , 10 in new_set)
print('Check if an element exist in Set ' , 50 not in new_set)

#Indexing and Slicing
#new_set[0] # TypeError: 'set' object is not subscriptable
#No modification allowed to individual element in set.


# Operations

fib = set( (1,1,2,3,5,8,13) )
prime = set( (2,3,5,15,7,11,13,15) )
print('\nFibnacci Set ', fib)
print('\nPrime Number Set ', prime)

print ('Union , All elems from both set ', fib | prime ) #fib.union(prime)
print ('Intersection , Common elems from both sets ', fib & prime) #intersection()
print ('Difference ', fib - prime)
print ('Difference ', prime - fib)#difference()
print ('Symmetric Difference : Unique from both set, excluding common elems ', fib ^ prime)#symmetric_difference()

#Built In Functions
print ('\nMin element in set ', min(prime))
print ('Max element in set ', max(prime))
print ('Length of Set ', len(prime))
print ('Sorting Set Elements ', sorted(prime)) # Ascending Order
print ('Sorting in reverse Order ', sorted(prime, reverse=True))

s = {'One', 'Two', 'Four', 'Three'}
print('\n min element in set ', min(s))

s = {2,'Two',2.1}
#print('\n min element in set ', min(s)) #TypeError: '<' not supported between instances of 'str' and 'int'


