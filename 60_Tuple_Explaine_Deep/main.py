


"""

Add Items
Once a tuple is created, you cannot add items to it. 
Tuples are unchangeable.


"""

"""
thistuple = ("apple", "banana", "cherry")
thistuple[3] = "orange" # This will raise an error
print(thistuple)
"""


"""
Remove Items
Note: You cannot remove items in a tuple.

Tuples are unchangeable, so you cannot remove items from it, 
but you can delete the tuple completely:
 

"""

thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists
