# 1. Interpreted language - Python
 #  Compiler - C, C++, Java

 # 2. Object Oriented - Python, C++, Java

 # 3. Function - Python, C 

 # 4. Scripting Language - No Compilation Step - Python, JavaScript

import math

# print(dir(math))
# # import pdb ;pdb.set_trace();
# print("Hello")
# a = 10
# print(type(a))
# b = 20
# # print(10/0)
# a = "Anusha"
# print(type(a))
# b = "Anusha1"
# print(id(a), id(b))
# c = 10
# d = 10
# print(id(c), id(d))
# c = 12340009
# d = 12340009
# print(id(c), id(d))

# print("Hello")
# print "Hello"

#REPL - READ , EXECUTE, PRINT, LOOP

# IDLE - Intergrated Language Deveol Env - Sublime, VS Code, PyCharm, Eclipse


# print(a/b)
# print(a/c)
# print(b/a)

#import pdb ;pdb.set_trace();

# n - next line
# c - continue

# r - return
# q - quit





# Print Function
# print([values,], sep=" ", end="\n", flash=False)
# print()
# print(10)
# print(10,20,30)
# print(10,20,30, sep="@", end="&&");print(10,20,30, sep="*", end="&&&");

# Python shell act as calculator
# Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0] on linux
# Type "help", "copyright", "credits" or "license" for more information.
# >>> 10 + 20
# 30
# >>> 10 * 10
# 100
# >>> 10 ** 10
# 10000000000
# >>> 10 / 3
# 3.3333333333333335
# >>> 10 // 3
# 3
# >>> #3.99999 - 3 - floor value
# >>> # 3.00001 - 4 - ceil value
# >>> import math
# >>> dir(math)
# ['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']
# >>> math.floor(3.999)
# 3
# >>> math.ceil(3.000001)
# 4
# # >>> 
# >>> pow
# <built-in function pow>
# >>> pow(10,2)

# 100
# >>> 10 ** 2
# 100
# >>> 10 % 3
# 1
# >>> int(10/3)
# 3
# >>> 10 // 3
# 3
# >>> import sys
# >>> dir(sys)
# ['__breakpointhook__', '__displayhook__', '__doc__', '__excepthook__', '__interactivehook__', '__loader__', '__name__', '__package__', '__spec__', '__stderr__', '__stdin__', '__stdout__', '__unraisablehook__', '_base_executable', '_clear_type_cache', '_current_frames', '_debugmallocstats', '_framework', '_getframe', '_git', '_home', '_xoptions', 'abiflags', 'addaudithook', 'api_version', 'argv', 'audit', 'base_exec_prefix', 'base_prefix', 'breakpointhook', 'builtin_module_names', 'byteorder', 'call_tracing', 'callstats', 'copyright', 'displayhook', 'dont_write_bytecode', 'exc_info', 'excepthook', 'exec_prefix', 'executable', 'exit', 'flags', 'float_info', 'float_repr_style', 'get_asyncgen_hooks', 'get_coroutine_origin_tracking_depth', 'getallocatedblocks', 'getcheckinterval', 'getdefaultencoding', 'getdlopenflags', 'getfilesystemencodeerrors', 'getfilesystemencoding', 'getprofile', 'getrecursionlimit', 'getrefcount', 'getsizeof', 'getswitchinterval', 'gettrace', 'hash_info', 'hexversion', 'implementation', 'int_info', 'intern', 'is_finalizing', 'maxsize', 'maxunicode', 'meta_path', 'modules', 'path', 'path_hooks', 'path_importer_cache', 'platform', 'prefix', 'ps1', 'ps2', 'pycache_prefix', 'set_asyncgen_hooks', 'set_coroutine_origin_tracking_depth', 'setcheckinterval', 'setdlopenflags', 'setprofile', 'setrecursionlimit', 'setswitchinterval', 'settrace', 'stderr', 'stdin', 'stdout', 'thread_info', 'unraisablehook', 'version', 'version_info', 'warnoptions']
# >>> sys.builtin_module_names
# ('_abc', '_ast', '_bisect', '_blake2', '_codecs', '_collections', '_csv', '_datetime', '_elementtree', '_functools', '_heapq', '_imp', '_io', '_locale', '_md5', '_operator', '_pickle', '_posixsubprocess', '_random', '_sha1', '_sha256', '_sha3', '_sha512', '_signal', '_socket', '_sre', '_stat', '_statistics', '_string', '_struct', '_symtable', '_thread', '_tracemalloc', '_warnings', '_weakref', 'array', 'atexit', 'binascii', 'builtins', 'cmath', 'errno', 'faulthandler', 'fcntl', 'gc', 'grp', 'itertools', 'marshal', 'math', 'posix', 'pwd', 'pyexpat', 'select', 'spwd', 'sys', 'syslog', 'time', 'unicodedata', 'xxsubtype', 'zlib')
# >>> import builtins
# >>> dir(builtins)
# ['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'ZeroDivisionError', '_', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
# >>> min(10,20)
# 10
# >>> min([10,20])
# 10
# >>> min('Anusha', 'Sai')
# 'Anusha'
# >>> min('anusha', 'Sai')
# 'Sai'
# >>> max(10,20)
# 20
# >>> max('Anusha', 'Sai')
# 'Sai'
# >>> sum(10,20)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'int' object is not iterable
# >>> sum([10,20])
# 30
# >>> sum([10,20,-20])
# 10
# >>> type(10)
# <class 'int'>
# >>> type('Anusha')
# <class 'str'>
# >>> 
# KeyboardInterrupt
# >>> 

