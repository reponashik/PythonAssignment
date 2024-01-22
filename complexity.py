'''
Activity 2.3, 2.4 & 2.7
Complexity
context:  
complexity analysis, comparisions, looking into average search time.

'''
#importing binarysearchtree and linkedlist, which gives access respective classes
import binarysearchtree 
import linkedlist
#importing other relevant Python libraries
import random #for generating random values
import time #library necessary for complexity analysis
import math
import matplotlib.pyplot as plt #library necessary for plotting

#defining tree constants
TREE_SIZE = 100
NUMBER_OF_TREES = 20
NUM_TREES_PER_SIZE = 1000
#defining linkedlist constants
LINKEDLIST_SIZE = 100
NUMBER_OF_LINKEDLIST = 20
NUM_LINKEDLIST_PER_SIZE = 1000
#defining search number constant as per specification
SEARCH_NUMBER = 42

#2.3 Start 

#takes an input n and generates a tree of size n by populating it 
#with n random integers from 1 to 1000;
def random_tree(n):
    tree = binarysearchtree.BinarySearchTree()
    for i in range(n):
        val = random.randint(1, 1000)
        tree.insert(val) #method from binarysearchtree.py
    return tree

#defining list X and listY
X = []
Y = []

#populate list X
for i in range(5,101,5):
    X.append(i)
#print(X)

#generating 1000 random trees for s in X 
#searching for the value 42 defined as constant above
#using the time library function etime
#list Y storing the average time spent by "search"
for s in X:
    avg_time = 0
    for i in range(NUM_TREES_PER_SIZE):
        tree = random_tree(s)
        stime = time.perf_counter_ns()
        #perf_counter() function always returns the float value of time in seconds
        is_present = tree.search(SEARCH_NUMBER)
        etime = time.perf_counter_ns()
        avg_time += (etime-stime)
    Y.append(avg_time/NUM_TREES_PER_SIZE)

#defining linear relationship
c = (Y[1]-Y[0])/5
b = (2*Y[0]-Y[1])
#Solving the linear equation
#solving for t = c*n + b
Y2 = [Y[0], Y[1]]
for i in range(2, len(Y)):
    t = c*X[i] + b
    Y2.append(t)
    
#----------------------------------------------------
   
#solving for t = c*log2(n) + b
#solving the linear to obtain Y3 by computing t = Y[0]
#Y[1] and n = log2(5), log2(10) respectively

'''
Y[0] = log2(5)c2 + b2
y[1] = log2(10)c2 + b2
This is how it looks like mathematically.

'''
c2 = (Y[1]-Y[0]) 
#the remainder of the equation was equal to 1, hence it has been removed
b2 = Y[0]*(1 + math.log2(5)) - Y[1]*math.log2(5)

#estimating of average search time under an ideal
#logarithmic relationship to the size of the trees in X
Y3 = [Y[0], Y[1]]
for i in range(2, len(Y)):
    t = c2*math.log2(X[i]) + b2
    Y3.append(t)

#plot graph for linkedlist
#similar approach to Trees
def random_linkedlist(n):
    link = linkedlist.LinkedList()
    for i in range(n):
        val = random.randint(1, 1000)
        link.insert(val)
    return link

#defining list Y4 for linkedlist comparision question
Y4 = []
for s in X:
    avg_time = 0
    #similar approach to previous part, store average search time
    for i in range(NUM_LINKEDLIST_PER_SIZE):
        link = random_linkedlist(s)
        stime = time.perf_counter_ns()
        is_present = link.search(SEARCH_NUMBER)
        etime = time.perf_counter_ns()
        avg_time += (etime-stime)
    Y4.append(avg_time/NUM_LINKEDLIST_PER_SIZE)
    
#2.3 End 

#-----------------------------------------------------------------------------------

#2.4 Start

#plotting all the graphs using matplotlib function plt
plt.plot(X, Y)
plt.plot(X, Y2)
plt.plot(X, Y3)
plt.plot(X, Y4)
plt.legend(['BST','Linear','Logarithmic', 'LL'])
plt.xlabel('Size of trees')
plt.ylabel('Search time')
plt.ticklabel_format(axis='both', style='sci', scilimits=(0,0))
plt.show()

'''
#2.4.2
Complexity analysis X vs Y:
The graph of X vs Y looks like a logarithmic O(log(n)). Thus the complexity of BST is logarithmic.

#2.4.6
Complexity analysis X vs Y, Y2 and Y3:
The complexity of BST is logarithmic O(log(n)), while searching for a value in BST, 
there might be other processes running in the backgroud, and that can be the reason why 
the graph is not smooth and close to that of Y3.

#2.7.2
Complexity analysis X vs Y, Y2, Y3 and Y4:
The complexity of linkedlist is linear O(n) while that of BST in logarithmic.(log(n))
A logarithmic time complexity is usually faster than a linear time complexity
But for sufficiently large inputs (a very large linkedlist), linear time
complexity may be better - depending on the problem
'''