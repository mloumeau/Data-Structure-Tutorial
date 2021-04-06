# Big O Notation

The concept of big O notation is used to measure how long a problem will take a computer. However, we don't measure things in seconds, like one may intuitively think. We measure how many steps it will take the computer to finish a program.

"Measuring how many steps it will take to run a program?! That number must be **huge!!**"

Before you get overwhelmed, it's easier than you might think! We can generalize these numbers using the variable *n*.

## O(1)
Perhaps looking at an example will help clear this up a bit.


```python
testNumber = 10
if testNumber == 5:
    print("It's a match!")
else:
    print('testNumber and conditional are different!')
```

In this example, we have 4 steps.

* Declare the variable testNumber
* Check to see if testNumber is 5
    * If it is, then display that it is. 
* Reach the else statement (exit if conditional was True)
    * If not a match, let the user know (exit if conditional was False).

When testing for big O notation, we always assume the worst case scenario. In this case we would use the 4. For the time being, we can call this program O(4).


## O(n)
Things change once we incorporate loops. For example:

```python
def myFunction(n):
    for i in range(len(n)):
        print(i)
```

In this example function, we see that we are looping for *n* iterations. Since we can't give a concrete number for this, we say that this is O(n).


Here's another example:

```python
def anotherFunction(n):
    for i in range(len(n)):
        if i % 2 == 0:
            print(i)
```

So now we have the same example as before, but we have an if statement inside our loop. Logically speaking, we are going to have to add another step for each time we enter the loop, which will be *n* times. One would think that the big O notation would then just be doubled, right? O(2n).

This is where things simplify because computers are so fast. In big O notation, anytime we have a coefficient in front of our *n*, we can remove it altogether. This is because the factor of *n* will be taking up the mass bulk of the steps, so a few if-statements are deemed negligible to a computer.

The actual big O notation for `anotherFunction ` would be O(n)

## O(1) -- Continued

But wait! What does this mean for our first example of testing if our number met the conditional?

```python
testNumber = 10
if testNumber == 5:
    print("It's a match!")
else:
    print('testNumber and conditional are different!')
```

As we can see in this example, there is no variable n to change the complexity of the computation. It will always be set number of steps to perform. This means there is no *n* in this example. When there is no *n*, the complexity results to O(1).

Mathematically, the concept of dropping the coefficient holds true in this case if we manipulate the numbers a bit. Originally, we put O(4) for this scenario. If we change 4 to be 4 * 1, or 4(1), we can then drop the coefficient 4 and be left with the result of O(1).

## O(n<sup>2</sup>)

Another example would be:
```python
def nestedLoops(n):
    for i in range(len(n)):
        for j in range(len(n)):
            print(i,j)
```

In this exercise, we have a loop within a loop. For however big *n* is, it will need to be done another *n* times due to the nested for loops. *n* * *n* = *n<sup>2</sup>*. This means it is O(n<sup>2</sup>).

As one could imagine, we would like our algorithms to be as fast as possible. We try to avoid O(n<sup>2</sup>) and especially the dreaded O(2<sup>n</sup>).

## O(log(n))

One of the most optimal situations we can have is if the complexity of our algorithm is O(log(n)). This would essentially be the inverse of O(2<sup>n</sup>).
Perhaps the easiest way to understand this one would be with a binary search algorithm.

```python
def binarySearch(myArray, x):
    
    low = 0
    high = len(myArray) - 1 # -1 because we are dealing with 0-based indexing
    mid = 0
 
    while low <= high:
        #To get the middle, take the low + high, divide by 2 and take the floor.
        mid = (high + low) // 2
        #If the number we're looking for is larger than our middle index
        if myArray[mid] < x:
            #Our new lower bound is set to one more than mid
            low = mid + 1
        
        #If the number we're looking for is smaller than our middle index
        elif myArray[mid] > x:
            #Our new upper bound is set to one more than mid
            high = mid - 1
        else:
            #This is called only if the mid equals the number we're looking for
            return mid
    #The only way we get to here is if something wrong happened.
    return -1
```

One *very* important thing to note about this binary search algorithm is that our array we pass in *must* be sorted. If the array is not sorted, this efficient algorithm will not work.

This may make more sense if we walk through the concept. If we give ourself a sorted example array of `[0, 1, 2, 3 ,4, 5, 6, 7, 8, 9]` and we want to find the number 7, we will do the following:

* low = 0, high = len(array) - 1 --which equals 9, and mid = 0
* mid = 0 + 9 // 2  --which equals 4
* Since 4 is less than 7, low = mid + 1 --which equals 5
* mid = 5 + 9 // 2 --which equals 7
* Since 7 = 7, we return that the number we are looking for is in index 7.

What would normally take 8 steps to find the 7th index only took 2 with this method of binary search. We can see that is much more efficient than something such as nested for loops. To get a complexity of O(log(n)) will almost always be the goal.

The rest of the tutorial will be talking about the big O notation for the data structures included.