# conditional statements
age = 17

if age < 18:
    if age >= 16:   # nested conditional
        print("Little party, never killed nobody!")
    else:
        print("No party!")
elif age >= 18 and age < 30:            #more conditions
    print("Go to party!")
elif age > 30 and age < 65:
    print("Go to family.")
else:
    print("Be a good pensioner:D")