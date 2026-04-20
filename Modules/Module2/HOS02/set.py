# Sets in Python
# Using the set() Function
set1 = set([1, 2, 3, 4, 5])
print("Set of integers: ", set1)

# Using Curly Braces
mix_set = {1, 'hi', (1, 2, 3, 4)}
print("Set of mix data types: ", mix_set)

# Duplicate Elements in Set
dup_set = {1, 2, 2, 3, 3, 4, 5, 5}
print("Removed duplicates: ", dup_set)
# Add Set Items
# Adding elements using add()
language_set = {"C", "C++", "C#"}
print("Original set:", language_set)

language_set.add("Java")
print("Updated Set:", language_set)

# Adding using update()
language_set.update(["Python"])
print("Updated Set:", language_set)
# Joining Sets
language1 = {"C", "C++", "Java", "Python"}
language2 = {"PHP", "C#", "Perl"}

language1.update(language2)
print("Joined sets:", language1)
# Add Set Items Using Union Operator
lang1 = {"C", "C++", "Java", "Python"}
lang2 = {"PHP", "C#", "Perl"}
lang3 = {"SQL", "C#"}

combined_set1 = lang1.union(lang2)
combined_set2 = lang2 | lang3

print("Combined Set1:", combined_set1)
print("Combined Set2:", combined_set2)
# Combining a set and a list
lang_1 = {"C", "C++", "Java", "Python"}
lang_2 = ["PHP", "C#", "Perl"]

lang_3 = lang_1.union(lang_2)
print("Combined set and list:", lang_3)
# Checking if items exist in a set
language_set = {"C", "C++", "C#", "Java", "Python"}

if "Java" in language_set:
    print("Java is present in the set.")
else:
    print("Java is not present in the set.")

if "SQL" not in language_set:
    print("SQL is not present in the set.")
else:
    print("SQL is present in the set.")

# Checking subset
original_set = {1, 2, 3, 4, 5, 6, 7, 8}
is_subset = {5, 6}.issubset(original_set)
print("{5, 6} is a subset of the original set:", is_subset)

# Removing elements from a set
print("Before removing 3:", original_set)
original_set.remove(3)
print("After removing 3:", original_set)

print("Before removing 5:", original_set)
original_set.discard(5)
print("After removing 5:", original_set)
# Set Comprehension
set_1 = {x for x in range(1, 6)}
print("Set comprehension: ", set_1)

# Nested Set Comprehensions
nested_set = {(x, y) for x in range(1, 3) for y in range(1, 3)}
print("Nested set: ", nested_set)