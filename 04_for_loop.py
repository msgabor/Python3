# well defined how many times want to loop
for i in range(5):
    print("Gabe")
range1 = range(35)
print(list(range1))

# list created - for loop on length of list1
list1 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
for i in range(len(list1)):
    print(list1[i])

# simple solution: for each
for i in list1:
    print(i)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

for x in range(6):
    print(x)
else:
    print("Finally finished!")

# Nested for loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)

for x in [0, 1, 2]:
    pass


print("........enumeration..........")
enum_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
for index, names in enumerate(enum_list):
    print(index, names)
