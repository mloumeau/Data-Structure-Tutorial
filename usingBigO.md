# Big O Notation

The concept of big O notation is used to measure how long a problem will take a computer. However, we don't measure things in seconds, like one may intuitively think. We measure how many steps it will take the computer to finish a program.

"Measuring how many steps it will take to run a program?! That number must be **huge!!**"

Before you get overwhelmed, it's easier than you might think! We can generalize these numbers using the variable *n*.

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

One last example for the sake of this brief explanation:

```python
def nestedLoops(n):
    for i in range(len(n)):
        for j in range(len(n)):
            print(i,j)
```

In this exercise, we have a loop within a loop. For however big *n* is, it will need to be done another *n* times due to the nested for loops. *n* * *n* = *n<sup>2</sup>*. This means it is O(n<sup>2</sup>).

As one could imagine, we would like our algorithms to be as fast as possible. We try to avoid O(n<sup>2</sup>) and especially the dreaded O(2<sup>n</sup>).

Thethe tutorial will be talking about the big O notation for the data structures included.