
password = ("Anarchy")
ask_password = input("Please enter your password: ")
nr_of_attempts = 0

while ask_password != password:             # while password not equal with the contained password
    nr_of_attempts += 1                            #increase the nr of attempt
    if nr_of_attempts == 3:
        print("System locked!")
        break
    print("Wrong password. Try again!")
    ask_password = input("Enter your password again: ")

if ask_password == password:
    print("Code validation has been success, entering into the system...")



