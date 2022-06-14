# ordered, immutable, text representation

my_string = "Hello World"
print(my_string)

# Escape character '\'
my_string = 'I\'m a programmer'
print(my_string)

my_string = """Hello 
World"""
print(my_string)

# This will be single line output
my_string = """Hello \
World"""
print(my_string)

# Char extraction from string
char = my_string[1]
print(char)

# Substring
substring = my_string[1:5]
print(substring)

# Get every second character in elements
substring = my_string[::2]
print(substring)

# Reverse string
reverse = my_string[::-1]
print(reverse)

# strip()
my_string = "   Hello World   "
my_string = my_string.strip()
print(my_string)

# upper() & lower()
print(my_string.lower())
print(my_string.upper())

# startswith() & endwith()
print(my_string.endswith('World'))
print(my_string.startswith('Hello'))

# find(): If the searched character is found return index number, if not returns -1.
print(my_string.find('o'))
print(my_string.find('p'))

# count()
print(my_string.count('o'))

# replace
print(my_string.replace('World', 'Universe'))

# split(): You define any separator. By default is ' '.
my_string = 'How are you doing'
my_list = my_string.split(sep=' ')
print(my_list)

# join(): Concatenate list element as string
new_string = ' '.join(my_list)
print(new_string)

new_list = ['a'] * 1000000

from timeit import default_timer as timer

# bad concatenate method
start = timer()
new_string = ''
for i in new_list:
    new_string += i
stop = timer()
expensive_way = stop - start
print(expensive_way)

# best concatenate method
start = timer()
new_string = ''.join(new_list)
stop = timer()
better_way = stop - start
print(better_way)

print(expensive_way / better_way)

# String printing methods
# % method
var = 'Elvis'
my_string = 'The variable is %s' % var
print(my_string)

var = 7
my_string = 'The variable is %d' % var
print(my_string)

var = 3.1415926535897932384
my_string = 'The variable is %.3f' % var
print(my_string)

# .format() method
var = 'Elvis'
my_string = 'The variable is {}'.format(var)
print(my_string)

var = 3.1415926535897932384
var2 = 7
my_string = 'The variable is {:.2f} and {}'.format(var, var2)
print(my_string)

# f-String: A new feature that comes with Python 3.6
# It compiles at runtime, much faster and more convenient.
var = 3.1415926535897932384
var2 = 7
my_string = f'The variable is {var} and {var2}'
print(my_string)

my_string = f'The variable is {var} and {var2*3}'
print(my_string)