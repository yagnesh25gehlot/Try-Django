'''
loops,
datatype: int, no double in python, float, string, convert to string and vice versa
'''
import math
from collections import deque

a = 5
b= 2
print(a/b) # true division
a = -5
print(a//b) #floor division
a=-5.0
b=2.1
print(a//b)

a = -2.5
b = "yagnesh"
b= b + str(a) # string conversion
print(b)

b = '-234.6'
a = 'yagnesh'
b = 1 + float(b)
# a = int(a)
# print(a) not allowed
print(b)
print(round(b)) # nearest integer
print(math.ceil(b)) # greater integer
print(math.floor(b)) # smaller integer
print(int(b)) # remove decimal part
b = '-0000234.56'
print(float(b))
print(int(float(b))) # directly can't convert into integer


'''
int/float/double/math: +, -, *, /,//, floor, ceil, power, sqrt, log,max, min, abs, binarysearch, , conversions,
bitwise operators--> and, or, xor, 1<<1, !~,
conditionsL: && ||
'''
print(math.pow(10,3.2), 10**3.2, math.sqrt(1000), math.log(1000), (math.log(16)/math.log(2)),
      max(5.5 , 6), min(0, -7), abs(-8.23) )

print(2|4, 5&6, 5^6, 1<<2, 4>>1, ~1) # bit wise operators

print(min(-float('nan'), float('inf'))) #
float('inf') # interges don't have a maximum value so choose as per your choice


for i in range(0,7):
    if i>0 and i%2==0 or i%3==0:
        print("oh")
    elif i%5 ==0:
        print('ok')
    else:
        print('calm down')



'''
string: ith charcter, set ith charater, remmove, add, reverse, find something in it, substring, length, split,
'''
a = "Yagnesh Gehlot"

print(a[0::2], len(a), a[::-1], a[2:5], a.__add__("ulf Nikku")) # [start: end excluded: steps] , substring, add, reverse
a = a[:3:]+'b'+a[3+1::] # replacing the ith chacter in string
print(a, sorted(a))
for i in range(0,len(a)):
    print(a[i])
    # a[i]='b'
print(a)
print(a.find("Gehlot"), a.upper(), a.lower(), ('a' in a))
a = "Yagn//esh G//ehlot"
b = a.split(" ") # or by / no issue in it
print(b)
# .strip()




'''
list
arr
dynamic array, ith index, modify ith index, iterator, loop in it, remove last element, add, remove , 
get, clear, 2-d mattrix
convert one ds to another --> set, linkedlist, length, check null

Linked-list:
add first, add last, size
'''
a=[1,2,3,'e',4, 7] # can be used as (array, list, stack, vector)
a.append(5)
a.append(6)
a.pop()
a[0]=72
a[1]='kadar khan'
print(a[1:4:2], a[len(a)-1])
a=["ram", "nom", "japa", "karo", "rau"]
a= sorted( a, key = lambda x: (len(x), x[len(x)-1], -ord(x[len(x)-1]), x ), reverse=False) # all conditions in tuple


# a= sorted(a, key= lambda x: (x, len(x)))

print(a)
print(ord("A")) # gives unicode
a.clear()
a = lambda x,y: (x+y, x-y)
print(a(1,3))
a =[]
a.append([1,2,3])
a.append(9)
print(len(a), len(a[0]) )


from collections import deque
b = deque([1,2,3,a]) # used as (deque, queue, linkedlist)

b.append('7')
b.append('7')
b.appendleft('7')
b.appendleft('8')
b.pop()
b.popleft()
print(b)
for i,v in enumerate(b):
    print(i, v, b[i], b[0], b[-1])





'''
Treeset: add, remove, first, last, removefirst, removelast, checkIfElement exsists, iterate, front & back, ordering
ceiling floor, greater, lower, 
TreeMap: keys and values, set natural ordering

set: generatign hash code: modify, equals
hashset

heap: max, min, add, remove first, set natural order, iterate in it
'''

s = {1,100, 30} # hashset
s = {'key': 'value', 1:5} #hashmap
print(s)

from sortedcontainers import SortedSet, SortedDict
s = SortedSet([1, -2, 2, 3, -3], key=lambda x: (-abs(x), x))
s.add(-4)
s.remove(2)
print(s, s[0], s[-1], (-2 in s), s.bisect_left(2.5), s.bisect_right(2.5))
#[-4, -3, 3, -2, 1] element lesss that equal to x, and bisect_rignt elements grater that x
# we can use same for finding greater, smaller, ceil and floor
for i in reversed(s):
    print(i)


sorted_dict = SortedDict() # no ordering of elements
# Adding elements
sorted_dict["apple"] = 1
sorted_dict["kiwi"] = 2
sorted_dict["banana"] = 3
sorted_dict["grape"] = 4
# sorted(sorted_dict)
# del(sorted_dict['apple'])

for k,v in sorted_dict.items():
    print(k, "--> ", v, sorted_dict.peekitem(0)[1], sorted_dict.peekitem(-1)[1])
for v in sorted_dict.keys():
    v = a
    # sorted_dict[v]

for v in sorted_dict.values():
    v = a




class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Overriding __eq__() for custom equality comparison
    def __eq__(self, other):
        if isinstance(other, Person):
            return self.name == other.name and self.age == other.age
        return False

    # Overriding __hash__() to return a hash value based on name and age
    def __hash__(self):
        return hash((self.name, self.age))  # Combine name and age into a tuple and hash it

    # Optional: for better representation
    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"

# Create a set or dictionary
people_set = {Person("Alice", 25), Person("Bob", 30), Person("Alice", 25)}

# Print the set to show that duplicates are removed
print(people_set)  # Output: {Person(name=Alice, age=25), Person(name=Bob, age=30)}




import random

a = random.randint(1, 100)
print(a)
a = random.uniform(100.5, 2000.3)
print(a)
# a = int(input("give your input here"))
print(a)



'''
Treeset: add, remove, first, last, removefirst, removelast, checkIfElement exsists, iterate, front & back, ordering
ceiling floor, greater, lower, 
TreeMap: keys and values, set natural ordering

set: generatign hash code: modify, equals
hashset

heap: max, min, add, remove first, set natural order, iterate in it

input and output, random 
filehandeling
'''