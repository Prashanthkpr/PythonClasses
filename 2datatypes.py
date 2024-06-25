# bool 

# if 1:
#   print(True)
# if 0:
#   print(False)

# if ' ':
#   print('emty string')
# else:
#   print("else condition")

# == - it is check only values are equal or not

#  is -  it is check values and type are equal or not

# >>> bool(0)
# False
# >>> bool(1)
# True
# >>> bool(0.0000001)
# True
# >>> bool(0.0)
# False
# >>> bool('kpr')
# True
# >>> bool('')
# False
# >>> bool(' ')
# True
# >>> bool(0 == 0.0)
# True
# >>> bool(0.1 == 0.0)
# False
# >>> bool(0 is 0.0)
# False
# >>> bool(0 == None)
# False
# >>> bool(0 == '')
# False
# >>> bool()
# False



#Python Srings

name = "prashanth"

#positive index, 0 - p, 1-r, 2-a ...., len(name) - 1

#negative index, -1 - h, -2 - t, -3 - n ....

# print(name[0])
# print(name[1])
# print(name[-1])
# print(name[-2])
# print(len(name)) # function
# print(name.__len__()) # method
# print(name[9])  # IndexError: string index out of range
a = 10
# print(len(a)) #TypeError: object of type 'int' has no len()


# concatenation
# name + "reddy"

# print(name)

# name2 = name + "reddy" 

# print(name2)

# #print(name + 10) #TypeError: can only concatenate str (not "int") to str

# print(name + str(10))

# print(name + str(10.0))

# print(name + str([1,2]))

# # repetition

# print(name * 10)

#slicing

# str[[start]: stop: [step]] - default start - 0 index, stop - len(string) - 1, step - 1

# print(name[5])
# print(name[:5])  # name[0:5:1]
# print(name[:]) #name[0:len(name)]
# print(name[2:5])
# print(name[::2]) # name[0:end:2]
# print(name[:-2])
# print(name[-1:-4]) #name[-1:-4:1]
# print(name[-1:-4: -1])
# print(name[-4:-1])
# print(name[::-1]) # name[len(name): : -1] name.reverse(), reversed(string)
# print(name[::1]) # name[0: len(name): 1]
# print(name[::])
# # print(list(range(0, 10, -1)))
# # print(list(range(, , -1)))
# # print(dir(name))
# # print(name.reverse())
# print(list(reversed(name)))
# print(name)
# print(sorted(name))
# print(sorted(name, reverse=True))
# print(sorted(name, reverse=False))
# # print(sorted(name, key=lambda x: len(x)))
# print(name)

def reverse(name):
  result = ''
  for char in name:
    result = char + result
  return result

# print(reverse(name))

#Updating Strings

# print(name)

#name[0] = 'P' #TypeError: 'str' object does not support item assignment
# print(name)

#Single-Quoted Strings and Escaping Quotes

"Let's go!" #- string contains "'", So we are representating with ""

'"Hello, world!" she said' #- string contains '"', So we are representating with ''
'Let\'s go!' # with escape character \

"\"Hello, world!\" she said"

# print(str(10))
# print(int("10"))
# #print(int("10.0")) #ValueError: invalid literal for int() with base 10: '10.0'
# print(float("10.0"))
# print("Hello, world!")
# print("Hello, \nworld!")
# print(repr("Hello,\n world!"))
# print(str("Hello,\n world!"))
# print(type(name))
# print(type(10))


#Raw strings
path = "/home/shashi/Desktop/python"
# print(path)
# path = 'C:\nowhere'
# print(path)
# path = 'C:\\nowhere'
# print(path)
# path = r'C:\nowhere'
# print(path)
# path = "C:\\Program Files\\fnord\\foo\\bar\\baz\\frozz\\bozz"
# print(path)
# path = r"C:\Program Files\fnord\foo\bar\baz\frozz\bozz"
# print(path)
# print(len(name))
# print(name.__len__())
# print(dir(name))
#print(name.__dict__)
# import math
# print(math.__dict__)


