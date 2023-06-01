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