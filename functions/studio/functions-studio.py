# We want to COMPLETELY reverse a list by flipping the order of the entries AND flipping the order of characters in each element.

# a) Define a 'reverse_characters' function. Give it one parameter, which will be the string to reverse.
def reverse_characters(list_test1):
    return list_test1[::-1]
 
# b) Within the function, use the 'list' function to split a string into a list of individual characters
def reverse_characters(list_test1):
    char_list = list(list_test1)
    return list_test1[::-1] 

    

# c) 'reverse' your new list.
def reverse_characters(list_test1):
    char_list = list(list_test1)
    char_list[::-1]
    return list_test1
# d) Use 'join' to create the reversed string and return that string from the function.
def reverse_characters(list_text):
    char_list = list(list_text)
    char_list.reverse()
    reversed_string = "".join(char_list)
    return reversed_string

print(reverse_characters(list_test1))

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
# b) Loop through the old list.
# c) For each element in the old list, call reverse_characters to flip the characters or digits.
# d) Add the reversed string (or number) to the list defined in part ‘a’.
# e) Return the final, reversed list.
# f) Be sure to print the results from each test case in order to verify your code.
def new_function(old_list):
    new_list = []
    for element in old_list:
        reversed_element = reverse_characters(element)
        new_list.append(reversed_element)
    return new_list
print(new_function(list_test3))


list_test1 = ['apple', 'potato', 'Capitalized Words']
list_test2 = [123, 8897, 42, 1168, 8675309]
list_test3 = ['hello', 'world', 123, 'orange']


print(reverse_list_elements(list_test1))
print(reverse_list_elements(list_test2))
print(reverse_list_elements(list_test3))  