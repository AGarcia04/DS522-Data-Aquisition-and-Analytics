"""
DS 522 - Programming Exercise 02
Part 2: Possible Combinations

Question: Real-world use case of generating combinations.
A practical example is menu planning given a set of proteins and a set of sides,
all possible meal combinations can be generated to build a full restaurant menu.
Another use is in logistics: combining delivery stops to find the optimal route.
"""

import itertools

# Define two sets
set_a = {1, 2, 3}
set_b = {"A", "B", "C"}

list_a = sorted(set_a)
list_b = sorted(set_b)

print("Set A:", set_a)
print("Set B:", set_b)

# Combinations within each set (choose 2)
print("\n=== Combinations within Set A (r=2) ===")
for combo in itertools.combinations(list_a, 2):
    print(" ", combo)

print("\n=== Combinations within Set B (r=2) ===")
for combo in itertools.combinations(list_b, 2):
    print(" ", combo)

# Cartesian product of both sets
print("\n=== Cartesian Product: Set A × Set B ===")
for pair in itertools.product(list_a, list_b):
    print(" ", pair)

# All permutations of Set A
print("\n=== All Permutations of Set A ===")
for perm in itertools.permutations(list_a):
    print(" ", perm)