# statement = f'hello my name is {name}, my age is {age}' #NameError: name 'age' is not defined
# print(statement)

age = "28"
# statement = f'hello my name is {name}, my age is {age}'
# print(statement)
# statement = 'hello my name is {}, my age is {}'.format(name, age)
# print(statement)
# statement = 'hello my name is {1}, my age is {0}'.format(age, name)
# print(statement)

# print(name)
# print(name.isalnum()) # a-z, A-Z, 0-9
# print("Prashanth@123".isalnum()) 

# print(name.isalpha()) # a-z, A-Z
# print("Prashanth123".isalpha())
# print(name.islower()) # all letters in small letters
# print("Prashanth".islower())
# print("prashanth123".islower())
# print("123".islower()) # no alphabates

# print(name.isupper()) # all letters in capital letters
# print("KPR".isupper())
# print("PRASHANTH123".isupper())
# print("123".isupper()) # no alphabates

# print("PRASHANTH123".isnumeric()) # only numbers
# print("123".isnumeric())
# print("123@#".isnumeric())

# print("Prashanth Kasam".isspace()) # only spaces
# print("".isspace())
# print(" ".isspace())
# print("    ".isspace())

# print("Prashanth".istitle())
# print("PRashanth".istitle())
# print("Prashanth Kasam".istitle())
# print("PrashanthKasam".istitle())
# print("Prashanth @ Kasam".istitle())
# print("Prashanth @Kasam".istitle())
# print(dir(str))
# print(name.isascii())
# print("普拉桑特".isascii())

# print("123".isdecimal())
# print("123".isdigit())
# print("123".isnumeric())
# print("\u0030".isdecimal())  #unicode for 0
# print("\u0030".isnumeric())  #unicode for 0
# print("\u0030".isdigit())  #unicode for 0
# print("123.10".isdecimal())
# print("123.10".isnumeric())
# print("123.10".isdigit())

# print("123a".isdecimal())
# print("123a".isnumeric())
# print("123a".isdigit())

# print("kpr".isidentifier())
# print("@kpr".isidentifier())
# print("_kpr".isidentifier())
# print("0kpr".isidentifier())
# print("kpr0".isidentifier())

# print("kpr".isprintable())
# print("普拉桑特".isprintable())
# print("\n".isprintable())
# print("\n")
# print(" ".isprintable())
# print("\t".isprintable())

# join

print(name)

# print(" ".join(name))
# print("@".join(name))
# #print("#".join([1,2,3])) #TypeError: sequence item 0: expected str instance, int found

# print("123".join(name))

# print(",".join(name))

# print(",".join(['vijay', 'prashanth', 'ravi']))

#split

# print(name.split()) # default ''
# print("prashanth kasam".split())
# print("prashanth kasam".split('a'))
# print("prashanth kasam".split('as'))

# replace

#print(name.replace()) #TypeError: replace expected at least 2 arguments, got 0

# print(name.replace("a", "b"))
# print(name.replace("as", "bbbb"))
# print(name.replace("as", ""))
# print("1Prasha1nth1".replace("1", ""))

# Capitalize
# print(name.capitalize())
# print("prashanth kasam".capitalize())
# print("prasHanTh Kasam".capitalize())

# title
# print(name.title())
# print("prashanth kasam".title())
# print("prasHanTh Kasam".title())

#swapcase

# print("PraShaNth".swapcase())

# find

# print(name.find('a')) # start - 0, end - len(name)
# print(name.find('a', 3)) # start - 3, end - len(name)
# print(name.find('a', 3, 5)) # start - 3, end - 4

# # if no index found then it will return -1

# print(name.find('an'))
# print(name.find('An'))
# print(name[-6], name[-1])
# print(name.find('an', -6, -1))
# print(name[-6:-1])
# print(name[-1:-6])
# print(name.find('an', -1, -6))

#rfind

# print(name.rfind("a"))
# print(name[-6:9])
# print(name.rfind('h', -6, 9))

#index

# print(name.index("a"))
# #print(name.index("A")) #ValueError: substring not found
# print(name.find("A"))

