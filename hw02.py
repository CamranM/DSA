
# linked list


"""
Node class used for Problem 2-5
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, data):
        self.data = data

    def setNext(self, node):
        self.next = node





"""
2. transform(lst)
Transform an unordered list into a Python list
Input: an (possibly empty) unordered list
Output: a Python list
"""
'''
This function takes a linked list as an argument, iterates through the linked list, and appends the numerical
value in a node into a python list. It returns the python list.
'''
def transform(lst):
    curr = lst # this variable is the pointer that points to the current node we are working with. It is initialized
    # as the head of the linked list
    python_list = [] # creates an empty list

    ''' 
    # this while loop iterates through a linked list, as long as we are not at the last node. If we are at the last node,
    the loop ends. It is an indefinite loop
    '''
    while curr is not None:
        python_list.append(curr.getData()) # appends the numerical value of the current node
        curr = curr.getNext() # move the pointer to point to the next node

    return python_list # returns the python list


"""
3. concatenate(lst1, lst2)
Concatenate two unordered lists
Input: two (possibly empty) unordered list
Output: an unordered list
"""
'''
This function takes two linked lists as input, and concatenates them together in an unordered way. It returns the new
concatenated list 
'''
def concatenate(lst1, lst2):
    curr = lst1 # this variable is the pointer that points to the current node we are working with. It is initialized
    # as the head of the first linked list
    prev = None # this variable points to the previous node. It is initially set to None since there is no node before
    # head
    if not lst1: # if the first list is empty, then we can return the second list
        return lst2 # returns the second list

    ''' 
    # this while loop iterates through the first list, up until the last node of the first list, which causes the loop
    # to end. It is an indefinite loop.
    '''
    while curr is not None:
        prev = curr # previous gets set to the value of curr before we iterate curr
        curr = curr.getNext() # curr pointer gets set to the next node
    curr2 = lst2 # this variable is the pointer that points to the current node we are working with. It is initialized
    # as the head of the second linked list

    if lst2 is not None: # conditional statement that checks whether list 2 is empty. If not, this statement runs
        prev.setNext(curr2) # prev, pointed to the last node of the first list. Now, we set the pointer of the last node
        # to the beginning of the second linked list, which connects both lists

    return lst1 # returns lst1, which should be a connected linked list of both list 1 and list 2



"""
4. removeNodesFromBeginning(lst, n)
Remove the first n nodes from an unordered list
Input:
    lst -- an (possibly empty) unordered list
    n -- a non-negative integer
Output: an unordred list
"""
'''
This function removes n amount of nodes from the beginning of a linked list. It returns the new list with n nodes
removed 
'''
def removeNodesFromBeginning(lst, n):
    head = lst # the head variable head holds the head of the linked list
    curr = lst # this variable is the pointer that points to the current node we are working with. It is initialized
    # as the head of the first linked list
    count = 0 # iteration variable that makes sure that only n nodes will be removed

    ''' 
    # while loop that iterates through the linked list, as long as the current node does not point at None. If
    # n number of nodes have been removed, the loop ends. It is an indefinite loop.
    '''

    while curr is not None:
        if count < n: # conditional statement that checks whether the amount of nodes we have passed is more than n.
            # if not, we remove the current node
            head = curr.getNext() # this makes head point to the next node, which removes a node from the linked list
        else:
            break # if we have removed n nodes, the while loop ends.
        count += 1 # increments the count variable
        curr = curr.getNext() # # curr pointer gets set to the next node

    return head # returns the linked list with n number of nodes removed



"""
5. removeNodes(lst, i, n)
Starting from the ith node, remove the next n nodes
(not including the ith node itself).
Assume i + n <= lst.length(), i >= 0, n >= 0.
Input:
    lst -- an unrdered list
    i -- a non-negative integer
    n -- a non-negative integer
Output: an unordred list

lst = [1, 2, 3, 4, 5]
i = 2
n = 2
return [1, 2, 5]

i = 1
n = 2
return [1, 4, 5]

i = 0
n = 2
return [3, 4, 5]
"""

'''
this function removes n number of nodes after from the ith position in the linked list. It returns the new list with 
n nodes removed after the ith position
'''
def removeNodes(lst, i, n):
    head = lst # the head variable head holds the head of the linked list
    curr = lst # this variable is the pointer that points to the current node we are working with. It is initialized
    # as the head of the first linked list
    count_i = 0 # an iteration variable that counts to the ith position
    count_n = 0 # an iteration variable that counts the n nodes that are removed
    prev = None # this variable points to the previous node. It is initially set to None since there is no node before
    # head

    if n == 0: # if we are removing 0 nodes, we just return the original list, regardless of i
        return lst

    elif i == 0 and n !=0: # if i == 0, we can start removing n number of nodes from the beginning, which is the same
        # approach as the last question
        count = 0  # iteration variable that makes sure that only n nodes will be removed

        '''
        # while loop that iterates through the linked list, as long as the current node does not point at None. If
        # n number of nodes have been removed, the loop ends. It is an indefinite loop.
        '''
        while curr is not None:
            if count < n:  # conditional statement that checks whether the amount of nodes we have passed is more than n.
                            # if not, we remove the current node
                head = curr.getNext()  # this makes head point to the next node, which removes a node from the linked list
            else:
                break  # if we have removed n nodes, the while loop ends.
            count += 1  # increments the count variable
            curr = curr.getNext()  # # curr pointer gets set to the next node

        return head # returns the new linked list

    ''' 
    # this while loop runs only if n != 0 and i!=0. For these cases, the while loop goes to the ith position, starts
    # removing n number of nodes at i + 1, and returns the new linked list. It is an indefinite loop.
    '''
    while curr is not None:
        if count_i < i: # this conditional statement is  executed to get to the ith position in the linked list
            prev = curr # previous gets set to the value of curr before we iterate curr
            curr = curr.getNext() # this makes head point to the next node, which removes a node from the linked list via getNext() method
            count_i += 1 # increments count i
        elif count_i >= i and count_n < n: # this conditional statement executes if we have passed the ith position,
            # and currently want to remove n number of nodes
            curr = curr.getNext() # this makes head point to the next node, which removes a node from the linked list via getNext() method
            prev.setNext(curr) # by setting the previous node's pointer to 2 nodes in the future, we remove the node in between
            count_n += 1 # increment count i
        else: # this executes if we have passed the ith position and removed n nodes, and there are still nodes left in the linked list
            prev = curr # previous gets set to the value of curr before we iterate curr
            curr = curr.getNext() # this makes head point to the next node, which removes a node from the linked list via getNext() method

    return head # returns the new list













