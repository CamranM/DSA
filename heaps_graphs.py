# solving heaps and graphs problems

# import the heapq library for hte first problem
import heapq


"""
1. Top k Frequent Elements
"""

'''
This function extracts the top k frequent elements in a list through heaps by first initializing the item and its 
frequency in a dictionary using simple for loop. Then, using the .items() function which allows the extraction
of a key value pair as a tuple, it pushes key(item) value(frequency) pairs onto a new list using the heap push
function in reverse order, with the frequency first and the negative value of the key, as a negative value is needed
to ensure if two items have the same frequency, the higher item gets popped(since heappop naturally pops the lower item,
if two items have the same frequency, adding a minus reverses this). Next, when the number of key value pairs
is higher than k, I start popping the tuple with the lowest frequency. Finally, I created a third list and then
appended the negative value of the key(since it was negative in the heaplist, so reversing it) and return the 
list with k frequency items.
'''
def kFrequent(nums, k):
    frequency_dict = {} # creates the dictionary
    if nums == []: # if the nums list is empty, I just return an empty list since there are no items
        return []


    # This for loop iterates through each item in the nums list, and assigns a frequency to each item in the nums list
    for item in nums:
        if item not in frequency_dict: # initializes the key in the dictionary if it's not currently in the dictionary
            frequency_dict[item] = 1
        else:
            frequency_dict[item] += 1 # adding a frequency if its already in the dictionary


    heap_list = [] # creating the list that will push and pop
    i = 0 # creating the iteration variable

    # This for loop extracts each key value pair in the dictionary into a tuple through the items() function,
    # then, it pushes each key value pair in reverse order(value, -key, with -key being assigned because
    # negative value is needed to ensure if two items have the same frequency, the higher item gets popped(since heappop
    # naturally pops the lower item, if two items have the same frequency, adding a minus reverses this). Finally,
    # if the heap list contains more than k elements, its starts popping the lowest frequency after each iteration.
    for key, value in frequency_dict.items():

        # uses the heappush, which takes a heap and item argument and pushes the item to the heap. Here we push the
        # frequency and item as a tuple into the heap
        heapq.heappush(heap_list,(value, -key))
        i += 1 # increments iteration variable
        print(heap_list) # debugging

        # once the number of items in the list is greater than k, we have to start popping since we can only have k most
        # frequent items.
        if i > k:

            # naturally, heapop pops the tuple with the lowest frequency in the heap_list
            heapq.heappop(heap_list)
            print(heap_list) # debugging


    k_frequent = [] # creates the list that will store the k frequent items
    print(heap_list) # debugging

    # this for loop extracts the actual item value from the heap_list, which now contains the frequency, item pairs of
    # the k most frequent items
    for items in heap_list:

        # since the items were negative to ensure that if two items had the same frequency, the lower one wouldn't get
        #popped, we have to reverse this by appendnig the negative item
        k_frequent.append(-items[1])

    return k_frequent # returns the k most frequent items/elements

# testing code
''' 
nums = [1,1,1,2,2,3]
k = 2
hello = kFrequent(nums,k)
print(hello)
'''

"""
2. All paths from one vertex to another in DAG
"""
''' 
This function takes a list of edge pairs, a starting vertex, and an ending vertex, to find all of the possible paths
it can get from the starting vertex to the ending vertex. This is done through breadth first search through a graph,
which goes through each node at a time and a queue. First, I use a while loop that includes 
both a current variable(which holds the current path that we are working on) and the queue(holding paths that we still
need to explore. The while loop first extracts the last value in the current variable. If this is the same as the destination,
this means we have gone through a full path, so curr = the entire path, and we can append curr to the all_paths list.
Otherwise, thsi means tht we haven't reached the destination yet, so we have to go through the list again and 
see if the last value in curr matches with the first value in any edge within the edges list. If it does, we add that to 
the queue, and repeated the process until we eventually build up a list that contains the entire path.
Every valid path is stored inside of the all_paths list that will be returned. 
'''

def allPaths(edges, source, destination):
    print(edges) # debugging
    queue_list = [[source]] # creates the queue, and adds the source(starting vertex) as a list
    all_paths = [] # the list that will store all of the valid paths

    # this while loop iterates through each potential path that can lead to a valid path from the source to the
    # destination. Each iteration, The while loop pops from the queue, stores the last vertex of the popped edge, then
    # checks to see if that vertex is the same as the destination. If it is, we have a full path, but if not,
    # we find the items where the first vertex of the edge equals current's last edge, and then add the last vertex of
    # that edge to curr, creating a path. We do this until a path has been created, and all possible paths have been
    # created
    while queue_list != []:
        current = queue_list.pop(0) # pops the first item from the queue
        print(current) # debugging
        vertex_n = current[-1] # extracts the last vertex in current

        # if the last vertex is current is the destination, we have completed a full path, so we can append it to the
        # all paths list
        if vertex_n == destination:
            all_paths.append(current)

        # otherwise, we must find edges that start with the end of the current vertex to continue the path, and if we
        # find any(which we should since its aceyclic) we append current + the ending vertex of an edge to the queue,
        # then continue onto the next iteration)
        else:
            for item in edges:
                if vertex_n == item[0]:
                    queue_list.append(current + [item[1]])


    return all_paths # returns every path that leads from the source to the destination

# code for testing
''' 
edges = [('a', 'b'), ('a', 'c'), ('b', 'd')]
hello = allPaths(edges, 'a', 'd')
print(hello)
'''
