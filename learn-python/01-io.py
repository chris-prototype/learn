print('io')
print('****************************************************************************************************')

# provides access to the file system among other things
import os

# list files in the current directory
files = os.listdir('.')
if files:
    print('In the current directory files[0] is: ' + files[0])

print('io-user')
print('****************************************************************************************************')

# user input
user = input('Enter your name: ')

# create two strings
word1 = 'Hello '
print(f"{word1}{user}")

