reading_file = open("read.txt", "r", encoding="UTF-8")
# print(reading_file.read())            # read all docs
# print(reading_file.readline())        # read only line by line

for i in reading_file:
    print(i.strip())

line1st = reading_file.readline()
while line1st:
    print(line1st.strip())
    line1st = reading_file.readline()

reading_file.close()

# another option - context manager, closing automate method the file
with open("read.txt", "r", encoding="UTF-8") as file:
    for i in file:
        print(line1st.strip())

# read only parts of some file
# f = open("read.txt", "r")
# print(f.read(5))

# writing out
with open("write.txt", "w") as file:
    append_text = ("writing into file....")
    file.write(append_text)

# copy files

with open("read.txt", "r", encoding="UTF-(8") as infile:
    with open ("101_copy_file.txt", "w", encoding="UTF-8") as outfile:
        line = infile.readline()

        while line:
            outfile.write(line)
            line = infile.readline()


# append new line
with open("101_copy_file.txt", "a", encoding="UTF-(8") as file:
    newline = "\nAdd new line for testing!"
    file.write(newline)



# delete files
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")

os.rmdir("myfolder")        # delete folder
