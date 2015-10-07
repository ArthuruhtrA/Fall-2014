"""
    Author: Ari Sanders
    Assignment: AirExpress Test
    Date: 10/28/2014
"""

from myPriorityQueue import *

def main():
    pq = createPriorityQueue()
    print("Is the queue empty?", emptyQueue(pq) == True)
    insert(pq, Passenger("Fred", 5))
    print("Is front Fred/5?", \
          front(pq).name == "Fred" and front(pq).priority == 5)
    insert(pq, Passenger("Wilma", 7))
    print("Is size 2?", pq.size == 2)
    insert(pq, Passenger("Pebbles", 6))
    print("Is front Wilma/7?", \
          front(pq).name == "Wilma" and front(pq).priority == 7)
    print("dumping the queue:")
    while not emptyQueue(pq):
        print(remove(pq))

if __name__ == '__main__':
    main()
