mylist = ["cherry", "apple", "banana"]
print(mylist)

# Delete last element
item = mylist.pop() 

# Delete element by name
mylist.remove("cherry") 

# Delete all elements
item = mylist.clear() 

mylist=[1, 2, 3, 4, 5, 6, 7, 8, 9]

# Reverse the list
item = mylist.reverse()

# Sort the list
item = mylist.sort()

# Get all third item on list
item = mylist[::3] 
print(item)
print(mylist)

# Copy the list
# Option 1
copy = mylist[:] # second option mylist.copy() third option list(mylist) 
# Option 2
copy = mylist.copy() 
# Option 3
copy = list(mylist) 

# Tuples
mytuple=(0,1,2,3,4)

# Getting data with fewer variables than the number of elements
i1, *i2, i3 = mytuple
print(i1)
print(i2) # it's has all elements between i1 and i3 values.
print(i3)

# Size different list and tuples. Tuples is better for memory
import sys
mylist = [1,2,3,"hello",True]
mytuple = (1,2,3,"hello",True)
print(sys.getsizeof(mylist), "bytes")
print(sys.getsizeof(mytuple), "bytes")

# Performance create list and tuples 1000000 times. Tuple is better choice for productivity.
import timeit
print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1000000))
print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=1000000))