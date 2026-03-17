# INTRODUCTION

All basic python resources/functionalities that you need for resolve technical interview problems.

## Variables
- Dynamically typed -> you don't need to declare the type, the type is determined at runtime.

```python
n = 0
print('n = ',n)
n = 'adc'
print('n = ',n)
```

#### Multiple assignments
- You can create variable in one line passing different types of data
```python
a, b, c = 1, 'adc', False
```

#### Increment
```python
n = n + 1
n += 1
```
- ps: In python doesn't exist n++

#### Null Values
- Null values are assigned as **None**

## IF statements

```python
n = 1
if n > 2:
    n -= 1
elif n == 2:
    n += 1
else:
    n *= 2
```

## Logic Operator
- return true or false in statements
- parentheses need for multi-line conditions
- and = &&
- or = ||
- not = !
```python
n=1
m=2
if ((n>2 and n!= m) or n==m):
    n += 1
```

## While loops
```python
n = 0
while n<10:
    n+=1
```

- While with conditions on data structures
```python
from collections import deque
queue = deque([1, 2, 3])
while queue and queue[0] < 3:
    queue.popleft()
```

## Looping with for
- **i** is incremented by default, start in 0 and end in **n-1**
- use first and second param to make a range
- use third param to decrement or set the amount to decrement/increment
```python
n = 5
for i in range(n):
    print(i) # 0 - 1 - 2 - 3 - 4
```
- starting with some value
```python
n = 2
m = 6
for i in range(n, m):
    print(i) # 2 - 3 - 4 - 5
```
- decrementing
```python
n = 2
m = 6
for i in range(m, n, -1):
    print(i) # 6 - 5 - 4 - 3
```

## Basic operations
#### Multiply
    n*m
#### Division
- Is decimal by default
```5/2 = 2.5```
- Double slash rounds down
```5//2 = 2```
- Negative numbers will round down
```-3//2 = -2```
- To rounding towards zero
```int(-3/2) = -1```
#### Moding
- Same problem with negative numbers
```
10%3 = 1
-10%3 = 2
```

#### Math import
Very useful to math operations. Python native.

```python
import math

math.floor(3/2) # round down = 1
math.ceil(3/2) # round up = 2
math.sqrt(2) # raiz quadrada
math.pow(2, 3) # potencia = 8 also use 2**3
math.factorial(3) # factorial 1*2*3 = 6
math.gcd(12, 18) # max divisisor comum = 6
```

#### Max / Min Int
float("inf")
float("-inf")


## Data Structures
### Array
- Can be use as a stack
- Strings are also consider arrays
```python
arr = [1,2,3,4]
arr.append(5) # O(1)
arr.pop() # O(1)
arr.insert(1, 7) # O(n)
arr[1] = 3 # O(1) obs: you can't use this in strings
```
- Array of size
```python
n = 5
arr = [1] * n
```

- Reverse index
```python
arr = [1,2,3]
print(arr[-1])
```

- Slicing
```python
arr = [1,2,3,4]
print(arr[1:3]) # [2,3]
print(arr[:]) # [1,2,3,4]
print(arr[1:]) # [2,3,4]
print(arr[:-1]) # [1,2,3]
# also used to invert list
print(arr[::-1]) # [4,3,2,1]
```

- Reverse
```python
arr = [1,2,3,4]
arr.reverse() # 4, 3, 2, 1
```

- Sorting
```python
arr = [1,3,4,2]
#ascend order
arr.sort() # 1, 2, 3, 4
#descend order
arr.sort(reverse=True)
#string are sorted by alphabetic order by default
arr = ["ab", "bcd"]
arr.sort()
#use lambda functions as key to customize sort
arr.sort(key=lambda x: len(x))
```

- List Comprehension
```python
arr = [i+i for i in range(5)]
print(arr) # [0, 2, 4, 6, 8]
```
- 2-D lists
```python
arr = [[0] * 4 for i in range(4)] # create a 4x4 matrix with 0 values
```

- Combine list of Strings
```python
strings = ["ab", "cd", "ef"]
print("".join(strings)) # abcdef
```

#### Loop through arrays

