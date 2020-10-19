
for i in range(5):
    print("Gabe")

print("....................................")

range1 = range(15)
print(list(range1))                 # create a range from 0- to 15 and converted to a list[] - and print out

print("....................................")

# list created - for loop on length of list1
list1 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
for i in range(len(list1)):
    print(list1[i])

print("...........for each loop coming:.................")

# simple solution: for each
for i in list1:
    print(i)

print("........stop, when banana coming in the list:...............")

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break
print(".........jump over, when banana coming in he list:.................")

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

print("....................................")

for x in range(6):
    print(x)
else:
    print("Finally finished!")

print("....................................")

# Nested for loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)


print("........enumeration in list - how many items we have in the list ..........")
enum_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

for index, names in enumerate(enum_list):
    print(index, names)
