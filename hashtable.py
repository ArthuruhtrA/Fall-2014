"""
===Overhauled for BieberHash double-hashing by Ari Sanders on 11/11/2014===
file: hashtable.py
language: python3
author: sps@cs.rit.edu Sean Strout
author: jeh@cs.rit.edu James Heliotis
author: anh@cs.rit.edu Arthur Nunes-Harwitt
author: jsb@cs.rit.edu Jeremy Brown
"""
from rit_object import *

class HashTable(rit_object):
    """
           The HashTable data structure contains a collection of values
       where each value is located by a hashable key.
       No two values may have the same key, but more than one
       key may have the same value.
       table is the list holding the hash table
       size is the number of elements in occupying the hashtable

    """
    __slots__ = ( 'table', 'size' )
    _types    = (list, int)


def createHashTable(capacity):
  """
  createHashTable: NatNum? -> HashTable
  """
  aHashTable = HashTable([None for _ in range(capacity)], 0)
  return aHashTable

def HashTableToStr(hashtable):
  """
  HashTableToStr: HashTable -> String
  """
  result = ""
  for i in range(len(hashtable.table)):
      e = hashtable.table[i]
      if not e == None:
          result += str( i ) + ": "
          result += EntryToStr(e) + "\n"
  return result


class Entry(rit_object):
    """
       A class used to hold key/value pairs.
    """

    __slots__ = ( "key", "value" )
    _types = (object, object)


def EntryToStr(entry):
  """
  EntryToStr: Entry -> String
  return the string representation of the entry.
  """
  return "(" + str( entry.key ) + ", " + str( entry.value ) + ")"


def hash_function(name, capacity):
    """
        Hashes data mod capacity
        name = str, name of person
        capacity = int, how many seats there are
        returns: int, hash value for name
    """
    seat = 1
    for letter in name:
        seat *= ord(letter.upper()) - ord("A") + 1
    return seat % capacity


def hash_function_two(name, capacity):
    """
        Backup function for hash_function()
        name = str, name of person
        capacity = int, how many seats there are
        returns: int, hash value for name
    """
    seat = 0
    for letter in name:
        seat += ord(letter.upper()) - ord("A") + 1
    return seat % capacity


def keys( hTable ):
    """
    keys: HashTable(K, V) -> List(K)
    Return a list of keys in the given hashTable.
    """
    result = []
    for entry in hTable.table:
        if entry != None:
            result.append( entry.key )
    return result

def has( hTable, key ):
    """
    has: HashTable(K, V) K -> Boolean
    Return True iff hTable has an entry with the given key.
    """
    size = len(hTable.table)
    one = hTable.table[hash_function(key, size)]
    two = hTable.table[hash_function_two(key, size)]
    if (one and one.key == key) \
    or (two and two.key == key):
        return True
    return False

def put( hTable, key, value ):
    """
    put: HashTable(K, V) K V -> Boolean

    Using the given hash table, set the given key to the
    given value. If the key already exists, the given value
    will replace the previous one already in the table.
    If the table is full, an Exception is raised.
    """
    hash = hash_function(key, len(hTable.table))
    putRec(hTable, key, value, hash)

def putRec(hTable, key, value, hash):
    """
        Recursively moves everyone as necessary
        hTable = dict, hash table
        key = str, key to place
        value = object, value of key
        hash = int, hash code to place at
    """
    if not hTable.table[hash]:
        hTable.table[hash] = Entry(key, value)
        hTable.size += 1
        return
    elif hash_function_two(hTable.table[hash].key, len(hTable.table)) == hash:
        raise Exception("Could not seat everyone")
    temp = hTable.table[hash]
    hTable.table[hash] = Entry(key, value)
    putRec(hTable, temp.key, temp.value, hash_function_two(temp.key, len(hTable.table)))

def get(hTable, key):
    """
        Gets value of key
        hTable = dict, hash table
        key = str, key to find value for
        returns: object, value of key
    """
    return hTable.table[indexOf(hTable, key)].value

def indexOf(hTable, key):
    """
        Finds hash of key
        hTable = dict, hash table
        key = str, key to find hash of
        returns: int, hash of key
    """
    hash = hash_function(key, len(hTable.table))
    if hTable.table[hash].key == key:
        return hash
    hash = hash_function_two(key, len(hTable.table))
    if hTable.table[hash].key == key:
        return hash
    raise Exception("Hash table does not contain key.")
