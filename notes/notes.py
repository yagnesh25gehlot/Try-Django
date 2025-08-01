#       Python Notes
# import psycopg2

a = ["a", "b", "c"]
a.append("e")
print(id(a))
print("-->".join(a))


'''
Global Interpretor Lock:

1.The Global Interpreter Lock (GIL) is a mechanism in CPython (the default Python implementation) that ensures only one 
thread executes Python bytecode at a time, even on multi-core processors. This means Python threads are not truly
 parallel when executing CPU-bound tasks.
2. To avoid GIL we should multi processing instead of multithreading
3. In multithreaded envioronment GIL creates the bottel neck, means thread sare not parallel in python.
'''

# functions are also like variables

def print_me(a):
    print(f'you are fine honey {a} and {{ Hello }} \ \\ / //  \\\\  {{  and {a} }}')
x = print_me
x("yagnesh")



# del delete will the reference of a object from memory

class CustomError(Exception):
    pass

del print_me

def first_function():
    try:
        print(print_me)
    except Exception as e:
        print(e)
        raise CustomError(e)
    else:
        print("yagnesh is a good boy")
        pass
    finally:
        print(x)
        print(id(x))
        print("finally finally finally!")

try:
    first_function()
except CustomError as e:
    print("Error k uppar ek or error", e)

# pass does nothing. other wise gives intendation error
# continue skips the current iteration in loops.
# break terminates the loop.




'''
Multiprocessing and Multi-threading

1.Multiprocessing is used for CPU bound tasks. should be kept in if __name__ == '__main__', because spawn is happened
in macOS ad windows, but now in linux. each process have its own GIL.

2. Multithreading is used for I/O bound tasks. GIL is released during I/O process

3. Libraries like NumPy, Pandas, TensorFlow use C extensions to bypass the GIL by running code in C.
import numpy as np

arr = np.random.rand(10**7)
result = np.sum(arr) 

4. args are passed as args=(10**7,) not args=(10**7)
'''

import threading
import multiprocessing
import time

def long_running_function(limit):
    count = 0
    for _ in range(10, limit):
        count+=1



threads = [ threading.Thread(target=long_running_function, args=(10**2,)) for _ in range(5)]
processes = [ multiprocessing.Process(target=long_running_function, args=(100**1,)) for _ in range(5)]


# Modify the download function to accept two URLs
def download(url1, url2):
    response1 = url1
    response2 = url2
    return (response1, response2)  # Returning the content of both URLs


# List of tuples containing pairs of URLs
urls = [
    ("https://www.example.com", "https://www.example2.com"),
    ("https://www.example3.com", "https://www.example4.com"),
    ("https://www.example5.com", "https://www.example6.com"),
    ("https://www.example7.com", "https://www.example8.com"),
    # Add more pairs of URLs as needed
]


'''
if __name__ == '__main__':
    for process in processes:
        process.start()
    start_time = time.time()
    for process in processes:
        process.join()
    print(f'Time to run all process is {time.time() - start_time}')

    start_time = time.time()
    for i in range(5):
        threads[i].start()

    for i in range(5):
        threads[i].join()
    print(f'Time to run all threads is {time.time() - start_time}')

    from concurrent.futures import ThreadPoolExecutor

    # Using ThreadPoolExecutor to download concurrently
    with ThreadPoolExecutor() as executor:
        results = executor.map(lambda urls: download(*urls), urls)

    # Process the results
    for result in results:
        content1, content2 = result  # Unpack the content of both URLs
        print(f"Content of first URL: {len(content1)} characters")
        print(f"Content of second URL: {len(content2)} characters")

    # from multiprocessing import Pool
    # with Pool() as pool:
    #     results = pool.map(download, urls)
        # results = pool.apply_async(download, urls)
    # print(results," ok done!")
'''






'''
*args, **kwargs
functions return None if return nothing
type give what type it is
'''

def ab():
    def a():
        pass
    def b():
        pass
    return (a,b)

a,b = ab()
print(a, id(a))


import copy
z = 2,3
y1 = copy.copy(z) # shallow copy
y2 = copy.deepcopy(z) # deep copy
li = [1, 2, 3]
l1 = li.copy() # shallow copy
l2 = l1[:]
'''
start → The index where the slice starts (inclusive).
stop → The index where the slice ends (exclusive).
step → The step size (optional, defaults to 1).
new_list = original_list[start:stop:step]
'''
print(id(y1) , id(z), id(y2))
c,d = 1,2,
print(z, type(z), type(a), c, d) # z has become a tuple



