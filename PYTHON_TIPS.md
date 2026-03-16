# INTRODUCTION

All basic python resources/functionalities that you need for resolve technical interview problems.

## Variables
- Dynamicly typed -> you don't need to declare the type, the type is determined at runtime.

```python
n = 0
print('n = ',n)
n = 'adc'
print('n = ',n)
```

#### Multiple assigments
- You can create variable in one line passing different types of data
```python
 a,b,b = 1, 'adc', false
 ```

#### Increment
```python
n = n + 1 
n += 1
```
- ps: In python doesn`t exist n++

#### Null Values
- Null values are assigned as **None**

## IF statements

```python
n = 1
if n > 2:
    n -= 1
elif n == 2
    n += 1
else:
    n *= 2
```

## Logic Operator
- return true or false in statements
- parentheses need for multi-line conditions
and = &&
or == ||
not == !
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
## Looping with for
- **i** is incremented by default, start in 0 and end in **n-1**
- use first and second param to make a range
- use third param to decrement or set the amount to decrement/increment
```python
n = 5
for i in range(n):
    print(i) # 1 - 2 - 3 - 4
```
- starting with some value
```python
n = 2
m = 6
for i in range(n, m):
    print(i) # 2 - 3 - 4 -5
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
```3//2 = -2```
- To rounding towards zero
```int(-3/2) = -1```
#### Moding
- Same problem with negative numbers
```
10%3 = 1
-10%3 = 2
```

#### Math import
Very usefull to math operations. Python native.

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
arr[1] = 3 # O(1) obs: you can`t use this in strings
```
- Array of size
n = 5
arr = [1] * n

- Reverse index
arr = [1,2,3]
print (arr[-1])

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
arr.sort(ley=lambda x = len(x))
```

- List Comprehension
```python
arr = [i+i for i in range(5)]
print(arr) # 0, 2, 4, 8
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

# Withou index
for n in nums:
    print(n)

# With index and value
for i in n enumerate(nums):
    print (i,n)

# thrugh multiple arrays simultaneously
nums1 = [1,2]
nums2 = [3,4]
for n, m in zip(nums1, nums2)
    print(n,m) # 1 3 / 2 4
```

## Queues
- Work as stacks but the benefict is that you can pop from left()

```python
from collection import deque

queue = deque()
queue.append(1)
queue.append(2) # [1, 2]
queue.popleft() # [2]
queue.appendleft(1) # [1, 2]
queue.pop() # [1]
```

## Hashset
- Very useful because you can search and insert in constant time
- The values in set are unique
- Now also as dictionary
```python
mySet = set()
mySet.add(1) # {1}
mySet.add(2) # {1,2}
len(myset) # 2
1 in myset # True
mySet.remove(2) # {1}
mySet = { i for i in range (3)} # {0,1}
```

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
    print(key, myMap(key))

for val in myMap.values():
    print(val)

for key, val in myMap.items():
    print(key, val)
```

#### Tuples
- Cant be modify, values are unique. Can be use as key in hashmaps
```python
tup = (1,2,3)
myMap = {(1,2):3}
```

### Functions
- Recursive function can be done with inner functions
```python
def myFuc(a,b):
    def inner():
        a * b
    inner() # you dont need to pass the params, are available by default
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