#!/usr/bin/env python

# list exapmles

import os
import copy

clearscreen= lambda: os.system('cls')

clearscreen()

alist=[123, 'abc', 'hello', 22.2]

print('length of list' , len(alist))

# list.append(x)    Add an item to the end of the list. Equivalent to a[len(a):] = [x].
print("List before append method", alist)
alist.append('world!')
print(alist)
print('Length of list after append', len(alist))

# list.extend(iterable) Extend the list by appending all the items from the iterable. Equivalent to a[len(a):] = iterable.
print("List before append method", alist)
alist.extend([234, 'Robo'])
print(alist)

# list.insert(i, x)    Insert an item at a given position. The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).

print('Lsit before insert', alist)
alist.insert(7,'divya')
print(alist)

# list.remove(x)    Remove the first item from the list whose value is x. It is an error if there is no such item.

print('list and length of list before remove' , alist, len(alist))
alist.remove('divya')
print('list and length of list after remove ', alist, len(alist))

# list.pop([i])    Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list. (The square brackets around the i in the method signature denote that the parameter is optional, not that you should type square brackets at that position. You will see this notation frequently in the Python Library Reference.)

# list.pop with given position

print('list and length of list before pop' , alist, len(alist))
alist.pop(5)
print('list and length of list after pop ', alist, len(alist))

# list.pop without position

print('list and length of list before pop' , alist, len(alist))
alist.pop()
print('list and length of list after pop ', alist, len(alist))

#. list.clear()    Remove all items from the list. Equivalent to del a[:].

print('list and length of list before clear' , alist, len(alist))
#alist.clear() list.clear was added in Python 3.3.
del alist[:]
print('list and length of list after clear ', alist, len(alist))

alist.extend([123, 'abc', 'hello', 22.2, 123, 'hello'])
print(alist)

#. list.index(x[, start[, end]])    Return zero-based index in the list of the first item whose value is x. Raises a ValueError if there is no such item.    The optional arguments start and end are interpreted as in the slice notation and are used to limit the search to a particular subsequence of the list. The returned index is computed relative to the beginning of the full sequence rather than the start argument.
# only start value is considered and end will be excluded

print(alist.index(123,0,4))
print(alist.index('hello')) # will display first matching position

#. list.count(x)    Return the number of times x appears in the list.

print(alist.count('hello'))
print(alist.count(122))

#. list.reverse()    Reverse the elements of the list in place.

alist.reverse()
print("list after reverse", alist)

#. list.copy()    Return a shallow copy of the list. Equivalent to a[:].

copiedlist=copy.copy(alist)
print(copiedlist)

#. list.sort(key=None, reverse=False)    Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).

alist.sort()
print(alist)





