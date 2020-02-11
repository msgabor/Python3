# Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

fname = input("Enter file name: ")
filehandle = open(fname)

senders = list()
count = dict()

for row in filehandle:
    if row.startswith('From '):
        line = row.split()
        senders.append(line[1])
for sender in senders:
    count[sender] = count.get(sender, 0)+1

bigcount = None
bigsender = None

for sender, count in count.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bigsender = sender

print(bigsender, bigcount)
