#Question1 
class Node:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def insert(self, data):

        if data < self.data:
            if self.leftChild:
                
                self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
                return
        else:
            if self.rightChild:

                self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                return

    def PrintTree(self):
        if self.leftChild:
            self.leftChild.PrintTree()
        print( self.data),
        if self.rightChild:
            self.rightChild.PrintTree()

root = Node(27)
root.insert(14)
root.insert(35)
root.insert(31)
root.insert(10)
root.insert(19)
root.PrintTree()


#Question2


class Node:
 
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
 
def maxDepth(node):
    if node is None:
        return 0
 
    else:
 
        lDepth = maxDepth(node.left)
        rDepth = maxDepth(node.right)
 
        if (lDepth > rDepth):
            return lDepth+1
        else:
            return rDepth+1

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
 
 
print("Height of tree is %d" % (maxDepth(root)))


#Question3

class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key


def printInorder(root):

	if root:

		printInorder(root.left)

		print(root.val),

		printInorder(root.right)
  
def printPreorder(root):
     
    if root:
 
        print(root.val),
 
        printPreorder(root.left)
 
        printPreorder(root.right)
        
def printPostorder(root):
    if root:
 
        printPostorder(root.left)
 
        printPostorder(root.right)
 
        print(root.val),


if __name__ == "__main__":
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        print("\nInorder traversal of binary tree is")
        printInorder(root)
        print("\nPreorder traversal of binary tree is")
        printPreorder(root)
        print("\nPostorder traversal of binary tree is")
        printPostorder(root)


#Question4

class Node:

	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

def printLeafNodes(root: Node) -> None:

	if (not root):
		return

	
	if (not root.left and
		not root.right):
		print(root.data,
			end = " ")
		return

	
	if root.left:
		printLeafNodes(root.left)


	if root.right:
		printLeafNodes(root.right)

if __name__ == "__main__":

	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.right.left = Node(5)
	root.right.right = Node(6)
	

	printLeafNodes(root)


#Question5

class Node:
    def __init__(self, val: int):
        self.left = None
        self.right = None
        self.val = val

def bfs(root):
    if root is None:
        return

    queue = []
 
    queue.append(root)
 
    while(len(queue) > 0):
 
        print(queue[0].val, end = " ")
        node = queue.pop(0)

        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)

def dfs_in_order(root=None):
    if root:
        dfs_in_order(root.left)
        print(root.val,end=' ')
        dfs_in_order(root.right)


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    print("Following is BFS")
    bfs(root)
    print("\nFollowing is DFS from")
    dfs_in_order(root)


#Question 6

class Node:
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None

def isLeaf(node):
	if node is None:
		return False
	if node.left is None and node.right is None:
		return True
	return False

def leftLeavesSum(root):
	res = 0

	if root is not None:
		if isLeaf(root.left):
			res += root.left.key
		else:
			res += leftLeavesSum(root.left)

		res += leftLeavesSum(root.right)
	return res

root = Node(20)
root.left = Node(9)
root.right = Node(49)
root.right.left = Node(23)	
root.right.right = Node(52)
root.left.left = Node(5)
root.left.right = Node(12)
print ("Sum of left leaves is", leftLeavesSum(root))


#Question 7

class Node:  
    def __init__(self,data):  
        self.data = data
        self.left = None
        self.right = None
   
class SumOfNodes:  
    def __init__(self):  
        self.root = None
      
    def calculateSum(self, temp):  
        sum = sumRight = sumLeft = 0
          
        if(self.root == None):  
            print("Tree is empty")
            return 0
        else:  
            if(temp.left != None):  
                sumLeft = self.calculateSum(temp.left)
              
            if(temp.right != None):  
                sumRight = self.calculateSum(temp.right)
              
            sum = temp.data + sumLeft + sumRight
        return sum

bt = SumOfNodes()
bt.root = Node(5)
bt.root.left = Node(10)
bt.root.right = Node(15)
bt.root.right.right = Node(1)
bt.root.right.left = Node(2)
bt.root.left.left = Node(3)
bt.root.left.right = Node(4)

print("Sum of all nodes of binary tree: ",bt.calculateSum(bt.root))


#Question 8

class getNode:
	def __init__(self, data):

		self.data = data
		self.left = self.right = None


def countSubtreesWithSumX(root, count, x):

	if (not root):
		return 0
	ls = countSubtreesWithSumX(root.left,
							count, x)

	rs = countSubtreesWithSumX(root.right,
							count, x)

	Sum = ls + rs + root.data
	if (Sum == x):
		count[0] += 1
	return Sum

def countSubtreesWithSumXUtil(root, x):

	if (not root):
		return 0

	count = [0]
	ls = countSubtreesWithSumX(root.left,
							count, x)

	rs = countSubtreesWithSumX(root.right,
							count, x)

	if ((ls + rs + root.data) == x):
		count[0] += 1
	return count[0]


if __name__ == '__main__':
	root = getNode(5)
	root.left = getNode(-10)
	root.right = getNode(3)
	root.left.left = getNode(9)
	root.left.right = getNode(8)
	root.right.left = getNode(-4)
	root.right.right = getNode(7)
	x = 7
	print("Count =",countSubtreesWithSumXUtil(root, x))


#Question 9

from collections import deque

class Node:
	
	def __init__(self, key):
		
		self.data = key
		self.left = None
		self.right = None

def maxLevelSum(root):
	if (root == None):
		return 0
	result = root.data
	q = deque()
	q.append(root)
	
	while (len(q) > 0):
		count = len(q)

		sum = 0
		while (count > 0):
			temp = q.popleft()
			sum = sum + temp.data
			if (temp.left != None):
				q.append(temp.left)
			if (temp.right != None):
				q.append(temp.right)	
			count -= 1
		result = max(sum, result)

        return result
	
if __name__ == '__main__':
	
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(5)
	root.right.right = Node(8)
	root.right.right.left = Node(6)
	root.right.right.right = Node(7)
	print("Maximum level sum is", maxLevelSum(root))		


#Question 10

class newNode:
	def __init__(self, data):
		self.data = data
		self.left = self.right = None

def printOddNodes(root, isOdd = True):
	
	if (root == None):
		return

	if (isOdd):
		print(root.data, end = " ")

	printOddNodes(root.left, not isOdd)
	printOddNodes(root.right, not isOdd)

if __name__ == '__main__':
	root = newNode(1)
	root.left = newNode(2)
	root.right = newNode(3)
	root.left.left = newNode(4)
	root.left.right = newNode(5)
	root.right.left = newNode(6)
	root.right.right = newNode(7)
	printOddNodes(root)        
