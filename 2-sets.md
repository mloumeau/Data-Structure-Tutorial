# Sets

## Description

The next data structure we will be covering is a set. Sets are very commonly used in the industry, and are extremely practical.  They are called sets in python, but are called hash maps in other languages. A set can be notated with {} as opposed to () or [].  While sets are similar to lists and arrays, they differ in a couple areas.

## No Order

In lists or arrays, we are able to access whatever element we want through the index. For example

```python
myList = (0, 1, 2)
print(myList[1])
```

In a set, there is no such thing as order. If we were to do the same thing but with a set, we could get thrown an error.

```python
mySet = {0, 1, 2}
#DON'T SUBSCRIPT A SET, IT WILL THROW AN EXCEPTION
print(mySet[1])
```

We can't subscript sets since there is no order to them. It is just a pool of elements with no order.

## No Repeats

Sets are also different from lists and arrays because they do not allow repeats.
In a list or an array, we can have something like:

```python
myArray = [0, 1, 1, 2]
print(myArray)
```

However, if we declared a set to be the same thing, it would have a different result.

```python
mySet = {0, 1, 1, 2}
print(mySet)
```

The result of myArray would be `[0, 1, 1, 2]`, as perhaps anticipated.

However, the output for mySet would be `{0, 1, 2}`. Since python is so friendly, it will automatically get rid of repeats. This can be very useful when converting a list or array into a set to find out how many unique elements are inside of the data structure.

To cast a list/array into a set, we can do:

```python
myArray = [0, 1, 1, 2]
mySet = {0, 1, 2}

myArray = set(myArray)
print(myArray == mySet)
```

To include another element for a list/array, we use

```python
myArray.append(3)
```

To include another element for a set, we use:

```python
mySet.add(3)
```

## Big O Notation

Sets/hash maps are very useful tools that eliminate a lot of overhead that would take place if having to manipulate another data structure. When implemented correctly, we can expect the adding and removing from a set to have the complexity O(1).

## Coding Challenge

Of all the numbers between 0 - 100,000,000, find all the primes. Once all the primes are discovered, find the gaps between each prime. In the end, we want to know how many *unique* gaps there are between all the primes from 0 - 100,000,000.


### Example
The first few primes are (2, 3, 5, 7, 11...). The gap between 2 and 3 is 1. The gap between 3 and 5 is 2. The gap between 5 and 7 is 2. The gap between 7 and 11 is 4.

This gives us gaps of 1, 2, 2, and 4. Since we only want the number of unique gaps, the answer for the range of 0-11 would only be 3, not 4. This is because 2 is repeated.

### Hint
```python
from pyprimesieve import primes
```
Use pip to install pyprimesieve for very fast prime calculations.

## Solution

[Coding Solution](https://github.com/mloumeau/Data-Structure-Tutorial/blob/master/pythonFiles/setSolution.py)