```python
nums = [1,2,3]

#Using index with range and len. Access by index.
for i in range(len(nums)):
    print(nums[i])

# Without index
for n in nums:
    print(n)

# With index and value
for i, n in enumerate(nums):
    print(i, n)

# through multiple arrays simultaneously
nums1 = [1,2]
nums2 = [3,4]
for n, m in zip(nums1, nums2):
    print(n,m) # 1 3 / 2 4
```

## Queues
- Work as stacks but the benefit is that you can pop from left()

```python
from collections import deque

queue = deque()
queue.append(1)
queue.append(2) # [1, 2]
queue.popleft() # [2]
queue.appendleft(1) # [1, 2]
queue.pop() # [1]
```
- Access first element without removing
```python
queue[0] # first element
queue[-1] # last element
```

## Hashset
- Very useful because you can search and insert in constant time
- The values in set are unique
- Now also as dictionary
```python
mySet = set()
mySet.add(1) # {1}
mySet.add(2) # {1,2}
len(mySet) # 2
1 in mySet # True
mySet.remove(2) # {1}
mySet = { i for i in range(3)} # {0,1,2}
```

## HashMap (dict)
```python
myMap = {}
myMap['Ola'] = "Mundo"
len(myMap) # 1 - number of keys
"Ola" in myMap # True
myMap.pop("Ola")
myMap = {"Ola": "Mundo"}
```

- Loop through
```python
myMap = {"Ola": "Mundo"}
for key in myMap:
    print(key, myMap[key])

for val in myMap.values():
    print(val)

for key, val in myMap.items():
    print(key, val)
```

- dict.get() - returns default value if key doesn't exist (avoids KeyError)
```python
myMap = {"a": 1}
myMap["b"]           # KeyError!
myMap.get("b", 0)    # 0 (no error)
myMap.get("a", 0)    # 1
```

- dict.setdefault() - returns value if key exists, else creates it with default
```python
myMap = {}
myMap.setdefault("users", []).append("Ana")   # creates key with [] then appends
myMap.setdefault("users", []).append("Bob")   # key exists, just appends
# myMap = {"users": ["Ana", "Bob"]}
```

#### Tuples
- Can't be modified, values are unique. Can be use as key in hashmaps
```python
tup = (1,2,3)
myMap = {(1,2):3}
```

## Try / Except
- Used to handle errors without crashing the program
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

# catch any exception
try:
    risky_function()
except Exception as e:
    print(f"Error: {e}")

# bare except (bad practice, avoid)
try:
    risky_function()
except:
    pass
```

## Lambda functions
- Anonymous functions, useful as arguments for other functions
```python
# regular function
def double(x):
    return x * 2

# same as lambda
double = lambda x: x * 2

# common uses: sort, filter, map
arr = [3, 1, 2]
arr.sort(key=lambda x: x)

# as callback/handler
handlers = [lambda d: print(d), lambda d: d.update({"seen": True})]
```

## Type Hints
- Not enforced at runtime, but helps with readability and IDE support
```python
def is_allowed(client_id: str) -> bool:
    return True

def process(items: list[str], count: int = 0) -> dict:
    return {"items": items, "count": count}

# common types: str, int, float, bool, list, dict, None
# optional
from typing import Optional
def find(name: str) -> Optional[str]:
    return None
```

## Time module
- Useful for timestamps, measuring time, delays
```python
import time

time.time()      # current timestamp in seconds (float): 1710612345.123
time.sleep(1.5)  # pause execution for 1.5 seconds

# measuring elapsed time
start = time.time()
# ... some operation ...
elapsed = time.time() - start
print(f"Took {elapsed:.2f} seconds")
```

### Functions
- Recursive function can be done with inner functions
```python
def myFunc(a,b):
    def inner():
        a * b
    inner() # you don't need to pass the params, are available by default
```

- You can modify arrays but not variables
```python
def double(arr, val):
    def helper():
        nonlocal val

        for i, n in enumerate(arr):
            arr[i] = n * 2

        val *= 2

    helper()
    return arr, val

nums = [1,2]
val = 3

print(double(nums, val))
```

### Classes
```python
class MyClass:

    #constructor
    def __init__(self, nums):
        self.nums = nums
        self.size = len(nums)

    def getLength(self):
        return self.size

    def getDoubleLength(self):
        return 2 * self.getLength()
```


obs -> see heapq
