string1 = 'This dog is "awesome"!'
print("Quotes:", string1)
print("......................................................................................")
string2 = "My girlfriend is Ivett and she is 30 years old."
print("Original string literal:", string2)
string3 = string2.replace("Ivett", "Kitty"). replace("30", "27") + "..and really love her."
print("Manipulated string (replacements):", string3)
print("......................................................................................")
print("Lengths:", len(string3), "characters.")
print("Is string started with 'My'? = ", string2.startswith("My"))
print("Is string started with 'Him'? = ", string2.endswith("Him"))
print("Sliced original string:", string2[-3:], "from 'old' words!")
print("......................................................................................")
string4 = "Gabe"
string5 = "'The brave'"
string6a = string4 + string5
string6b = string4*5
print("Concatenated string:", string6a)
print("Concatenated string:", string6b)
print("......................................................................................")
string7 = "                 Tomorrow I will drink a beer!            "
print(string7.lstrip())
print(string7.rstrip())
print(string7.strip())  # remove whitespaces
print("......................................................................................")
string8 = "0,1,2,3,4,5,6"
print("Original string:", string8)
string9 = string8.split(",")
print("Splitted string", string9)
print("......................................................................................")
string10 = "Budapest"
print("Age:", 35, "City:", string10)
print("......................................................................................")
string11 = "Gabriel"
string12 = "shit"
print(f"It is {string11}'s {string12} 1st workday!")   # F string
print("I really like to write {a} code.".format(a="Python"))
print("......................................................................................")
string13 = "Gabri\tel"
string14 = "Gabri\\el"
print("TAB in string: ", string13)
print("Backslash in string: ", string14)
print("......................................................................................")
a = 5
b = 10j
string15 = str(a+b)
print("Concatenate 2 integers to string:", string15)
print("......................................................................................")
# STRING functions
string16 = "Gabe is the real brave in 1985."
string17 = string16.lower()
string18 = string16.upper()
string19 = string16.isdigit()   # scanning all char of strings
string20 = string16.isalpha()
string16.isspace()
string16.startswith("G")
string16.endswith("B")
print("Upper & lower case:", string17, "++", string18)
print("is digit:", string19, "++", "Is alphabetic:", string20)
print("......................................................................................")
string21 = "homeowner"
print("Find function:", string21.find("meow"))
string22 = string21.replace("home", "mor")
print("Replace:", string22)
print("......................................................................................")
string23 = "Hey" is "Hi"
string24 = "Hey" is not "Hi"
string25 = "Hey" is "Hey"
string26 = "Hey" in "Heyyyyehujja"
string27 = "Hey" is not "Hello"
print('Comparison: "Hey" is equal to "Hi"?', string23)
print('Comparison: "Hey" is not equal to "Hi"?', string24)
print('Comparison: "Hey" is equal to "Hi"?', string25)
print('Comparison: "Hey" is in "Heyyyyyehujja"?', string26)
print('Comparison: "Hey" is not in "Hello"?', string27)
print("......................................................................................")
