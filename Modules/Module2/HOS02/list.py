empty_list = []
print(empty_list)

# creating a list with strings
str_list = ["alpha", "bravo", "charlie"]

# creating a list with integers
int_list = [0, 1, 2, 3, 4, 5]

# Access Elements
print(str_list[2])        # access the 3rd element (index 2)
print(int_list[0:2])      # elements from index 0 to 1 (2 is excluded)
print(str_list[-1])       # last element
print(int_list[::-1])     # reverse list

# Updating values in a list
print(f"Original value at index 1: {str_list[1]}")
str_list[1] = 'beta'
print(f"Updated value at index 1: {str_list[1]}")

# Adding Elements:

# Append method
str_list.append('delta')  # appending a single element
print(str_list)

str_list.append(['echo', 'foxtrot'])  # appending a list as a single element
print(str_list)

# Insert method
str_list.insert(1, 'bravo')
print(str_list)

# Extend method
str_list.extend(('golf', 'hotel',  'india'))
print(str_list)

# Extend more with intlist
str_list.extend(int_list)
print(str_list)

# Join Lists
# Using concat operator
str_list_1 = ['Juliett', 'Kilo', 'Lima']
str_list_2 = list(('Mike', 'November')) # Converting tuple to a list
joined_str_list = str_list + str_list_1 + str_list_2
print(f"Joined List: {joined_str_list}")

# Using list comprehension
joined_list = [item for sublist in [str_list_1, str_list_2] for item in sublist]
print(f"Another joined list: {joined_list}")

# pop method
last_1 = str_list.pop()  # no argument
print(f"After popping without arguments: {str_list}")
print(f"Popped item: {last_1}")

# This will not return or print the popped item since we did not store it
str_list.pop(-1)  # removes last item
print(f"After popping of item in last index: {str_list}")

zero = str_list.pop(8)  # remove element at index 8
print(f"After popping 0: {str_list}")
print(f"Popped item: {zero}")

# Removing Elements
# remove method
str_list.remove('beta')
print(f"After removing 'beta': {str_list}")

print(f"After clearing the int_list: {int_list}")

# del keyword
del str_list[4]
print(f"After deleting index 4 item: {str_list}")

[print(i) for i in str_list]

# Sorted Function
int_list_1 = [10, 1, 8, 20, 15, 6, 47]

print("Unsorted list: ", int_list_1)

sorted_list = sorted(int_list_1)

print("Sorted list: ", sorted_list)

# Reverse
sorted_list.reverse()
print("Reersed list: ", sorted_list)

