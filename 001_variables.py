num1 = 10
num2 = 20
num3 = 3.14
num4 = 32.3e18
num5 = .876j
print((num1 + num2) * num3)
num1 = 90   # changed variable
num1 = 6.15
#######################################################

# input - giving back the string type
num1 = input("Enter the value of 1st number: ")
num2 = input("Enter the value of 2nd number: ")
num3 = num1 + num2
print(num3)


# type conversion here
num1 = int(input("Enter the value of 1st number: "))
num2 = int(input("Enter the value of 2nd number: "))
num3 = num1 + num2
print(num3)
print(type(num3))   # giving back type of variables
#######################################################

# greetings
greeting = "Welcome, "
name = input("Please enter your name: ")
greetings_message = greeting + name + "...! "
print(greetings_message)


#######################################################

var = "Bobby's World"
print(var)
print(len(var))     # giving back the length of string
print(var[0])       # giving back the 0th char of string
print(var[0:5])     # giving back the first 5 char of string
print(var.lower())
print(var.upper())
print(var.count("b"))


#Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

'''
#Illegal variable names:
2myvar = "John"
my-var = "John"
my var = "John"
'''