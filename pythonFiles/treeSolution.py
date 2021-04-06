#Class to make the tree with
class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
 

def sortedListFromBST(node):
    if node is None:
        return
    sortedListFromBST(node.left)
    print(node.data, end=' ')
    sortedListFromBST(node.right)
 

#Make the tree
root = Node(8)
root.left = Node(3)
root.right = Node(10)
root.left.left = Node(1)
root.left.right = Node(6)
root.right.right = Node(14)
root.right.right.left = Node(13)
root.left.right.left = Node(4)
root.left.right.right = Node(7)

#Call the function with the root
sortedListFromBST(root)