# indentaion & Blocks
# a = 10
# b = 10
# if a == b:
# 	print('True')
# 	print('print if condition')
# else:
# 	print(False)

statement = "We are learning Python, We are learning Python,We are learning Python, \
We are learning Python,We are learning Python,"
print(statement)

days = ['Monday', 'Tuesday', 'Wednesday', 
'Thursday', 'Friday']
# print(days)

statement = 'Hi, I am "Prashanth"'
# print(statement)
statement = "Hi, I'm Prashanth"
# print(statement)
statement = '''Hi, I'm "Prashanth"'''
# print(statement)
statement = """Hi, I'm "Prashanth"'"""
# print(statement)

statement = "We are learning Python, We are learning Python,We are learning Python, \
We are learning Python,We are learning Python,\
We are learning Python, We are learning Python,We are learning Python, \
We are learning Python,We are learning Python,\
We are learning Python, We are learning Python,We are learning Python, \
We are learning Python,We are learning Python,\
We are learning Python, We are learning Python,We are learning Python, \
We are learning Python,We are learning Python,\
We are learning Python, We are learning Python,We are learning Python, \
We are learning Python,We are learning Python,"
# print(statement)
# print("******************")
statement = """We are learning Python, We are learning Python,We are learning Python
We are learning Python,We are learning Python,
We are learning Python, We are learning Python,We are learning Python,
We are learning Python,We are learning Python,
We are learning Python, We are learning Python,We are learning Python, 
We are learning Python,We are learning Python,
We are learning Python, We are learning Python,We are learning Python, 
We are learning Python,We are learning Python,
We are learning Python, We are learning Python,We are learning Python,
We are learning Python,We are learning Python,"""
# print(statement)

# single line comment

"""
Multi line
comment
"""
'''
Multi line

comment

'''


# Multiple Statements on a Single Line

a = 10; b = 20;
# print(a) 
# print(b)

#import pdb; pdb.set_trace()

# a = 10
# b = 10

a = b = 10
# print(a, b)

# a = 10
# b = 20

a, b = 10, 20
# print(a, b)

a, b = b, a
# print(a, b)

# Python Identifiers

# 1. Variables - a-z, A-Z, 0-9,_ 
    # startswith _, a-z, A-Z,


 #Syntax
a1 = 10 # valid

_a1 = 20 # valid

# print(a1, _a1)
#1a = 30 # Not valid - invalid syntax