'''
Class:

Public members
all attributes and functionas are public by default

Private Members
Accessible only inside the class.
Use double underscore __ prefix to indicate private attributes or methods.
Name mangling: Python renames private members internally to _ClassName__attribute.

Protected Mehtords
Use a single underscore _ prefix.
Can be accessed in child classes but not recommended outside the class (it's a convention, not enforced).

Types of Inheritance supported:
Single Inheritance – One parent, one child.
Multiple Inheritance – A child inherits from multiple parents.
Multilevel Inheritance – A child inherits from another child.
Hierarchical Inheritance – Multiple children inherit from the same parent.
Hybrid Inheritance – A combination of different inheritance types.



Dunder methords of a class
__init__(), __del__(), 
__dict__ = have dictionary of all instance variable. \
__class__ = gives information about class

@staticmethord: utility methord inside a class
@classmethord: class mehtord

'''

class Jeev:
    pass

class Animal(Jeev):
    mouth = "mouth"
    hobby = "hobby"
    def __init__(self):
        print('I am animal')
    pass

class Dog(Animal, Jeev):
    mouth = "bad mouth" # class variable
    def __init__(self, leg):
        print( self.mouth, super().mouth)
        super().__init__()
        self.__leg = leg
        self._protected_leg = leg + leg
        self.public_leg = leg + leg + leg
    def __del__(self):
        pass

    @classmethod
    def just_dog_mehtord(cls):
        print("bas dog k bare m h print karna h")


    @staticmethod
    def just_cat_function_inside_dog(value):
        print(f"just print {value}")




dog = Dog(4)
# dog.__leg
print( dog._Dog__leg, dog._protected_leg, dog.public_leg, Dog.mouth)
try:
    print(dog.age)
except Exception as e:
    print(e)
    dog.age = 3
    print(dog.age)
print(dog.age, Dog.__dict__)


# final class
class FinalClass:
    def __init__(self):
        if type(self) != FinalClass:
            raise TypeError("Inheritance is not allowed!")

# class Child(FinalClass):  # ❌ Will raise an error
#     pass

obj = FinalClass()  # ✅ Works fine

attributes = {'name': 'Bob', 'age': 25, 'city': 'New York'}
for key, value in attributes.items():
    setattr(dog, key, value)
    hasattr(dog,'name')
    delattr(dog,key)
    dog.__setattr__(key, value+ value)
    print(dog.__dict__[key])

Dog.just_dog_mehtord()
Dog.just_cat_function_inside_dog(32)
print(type(dog), dog.__class__)


'''
Python does not have interfaces
Enum: cant use self, cant use class methord and static methords
Abstract class
'''

from enum import Enum


class Week(Enum):
    MONDAY=1
    TUESDAY=2
    # def __init__(self):
    #     self.day = 'kuch bhi'
    #     self.MONDAY = 3
    # def random_function(self):
    #     print('not same as java enum, just cant call constructor')

    @classmethod
    def random(cls):
        print("just do it")


    @staticmethod
    def random1():
        print("just do it again")

day = Week.TUESDAY
# day1 = Week()  : cannot call constructor
print(Week.MONDAY, Week.TUESDAY, day, day.__class__, day.random(), day.random1(), 'ok')



from abc import ABC, abstractmethod

class Billa(ABC):
    @abstractmethod
    def mi(self, value):
        pass

class Kity:
    def __init__(self, value):
        print("Kitty jag gaye", value)

class Sher:
    def __init__(self, value):
        print("Sher h hum", value)

class Tiger:
    value = 'parcel'
    pass

class Cat(Billa, Kity, Sher, Tiger):
    __p2 = 56
    _p3 = 82
    def __init__(self, value):
        self.__p1 = 12
        # super().__init__(self)
        Kity.__init__(self, value)
        Sher.__init__(self, value)
        # Tiger.__init__(self)


# cant have same function names
#     def mi(self):
#         print("not this")

    def mi(self, value):
        print("this one", value)

cat = Cat(72)
cat.mi(72)
print(cat._p3, cat._Cat__p1)
# cat.mi()


cat.__setattr__("John", cat)
delattr(cat, "John")
print(cat.__dict__)



class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
        self.date = {}
        self.__sufficient = 'Yagnesh'


    @property
    def  sufficient(self):
        return self.__sufficient

    @sufficient.setter
    def sufficient(self,value):
        self.__sufficient = value

    @sufficient.deleter
    def sufficient(self):
        del self.__sufficient


    def __getitem__(self, key):
        return self.date[key]

    def __setitem__(self, key, value):
        self.date[key] = value

    def __eq__(self, value):
        if value.day == day and value.month == self.month and value.year == self.year:
            return True
        return False

    def __repr__(self):
        return f"{self.day} +  {self.month} + {self.year}"


    @classmethod
    def get_date(cls, date):
        day, month, year = date.split('-')
        return cls(int(day), int(month), int(year))

date = Date(28,10,2024)
print(date,day)
date1 = Date.get_date('27-08-2024')
print(str(date.month), date.__class__.mro()) # method resolution order

