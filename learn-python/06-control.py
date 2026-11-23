print('****************************************************************************************************')
print('control')
print('****************************************************************************************************')

fruits = ["apple", "banana", "cherry"]
for i, fruit in enumerate(fruits):
    print(i, fruit)


letters = ['a', 'b', 'c']
for letter in letters:
  print(letter)


for a in range(4):
  print(a)

# this is a nested list comprehension; equivalent of an embedded for loop that creates a list
# outer loop is - 'for row in matrix'; inner loop is - 'for number in row'
# prints [0, 1, 2, 3]
matrix = [[0,1], [2,3]]
flat_list = [number for row in matrix for number in row]
print(flat_list)

# prints 0, 1, 2, 3
i = 0
while i <= 3:
    print(i)
    i += 1

# prints Positive
x = 10
if x > 0:
    print('Positive')
elif x == 0:
    print('Zero')
else:
    print('Negative')
