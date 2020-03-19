# Assignment statements in Python do not copy objects. they create bindings between a target and an object.


num_list = [1,2,3,4]
pow_list = [1,4,9,16]

print('num_list ', num_list)
print('pow_list ', pow_list)

num2_list = num_list
print('num2_list ', num2_list)

num2_list.append(5)
print('num2_list ', num2_list)
print('num1_list ', num_list) # Original List has also changed

# Sometimes we do not want original list not to be changed

# This can be achieved using copy module in python

# 2 types of copy available : deepcopy and shallowcopy

import copy

# Shallow Copy : Original List does not impacted
# constructing a new collection object and then populating it with references to the child objects found in the original
num3_list = copy.copy(num2_list)
num3_list.insert(1, 6)
print('\nnew list : num3_list ', num3_list)
print('old list : num2_list', num2_list)

num3_list.append([7,8])
num4_list = copy.copy(num3_list)
num4_list.append(9)
print('\n old list : num3_list', num3_list)
print('new list : num4_list', num4_list)

# Deep Copy : Original List Gets Impacted
# first constructing a new collection object and then recursively populating it with copies of the child objects found in the original.

num_list = [1,2,3,4]
num1_list = copy.deepcopy(num_list)
num1_list.insert(1, 6)
print('\nold list ', num_list)
print('new list ', num1_list)

num1_list.append([7,8])
num2_list = copy.deepcopy(num1_list)
num2_list.append(9)
print('\nold list ', num1_list)
print('new list ', num2_list)

# Child List Gets impacted in case of shallow copy()
org_list = [1,2,3,[4,5,6]]
shallow_list = org_list.copy()
shallow_list[3][1] = 7
print('\nOrg list ', org_list)
print('shallow list ', shallow_list)

# # Child List does not gets impacted in case of deep copy()
org_list = [1,2,3,[4,5,6]]
deep_list = copy.deepcopy(org_list)
deep_list[3][1] = 7
print('\nOrg list ', org_list)
print('shallow list ', deep_list)