# standards
  #should be small letters
  #seperate with _

first_name = 'Kasam' # standard
FirstName = 'Kasam' # Not Standard
firstName = 'Kasam' # Not Standard

#2 functions, methods 

  # lower case, seperate with underscore

# Class

  #  Title Case

   # PythonCourse

# Contants
  # Upper Case, seperate with underscore

  # LIST_OF_NAMES = []


#   >>> import keyword
# >>> dir(keyword)
# ['__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'iskeyword', 'kwlist']
# >>> keyword.kwlist
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
# >>> global = 10
#   File "<stdin>", line 1
#     global = 10
#            ^
# SyntaxError: invalid syntax
# >>> keyword.kwlist.__len__()
# 35
# >>> len(keyword.kwlist)
# 35
# >>> if True and False:
# ... print("And")
#   File "<stdin>", line 2
#     print("And")
#     ^
# IndentationError: expected an indented block
# >>> print("And")
# And
# >>> import pandas as pd
# >>> import pandas
# >>> a = 10
# >>> a
# 10
# >>> del a
# >>> a
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'a' is not defined
# >>> import gc
# >>> from math import floor
# >>> 10 in [10,20,30]
# True

# pass keyword

def find_large_number():
  pass


# input vs raw_input

#python 2 

#input - datatype return number or string 
# raw_input - datatype return always string only

# >>> a = input("enter any number: ")
# enter any number: 10
# >>> type(a)
# <type 'int'>
# >>> b = input("enter any number: ")
# enter any number: 10.5
# >>> type(b)
# <type 'float'>
# >>> name = input("enter any name: ")
# enter any name: kpr
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<string>", line 1, in <module>
# NameError: name 'kpr' is not defined
# >>> name = input("enter any name: ")
# enter any name: 'kpr'
# >>> type(name)
# <type 'str'>
# >>> a = input("enter any number: ")
# enter any number: 10
# >>> type(a)
# <type 'int'>
# >>> a = raw_input("enter any number: ")
# enter any number: 10
# >>> type(a)
# <type 'str'>
# >>> name  = raw_input("enter any name: )
#   File "<stdin>", line 1
#     name  = raw_input("enter any name: )
#                                        ^
# SyntaxError: EOL while scanning string literal
# >>> name  = raw_input("enter any name: ")
# enter any name: kpr
# >>> type(name)
# <type 'str'>
# >>> 


# python3

#input - datatype return always string only
# raw_input - deprecated

# >>> a = input("enter any number: ")
# enter any number: 10
# >>> type(a)
# <class 'str'>
# >>> name = inupt("enter any name: ")
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'inupt' is not defined
# >>> name = input("enter any name: ")
# enter any name: kpr
# >>> type(name)
# <class 'str'>
# >>> b = 
# KeyboardInterrupt
# >>> b = input("enter any number: ")
# enter any number: 10.5
# >>> type(b)
# <class 'str'>
# >>> 
# >>> 
# >>> a = raw_input("")
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'raw_input' is not defined
# >>> 

# range vs xrange

# python2 

#range - return list

# xrange - return obj

# python3 

# range - return obj
# xrange - deprecated


# range([start], stop, [step]) # start - include, stop -exclude

# numbers = range(10) # range(0, 10, 1)
# print(numbers)
# print(list(numbers))
# print(type(numbers))

# numbers = range(0, 12) # range(0, 12, 1)
# print(list(numbers))

# numbers = range(0, 12, 2) # range(0, 12, 2)
# print(list(numbers))

# numbers = range(10, 0) # range(10, 0, 1)
# print(list(numbers))

# numbers = range(10, 0, -1) # range(10, 0, -1)
# print(list(numbers))

# numbers = range(-10, 0) # range(-10, 0, 1)
# print(list(numbers))

# numbers = range(-10, 0, -2) 
# print(list(numbers))
# numbers = range(10, -4, -2) 
# print(list(numbers))

# 0, 3, 6, 12 ... 99

# numbers = range(0, 100, 3)
# print(list(numbers))
