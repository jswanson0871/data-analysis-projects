my_string = "LaunchCode"


# a) Use string methods to remove the first three characters from the string and add them to the end.
s = "LaunchCode"
modified = s[3:] + s[:3]
print({modified})

# Use a template literal to print the original and modified string in a descriptive phrase.
s = "LaunchCode"
modified = s[3:] + s[:3]
print(f'The original string is "{s}", and the modified string is "{modified}".')


# b) Modify your code to accept user input. Query the user to enter the number of letters that will be relocated.
s = input("Launchcode")
n = int(input("enter in number for relocation"))
modified = s[n:] + s[:n]
print (f"{modified}")

# c) Add validation to your code to deal with user inputs that are longer than the word. In such cases, default to moving 3 characters. Also, the template literal should note the error.
s = input("Launchcode")
n = int(input("enter in number for relocation"))
if n > len(s):
    print(f'Error: "{n}" exceeds the number of characters in the word "{s}". Defaulting to 3.')
    n = 3
modified = s[n:] + s[:n]
print (f"{modified}")