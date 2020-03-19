# tuple class creates immutable sequence type
# once created can not be modified
# created using () operator

empty_tuple = ()
print('Empty Tuple ', empty_tuple)

tupleA = (10, 20, 10, 30)
print('Tuple :', tupleA)

tupleA = (10, 20, 30, 'Rocky', 10.01)
print('Tuple :', tupleA)


print(tupleA[0])

#tupleA[0] = 2.5 #TypeError: 'tuple' object does not support item assignment

print(tupleA[0])

#del tupleA[0] TypeError: 'tuple' object doesn't support item deletion

del tupleA #Delete whole tuple







