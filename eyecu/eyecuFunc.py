"""
Program for binary search tree homework.

Author: Aaron Deever
Author: Ari Sanders

file: eyecuFunc.py
"""

from rit_object import *

class EyecuBST(rit_object):
    """ this binary search tree will support inserts, height
    of tree from given element, subtree size from a given element,
    imbalance measurement.
    left:  EyecuBST representing the left sub-tree of this node.
    right: EyecuBST representing the right sub-tree of this node.
    parent: EyecuBST representing the parent node of this node.
    All nodes have a parent node, except for root of the tree (uses None).
    value: the data value associated with this node.
    height: the height of the subtree associated with this node.
    The height is defined as the maximum of the height of the
    left and right subtrees, plus 1.  A leaf node has a height of 0.
    An empty tree as represented by None is defined to have a height
    of -1.
    size: the number of nodes contained in this binary tree.
    imbalance: the difference in the height of the
    left and right subtrees.

    """
    __slots__ = ('left', 'right', 'parent',
                 'value', 'height', 'size', 'imbalance')
    _types    = ('EyecuBST', 'EyecuBST', 'EyecuBST',
                 int, int, int, int)

def createEyecuBST(el, parent):
    """ creates a BST containing just this node, and connected
    to the given parent node, which is None if this is the root.
    Returns the tree node.
    """
    return EyecuBST(None, None, parent, el, 0, 1, 0)

def eyecuToString(tr):
    """ takes an EyecuBST tree and generates a string containing
    an inorder processing of the nodes of the tree.  For each
    node, the string contains the following information:
    value, height, size, imbalance.
    Returns the string
    """

    if tr == None:
        return ""
    else:
        thisNodeStr = "Value: " + str(tr.value) + ", Height: " + \
        str(tr.height) + ", Size: " + str(tr.size) + ", Imbalance: " + \
        str(tr.imbalance) + "\n"
        
        return eyecuToString(tr.left) + thisNodeStr + eyecuToString(tr.right)

def insert(tr, el):
    """ function to insert an element into a binary search tree
    following the rules of binary search trees.
    
    return: an updated tree
    precondition: assumed all elements unique
    """

    # replace with your insert function code

    if not tr:
        return createEyecuBST(el, None)
    tr.size += 1
    if el < tr.value:
        tr.height += mantainHeight(tr, tr.left)
        if not tr.left:
            if not tr.right:
                tr.imbalance = 0
            else:
                tr.imbalance = tr.right.height
            tr.left = createEyecuBST(el, tr.parent)
        else:
            if not tr.right:
                tr.imbalance = tr.left.height
            else:
                tr.imbalance = abs(tr.left.height - tr.right.height)
            tr.left = insert(tr.left, el)
        return tr
    else:
        tr.height += mantainHeight(tr, tr.right)
        if not tr.right:
            if not tr.left:
                tr.imbalance = 0
            else:
                tr.imbalance = tr.left.height
            tr.right = createEyecuBST(el, tr.parent)
        else:
            if not tr.left:
                tr.imbalance = tr.right.height
            else:
                tr.imbalance = abs(tr.left.height - tr.right.height)
            tr.right = insert(tr.right, el)
        return tr

def mantainHeight(tr, direction):
    if not direction:
        height = 0
    else:
        height = direction.height
    if not tr.left:
        left = 0
    else:
        left = tr.left.height
    if not tr.right:
        right = 0
    else:
        right = tr.right.height
    if max(left, right) == height:
        return 1
    else:
        return 0

def treeHeight(tr):
    """ 
    Returns the height of the tree rooted at this node. Returns -1
    if input tr is an empty tree (None).
    """

    # replace with your treeHeight function code
    if not tr:
        return -1
    else:
        #Code goes here
        return tr.height

def treeSize(tr):
    """ 
    Returns the size of the tree rooted at target node. Returns 0
    is input tr is an empty tree (None)
    """
    
    # replace with your treeSize function code
    if not tr:
        return 0
    else:
        #Code goes here
        return tr.size

def treeImbalance(tr):
    """ 
    Returns the imbalance of the tree rooted at target node. Returns 0
    is input tr is an empty tree (None)
    """
    
    # replace with your treeImbalance function code
    if not tr:
        return 0
    else:
        return tr.imbalance

def findNode(tr, val):
    """ finds the target node in the tree.  Returns the node reference.
    Returns None if the node is not in the tree.

    precondtion:  val is non-negative integer.
    
    """

    # replace with your findNode function code
    if not tr:
        return None
    else:
        if tr.value == val:
            return tr
        elif val > tr.value:
            return findNode(tr.right, val)
        elif val < tr.value:
            return findNode(tr.left, val)

# YOU MAY ADD ADDITIONAL FUNCTIONS AS NECESSARY
