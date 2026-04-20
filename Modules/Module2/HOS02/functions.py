# Function to generate a list of numbers
def print_numbers(limit):
    """This prints a list of numbers starting 0 to the limit-1"""
    i = 0  # initialize
    numbers = []

    # Loop until limit
    while i < limit:
        numbers.append(i)
        i = i + 1  # increment

    return numbers  # return list


# User input
user_limit = int(input("Give a limit: "))
print(print_numbers(user_limit))
# Define a function called print_text
def print_text(str):
    """This prints a passed string into this function"""
    print(str)
    return


# Call the function
print_text("First call to the user-defined function.")
print_text("Second call to the same user-defined function.")