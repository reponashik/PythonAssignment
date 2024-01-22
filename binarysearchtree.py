'''
Activity 2
Binary search tree (BST)
context:  
for any parent node, its data value must be higher than the 
data from any child node to its left, and lower
than the data of any child node to its right. 

'''
#setting optional limit in size to 101
LIMIT = 101 

#2.1 Start 

#class TreeNode
#defining constructor class
#defining left, right and current values of the node of the tree as attributes
class TreeNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val
        
#class BinarySearchTree
class BinarySearchTree:
    #firstly, root of the tree is set to none
    root = None
    #the limit is 101, the constant definition is at the top of the program
    #limit can be easily changed for testing purposes
    limit = LIMIT
    #initially set to 0 nodes - empty tree
    curr_nodes = 0

    #method to check if tree is empty, if root is null, then tree = empty
    #returns a boolean
    def is_empty(self):
        if(self.root is None):
            return True
        else:
            return False
    
    #method to check if tree is full, comparing current nodes to limt size
    #returns a boolean
    def is_full(self):
        if(self.curr_nodes == self.limit):
            return True
        else:
            return False

    #method to insert a node in the tree
    #in case root is null, then assign new value to root 
    #othwerwise call function helper_insert(): defined in upcoming sections
    #update the current nodes value
    #there is also a check being executed on whether the tree is full
    def insert(self, val):
        if(self.root == None):
            self.root = TreeNode(val)
            self.curr_nodes += 1
            return
        if(self.curr_nodes == self.limit):
            print("Cannot insert. Tree is full.")
            return
        temp = helper_insert(self.root, val)
        self.curr_nodes += 1
        
    #search method
    #calls helper_search: defined in upcoming sections
    #checks on whether the node is present in the tree
    def search(self, val):
        node = helper_search(self.root, val)
        if node is None:
            # print(f"Key {val} is NOT present in tree")
            return False
        else:
            # print(f"Key {val} is present in tree")
            return True

    #method to delete a node from the tree
    #calls helper_delete: defined in upcoming section
    #using templating to access the object the user wishes to delete in a print statement
    def delete(self, val):
        node = helper_delete(self.root, val)
        if node is not None:
            print(f"Key {val} is deleted from tree")
        else:
            print(f"Key {val} is NOT present in tree. Thus no deletion took place.")
        self.curr_nodes -= 1

    #transverse method
    #calling helper_inorder() : defined in the upcoming section
    def traverse(self):
        helper_inorder(self.root)
    
    #function to print the tree
    #calling helper_printTree() : defined in the upcoming section
    def print_tree(self):
        print("The tree can be visualized as: ")
        helper_printTree(self.root, 0)

#------------------------------------------------------------------------------------------------------

#helper functions for the tree functionalities

#function called in search()
def helper_search(node,val):
    #if the node being searched is equal to the target value, return node
    if node is None or node.val == val:
        return node
    if node.val < val:
    #if the node being searched value is less than target value (val)
    #recursively call this function again with node.right as argument
        return helper_search(node.right,val)
    else:
        #if the node being searched is more than target value (val)
        #recursively call this function again with node.left as argument
        return helper_search(node.left,val)

#function called in insert()
def helper_insert(node, val):
    if node is None:
        return TreeNode(val)
    else:
        if node.val == val:
            return node
        elif node.val < val:
            node.right = helper_insert(node.right, val)
        else:
            node.left = helper_insert(node.left, val)
    return node

#function useful in the delete helper function 
#assigns smaller value to the left of a node if smaller
def minValueNode(node):
    current = node
    while(current.left is not None):
        current = current.left
    return current

#function in delete() 
#function maintains tree integrity

def helper_delete(node, val):
    if node is None:
        return node
    #recursively recall function if val to be deleted is smaller than node value
    #with node.left value as argument
    if val < node.val:
        node.left = helper_delete(node.left, val)
    #recursively recall function if val to be deleted is bigger than node value
    #with node.right value as argument
    elif(val > node.val):
        node.right = helper_delete(node.right, val)
    #effectively, this is the section to fix the tree integrity
    #to do this, I use a value called temp
    #temp momentarily copies the next bigger or smaller value
    #to then take the place that was previously occupied by the 
    #deleted node in question
    else:
        if node.left is None:
            temp = node.right
            node = None
            return temp
        elif node.right is None:
            temp = node.left
            node = None
            return temp
        #this is where temp is assigned the appropriate value
        temp = minValueNode(node.right)
        #assigning node value to temp value
        node.val = temp.val
        node.right = helper_delete(node.right, temp.val)
    return node

#recursively call the function to print the root each time in order from
#left to right 
def helper_inorder(root):
    if root:
        helper_inorder(root.left)
        print(root.val)
        helper_inorder(root.right)

#vertically print root values based on tree order level
def helper_printTree(root, space = 0): 
    if (root == None) :
        return
    space += 10
    helper_printTree(root.right, space)
    print()
    for i in range(10, space):
        print(end = " ")
    print(root.val)
    helper_printTree(root.left, space)
    
#---------------------------------------------------------------------------------

#testing

#tree = BinarySearchTree()
#tree.insert(7)
#tree.insert(3)
#tree.insert(2)
#tree.insert(10)
#tree.insert(5)
#tree.insert(11)
#tree.delete(10)
#tree.search(5)
#tree.search(10)
#tree.print_tree()
