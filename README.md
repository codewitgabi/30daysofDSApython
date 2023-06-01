# Project Description
**30 days of DSA-python** covers some very important concepts in Data Structures and Algorithms. Begin your journey of *DSA* today to understand how to get things done with it.

## Arrays
Array is a container which can hold a fixed number of items and these items should be of the same type.

** Important Terms **
* Element: Each item stored in an Array
* Index: Each location of an element in an array has a numerical value used to identify the element.

Array is created in python by importing array module and declared as shown below

```
from array import *
arr = array(typecode, [initializers])
```

Some of the available typecodes are as follows;
* b: Represents signed integer of size 1 byte
* B: Represents unsigned integer of size 1 byte
* c: Represents character of size 1 byte
* i: Represents signed integer of size 2 bytes
* I: Represents unsigned of size 2 bytes
* f: Represents floating point of size 4 bytes
* d: Represents floating point of size 8 bytes

### Accessing Array Elements
We can access each element of an array using the index of that element

### Insertion Operation
Insertion operation is to insert one or more data elements into an array. Based on the requirement, a new element can be added at the beginning, end or any given index of array.

```
from array import array

arr = array("i", [5, 10, 15, 20])
arr.insert(12, 0)

print(arr) # 12, 5, 10, 15, 20
```

### Deletion Operation
Deletion refers to removing an existing element from an array and reorganizing all elements from an array.

```
from array import array

arr = array("i", [5, 10, 15, 20])
arr.remove(10)
del arr[2]

for elem in arr:
    print(elem)

# output -> 5, 15
```

### Search Operation
You can perform a search for an array element based on its value or index.

```
from array import array

arr = array("i", [5, 10, 15, 20])

print(10 in arr) # True
print(arr.index(15)) # 2
```

### Update Operation
Elements in an array can be modified after creation.

```
from array import array

arr = array("i", [2, 4, 6, 8, 10])

arr[3] = 0

for elem in arr:
    print(elem)
  
# output -> 2, 4, 6, 0, 10
```

## Lists
The list is most versatile data type available in Python, which can be written as a list of comma-separated values between square brackets. The most important thing about a list is that elements need not be of the same datatype.

```
# example
list1 = ["Physics", "Chemistry", "Maths"]
list2 = [1, 2, 3, "a", "b"]
```

Similar to string indices, list indices start from 0 and can be sliced, concatenated and so on.

### Accessing Values
To access elements in a list, use the square bracket for slicing and the index or indices to obtain value available at that index.

```
list1 = [1, 2, 3, 4, 5]

print(list1[3]) # 4
print(list1[-1]) # 5
print(list1[:3]) # [1, 2, 3]
```

### Updating List Elements
You can update single or multiple elements of list by giving the slice on the left hand side of the assignment operator and you can add to the list using the .append() method.

```
list1 = [1, 2, "a", { "a": 3 }, 4]

list1[1] = 10
list1[-1] = 3
list1.append(6)

print(list1) # [1, 10, "a", { "a": 3 }, 3, 6]
```

### Deleting List Elements
To remove an element from a list, you can use the `del` keyword or .remove() method.

```
list1 = [1, 2, "a", { "a": 3 }, 4]

del list1[-2]
list1.remove(2)

print(list1) # [1, "a", 4]
```

### Basic List Operations
```
print(len("a", "b", 3)) # 3
print([1, 2, 3] + [4, 5, 6]) # [1, 2, 3, 4, 5, 6]
print(["a"] * 5) # ["a", "a", "a", "a", "a"]
print(5 in [3, 5, 8]) # True
for i in [1, 2, 3]: print(i) # 1, 2, 3
```