
# LIST[] - is a collection which is ordered and changeable. Allows duplicate members. - mutable/able to modification
# TUPLE() - is a collection which is ordered and unchangeable. Allows duplicate members.
# Set - is a collection which is unordered and unindexed. No duplicate members.
# Dictionary{} - is a collection which is unordered, changeable and indexed. No duplicate members

#############################################################################
list1 = []
list1.append(100)   # append - add item
list1.append(200)
list1.append(300)
list1.append("Gabor")
list1.append("Csirke")
# list1.remove("")
# list1.clear() - delete all item from array
list1.insert(1, "Lacika")   # 2nd position insert string
print(list1)
list1.reverse()
print(list1)
#############################################################################
list2 = [15, 8, 78, 23, 1, 65, 184]
list2.sort()    # ascending sorting (only numbers or strings in array list)
print(list2)
#############################################################################
list3 = ["Xena", "Lacika", "Enikő", "Csirke"]
# list3.sort()
print(list3)
print(len(list3))
# indexing
print(list3[0])     # 0th  item indexing 0,1,2,3,4 etc
print(list3[-1])
# slicing array list
print(list3[0:2])   # does not contains 3rd items, not inclusive
print(list3[2:4])
#############################################################################
# multi dimension lists
list4 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(list4)
print(list4[0])     # get 1 st list all items
print(list4[2][0])  # get back from 3rd list the 0th items
#############################################################################
range1 = range(50)
print(list(range1))     # cast to list the range 0-50 (not inclusive - 0-49)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist)
print(thislist[2:5])
print(thislist[:4])
print(thislist[2:])
print(thislist[-4:-1])
thislist[1] = "blackcurrant"    # add new item into array list
print(thislist)
print(len(thislist))
thislist.append("orange")
print(thislist)
thislist.insert(1, "orange")
print(thislist)
# thislist.remove("banana")
print(thislist)
thislist.pop()
print(thislist)
# del thislist[0]
# del thislist
# thislist.clear()
# print(thislist)
# COPY
mylist = thislist.copy()
print(mylist)
mylist = list(thislist)
print(mylist)
#############################################################################
# JOIN/MERGE
list7 = ["a", "b", "c"]
list8 = str[1, 2, 3]
list9 = list7 + list8
print(list9)
#############################################################################
# NEW PRACTICE
create_list1 = []
create_list1.append("Gabe")
create_list1.insert(5, "Lacika")   # 5th. position insert string
create_list1.append(100)
create_list2 = [10, 20, 30]
create_list2.clear()
print("First list:", create_list1)
print("Second list:", create_list2)

print("........................................")

# COPY
old_list = [100, 200]
new_list = old_list
new_list.append("Gabe")

print("Old list:", old_list)
print("New list", new_list)

print("........................................")

# mixed list
list_copy = ['cat', 0, 6.7]
# copying a list
new_list = list_copy.copy()
# Adding element to the new list, and remove
new_list.append('dog')
new_list.remove("cat")
count = new_list.count(6.7)
print("Which element is 6.7 in this list? ", count)
print(new_list)

print("........................................")

# Inserting a Tuple (as an Element) to the List
mixed_list = [{1, 2}, [5, 6, 7]]
# number tuple
number_tuple = (3, 4)
# inserting tuple to the list
mixed_list.insert(1, number_tuple)
print('Updated List: ', mixed_list)

print("........................................")

# programming languages list
languages = ['Python', 'Java', 'C++', 'French', 'C']
# remove and return the 4th item
return_value = languages.pop(3)     # popping the indexed item from list = French is not a programming language
print('Return Value:', return_value)
# Updated List
print('Updated List:', languages)
languages.reverse()
print("Reversed list: ", languages)

print("........................................")
list3 = ["Xena", "Lacika", "Enikő", "Csirke"]
print("This is original list:", list3)
list3.sort()
print("THis is the sorted list", list3)
print("This is the length list: ", len(list3))

print("........................................")

# language list - Using extend() Method
language = ['French', 'English', 'German']
# another list of language
language1 = ['Spanish', 'Portuguese']
language.extend(language1)
# Extended List
print("1st list:", language)
print("2ns list:", language1)
print("Final extended list:", language)

# JOIN/MERGE
list7 = ["a", "b", "c"]
list8 = ["d", "e", "f"]
list9 = list7 + list8
print("Merged 2 list:", list9)