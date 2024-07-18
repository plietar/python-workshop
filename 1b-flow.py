# ==========================================================
# flow

# ----------------------------------------------------------
# logic

print(True  |  False) # True
print(True or  False) # True
print(True  &  False) # False
print(True and False) # False
print(not True)       # False
print(not [0,1,0])    # False
print(not [])         # True
print(1 == None)      # False
print(1 != None)      # True
print(1 in [0,1,2])   # True
print(0 < 1 < 2)      # True

# ----------------------------------------------------------
# if/else

if False:
  print('A')
elif False:
  print('B')
else:
  print('C')

print('A' if False else 'B')

# ----------------------------------------------------------
# loops

for a in 'abc':
  print(a,end=' ')
print()
# a b c

for i in range(0,3,1): # start,stop,step
  print(i,end=' ')
print()
# 0 1 2

i = 0.0
while i < 3.0:
  print(i,end=' ')
  i += 0.5
print()
# 0.0 0.5 1.0 1.5 2.0 2.5

# not shown: yield, break, continue <- next

# ----------------------------------------------------------
# comprehensions

print([i for i in range(3)])
# [0,1,2]

print([i for i in range(10)
  if (i % 2 == 0) ])
# [0,2,4,6,8]

print([i if (i % 2 == 0) else None
  for i in range(10)])
# [0,None,2,None,4,None,6,None,8,None]

# ----------------------------------------------------------
# enumerate + zip

print([ij for ij in enumerate('abc')])
# [(0,'a'),(1,'b'),(1,'c')]

print([ij for ij in zip([3,4,5],'abc')])
# [(3,'a'),(4,'b'),(5,'c')]

print([j for i,j in zip([3,4,5],'abc')])
# ['a','b','c']

print([ij for ij in zip([3,4,5],'a')])
# [(3,'a')] stops at shortest (*)

# ----------------------------------------------------------
# functions

def f0():
  return 'hello!'
print(f0()) # hello!

def f1():
  return 3,4,5
a,b,c = f1()
print(b) # 4

def f_abc(a,b,c=3):
  return a+b+c
print(f_abc(1,2)) # 6

def f_kwds(*args):
  return args
print(f_kwds(1,2,3)) # (1,2,3)

def f_kwds(**kwds):
  return kwds
print(f_kwds(a=1,b=2,c=3)) # {'a':1,'b':2,'c':3}

# ----------------------------------------------------------
# lambda functions

f = lambda x: x+1
print(f(1)) # 2

# ----------------------------------------------------------
# packages

import random # import everything in random
print(random.uniform(0,1))

import random as rnd # import everything using an alias
print(rnd.uniform(0,1))

from random import uniform # import just uniform
print(uniform(0,1))

from random import uniform as uni # import just uniform using an alias
print(uni(0,1))

from random import * # import everything without prefix (like R)
print(betavariate(1,1))

# ----------------------------------------------------------
# local package: needs 2 things
# 1. a file __init__.py: runs on load & can be empty
# 2. other files with functions / variables

from pkg import greetings # import everything in greetings file
greetings.hello('world')  # hello world!

greetings.punct = '.'     # modify the package variable
greetings.hello('world')  # hello world.
