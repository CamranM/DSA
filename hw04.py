# Homework 4 hw04.py
# name: Camran Mori-Khan


"""
Problem 1
"""
'''
This function identifies the smallest number in a list using recursion
'''
def smallest(plist):
    a = plist[0] # first item in the list
    b = plist[1:] # the rest of the list
    if len(b) == 0: # base case
        return plist[0]
    else:
        if a < smallest(b):
            return a # returns the smallest number via recursion
        else:
            return smallest(b) # if the first element isn't the smallest number, we don't consider it


"""
Problem 2 (linear version)
"""

'''
This function identifies the numbers that are equal to their indexes via linear recursion search
'''
def linearSearchValueIndexEqual(plist, i =0):
    correct_index_list = []
    if len(plist) == 0: # base case, if the list is empty then we return the numbers with the correct indicies
        return correct_index_list
    else:
        if plist[0] == i: # if the first number in plist is equal to its index, we add it to the list that contains the correct elements
            correct_index_list.append(plist[0])
            return correct_index_list + linearSearchValueIndexEqual(plist[1:], i + 1) # we use recursion to iterate over each element in the list, where the
            # argument is always plist[1:], which is used to iterate through the list
        else:
            return linearSearchValueIndexEqual(plist[1:], i + 1)

"""
Problem 2 (binary version)
"""
def binarySearchValueIndexEqual(plist):

    return

"""
Problem 3 (ladder)
"""

def ladder(rungs):
    return



