# Sets: unordered, mutable, unique values

# Create set
# Option 1
myset = {1, 2, 3, 4, 1, 3}
print(myset)

# Option 2
myset2 = set("Hello")
print(myset2)

# Create empty set
myset = set()

# Add elements 
myset.add(1)
myset.add(2)
myset.add(3)
print(myset)

# Remove elements
# Option 1: If you want to delete elements you must delete by values otherwise you will get error.
myset.remove(3)
print(myset)

# Option 2 (No Error): Again, you can delete the elements according to their values, but if you try to delete a value that is not in the set, you will not get an error.
myset.discard(3) # Normally we don't have 3 values but we did not got error.
print(myset)

# Delete all elements
myset.clear()
print(myset)

# Get the first item in the set and subtracts it from the set.
myset = {1, 2, 3, 4, 1, 3}
print(myset.pop())
print(myset)

# Iterations with loops
for i in myset:
    print(i)

# Union / Intersection
odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

u = odds.union(evens)
print(u)

i = odds.intersection(primes)
print(i)

# Difference 
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

diff = setA.difference(setB)
print(diff)

# Symmetric difference: Just hold unique values on the lists. It will delete same value and join different values.
s_diff = setA.symmetric_difference(setB)
print(s_diff)

# Combining 2 sets
setA.update(setB) 
print(setA)

# Get only values ​​in both sets.
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

setA.intersection_update(setB)
print(setA)
