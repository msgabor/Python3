def my_first_functions():
    print("Have been defined 1st function..")


my_first_functions()  # called previously defined function

print("........................................")


def my_function1(fullname):  # can add as many arguments as you want, just separate them with a comma
    print(fullname + " Torwalds")


my_function1("Emil")
my_function1("Tobias")
my_function1("Linus")


def my_function2(fname, lname):
    print(fname + " " + lname)


my_function2("Emil", "Reese")


def my_function3(*kids):
    print("The youngest child is " + kids[2])


my_function3("Emil", "Tobias", "Linus")


def my_function4(child3, child2, child1):
    print("The youngest child is " + child2)


my_function4(child1="Emil", child2="Tobias", child3="Linus")


def my_function5(**kid):
    print("His last name is " + kid["lname"])


my_function5(fname="Tobias", lname="Refsnes")


def my_function6(country="Norway"):
    print("I am from " + country)


my_function6("Sweden")
my_function6("India")
my_function6()
my_function6("Brazil")


def my_function7(food):
    for x in food:
        print(x)


fruits = ["apple", "banana", "cherry"]

my_function7(fruits)


def my_function8(x):
    return 5 * x


print(my_function8(3))
print(my_function8(5))
print(my_function8(9))


def tri_recursion(k):
    if (k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


print("\n\nRecursion Example Results")
tri_recursion(6)

'''Parameters or Arguments?
The terms parameter and argument can be used for the same thing: information that are passed into a function.

From a function's perspective:
A parameter is the variable listed inside the parentheses in the function definition.
An argument is the value that are sent to the function when it is called.'''

names1 = ["Gabe, Leslie, Cube, Sausage"]
names2 = ["Isabelle, Timon, Carol"]

def name_printer(name_list):
    for names in name_list:
        print(names)


name_printer(names1)
name_printer(names2)

num1 = 10
num2 = 20

print("..............................................")
def summarize1():
    print(num1 + num2)


def summarize2(num1, num2, num3 = 4):
    return num1 + num2 + num3


def summarize3(* args):
    return sum(args)


summarize1()

print("..............................................")

result = summarize2(45, 25)
print(result)

print("..............................................")

summarize3()
print(summarize3(100, 20, 20, 30, 40, 450))
