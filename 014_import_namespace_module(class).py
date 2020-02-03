import math
from math import sin, cos
print(sin(4))
print(cos(3))

print("............................................")

import FirstClass
FirstClass.call_function_from_another_file()  # calling function from another file --> namespace = another class/module
print(FirstClass.color)
print(FirstClass.names)

print("............................................")

import FirstClass as something                # --> if module are in another folder, can give alias name
print(something.color)
print(something.names)

from FirstClass import Class                    # import just the Class from another module = now is empty Class
o = Class()

print("............................................")

import datetime
x = datetime.datetime.now()
print(x)