print(date == date1)

date["yagnesh"]=72
print(date["yagnesh"])
print(date.__repr__())
print(locals())
print(globals())

y=20
x=200
try:
    print(eval('date'))
except Exception as e:
    print(e)

type(dog)

# Define a method outside of the class
def greet(self):
    return f"Hello, my name is {self.name}!"

# Creating the class dynamically
Person = type('Person', (), {'species': 'Homo sapiens', 'cheat': greet})
p = Person()
p.name = "Alice"  # Adding an attribute dynamically
print(p.cheat())
# del(dog)
# del dog


class Child:
    def __new__(cls, a):
        instance = super().__new__(cls)
        instance.value = a
        return instance


    def __init__(self, a):
        self.value1 = a

    def clone_yes(self):
        return "boo"

child = Child(1)
print(child.value1, child.value)


class Play(Child):
    def clone_yes(self):
        return "boo ya"

play = Play(1)
print(play.clone_yes(), Child.clone_yes(play))


class Validate(type):
    def __new__(cls, name, bases, dct):
        if "status" not in dct:
            raise ValueError("Status not present.")
        return super().__new__(cls, name, bases, dct)

class Obj(metaclass=Validate):
    status = True






# obj = Obj()

class Objc:
    name = True
    status = True
    def __enter__(self):
        print("entered in the context")
        return self


    def __exit__(self, exc_type, exc_value, traceback):
        print("Exited the context.")
        # Optionally, handle exceptions here
        if exc_type:
            print(f"An exception occurred: {exc_value}")
        return False  # Return False to propagate exceptions (default behavior).


with Objc() as o:
    print("what it is.")



def generator_function(n):
    for i in range(0,n+1):
        yield i
    yield "done"
generator = iter(generator_function(1))
print(next(generator))
print(next(generator))
print(next(generator))
# print(next(generator))
# obj = Objj()
a = "hello"
iter = a.__iter__()
print(iter.__next__())
print(iter.__next__())
print(iter.__next__())
print(iter.__next__())
print(next(iter))
print("--"*30)



# DSA
entries = [1,2,3]
entries.append(4)
entries.remove(1)
# entries.pop()
for i in entries:
    print(i)
entries.clear()

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

    def add(self, head, v):
        node = LinkedList(v)
        root = head
        while root.next:
            root = root.next
        root.next = node

    def print(self, head):
        root = head
        while root:
            print(root.value,end="->")
            root = root.next

a = LinkedList(1)
a.add(a, 2)
a.add(a, 3)
a.print(a)


from collections import deque
a = deque([1,2])
a.append(3)
a.appendleft(0)
a.append(3)
a.appendleft(0)
a.pop()
a.popleft()

for i in a:
    print(i,end=" ")

#  Stack
entities = []
entities.append(7)
entities.append(8)
entities.append(8)
entities.append(9)
entities.pop()  # Corrected 'entries' to 'entities'
for i in entities:
    print(i)


s = {111, 1, 2, 3, 4, 5}

for a,b in enumerate(s):
    print(a,"is index and value is",b, end="-->")
s.add(5)
s.add(6)
s.add(7)
s.remove(2)
s.discard(88)
s.pop()
s.add(88)
s.add(10)

s.pop()
# s.remove(77)
for i in s:
    print(i,end="..")

s= {88:77, 'a': 1, "abc": 45, 1: 7}
s[77]=88
s.pop(1)
s.get('a')

for v in s:
    print(s)

for k,v in s.items():
    print(k,"-",v, end="    ")

# min heap and max heap

import heapq
a = [] # min heap
b = [] # max heap

heapq.heappush(a,1)
heapq.heappush(a, 2)
heapq.heappush(a,1)
heapq.heappush(a,0)

heapq.heappush(b,-1)
heapq.heappush(b, -2)
heapq.heappush(b,-1)
heapq.heappush(b,-0)

for i in a:
    print(i, end="mi")

for i in b:
    print(-1*i, end="ma")


entries = ['yes' for x in range(0,20) if x%2 == 0]
print(entries)

entries = [ 'yes' if x%2==0 else 'no' for x in range(0,10)]
print(entries)

entries = ('yes' for x in range(0,3) if x%2==0)
print(entries)
print(next(entries))
print(next(entries))
entries = {'yes' for x in range(0,3) if x%2==0}
print(entries)
user = {'a':'b', 'c':'d'}
entries = {x:y for x,y in user.items()}
print(entries)

try:
    v = ""
    # with open('README.md','w') as file:
    #     file.write("Hellow world \n")
    with open('README.md','a') as file:
        file.write("Hellow world \n")
    with open('README.md','r') as file:
        v = file.read()
        print(v)
        print(str(v))