# name_e = name.encode("utf-8")
# print(name_e)
# print(name_e.decode("utf-8"))

# name_e = name.encode("utf-16")
# print(name_e)
# #print(name_e.decode("utf-8")) #UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte
# print(name_e.decode("utf-16"))

# strip

# print("  prashanth ".strip())
# print("@  prashanth @".strip())
# print("@  prashanth @".strip('@'))
# print("@  prashanth @".strip('@ '))
# print("@  prashanth reddy @".strip(' '))
# print("@  prashanth reddy @".lstrip(' @'))
# print("@  prashanth reddy @".rstrip(' @'))

#center

#print(name.center()) #TypeError: center expected at least 1 argument, got 0

# print(name.center(15))
# print(name.center(16))
# print(name.center(17))
# print(name.center(16))
# print(name.center(15, '@'))
# print(name.center(6, '@'))
# print(name.ljust(16, '@'))
# print(name.rjust(16, '@'))
# print(name.zfill(16))
# print("12345".zfill(8))
# print("7".zfill(2))


# startswith() vs endswith()

# print(name.startswith("pras"))
# print(name.startswith("Pras"))
# print(name.startswith("p"))


# print(name.endswith("nth"))
# print(name.endswith("Nth"))
# print(name.endswith("h"))


# print(name.startswith("pras", 2,6))
# print(name.startswith("as", 2,6))
# print(name.startswith("p", 2,6))

#count

# print(name.count("a"))
# print(name.count("h"))
# print(name.count("as"))

# print(name.count("a", 2,6))
# print(name.count("h", 2,6))
# print(name.count("as",2,6))

#maketrans() and translate()

# intab = "abc"

# outtab = "123"

# tab = str.maketrans(intab, outtab)

# string = "abcdabcd"

# print(string.translate(tab))


# intab = "abcd"

# outtab = "123"

# tab = str.maketrans(intab, outtab) #ValueError: the first two maketrans arguments must have equal length

# string = "abcdabcd"

# print(string.translate(tab))


# Lists

list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5 ];
list3 = ["a", "b", "c", "d"];

# print(list('123'))

# print(list1 + list2 )  #concat

# print(list1 * 2) # repetation

# # slicing
# print(list1[3])
# print(list1[-2])

# print(list1[:])
# print(list1[::])

# print(list1[2:-1])
# print(list1[::-1])  # start -0, stop - len(string), step = -1

# print(list1[::2])

list4 = [list1, 2, 3, list2, [5,6, list3]]
# print(list4)

# print(list4[2])
# print(list4[3])
# print(list4[3][2])
# # print(list4[4][3][2]) #IndexError: list index out of range
# print(list4[4][2][2])
# print(list4[-1][-1])
# # print(list4[-2][5]) #IndexError: list index out of range

# print(list4[-4:][2][1])


# update
# list4[-4:][2][1] = 'abc'
# print(list4)
# list4[1] = 'new'
# print(list4)
# print(list4[-4:][2][1][-1])

# del list4[2]
# print(list4)
# print(list4[-4:][2][1][-1])
# print(len(list4))

# print('new' in list4)
# print('a' in list4)
# print([5, 6, ['a', 'b', 'c', 'd']] in list4)
# print('a' in list4[-1][-1])
# print('a' in list4[-1][-1])
#print('9' in list4[0][2]) #TypeError: argument of type 'int' is not iterable
# print('7' in str(list4[0][2]))
# print('7' in str(list4[0][2]))


# print(max([1,2,35,10]))
# print(min([1,2,35,10]))
# print(list('prashanth'))
#print(list(100)) TypeError: 'int' object is not iterable

# List Methods

# print(list4)

# # append

# list4.append(10)
# print(list4)

# list5 = list4.append(20)
# print(list5)  # None will be return in to the list5

# # Count

# # print([1,2,3,1,3,4,4,4].count(4))
# # print([1,2,3,1,3,4,4,4].count(1))
# # print(list4.count(2))
# # print(list4[3].count(2))
# # print(list4.count([1,2,3,4,5]))

