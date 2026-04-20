# Tuples as keys and strings as values
dict_1 = {
    ('Canada', 'Philippines', 'USA', 'Korea'): 'Countries',
    ('Ottawa', 'Manila', 'Washington, D.C.', 'Seoul'): 'Cities'
}
print(dict_1)

# Strings as keys and lists as values
dict_2 = {
    'Countries': ['Canada', 'Philippines', 'USA', 'Korea'],
    'Cities': ['Ottawa', 'Manila', 'Washington, D.C.', 'Seoul']
}
print(dict_2)

# Accessing values using keys
print("Cities: ", dict_2['Cities'], "\nCountries: ", dict_2['Countries'])

# Updating a value in the dictionary
dict_2['Cities'][1] = 'Cebu'
print("Updated Cities: ", dict_2['Cities'])

# Adding key:value pair
dict_2['Continent'] = ['North America', 'Asia', 'North America', 'Asia']
dict_2['Country Code'] = ['+1', '+63', '+1', '+82']
print("Updated dictionary: ", dict_2)

# Deleting using del
del dict_2['Country Code']
print("After del statement: ", dict_2)

# Using pop()
continent = dict_2.pop('Continent')
print("Continents: ", continent)
print("After pop method: ", dict_2)

# Compare Dictionaries
dict_A = {
    'Countries': ['Canada', 'USA'],
    'Cities': ['Ottawa', 'Washington, D.C.'],
    'Continent': ['North America', 'North America']
}

dict_B = {
    'Cities': ['Ottawa', 'Washington, D.C.'],
    'Continent': ['North America', 'North America'],
    'Countries': ['Canada', 'USA']
}

print(dict_A == dict_B)
dict_1 = {'Countries': ['Canada', 'USA'], 'Continent': ['North America', 'North America']}
dict_2 = {'Cities': ['Ottawa', 'Washington, D.C.']}

combined_dict = [dict_1, dict_2]

# Iterating through list of dictionaries
for item in combined_dict:
    for key, value in item.items():
        print("Key:", key, "\tValue:", value)
        # Using the key to get highest value
gpa = {
    'Apple': 3.905,
    'Brian': 3.911,
    'Charles': 3.899,
    'Diane': 3.989,
    'Edmund': 3.998
}

highest = max(gpa, key=gpa.get)
print(highest + ' has the highest gpa with a score of ' + str(gpa[highest]))
