print('****************************************************************************************************')
print('strings')
print('****************************************************************************************************')


# strings can be iterated like lists
  def is_palindrome(x: int) -> bool:
    s = str(x)
    length = len(s)
  
    for i in range(length // 2):
        if s[i] != s[length - 1 - i]:
            return False
  
    return True


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

