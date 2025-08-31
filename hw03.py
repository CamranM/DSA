# Homework 3 hw03.py
# Author Name: Camran Mori-Khan
#
# This program solves problems using stacks, including solving a mathematical problem written in rpn, determining
# whether a string is valid or not, and reversing a string.



class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()
        else:
            print("pop() error: Stack is empty.")
            return None

    def peek(self):
        if self.items:
            return self.items[-1]
        else:
            print("peek() error: Stack is empty.")
            return None

    def size(self):
        return len(self.items)


"""
1. postfixEval
Input type: a list of strings
Output type: a floating point number
"""

'''
This function takes a list of operators an operands in rpn form as input. Then, it pushes all operands onto a stack,
using a for loop to iterate through the list. When the for loop reaches an operator, it pops the last two items in the
stack, does the computation on the two operands, and the result is pushed back into the stack. Finally, the function
returns the total, which is the last item in the stack.
'''

def postfixEval(expr):
    operators = ["+", "-", "*", "/"]
    stack = Stack() # create an instance of the stack class

    # iterates through each item in the expr list
    for item in expr:
        # all operands will be pushed onto the stack, and operators will not be pushed
        if item not in operators:
            # pushes the operand onto the stack
            stack.push(item)
            # if the stack is empty, there are no operands, so the total is 0
            if stack.isEmpty():
                return 0

        # if the item is an operator, we start doing math with the two latest operands
        else:
            two = stack.pop() # popping the last operand in the stack
            one = stack.pop() # popping the second to last operand in the stack
            one = float(one) # converting to a floating point number
            two = float(two) # converting to a floating point number

            # if the operator is a plus, we add the two operands
            if item == "+":
                new = one + two
            # if the operator is a minus, we add the two operands
            elif item == "-":
                new = one - two
            # if the operator is multiplication, we add the two operands
            elif item == "*":
                new = one * two
            # the operator must be division
            else:
                new = one / two

            # convert result of the operator on the two operands into a float
            new = float(new)
            # push the new number onto the stack
            stack.push(new)
            

    # stores the last number in the stack in a variable that will be returned
    total = stack.peek()
    # to make sure that the last number in the stack is a float
    total = float(total)
    # returns the last item in the stack
    return total



"""
2. validParentheses
Input type: a string
Output type: a Boolean
"""

'''
This function returns whether a string is considered valid, where all open parenthesis are closed and it returns True,
if all open parenthesis are correctly closed. The function takes a string as input, containing parenthesis and letters. 
It pushes all parenthesis onto a stack using the .push method, then removes all closed parenthesis using .pop. This is 
to ensure that if a closed parenthesis is  added without any open parenthesis in the stack at that moment, the function 
returns false. By using counter variables, it counts the amount of each open and closed parenthesis that have 
been pushed to the stack. If the amount of open and closed parenthesis are the same, the function returns true,
and if the amounts are different, the function returns false.
'''
def validParentheses(s):
    stack = Stack() # create an instance of the stack class
    open_bracket = ["(", "[", "{"] # list of open parenthesis
    closed_bracket = [")", "]", "}"] # list of closed parenthesis
    a_closed = 0 # count the amount of ")" parenthesis in the string
    b_closed = 0 # count the amount of "]" parenthesis in the string
    c_closed = 0 # count the amount of "}" parenthesis in the string
    a_open = 0 # count the amount of "(" parenthesis in the string
    b_open = 0 # count the amount of "[" parenthesis in the string
    c_open = 0 # count the amount of "{" parenthesis in the string

    for item in s:
        if item in open_bracket or closed_bracket: # push all parenthesis onto the stack
            stack.push(item)

            # if the stack is in the open bracket list, the respective iteration variable is incremented
            if stack.peek() in open_bracket:
                if stack.peek() == "(":
                    a_open += 1
                elif stack.peek() == "[":
                    b_open += 1
                elif stack.peek() == "{":
                    c_open += 1

            # if the stack is in the closed bracket list, the respective iteration variable is incremented
            elif stack.peek() in closed_bracket:
                if stack.peek() == ")":
                    a_closed += 1
                elif stack.peek() == "]":
                    b_closed += 1
                elif stack.peek() == "}":
                    c_closed += 1

                # if at any point, the number of closed parenthesis of any of the 3
                # parenthesis is greater than the number of open parenthesis of the same type, we know this is not
                # valid, and the given string must be false
                if a_closed > a_open or b_closed > b_open or c_closed > c_open:
                    return False

                # popping all closed parenthesis to ensure that a closed parenthesis isn't added before an open one
                stack.pop()

                # if there is a closed parenthesis with no open parenthesis before it, the string must not be valid
                if stack.peek() is None:
                    return False

    # if the number of each open and closed parenthesis is the same, the string is valid
    if a_open == a_closed and b_open == b_closed and c_open == c_closed:
        return True
    # if the number of each open and closed parenthesis isn't the same, the string isn't valid
    else:
        return False

"""
3. reverseString
Input type: a string
Output type: a string
"""

'''
This function takes a string as input, pushes all of the letters in the string onto a stack using the .push method.
Then, it pops each item in the stack and adds it to an empty string variable. By doing so, it reverses the original
string. The function returns the reversed string 
'''
def reverseString(s):
    reversed_string = "" # variable that will hold the reverse string
    stack = Stack() # create an instance of a stack

    for item in s: # iterate through the string
        stack.push(item) # push all letters in the string onto the stack

    # this while loop iterates through each item in the stack, popping each item and adding it to the reversed_string
    # variable. The loop is definite, and terminates when stack.peek() is None, meaning there is no items left in the
    # stack
    while stack.peek() is not None:
        letter = stack.pop()
        reversed_string += letter
    return reversed_string # returns the reversed string






