reading_file = open("read.txt", "r", encoding="UTF-8")
# print(reading_file.read())            # read all docs
# print(reading_file.readline())        # read only line by line

# with for loop
for lines in reading_file:
    print(lines.strip())

# with while loop
line1st = reading_file.readline()
while line1st:
    print(line1st.strip())
    line1st = reading_file.readline()

reading_file.close()

print("********************************************************************")

# another option - context manager, closing automate method the file
with open("read.txt", "r", encoding="UTF-8") as file:
    for i in file:
        print(line1st.strip())
print("********************************************************************")
# read only parts of some file
# f = open("read.txt", "r")
# print(f.read(5))
print("********************************************************************")
# writing out
with open("write.txt", "w", encoding="UTF-8") as file:
    append_text = ("writing into file....")
    append_text = ("ez egy kibaszott teszt a fileba iratáshoz.....")
    file.write(append_text)
with open("write.txt", "r", encoding="UTF-8") as file:  # itt olvasom vissza h mit irtam bele
    for written_lines in file:
        print("It has been written into .txt:", written_lines.strip())

print("********************************************************************")

# copy files

with open("read.txt", "r",
          encoding="UTF-(8") as infile:  # open read.txt mint bemenő fiel, ebből olvasa ki amit másolunk
    with open("copied_files.txt", "w", encoding="UTF-8") as outfile:  # ebbe a fileba másoljuk át
        lines_for_copy = infile.readline()

        while lines_for_copy:
            outfile.write(lines_for_copy)
            lines_for_copy = infile.readline()
            print("Lines has been copied from infile to outfile.")
print("********************************************************************")

# TEST - PRACTICE
with open("infile_for_copy.txt", "r", encoding="UTF-8") as infile:
    with open("practice_text.txt", "w", encoding="UTF-8") as outfile:
        sorok = infile.readline()

        while sorok:
            print("File contains these lines:", sorok)
            outfile.write(sorok)
            sorok = infile.readline()
            print("All lines has been copied.")

print("********************************************************************")

# append new line - hozzáfűzés
with open("append_file.txt", "a", encoding="UTF-(8") as file:
    newline_append1 = "\nAdd new line for testing!"
    newline_append2 = "\nThis is an appended line to testfile...."
    file.write(newline_append1)
    file.write(newline_append2)
    print("Lines has been appended to textfiles.")

print("********************************************************************")

'''
# delete files
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")

os.rmdir("myfolder")        # delete folder
'''

# reading txt file and converting into list

with open("cars.txt", "r") as file:
    for read_cars in file:
        print(read_cars.strip())

        list_cars = [read_cars]  # moved into list from txt
        print("Moved into list:", list_cars)
