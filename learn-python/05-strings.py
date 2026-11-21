print('****************************************************************************************************')
print('strings')
print('****************************************************************************************************')

# a formatted or f string
name = 'Joe'
age = 50
print(f'My name is {name} and I am {age} years old.')

# common string methods - upper, lower, capitalize
food = 'avocado'
print(food.upper())
print(food.lower())
print(food.capitalize())

# common string methods - split
# splits a string into a list
a = 'a, b, c'
b = a.split()

print(b) # ['a', 'b', 'c']

# replace characters in a string
c = a.replace('a', 'z') # z, b, c
print(c)