# # extend

# list4.append([1,2,3,4,5])
# # print(list4)

# list4.extend([1,2,3,4,5])
# # print(list4)

# # # list4.extend(100)
# # # print(list4)

# # list4.extend('abcd')
# # print(list4)

# # list4.extend((10,20,30))
# # print(list4)

# # list4.extend({'a': 1, 'b': 20})
# print(list4)

# # Index

# # print("Prashanth".index("a"))

# # print(list4.index(3))
# # print(list4.index(20))
# #print(list4.index(100)) # ValueError: 100 is not in list

# #print(dir(list))
# # print(dir(str))
# # print(list4)
# # print(name)
# # name[2] = 'Y'
# list4[2] = 300  # updation
# print(list4)

# # insert

# list4.insert(2, 400) # insert
# print(list4)

# # pop

# del list4[2]  # delete statement
# print(list4)

# result = list4.pop()
# print(result)
# print(list4)
# #print([].pop()) #IndexError: pop from empty list

# del list4[0][3]
# print(list4)
# result = list4.pop(0)
# print(result)
# print(list4)
# #print(list4.pop(20)) #IndexError: pop index out of range

# # remove

# result = list4.remove(300)
# print(result)
# print(list4)

# list4.remove(2)
# # list4.remove(2, 5)
# print(list4)
# #list4.remove(300) #ValueError: list.remove(x): x not in list

# result = list4.reverse()  # no return 
# print(result)
# print(list4)
# reverse
# list4 = list(reversed(list4)) # return reverse object iterator
# print(list4)

# # Sort

# # list4.sort() #TypeError: '<' not supported between instances of 'int' and 'list'
# # print(list4)

# list5 = [3,3,2,1,5,2,6,10,20, 30.5]

# # list5.sort()
# # print(list5)

# result = sorted(list5)
# print(result)

# result = sorted(list5, reverse=True)
# print(result)

# list6 = ['prashanth', 'anusha', 'sai', 'venkat', 'rakesh', 'sanju']

# result  = sorted(list6)
# print(result)

# result = sorted(list6, reverse=True)
# print(result)

# result = sorted(list6, key=lambda x: len(x), reverse=True)
# print(result)

# print(list4)

# # copy

# list7 = list4  # reference
# # print(list7, list4)

# list7[0][0] = 100  # reference
# print(list7)
# print(list4)
# list7[-1] = 400
# print(list7)
# print(list4)

# list8 = list4.copy() # shallow copy  [list, [list, [list], int, [int], [list], int]]
# print(list8)
# list8[-1] = 4000
# print(list8)
# print(list4)
# list8[0][0] = 1000
# print(list8)
# print(list4)

# import copy

# list9 = copy.copy(list4) # shallow copy
# print(list9)

# list10 = copy.deepcopy(list4)  # deep copy
# print(list10)
# print(list10[-1])
# list10[-1] = 7
# print(list10)
# print(list4)

# list10[0][0] = 2000
# print(list10)
# print(list4)


# # clear

# list10.clear()
# print(list10)

# print(name)

# print(bytes(name, 'utf-8'))
# print(bytes(name, 'utf-16'))
# print(bytes(name, 'utf-32'))

# print(bytearray(name, 'utf-8'))


# Tuples


# List vs Tuple

# list - mutable , []
# tuple - immutable, ()

# t1 = (10)
# print(t1)
# print(type(t1))

# t1 = (10,)
# print(t1)
# print(type(t1))

# t1 = ()
# print(t1)
# print(type(t1))

# t1 = tuple()
# print(t1)
# print(type(t1))

# l1 = list() # l1 = [] , s1 = '' or s1 = str()
# print(l1)
# print(type(l1))

# print(list4)

# t2 = tuple(list4)
# print(t2)
# print(type(t2))

# print(t2[0][3])

# del element

# print(t2[-1][2][0])
# del t2[-1][2][0]
# print(t2)

#del t2[1] # TypeError: 'tuple' object doesn't support item deletion

# print(t2)

