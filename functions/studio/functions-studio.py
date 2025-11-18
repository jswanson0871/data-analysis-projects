# We want to COMPLETELY reverse a list by flipping the order of the entries AND flipping the order of characters in each element.

# a) Define a 'reverse_characters' function. Give it one parameter, which will be the string to reverse.
def reverse_characters(s):
    """
    Reverses the characters in a string.
    
    Parameters:
    s (str): The string to reverse.
    
    Returns:
    str: The reversed string.
    """
    return s[::-1]
# b) Within the function, use the 'list' function to split a string into a list of individual characters
    def reverse_characters(s):
    split = list(s)
    return split
# c) 'reverse' your new list.
    list_test1 = ['apple', 'potato', 'Capitalized Words']

def reverse_characters(s):
    return s[::-1]

reverse_list = reverse_characters(list_test1)

print(reverse_list)
# d) Use 'join' to create the reversed string and return that string from the function.
def reverse_characters(lst):
    reversed_string = ', '.join([s[::-1] for s in lst])
    return reversed_string
# e) Create a variable of type string to test your new function. # f) Use 'print(reverse_characters(my_variable_name))'; to call the function and verify that it correctly reverses the characters in the string.
 list_test1 = ['apple', 'potato', 'Capitalized Words']

def reverse_characters(lst):
    reversed_strings = [s[::-1] for s in lst]
    return reversed_strings

reverse_list = reverse_characters(list_test1)
# g) Use method chaining to reduce the lines of code within the function.
def reverse_characters_list(lst):
    return [s[::-1] for s in lst]
print(reverse_characters_list(list_test1))

# 2) The 'split' method does not work on numbers, but we want the function to return a number with all the digits reversed (e.g. 1234 converts to 4321 and NOT the string "4321")
def reverse_characters(i):
    return int(str(i)[::-1])
print(reverse_characters(1234))
# a) Add an if statement to your reverse_characters function to check the typeof the parameter.
def reverse_characters(i):
    if isinstance(i, int):
        return int(str(i)[::-1])
    else:
        return "ERROR: TRY AGAIN"

print(reverse_characters(1234))
# b - d) If type is ‘string’, return the reversed string as before. If type is ‘number’, convert the parameter to a string, reverse the characters, then convert it back into a number. Return the reversed number.
def reverse_characters(i):
    if isinstance(i, str):
        return i[::-1]  
    elif isinstance(i, int):
        return int(str(i)[::-1]) 
    else:
        return "ERROR: TRY AGAIN"
# e) Be sure to print the result returned by the function to verify that your code works for both strings and numbers. Do this before moving on to the next steps.

# 3) Create a new function with one parameter, which is the list we want to change. The function should:
# a) Define and initialize an empty list.
list_test4 = []
# b) Loop through the old list.
for old_list in list_test4
print(list_test4)
# c) For each element in the old list, call reverse_characters to flip the characters or digits.
# d) Add the reversed string (or number) to the list defined in part ‘a’.
# e) Return the final, reversed list.
# f) Be sure to print the results from each test case in order to verify your code.



list_test1 = ['apple', 'potato', 'Capitalized Words']
list_test2 = [123, 8897, 42, 1168, 8675309]
list_test3 = ['hello', 'world', 123, 'orange']
