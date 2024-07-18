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
# [(1,'a'),(2,'b'),(3,'c')]

print([ij for ij in zip([1,2,3],'abc')])
# [(1,'a'),(2,'b'),(3,'c')]

print([j for i,j in zip([1,2,3],'abc')])
# ['a','b','c']

print([ij for ij in zip([1,2,3],'a')])
# [(1,'a')] stops at shortest (*)

# ----------------------------------------------------------
# functions

def f0():
  return 'hello!'
print(f0()) # hello!

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
