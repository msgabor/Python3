# First product method.
# Takes two argument and print their product


def product(a, b):
    p = a * b
    print(p)


# Second product method
# Takes three argument and print their
# product
def product(a, b, c):
    p = a * b * c
    print("Result of function overloading:", p)


# Uncommenting the below line shows an error
# product(4, 5)

# This line will call the second product method
product(4, 5, 5)


'''Python does not supports method overloading.
We may overload the methods but can only use the latest defined method.'''