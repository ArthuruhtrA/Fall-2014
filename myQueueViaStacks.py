from myStack import *

class QueueViaStacks(rit_object):
    __slots__ = ("stack1", "stack2", "size")
    _types = (object, object, int)

def moveStacks(queue):
    """
        Moves all elements from one stack onto the other stack
        End conditions: data has moved from one stack to the other
        Returns None
    """
    if emptyStack(queue.stack1):
        while not emptyStack(queue.stack2):
            queue.stack1 = push(queue.stack1, top(queue.stack2))
            queue.stack2 = pop(queue.stack2)
    else:
        while not emptyStack(queue.stack1):
            queue.stack2 = push(queue.stack2, top(queue.stack1))
            queue.stack1 = pop(queue.stack1)

def enqueue(queue, element):
    """
        Utilizes one or both stacks to enqueue the element
        End conditions: additional element is on stack1, so is all other data
        Returns None
    """
    if emptyStack(queue.stack1):
        moveStacks(queue)
    queue.stack1 = push(queue.stack1, element)
    queue.size += 1

def dequeue(queue):
    """
        Utilizes one or both stacks to dequeue the element at the front
        End conditions: all data is on stack2, the top of which has been removed
        Returns None
    """
    if emptyQueue(queue):
        raise IndexError("pop on empty queue")
    if emptyStack(queue.stack2):
        moveStacks(queue)
    queue.stack2 = pop(queue.stack2)
    queue.size -= 1

def front(queue):
    """
        Determines the front element of the queue.
        Returns Node.data
    """
    if emptyQueue(queue):
        raise IndexError("front on empty queue")
    if emptyStack(queue.stack2):
        moveStacks(queue)
    return top(queue.stack2)

def back(queue):
    """
        Determines back element of the queue.
        Returns Node.data
    """
    if emptyQueue(queue):
        raise IndexError("back on empty queue")
    if emptyStack(queue.stack1):
        moveStacks(queue)
    return top(queue.stack1)

def emptyQueue(queue):
    """
        Despite the name, this does not empty a queue.
        It determines whether or not the queue is empty.
        Returns Boolean
    """
    if emptyStack(queue.stack1) and emptyStack(queue.stack2):
        return True
    return False
