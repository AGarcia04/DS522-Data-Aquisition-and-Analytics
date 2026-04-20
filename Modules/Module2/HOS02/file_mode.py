with open('hello.txt', 'a') as file:  # "a" for append mode
    file.write('\nThis is a new content I just appended')

with open('new.txt', 'w') as new_file:  # "w" for write mode
    new_file.write('This is a new file')

# Reading the existing file
with open('hello.txt') as file:
    texts = file.read()
print(texts.rstrip())

# Reading the new file
with open('new.txt') as file:
    texts = file.read()
print(texts.rstrip())