
# binary trees problems 



class BinaryTreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None
"""
1. Iterative preorder traversal of a binary tree
"""

'''
This function iteratively traverses through a binary tree using one stack and one list. The stack pushes all of the right
nodes and then the left nodes, then pops the nodes, and their values are added to a list in the correct preorder order. 
Finally, the function returns the list with the node values 
'''

def preorder(root):

    iterative_stack = [] # creates the stack
    node_vals = [] # creates the list that will be used to store the node values
    if root is None: # if the root is None, this means this is an empty binary tree, and we return an empty list
        return node_vals
    else: # otherwise, we first add the root node to the stack
        iterative_stack.append(root)


    # this while loop iterates through every node in the binary tree. Each time, it pops the value from the stack,
    # adds it to the node_vals list, and pushes the right and left children of the previous node onto the stack.
    # Since the left node is pushed second, it is added to the node_vals list first. The loop ends once the stack is
    # empty(ie, we have reached the rightmost leaf on the right subtree. The while loop is definite.
    while iterative_stack != []:
        node_val = iterative_stack.pop() # this will pop the last item in the stack
        node_vals.append(node_val.val) # this appends the item that was just popped into the node_vals list
        if node_val.right is not None: # if the current node's right child is not none, we push it to the stack
            iterative_stack.append(node_val.right)
        if node_val.left is not None: # if hte current node's left child is not none, we push it to the stack
            iterative_stack.append(node_val.left)
    return node_vals # the list with values in preorder traversal is returned


"""
2. Reconstruct Binary Tree
"""
'''
This function reconstructs a binary tree given two lists which represent the binary tree through recursion. First, the
root node is defined, and knowing that the root node is the first item in the preorder list(since preorder traverses
the root node first) we split up the inorder list(since the inorder list is in the format left subtree, root, right
subtree) and implement recursion to build both the left and right subtrees
'''

# inorder traversal can be divided as [left-subtree-nodes, root, right-subtree-nodes]
# preorder traversal can be divided as [root, left-subtree-nodes, right-subtree-nodes]

def reconstructBT(preorder, inorder):


    # a try and except block was used in case the list was empty, or if the root didn't exist in the inorder list
    try:
        root = BinaryTreeNode(preorder[0]) # creates the root node, and the value is the first index of the preorder list
        root_index_inorder = inorder.index(preorder[0]) # finds the index of the root node value in the inorder list
        left_subtree_inorder = inorder[:root_index_inorder] # creates a left partition of the inorder list(left subtree)
        right_subtree_inorder = inorder[root_index_inorder + 1:] # creates a right partition of the inorder list(right subtree)
        left_subtree_preorder = preorder[1:root_index_inorder+1] # creates a left partition of the preorder list(left subtree)
        right_subtree_preorder = preorder[root_index_inorder+1:] # creates a right partition of the inorder list(right subtree)
    except:
        return None


    # the base case, where once either of the lists are empty, we return none because
    # the tree has been created, as all values in either of the lists have been recusrrively traversed on.
    # Since the values are the same(but in different order), we can return once
    # either of the lists have been processed, not both
    if inorder == [] or preorder == []:
        return

    # We create the left subtree and right subtree by recursively calling reconstructBT function, where the
    # inputs are the left partition(as in left subtree node values) of both lists for creating the left root and the right
    # partition(as in right subtree node values) for creating the right subtree.
    else:
        root.left = reconstructBT(left_subtree_preorder, left_subtree_inorder)
        root.right = reconstructBT(right_subtree_preorder, right_subtree_inorder)

        # the root is returned at each step to return the expanded tree every recursion
        return root

"""
3. Convert Binary Search Tree
"""

'''
This function converts a binary search tree into a greater sum tree using helper functions. First, I employed
the strategy of creating both the inorder and preorder lists of the binary tree by traversing through the binary tree
using preorder and inorder traversal, using the preorder function from the first problem. Then, the function uses a for loop to 
calculate the greater sum values for each item in both the preorder and inorder lists, and appends them to a new list.
Finally, both the new preorder and inorder lists are passed into the same function as the second problem, which creates
the tree using both the preorder and inorder list using recursion.
'''

