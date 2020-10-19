print(".....break.........")
for i in range(10):
    if i == 6:
        break
    print(i)

print("........................")

num = 0
while True:
    print(num)
    num += 1
    if num == 5:
        break

print(".........................")

number = 0
while True:
    number += 1
    if number % 2 == 1:
        continue
    print(number)
    if number > 20:
        break