#t2[1] = 20 #TypeError: 'tuple' object does not support item assignment

# t2[-1][2][0] = 'a'
# print(t2)

#del t2[0]

# print(dir(tuple))

# print(t2.count(3))
# print(t2.index(2))
# print(t2.index(10)) #ValueError: tuple.index(x): x not in tuple
#print(t2[10]) #IndexError: tuple index out of range

# print(t1)
# del t1
# print(t1) #NameError: name 't1' is not defined   - Exception

# t2.clear() #AttributeError: 'tuple' object has no attribute 'clear'
# print(t2)

#t2.find(10)

# print(t2[-5])

# t3 = (10,)
# print(t3)
# print(type(t3))
# print(t2 + t3)
# print(t2)

# t2.append(t3) #AttributeError: 'tuple' object has no attribute 'append'
# t2.extend(t3) #AttributeError: 'tuple' object has no attribute 'append'



# Dictinaries

# d1 = {}

# d2 = dict()

# print(type(d1), type(d2))

# d1 = {'name': 'prashanth', 'gender': 'male'}
# print(d1)
# d1['name'] = 'rakesh'
# print(d1)
# # d2 = {1: 'prashanth', 1.0: 'venkat', 1.5: 'sanju', [1,2]: 'anusha'} #TypeError: unhashable type: 'list'
# d2 = {1: 'prashanth', 1.0: 'venkat', 1.5: 'sanju', (1,2): 'anusha'}
# print(d2)
# d2 = {1: 'prashanth', 1.0: 'venkat', 1.5: 'sanju', (1): 'anusha'}
# print('d2', d2)
# d3 = {1: 'prashanth', 1.0: 'venkat', 1.5: 'sanju', (1,): 'anusha'}
# print('d3', d3)

# # Number, String, Tuple, Frozenset - immutable

# # List, Dict, Set - Mutable

# d2['name'] = 'prashanth' # insert or update
# print(d2)
# print(d2['name'])
# print(d2[1])
# print(d2[1.0])
# #print(d2[1.4]) #KeyError: 1.4

# del d2[1]
# print(d2)
# del d3
# #print(d3) #NameError: name 'd3' is not defined

# # print(len(d2))
# s1 = str(d2)
# # print(s1, type(s1))

# # JSON - javascript object notation - rest api

# # XMl - SOAP api 

# #import json

# # d3 = d2.clear()
# # print(d3)
# # print(d2)

# d3 = d2.copy() #shallow copy

# print(d3)

# d3['name'] = 'sai'
# print(d2, d3)

# d4 = d2  # reference
# d4['name'] = 'anusha'
# print(d2, d4)

# d2['items'] = {'fruit': 'mango', 'color': 'red'}
# print(d2, d3, d4)

# d5 = d2.copy()
# print(d5)
# d5['items']['fruit'] = 'apple'
# print(d5)
# print(d2)
# d5['name'] = 'prashanth'
# print(d5, d2)

# print(d2['name'])

# # get method

# print(d2.get('name'))
# print(d2.get('name1'))
# print(d2.get('name2', 'prashanth'))  # prashanth - default value if key not exists
# print(d2.get('name', 'prashanth'))

# # keys
# keys = d2.keys()
# print(keys)
# # for key in keys:
# #   print(key)
# # # print(keys[0])
# # for char in 'prashanth':
# #   print(char)
# # keys = list(d2.keys())
# # print(keys)
# # print(keys[0])

# values = d2.values()
# print(values)

# items = d2.items()
# print(items)


# # fromkeys

# # dict = dict.fromkeys(seq)

# # string , list, tuple - sequence

# d6 = dict.fromkeys('prashanth')
# print(d6)

# d6 = dict.fromkeys('prashanth', 'general')
# print(d6)

# d6 = dict.fromkeys(('prashanth', 'sai', 'anusha', 'venkat'))
# print(d6)

# # for item in d2.items():
# #   print(item, item[0], item[1])


# d2['name'] = 'venkat'
# res = d2.setdefault('name2', 'sai')
# print(d2, res)
# res = d2.get('name3', 'sanju')
# print(res, d2)

