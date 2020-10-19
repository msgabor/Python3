

name_age = {"Gabe": 34,
            "Leslie": 34,
            "George": 33}

for key in name_age.keys():
    print("This is the dict key-value pair 'key':", key)
print("....................................")
for value in name_age.values():
    print("This is the dict key-value pair 'value':", value)
print("....................................")
for key, value in name_age.items():
    print("This is the dict key-value pair 'key + value':", key, value)

dict1 = {"data1": [1, 2, 3, 4], "data2": 78, "data3": (5, 6, 7, 8)}
# nested dictionary with an tuples merged
