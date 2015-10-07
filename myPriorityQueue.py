"""
    Author: Ari Sanders
    Assignment: airExpress Priority Queue
    Date: 10/22/2014
"""

from myNode import *

class PriorityQueue(rit_object):
    """
    object is specified as the type of the 'front' and
    'back' slots so that either None or a Node object
    can be used as valid assignments.
    """
    __slots__ = ( 'front', 'back', 'size' )
    _types    = ( object,  object, int    )

class Passenger(rit_object):
    __slots__ = ("name", "priority")
    _types = (str, int)

def createPriorityQueue():
    """Creates a new empty PriorityQueue"""
    return PriorityQueue(None, None, 0)

def insert(queue, element):
    """Insert an element into the back of the queue"""
    if emptyQueue(queue):
        queue.front = Node(element, None)
    else:
        #Search queue for location to insert
        if element.priority >= queue.front.data.priority:
            queue.back = Node(element, queue.front)
        else:
            temp = queue.front
            while temp.next != None and temp.next.data.priority < element.priority:
                temp = temp.next
            temp.next = Node(element, temp.next)
    queue.size += 1

def remove(queue):
    """Remove the front element from the queue (returns None)"""
    if emptyQueue(queue):
        raise IndexError("dequeue on empty queue")
    output = queue.front
    queue.front = queue.front.next
    if emptyQueue(queue):
        queue.back = None
    queue.size -= 1
    return output

def front(queue):
    """Access and return the first element in the queue without removing it"""
    if emptyQueue(queue):
        raise IndexError("front on empty queue")
    return queue.front.data

def emptyQueue(queue):
    """Is the queue empty?"""
    return queue.front == None
