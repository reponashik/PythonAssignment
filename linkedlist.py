'''
Activity 2.5 & 2.6
Linkedlist
context:  
Linkedlist, linkedlist operations and linkedlist complexity analysis

'''
#2.5 Start 

#defining optional limit in size as constant
LIMIT = 101

#class ListNote
class ListNode:
    #defining class List Node constructor class
    def __init__(self, data):
        #attributes data and link to next value defined
        self.data = data  
        self.next = None 
    #separate method part of the class to print the data in the node
    def print_node(self):
        print(self.data)
                          
#class LinkedList
class LinkedList:
    #defining attributes
    #head is the first node, and it is defined under, initially empty
    head = None
    #it is also important to have the tail of the linkedlist as an attribute, initially empty
    tail = None
    #constant defined at the top of the program
    limit = LIMIT
    #current nodes in the linkedlist initially set to 0
    curr_nodes = 0

    #method to check if linkedlist is empty 
    #if node does not contain a value, assign true
    #otherwise false
    def is_empty(self):
        if(self.node is None):
            return True
        else:
            return False
    
    #method to check if the linkedlist is full
    #compares the current nodes with the limit set
    #if equal, returns True
    def is_full(self):
        if(self.curr_nodes == self.limit):
            return True
        else:
            return False
        
    #method to print a visual representation of the list   
    def __str__(self):
        print("Visualization of LinkedList:")
        node = self.head
        #using an arrow to represent "pointer"
        while(node is not None):
            print(node.data, end = "-->")
            node = node.next


#2.5 End 

#------------------------------------------------------------------------

#2.6 Start
    
    #method to insert an element 
    #firstly, the method check if the linkedlist is full
    #if the head (first element) is empty, assign new value to head
    def insert(self, val):
        if self.is_full():
            print("Cannot insert, LinkedList Full.")
            return
        if self.head is None:
            self.head = ListNode(val)
            self.tail = self.head
            #update current nodes
            self.curr_nodes += 1
            return
        #inserting at the end 
        #allocating memory for new node
        self.tail.next = ListNode(val)
        #change next of last node to recently created node
        self.tail = self.tail.next
        #update current nodes
        self.curr_nodes += 1

    #method for searching in linkedlist
    def search(self, val):
        #making head the current node
        node = self.head
        #run a loop until current is null, meaning it points to last element
        while node is not None:
            if node.data == val:
                #in each iteration check if key = value
                # print(f"Key {val} is found in LinkedList")
                return True
            node = node.next #moving to next element
        # print(f"Key {val} is NOT present in LinkedList")
        return False

    #method to delete element from linkedlist
    def delete(self, key):
        #point temp to head
        temp = self.head
        if (temp is not None):
            if (temp.data == key):
                #point head to the second node
                self.head = temp.next
                temp = None
                self.curr_nodes -= 1
                print(f"Key {key} is deleted from the LinkedList")
                return
        while(temp is not None):
        #using a while loop to transverse to next elements of the linkedlist
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        #case in which value does not exist
        if(temp == None):
            print(f"Key {key} is not present in LinkedList, and thus no deletion took place.")
            return
        prev.next = temp.next
        #update current nodes
        self.curr_nodes -= 1
        print(f"Key {key} is deleted from the LinkedList")
        temp = None
    
    #method to transverse the linkedlist
    #displaying the content occurs by moving temp node to the next one in the main while loop
    def traverse(self):
        print("Traversal of LinkedList: ")
        node = self.head
        while(node is not None):
            print(node.data, end = " ")
            #moving to next node
            node = node.next
        print()
        
def helper_printList(node):
    while(node is not None):
        print(node.data, end = "-->")
        node = node.next

#------------------------------------------------------------------------------------------------

#testing 

#mylink = LinkedList()
#mylink.insert(1) #head
#mylink.insert(2)
#mylink.insert(3)
#mylink.insert(4)
#mylink.insert(5)
#mylink.insert(6)
#mylink.delete(10)
#mylink.delete(3)
#mylink.insert(10) #tail
#mylink.__str__()
#mylink.traverse()
#print(mylink.search(10))
#print(mylink.search(100))