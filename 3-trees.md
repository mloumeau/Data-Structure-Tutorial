# Trees

# Description
Trees are arguably the most valuable data structure since we can convert certain problems into a complexity of O(log(n)). If we are able to sort our array and create a binary search tree, our program will be able to run much quicker.

## So What is a Binary Search Tree?

A binary search tree is a bunch of nodes that connect to each other in a (typically) downward fashion.

![Binary Search Tree](Binary_search_tree.png)

Every tree starts off with a root. In the case of this picture example, we see that 8 is our root. The '8' node connects to the '3' node and the '10' node. In this regard, 8 is the parent node, and 3 and 10 are the child nodes. **For each parent node, up to two children nodes are permitted in a binary search tree.**  We can now view 3 as a parent node with the two children of 1 and 6. This process continues on until we reach the bottom nodes with no children, which are also called leaf nodes.

## Walking Through the BST

An explanation of a binary search algorithm can be found at the bottom of:
[Using Big O](https://github.com/mloumeau/Data-Structure-Tutorial/blob/master/usingBigO.md)

We can see that our original sorted array is `[1, 3, 4, 6, 7, 8, 10, 13, 14]` by looking at the picture example. If we were to use a normal iterative search algorithm to look for 14 for example, it would require searching through every value inside the array until it reaches 14. Since 14 is the last element inside the array, it would require looking through every element of the list giving it a complexity of O(n).

This is where the beauty of binary search trees may start to come through. If we wanted to look for 14 inside of our BST picture, it would only take 3 steps. It would check for 8 -> 10 -> 14. Much quicker! The incredible thing about this data structure is that it is more efficient as the data gets bigger.

Another way of looking at O(log(n)) is by saying "2 to the ? power would give me n?". For example, if our array had 8 elements in it, then we could easily see that 2 to the 3rd power would give us our n.

This means that with an array of 8 elements, the longest it will take to find a desired number will be a path of 3 nodes.

But what happens when our n isn't a perfect power of 2? Simple. If there is a decimal to our exponent, then we round up to the nearest integer. For example, our BST picture has a length of 9 elements. We know that 2<sup>3</sup> = 8 and 2<sup>4</sup> = 16. The actual answer for log<sub>2</sub>(n) would be ~3.1 or thereabouts. This means that we round our answer up to 4, and we now know that the longest possible path to find our answer will be a path of 4 nodes. As we can see in our example, 4 is indeed the longest length of any path in the tree.

## Bigger Numbers

As stated above, this becomes very powerful when the numbers become very large. The larger the length of the array, the more useful a BST will be. Let's take a medium sized number such as 4,000. If we have a sorted array of 1 - 4,000 and the number we are looking for is the last element in the array (4,000), then it will take 4,000 steps to do so with a traditional searching algorithm. If we can sort our array and create a binary search tree, our answer will reduce to the ceiling of log<sub>2</sub>(4,000). If we list the powers of 2 we get:
* 2<sup>1</sup> = 2
* 2<sup>2</sup> = 4
* 2<sup>3</sup> = 8
* 2<sup>4</sup> = 16
* 2<sup>5</sup> = 32
* 2<sup>6</sup> = 64
* 2<sup>7</sup> = 128
* 2<sup>8</sup> = 256
* 2<sup>9</sup> = 512
* 2<sup>10</sup> = 1,024
* 2<sup>11</sup> = 2,048
* 2<sup>12</sup> = 4,096

Our number falls between 11 and 12. We can round up to 12, and know that 12 will be our maximum number of steps for a list of 4,000 elements! How much more efficient!

Now imagine this with an array of 1,000,000,000,000 elements! Much better!


## Navigating Through BSTs

Since we don't have a great way of knowing when to stop our loop, for loops are not the best for traversing through a tree. A while loop could work, but there is an even better method that is most commonly used when navigating through a binary search tree. That method is known as recursion.

## Recursion

Being that we are Python programmers, it is all but guaranteed that we have used loops to iterate through different scenarios. What may not be known as widely is the concept of recursion.

Recursion is the process of having a function call itself over and over again. This may sound like a recipe for an infinite loop, and you might be right! It is absolutely imperative that a recursive function has a base case.

What is a base case? Perhaps a coding example might make things easier to see.

```python
def recursiveFunction(num):
    #This is the base case
    if num < 1:
        #If the number is 0 or less, exit the recursive loop
        return
    print(num)
    recursiveFunction(num-1)
```

This function prints the positive number inputted by the user and all of the preceeding numbers before it until it reaches 0. (Better keep that number small!).  

For example, if we passed in 5, it would print out 5, 4, 3, 2, 1.

If we passed in -4, it would return without doing anything.

The base case is equivalent to a parameter for a loop.

`while x < 5`

or

`for x in range(12)`.

We need to have a scenario where the loop is told to break out. In the case of our example above, we exit out of the loop when we see anything less than 1. This includes 0, as well as all negative numbers.


## Understanding BSTs with Code

To better understand how recursion fits in with binary search trees, we can examine the following code:

```python
class BST:
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None
```

While this may look confusing on the surface, it is simply a class within a class. The outer class is named BST, and has a constructor of one variable named root. The inside class is called Node and its constructor contains three variables -- data, left, and right.  Data means what number the node represents, left means its left child, and right means its right child.

To create a new Node, we would need to do something like:

```python
tree = BST
tree.root = BST.Node(5)
tree.root.left = BST.Node(3)
tree.root.right = BST.Node(7)
```

From here, we can use recursion to insert a node. We split the process into two functions. The first is to initialize the root of a tree if there is not one already. From there, we call the recursive function that proceeds to call itself until a proper location for the node has been achieved.

```python
def insert(tree, nodeToInsert):
    if tree.root is None:
        tree.root = BST.Node(nodeToInsert)
    else:
        insertRecursive(nodeToInsert, tree.root)

def insertRecursive(data, node):
    if data == node.data:
        return
    if data < node.data:
        if node.left is None:
            node.left = BST.Node(data)
        else:
            insertRecursive(data, node.left)
    else:
        if node.right is None:
            node.right = BST.Node(data)
        else:
            insertRecursive(data, node.right)
```

Notice how the base case for this is to see if the node we want to insert is already found within the tree. If it is, return without doing anything. Otherwise, the function will constantly check for the left and right positions until the proper location is found. Once the location is found, the else statement which triggers the recursion will never be activated, meaning the function will come to a halt, with a new node inserted in its proper location.

## Coding challenge

Here is an ASCII form of the BST demonstrated in the image above.

                  8
               /    \
              /      \
             /        \
            /          \
           3            10
          / \            \
         /   \            \
        1      6          14
              / \         /
             /   \       /
            4     7    13

Create a Node class and use it to create this tree.

Once the tree has been crafted, create a function that will print out numbers in order. Remember, this BST was properly initiated with a sorted list. The answer we get back should be sorted as well.

### Hint

Remember to use recursion. It may be easy to overthink this.

## Solution

[Coding Solution](https://github.com/mloumeau/Data-Structure-Tutorial/blob/master/pythonFiles/treeSolution.py)