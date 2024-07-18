# ==========================================================
# basics

# (!) python error
#  <- {approx R syntax}
# (*) different behaviour from R

# ----------------------------------------------------------
# hello world

print('hello world!')

# variable assignment
a = 1   # OK
_ = 2   # OK
# . = 3 # (!) invalid syntax

# ----------------------------------------------------------
# single object types

# types
print(type(1))
print(type(1.0))
print(type('a'))
print(type(True)) # <- TRUE
print(type(None)) # <- NULL

# casting: changing type
print(bool(1))  # True
print(float(1)) # 1.0
print(int('1')) # 1

# False-y things
print(bool(False or 0 or [] or {} or None)) # False (*)

# ----------------------------------------------------------
# strings <- character()
s1 = 'ab'
s2 = 'c'
print(s1[0]) # a
print(s1+s2) # abc

# ----------------------------------------------------------
# tuples <- c()
t = (3,4)
print(t)    # (3,4)
print(t[0]) # 3
# t[1] = 0  # (!) does not support item assignment
t0,t1 = t   # expandable (*)
print(t0)   # 3

# ----------------------------------------------------------
# list <- c()
l = [3,4]
print(l)      # [3,4]
print(l[0])   # 3
l[0] = 3      # OK
print(l0)     # 3
# l[2] = 5    # (!) list assignment index out of range

# modifying lists
print([l,5])       # [[3,4],5] nested (*)
print(l.append(5)) # None, l modified in-place (*)
print(l)           # [3,4,5]
l.extend([6,7])    # None, l modified in-place (*)
print(l)           # [3,4,5,6,7]

# indexing lists (*)
print(l[0:3])     # [3,4,5] l[3] is not included
print(l[:3])      # [3,4,5] all elements up to but not including l[3]
print(l[3:])      # [6,7]   all elements from l[3] to end
print(l[-1])      # 7       index backwards from end
print(l[-3:])     # [5,6,7] last 3 elements
# print(l[3.0])   # (!) list indices must be integers or slices
# print(l[[0,3]]) # (!) list indices must be integers or slices

# list misc (*)
print(len(l))     # 5
print(l.index(3)) # 0
print(l.count(3)) # 1
# le = l.pop(-1)    # remove last element in-place
# print(l)          # [3,4,5,6]
# print(le)         # 7

# operators
# print(l+1) # (!) can only concatenate list to list
# print(l-1) # (!) unsupported operand type(s) for -
print(l+l)   # [3,4,5,6, 3,4,5,6]
print(l*2)   # [3,4,5,6, 3,4,5,6]
# print(l*l) # (!) can't multiply sequence by non-int

# ----------------------------------------------------------
# dicts <- list()
d1 = {'a':1,'b':2} # construct
d2 = dict(a=1,b=2) # alt construct
print(d1)          # {'a':1,'b':2}
print(d2)          # {'a':1,'b':2}

# accessing dicts
print(d1['a'])         # 1
# print(d1.a)          # (!) object has no attribute 'a'
# print(d1[('a','b')]) # (!) key error (*)
d1['a'] = 0            # OK to overwrite
d1['c'] = 4            # OK to add new
d1[(0,1)] = 99         # OK keys can be anything
print(d1)              # {'a':0,'b':2,'c':4,(0,1):99}
d1.update(d2)          # overwrite keys 'a','b'
d1.update(c=3)         # overwrite key 'c'
print(d1)              # {'a':1,'b':2,'c':3,(0,1):99}

# iterating over dicts (*)
print(len(d1))     # 4
print(d1.keys())   # ['a','b','c',(0,1)]
print(d1.values()) # [1,2,3,99]
print(d1.items())  # [('a',1),('b',2),('c',3),((0,1),99)]

# ----------------------------------------------------------
# variable modification
print(2^2)         # 0 (*)
print(2**2)        # 4 (*)
a += 1; print(a)   # 2
a *= 3; print(a)   # 6
a /= 2; print(a)   # 3.0
a -= 1; print(a)   # 2.0
l += [0]; print(l) # [3,4,5,6,7,0]

