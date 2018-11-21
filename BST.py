from random import randint

"""
---------------------------------
Assignment 5 Binary Search Trees
Student Name: Michael Reinhart
Student Number:  20001556
Date Modified : April 1 2017
---------------------------------

This module implements binary search trees.
The tree elements may be of any type.  Duplicates are not allowed.

Example for CISC 121

"""


# A BST node is a dict with three elements:
# 1. data: the value in the node
# 2. left: a reference to the left subtree
# 3. right: a reference to the right subtree

# Prints an indented display of the tree -- useful for debugging.
# The output will look kind of like a sideways version of a drawing
# of the tree.
def display(tree, indent=5):
    if tree == None:  # empty
        pass
    else:
        # right tree first (so it's on the right when you tilt your
        # head to the left to look at the display)
        display(tree['right'], indent + 3)
        print()
        print("    " * indent + str(tree['data']))
        # now the left tree
        display(tree['left'], indent + 3)


# adds a value to a BST and returns a pointer to the modified BST
def add(tree, value):
    if tree == None:
        return {'data': value, 'left': None, 'right': None}
    elif value < tree['data']:
        tree['left'] = add(tree['left'], value)
        return tree
    elif value > tree['data']:
        tree['right'] = add(tree['right'], value)
        return tree
    else:  # value == tree['data']
        return tree  # ignore duplicate


def printValues(tree):
    if tree == None:
        return
    printValues(tree['left'])
    print(tree['data'])
    printValues(tree['right'])


'''
def changeLeaves(tree):
    if tree == None:
        return {'data':[tree['data'][0],'lief'], 'left':None, 'right':None}
    if tree['right'] == None and tree['left'] == None:
        tree['data'] = [tree['data'][0],'lief']
    else:
        changeLeaves(tree['right'])
        changeLeaves(tree['left'])
'''


def changeLeaves(tree):
    if tree['data'] != None:
        if tree['right'] == None:
            if tree['left'] == None:
                tree['data'] = [tree['data'][0], 'Lief']
                changeLeaves(tree['left'])
            else:
                changeLeaves(tree['right'])
    return tree


def countNodes(tree):
    pass


def printReverse(tree):
    pass


def main():
    aList = ['Wendy', 'Carol', 'John', 'Cary', 'Will', 'Bill', 'jill']
    myTree = None  # create an empty tree
    # Create a tree with the nodes [20, 2, 25, 14, 1, 23, 75, 93, 74]
    # Note that the add function always returns the root of the BST!
    myTree = add(myTree, [20, aList[randint(0, 6)]])
    myTree = add(myTree, [2, aList[randint(0, 6)]])
    myTree = add(myTree, [25, aList[randint(0, 6)]])
    myTree = add(myTree, [14, aList[randint(0, 6)]])
    myTree = add(myTree, [1, aList[randint(0, 6)]])
    myTree = add(myTree, [23, aList[randint(0, 6)]])
    myTree = add(myTree, [75, aList[randint(0, 6)]])
    myTree = add(myTree, [93, aList[randint(0, 6)]])
    myTree = add(myTree, [74, aList[randint(0, 6)]])

    changeLeaves(myTree)

    display(myTree, 0)
    printValues(myTree)


main()