def convertBSTtoGST(root):

    '''
    This function iteratively traverses through a binary tree using one stack and one list. The stack pushes all of the right
    nodes and then the left nodes, then pops the nodes, and their values are added to a list in the correct preorder order.
    Finally, the function returns the list with the node values
    '''

    def preorder(root):
        iterative_stack = [] # creates the stack
        preorder_list = [] # creates the list that will be used to store the node values
        if root is None: # if the root is None, this means this is an empty binary tree, and we return an empty list
            return preorder_list
        else:  # otherwise, we first add the root node to the stack
            iterative_stack.append(root)


        # this while loop iterates through every node in the binary tree. Each time, it pops the value from the stack,
        # adds it to the node_vals list, and pushes the right and left children of the previous node onto the stack.
        # Since the left node is pushed second, it is added to the node_vals list first. The loop ends once the stack is
        # empty(ie, we have reached the rightmost leaf on the right subtree. The while loop is definite.
        while iterative_stack != []:
            node_val = iterative_stack.pop() # this will pop the last item in the stack
            preorder_list.append(node_val.val) # this appends the item that was just popped into the node_vals list
            if node_val.right is not None: # if the current node's right child is not none, we push it to the stack
                iterative_stack.append(node_val.right)
            if node_val.left is not None: # if hte current node's left child is not none, we push it to the stack
                iterative_stack.append(node_val.left)
        return preorder_list # the list with values in preorder traversal is returned
    preorder_list = preorder(root) # creates an instance of hte preorder function, with the variable holding the preorder lsit


    ''' 
    This function iteratively traverses through the binary tree using inorder. First, it goes all the way down to the left node, simeoustaneously
    pushing each left node to a stack. Then, once there are no more left nodes it pops and appends to the stack.
    then, it checks curr.right, and if that's also none, it goes back and pops the parent of the left leaf,
    appends it to the list, checks the right node, pushes it to the stack if its not none, and so on.
    '''


    def inorder(root):
        iterative_stack = [] # creates the stack
        inorder_list = [] # creates the list that will be used to store the node values
        if root is None:  # if the root is None, this means this is an empty binary tree, and we return an empty list
            return inorder_list
        current = root # creates the current variable which will hold the current node


        # This while loop iterates through all nodes in the tree through in order traversal. The while loop terminates
        # when either current is None(the right most leaf node) or the stack is empty(there are no more previous nodes
        # we have to go back to). It is a finite loop.
        while current is not None or iterative_stack != []:
            # This loop runs until we hit the left most node, pushing each left node to the stack
            while current is not None:
                iterative_stack.append(current) # pushing to the stack
                current = current.left # curr gets updated to the next left child

            current = iterative_stack.pop() # pop the top item from the stack
            inorder_list.append(current.val) # add that value to the inorder list
            current = current.right # move on to the right leaf, if it doesn't exist, we go through the bigger while loop again
        return inorder_list
    inorder_list = inorder(root) # calling the inorder function


    print(preorder_list) # for debugging
    print(inorder_list) # for debugging
    gst_inorder_list = [] # creates the inorder list that will be passed into the next function as a parameter
    gst_preorder_list = [] # creates the preorder list that will be passed into the next function as a parameter

    # these two for loops create the values for the gst, using the sum function

    for i in range(len(inorder_list)):
        # since for the inorder list, its in ascending order, I can just sum up every time including and to the right
        # of the current item
        new_item = sum(inorder_list[i:])
        # appends the greater sum value to the greater sum list
        gst_inorder_list.append(new_item)


    # for the preorder, a nested was used to iterate through the list for each item, creating a new list
    # that held the items that had greater value than the item in focus, and summing hte items, and
    # appending it to the gst preorder list
    for item in preorder_list:
        temp_list = [] # creating a temporary list that stores all of hte values greater or equal to item
        for value in preorder_list:
            if value >= item: # if the value is greater or equal to the current item, it will be added in the calculation
                temp_list.append(value)
        new_item = sum(temp_list) # the new item is created via the sum function
        gst_preorder_list.append(new_item) # the new item is added to the gst preorder list


    print(gst_preorder_list) # for debugging
    print(gst_inorder_list) # for debugging

    '''
    This function reconstructs a binary tree given two lists which represent the binary tree through recursion. First, the
    root node is defined, and knowing that the root node is the first item in the preorder list(since preorder traverses
    the root node first) we split up the inorder list(since the inorder list is in the format left subtree, root, right
    subtree) and implement recursion to build both the left and right subtrees
    '''

    def reconstructBT(gst_preorder_list, gst_inorder_list):
        # a try and except block was used in case the list was empty, or if the root didn't exist in the inorder list
        try:
            root = BinaryTreeNode(gst_preorder_list[0])  # creates the root node, and the value is the first index of the preorder list
            root_index_inorder = gst_inorder_list.index(gst_preorder_list[0])  # finds the index of the root node value in the inorder list
            left_subtree_inorder = gst_inorder_list[:root_index_inorder]  # creates a left partition of the inorder list(left subtree)
            right_subtree_inorder = gst_inorder_list[root_index_inorder + 1:]  # creates a right partition of the inorder list(right subtree)
            left_subtree_preorder = gst_preorder_list[1:root_index_inorder + 1]  # creates a left partition of the preorder list(left subtree)
            right_subtree_preorder = gst_preorder_list[root_index_inorder + 1:]  # creates a right partition of the inorder list(right subtree)
        except:
            return None

        # the base case, where once either of the lists are empty, we return none because
        # the tree has been created, as all values in either of the lists have been recusrrively traversed on.
        # Since the values are the same(but in different order), we can return once
        # either of the lists have been processed, not both
        if gst_inorder_list == [] or gst_preorder_list == []:
            return

        # We create the left subtree and right subtree by recursively calling reconstructBT function, where the
        # inputs are the left partition(as in left subtree node values) of both lists for creating the left root and the right
        # partition(as in right subtree node values) for creating the right subtree.
        else:
            root.left = reconstructBT(left_subtree_preorder, left_subtree_inorder)
            root.right = reconstructBT(right_subtree_preorder, right_subtree_inorder)

            # the root is returned at each step to return the expanded tree every recursion
            return root

    root = reconstructBT(gst_preorder_list, gst_inorder_list) # calls the reconstructBT function
    return root # returns the root of the greater sum tree