except (KeyError, ValueError) as e:
    print('first', e)
except Exception as e:
    print('second',e)
else:
    print('third')
finally:
    print('fourth')

'''custom exception class'''

class NetworkException(Exception):
    def __init__(self, message=None, debug=None):
        super().__init__(self, message)
        self.message = message
        self.debug = debug

try:
    raise ('some problem in network')
except (NetworkException) as e:
    print(e.__class__)
    print(e)



from threading import Thread
from multiprocessing import Process, Queue
import time


queue = Queue()

def fun1(q):
    for i in range(0,5):
        t1 = time.time()
        try:
            value = q.get(timeout=5)  # Get value with timeout
            print('Waiting finished for fun1 after', (time.time()-t1), value)
        except Exception as e:
            print("Queue is empty, fun1 timeout!")
        time.sleep(1)
def fun2(q):
    for i in range(0,5):
        time.sleep(1.5)
        q.put('fun2')  # Fix: Use put() instead of add()
        print('Value added by fun2')



# t1 = Thread(target = fun1, args=(2,), daemon=True,name='t1')
# t2 = Thread(target = fun2, args=(2,), daemon=True,name='t2')


# if __name__ == '__main__':
#     t1 = Process(target = fun1, args=(queue,), daemon=True,name='t1')
#     t2 = Process(target = fun2, args=(queue,), daemon=True,name='t2')
#
#     t1.start()
#     t2.start()
#
#     t1.join()
#     t2.join()


''' acyncio --> corotunes , best for networking, db calls, socket programming .. better than
threading, just stop the thread. dont hold the thread just wait the current process to complete
meanwhile other functions or courutines can work 
'''

import asyncio
import aiohttp

cntt = 0

async def fun1():
    print('function-1 started')
    global cntt
    await asyncio.sleep(2)
    print('function-1 finished', cntt)
    cntt = cntt + 1

async def fun2():
    print('function-2 started')
    global cntt
    await asyncio.sleep(2)
    print('function-2 finished', cntt)
    cntt = cntt + 1


async def http_caller(session, url):
    async with session.get(url) as response:
        res = await response.json()
        res = 'get the result'
        return res



async def main1():
    # li = [fun1(), fun2()]
    async with aiohttp.ClientSession() as session:
        tasks = [http_caller(session, 'https://jsonplaceholder.typicode.com/posts') for _ in range(0,4)]
        tasks = await asyncio.gather(*tasks)
        print(tasks)

    # await asyncio.gather(*li)
    # print('before finally!!')

asyncio.run(main1())
print('finaly!!')


'''Flask basics'''

from flask import Flask, jsonify, request

app = Flask(__name__)

li = []

@app.route('/home/*', methods=["GET"])
def task1():
    target = "ok"
    value = [{"yagnesh": li}, {"target":target}]
    return jsonify(value),200

@app.route('/homes/<job_id>', methods=["POST"])
def task2(job_id):
    global li
    li.append(job_id)

    re = request.get_json()
    li.append(re)
    print(re)

    re = request.args.to_dict()
    print(re)
    li.append(re)

    value = {"yagnesh": "sucess", "target":"ok"}
    return jsonify(value)


async def call_test_endpoint():
    url = "http://127.0.0.1:5010/home/*"  # Flask server URL
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as response:
                response.raise_for_status()  # Raise an error for HTTP 4xx/5xx
                return await response.json()  # Return JSON response
        except aiohttp.ClientError as e:
            return {"error": str(e)}  # Handle exceptions

# Run the async function
async def main():
    result = await call_test_endpoint()
    print(result)


if __name__ == '__main__':
    app.run("0.0.0.0", 5010,debug=True)
    Thread(target=main)




















'''
__new__() 
__call__
middleware--> setting.py
'''

'''

databases, sql, locking, authentications, rate limiter, api, caching, db optimization, seriazliation & deser
security, 



Django:

middlewares

caches

triggers orm

database optimization: db_index, caching, --> lazy query, foreign key ka data nahi ata, , bulk update, centry to 
perform query analytics also debug_toolbar

select_related: used to optimize query in case of when we want attribute realted to foreign key
prefetch_related: ''  used when we need attribute which have manytomany or manytoone relationship with other model


authenticationa and authorization: BasePermission--> make class using this and
 then use similar --> permission_classes = [IsAuthenticated, IsAdminUserOnly]


class BurstRateThrottle(BaseThrottle):

Serializers convert Django model instances to JSON (and vice versa). They act as the bridge between the database and API responses.


celery: background task queue
celery beats: to set up periodic chrone job, or at partcular time


django prevent sql query injection: parameterized query, or basic orm, Q sanitize the input query

cross site request frogery: prevent django by maintaing sessions and sql
django middlewares, etc


exception handeling: middleware
loggingz: logger module
'''





































