
password = ("Anarchy")
text1 = input("Please enter your password: ")
attempt = 0

while text1 != password:
    attempt += 1
    if attempt == 3:
        print("System locked!")
        break
    print("Wrong password. Try again!")
    text1 = input("Enter password: ")

if text1 == password:
    print("Code validation has been success, entering into system...")

