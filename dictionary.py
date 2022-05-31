# Create dictionary on 2 different way.
mydict = {"name": "Max", "age": 28, "city": "New York"}
print(mydict)
mydict2 = dict(name="Mary", age=27, city="Boston")
print(mydict2)

# Get data by key
value = mydict["name"]
print(value)

# Add new value with key
mydict["email"] = "max@xyz.com"
print(mydict)

# If you want to add another value for same key, it will overwrite.
mydict["email"] = "coolmax@xyz.com"
print(mydict)

# Delete value by key
del mydict["name"]
# mydict.pop("name") another option for delete value by the key
print(mydict)

# Remove the last value. 
# Note: This function runs for Python 3.7 and higher version.
mydict.popitem()
print(mydict)

# Is there specific key in dictionary
# Option 1
if "name" in mydict2:
    print(mydict2["name"])

# Option 2
try:
    print(mydict2["name"])
except:
    print("Error")

# Navigating the key and value in dictionary
for key, value in mydict2.items():
    print(key, value)

# Copy dictionary
# Wrong way!
mydict_copy = mydict2
print(mydict_copy)
print(mydict2)

# Both will be change, because both dictionary point to same memory.
mydict_copy["email"] = "abc@xyz.com"
print(mydict2)
print(mydict_copy)

# Correct ways!
mydict_copy = mydict2.copy()
mydict_copy = dict(mydict2)

# Merge 2 dictionary
# They may be has different key but doesn't matter, they will be merge
mydict = {"name": "Max", "age": 28, "email": "hw@xyz.com"}
mydict2 = dict(name="Mary", age=27, city="Boston")

mydict.update(mydict2)
print(mydict)

# Numbers can be key
mydict = {3: 9, 4: 16, 5: 25, 6: 36}
print(mydict)

value = mydict[3]
print(value)

# Also tuples can be key but list can't be key because lists are changeable data types.
mytuple = (8,7)
mydict = {mytuple: 15}
print(mydict)




