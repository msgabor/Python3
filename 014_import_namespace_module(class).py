import math
from math import sin, cos

print(sin(4))
print(cos(3))

print("............................................")

import FirstClass
import FirstClass as something
from FirstClass import Class
o = Class()

FirstClass.call_function_from_another_file()

print(FirstClass.color)
print(FirstClass.names)
print("............................................")
print(something.color)
print(something.names)


import datetime

x = datetime.datetime.now()

print(x)
