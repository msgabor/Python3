try:
    print(x)
except NameError as e:
    print("Something went wrong:", e)
except IndexError as e:
    pass
finally:
    print("The 'try except' is finished")

print("*******************************************************")

try:
    f = open("demofile.txt")
    f.write("Lorum Ipsum")
except NameError as e:
    pass
except FileNotFoundError as e:
    print("Something went wrong when writing to the file:", e)
finally:
    pass

