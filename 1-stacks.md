# Stacks

# Description

Stacks are one of the most primitive data structures out there. That being said, they are quite inexpensive and are used quite frequently. Since we are Python programmers, stacks may not be as well known. In other coding languages, take C# for example, a stack can be a data type just like int or string.

So what is a stack? Well, it's quite simple. A stack is an array (or a list in python) that can only add an element to the end.

```python
myStack = [0, 1, 2]
myStack.append(3)
```

In our example above, we have an array of `[0, 1, 2]`. We then added 3 to the end `[0, 1, 2, 3]`, which is legal for a stack. If the 3 was added anywhere else, such as `[0, 3, 1, 2]` or `[3, 0, 1, 2]`, this would no longer be a stack. 

Simple, right? Well there's one more caveat. We can only grab the last element out of the stack as well! To perform this action, we can use the pop method built into python.

```python
myStack = [0, 1, 2, 3]
myStack.pop()
```

This pop feature removes (and returns) the last element of an array, list, or stack. After performing the pop method, myStack would now look like this.

```python
myStack = [0, 1, 2]
```

To clarify what it means to not only remove but actually return a value from the pop method, we can see that printing out the results will display the (former) last element of the list.

```python
myStack = [0, 1, 2]
popResults = myStack.pop()
print(myStack)
print(popResults)
```

# Big O Notation

Since stacks are so simple, they have great performance. Because the only element that is being used is the last one, we only need to access the end of the stack. To add to the end of stack (myStack.append()), it is complexity O(1). Likewise, to access the back of the stack (myStack.pop()), it is also complexity O(1).

# Coding Challenge

Given a test case of different styles of brackets - (), [], {} - write a program using a stack to determine whether the given input is a valid set of brackets.

Valid:
* `({[]})`
* `([](){})`

Invalid:
* `{[(]`
* `([)]`

## Test Cases
* "`()`"
Valid
* "`()[]{}`"
Valid
* "`(]`"
Invalid
* "`([)]`"
Invalid
* "`{[]}`"
Valid

## Solution

[Coding Solution](https://github.com/mloumeau/Data-Structure-Tutorial/blob/master/pythonFiles/stackSolution.py)