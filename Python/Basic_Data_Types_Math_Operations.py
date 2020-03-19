x = 5 #Integer
y = 10 #Integer
y = 10.05 #Float
y = 0xA #HexaDecimal
y = 0o12 #Octal
y = 0b1010 #Binary
print('x = ',x ,',','y = ',y)

#Comparison Operators
print('\nx == y', x == y)
print('x != y', x != y)
print('x <= y', x <= y)
print('x >= y', x >= y)
print('x < y', x < y)
print('x > y', x > y)

#Usual Opeartors
print('\nx + y = ' , x+y )
print('x - y = ' , x-y )
print('x * y = ' , x*y )
print('x / y = ' , x/y )

#Builtin Functions
print('\npow(x,y) =', pow(x,y))
print('abs(-x) =', abs(-x))
print('int(x) =', int(x))
print('int(y) =', int(y))

#Inline Notations Can Also Be Used
print('\nx = x+y ')
x += y
print('x = x-y ')
x -= y
print('x = x*y ')
x *= y
print('x = x/y ')
x /= y


#Multiple Assignments Can also be done
x, y, z = 4, 2, 10
print('\nx = ',x ,',','y = ',y)

#Bitwise Operators
print('\nOR: ', x | y)
print('NOR: ', x ^ y)
print('AND: ', x & y)
print('Left Shift ', x << y)
print('RIght Shift ', x >> y)
print('Inc=version ', -x)

######################################################################
#math module provides couple of constants
import math

pi = math.pi
exp = math.e

print('\nThe value of Pi ', pi)
print('The value of Exp ', exp)
print('Factorial ', math.factorial(5))
print('Log ', math.log(x))
print('Pow ', math.pow(x, 5))
print('Square Root ', math.sqrt(x))
print('Exponential ', math.exp(x))


#Float class can be used to create special numbers
pos_inf = float('inf')
neg_inf = float('-inf')
not_a_num = float('nan')

print ('\nPositive Infinte Number ', pos_inf)
print ('Negetive Infinite Number ', neg_inf)

# math module provide functions to detect these special numbers
print('\nmath.isinf(pos_inf) ', math.isinf(pos_inf))
print('math.isinf(neg_inf) ', math.isinf(neg_inf))
print('math.isnan(not_a_num) ', math.isinf(not_a_num))

# A NaN value is never equal to another NaN value
print('\nnot_a_num == not_a_num ', not_a_num == not_a_num)



# BOOLEAN : True or False
# The bool class is subclass of 'int'
# Zero value is considered as False and Non-Zero value is considered as True
x = 1
print('bool(x) ', bool(x))

y = 0
print('bool(y) ', bool(y))

#False values are
if not None: print('\nNone is False')
if not (0 or 0.0 or 0j): print('Zero is False')
if not ('' or [] or {}): print('Empty Sequences are False')
if not False: print('False is False')

# Implicit Type Conversion
x, y = 5 , 0.3
print('x type ', type(x))
print('y type ', type(y))

x = y
print('Float can be assigned to variable ', type(x))

x, y = 5 , 0.3
y = x
print('int can be assigned to float variable ', type(y))

b, i = True, 5
print('b type ', type(b))
print('i type ', type(i))

b = i
print('int can be assigned to boolean variable ', b)

b, i = False, 5
print('False considered to be 0 ', b + i)

b, i = True, 5
print('True considered to be 1 ', b + i)


