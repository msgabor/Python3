# tuples - unchangeable
this_tuple = ("apple", "banana", "cherry")
print(this_tuple)
print(this_tuple[-4:-1])
print("....................................")
this_tuple = ("apple", "banana", "cherry")

for x in this_tuple:
    print(x)
print(len(this_tuple))
print("....................................")

# JOIN 2 tuples
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)
print("....................................")

# SETS
set1 = {"apple", "banana", "cherry"}
print(set1)

set1 = {"apple", "banana", "cherry"}
set1.add("orange")
print(set1)
print("....................................")

# DICTIONARIES
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)

x = thisdict.get("model")
print("....................................")

# change values
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["year"] = 2018

if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")


# Nested Dictionaries
myfamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}
'''
clear()     Removes all the elements from the dictionary
copy()	    Returns a copy of the dictionary
fromkeys()  Returns a dictionary with the specified keys and values
get()	    Returns the value of the specified key
items()	    Returns a list containing a tuple for each key value pair
keys()	    Returns a list containing the dictionary's keys
pop()	    Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary
'''