# # update -  one dict adding to the existing dict

# d2.update({'name': 'kpr', 'name4': 'anusha'})
# print(d2)

#  # pop

# res = d2.pop('name4')
# print(res, d2)

# #res = d2.pop('name4') #KeyError: 'name4'
# res = d2.pop('name4', 'NA')
# print(res, d2)

# # print(dir(dict))

# # popitem

# res = d2.popitem()
# print(res, d2)

# res = d2.popitem()
# print(res, d2)


# Set Data Type


 # {}, order is not preserved, no indexing, no keys.

# s1 = set()

# print(type(s1))

# s2 = {10, '10', 10.0, 'anusha', 'anusha'}
# print(s2)
# # #s2[0] #TypeError: 'set' object is not subscriptable
# # for s in s2:
# #   print(s)

# s3 = {10,  30, 40}
# print(s3)

# s4 = set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun", "Sun"])
# print(s4)

# # s3.add([10,20]) #TypeError: unhashable type: 'list'
# s3.add(20)
# print(s3)

# s3.update({50,60})
# print(s3)


# s3.update([70,80])
# print(s3)

# s3.add((90, 100))

# print(s3)

# # discard

# res = s3.discard(80)
# print(res)
# print(s3)

# res = s3.discard(100)
# print(res)
# print(s3)

# # remove
# print('----------remove------------')
# res = s3.remove(60)
# print(res)
# print(s3)


# # res = s3.remove(100) #KeyError: 100
# # print(res)
# # print(s3)

# # pop
# print('----------pop------------')
# res = s3.pop()
# print(res)
# print(s3)


# res = s3.pop()
# print(res)
# print(s3)


# DaysA = set(["Mon","Tue","Wed"])
# DaysB = set(["Wed","Thu","Fri","Sat","Sun"])
# print(DaysA, DaysB)

# AllDays = DaysA|DaysB

# print(AllDays)
# print(DaysA, DaysB)

# A = {1, 2, 3, 4, 5}

# B = {4, 5, 6, 7, 8}

# res = A.union(B)
# print(res)
# print(A)

# res = B.union(A)
# print(res)
# print(B)


# DaysA = set(["Mon","Tue","Wed"])
# DaysB = set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])

# print(DaysA > DaysB)
# print(DaysA < DaysB)

# # all

# l1 = [10.0, 10, 'anusha', True]
# print(all(l1))

# l1 = [10.0, 10, 'anusha', True, '']
# print(all(l1))
# l1 = [10.0, 10, 'anusha', True, 0]
# print(all(l1))

# print('---------any---------')
# l1 = [10.0, 10, 'anusha', True]
# print(any(l1))

# l1 = [10.0, 10, 'anusha', True, '']
# print(any(l1))
# l1 = [10.0, 10, 'anusha', True, 0]
# print(any(l1))

# l1 = [0.0, False, 0, '']
# print(any(l1))

l1 = [10, 20, 30]

# for item in l1:
#   print(item)

# for index in range(len(l1)):
#   print(index, l1[index])


# # enumetate
# print('--------------enumerate------------')
# for index, value in enumerate(l1):
#   print(index, value)
s1 = {1,2,3}
s2 = {4,5,6, 1,2,3}
print(s1.isdisjoint(s2)) # null intersection

print(s1.issubset(s2)) # Return True if another set contains this set

print(s1.issuperset(s2)) #Return True if this set contains another set


#frozenset - immutable set

f1 = frozenset([1,2,3])
print(f1)
print(type(f1))
# f1.add(10)


# bytes and bytesarray

b1 = bytes(10)
print(b1)

b2 = bytes('prashanth', 'utf-32')
print(b2)

b3 = bytes([1,2,3]) #TypeError: encoding without a string argument
# print(b3)

b1 = bytearray(10)
print(b1)

b2 = bytearray('普拉桑特kpr', 'utf-8', 'ignore')
print(b2)

b3 = bytearray([1,2,3])
print(b3)