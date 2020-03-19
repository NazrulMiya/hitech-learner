# List is used to store heterogeneous elemnts.
# It can store elements of mixed data type
# It is index based, index starts from 0
# Elements in a list are mutable
# List is created using [] operator

#Empty List
empty_list = []
print('Empty List ', empty_list)

empty_list = list()
print('Empty List ', empty_list)

# List of elements
listA = ['Rocky', 30, 10000.0]
print('listA = ', listA)

# String to List
print('\nString to List :', list('Hello'))

# Tuple to List
print('\nTuple to List :', list((10,20,30,40)))

# Operations and Functions
print('\nIN Operator :', 30 in listA)
print('NOT IN Operator :', 30 not in listA)

listA.append(['New York',560103])
print('\nAdding elements into list : At the end :', listA)

listA.insert(3,1234567890)
print('Adding elements in between ',  listA)

listA.extend(['USA', 'Near Snt Jones Hospital'])
print('Adding another list :', listA)

print('\nLength of List :', len(listA))
#print('Min value in list :', min(listA)) # Error when Mixed Data Types Used
#print('Max value in list :', max(listA)) # Error when Mixed Data Types Used
#print('Sorting a list :', sorted(listA)) # Error when Mixed Data Types Used
print('Sorting in reverse order :', listA.reverse())

new_list = [40, 30, 20, 60, 50, 10]
print('\nMin value in list :', min(new_list)) 
print('Max value in list :', max(new_list)) 
print('Sorting a list :', sorted(new_list)) 

new_list.remove(60)
print('\nRemoving 60 from List ', new_list)

print('Removes an element from last and return it ', new_list.pop())

new_list.clear()
print('Removing All elements from list ', new_list)

del new_list

#print(new_list)

# Indexing and Slicing
new_list = list(range(1, 10))
print('\nNew List :', new_list)

print('4th Eleemnt :', new_list[3]) # n-1
print('4th up to 8th: ', new_list[4:9]) #n-1
print('All Eleemnts: ', new_list[:])
print('All 2nd alternate elements: ', new_list[::2]) #[start : up to stop : step]
print('Last Element: ', new_list[-1])
print('2nd Last Element: ', new_list[-2])
print('All elements from last: ', new_list[::-1])

new_list[4] = 50
print('Updating 4th indexed element :', new_list)

new_list = [10, 20, 30, 40, [50, 70]]
new_list[4].append(80)
print('appended to sublist ', new_list)
new_list[4].append([85,90])
print('inserted new list into sublist ', new_list)
