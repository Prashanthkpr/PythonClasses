# floor division

print(10/3)
print(10//3)
print(10*2)
print(10**2)
print(10%3)

a = 10

a += 10 # a = a + 10
print(a)

a *= 10 # a = a * 10
print(a)

b = 0

if a:
	print(True)
else:
	print(False)


if a or b:
	print(True)
else:
	print(False)

if a or a / b:
	print(True)
else:
	print(False)

# if a / b or a:
# 	print(True)
# else:
# 	print(False)

# if a and a / b:
# 	print(True)
# else:
# 	print(False)

# if b and a / b:
# 	print(True)
# else:
# 	print(False)


# OR  True True True
# 	False False False
# 	True False True
# 	False True True  

# AND  True True True
# 	False False False
# 	True False False
# 	False True False 


# if (b and a / b):
# 	print(True)
# else:
# 	print(False)

# if (b and a / b) and a:
# 	print(True)
# else:
# 	print(False)

# if b and (a / b and a):
# 	print(True)
# else:
# 	print(False)

# if b or (a / b and a):
# 	print(True)
# else:
# 	print(False)

# if a | a / b:  # bitwise operaters
# 	print(True)
# else:
# 	print(False)

if 'anb' in 'anusha':
	print(True)
else:
	print(False)

if 'an' in 'anusha':
	print(True)
else:
	print(False)

if 10 in [20, 10, 30]:
	print(True)
else:
	print(False)

if 10 in [20, (10,), 30]:
	print(True)
else:
	print(False)

if 10 in {'a': 10, 'b': 20}:
	print(True)
else:
	print(False)

if 'a' in {'a': 10, 'b': 20}:
	print(True)
else:
	print(False)

# if 10 in 20:  #TypeError: argument of type 'int' is not iterable
# 	print(True)
# else:
# 	print(False)


#sequences - string, list, tuple - index 

#iterables - string, list, tuple, dict, set , frozenset

# if 10 in '1000': #TypeError: '<' not supported between instances of 'int' and 'str'
# 	print(True)
# else:
# 	print(False)

# if '10' in '1000':
# 	print(True)
# else:
# 	print(False)

# print(10 < '1000') #TypeError: '<' not supported between instances of 'int' and 'str'

# print(10.0 < '10.0')

if 10 in {'a': 'apple', 'b': 'ball'}: # 10 in ['a', 'b']
	print(True)
else:
	print(False)

# print('100' < 10) #TypeError: '<' not supported between instances of 'str' and 'int'


if 10 not in [10, 20]:
	print(True)
else:
	print(False)

print(10 == 10.0) # it will check values
print(10 is 10.0) # it will check values and data types