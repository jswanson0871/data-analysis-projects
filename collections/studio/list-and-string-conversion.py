proto_list1 = "3,6,9,12"
proto_list2 = "A;C;M;E"
proto_list3 = "space delimited string"
proto_list4 = "Comma-spaces, might, require, typing, caution"

strings = [proto_list1, proto_list2, proto_list3, proto_list4]

# a) Use the 'in' method to check to see if the words in each string are separated by commas (,), semicolons (;) or just spaces.
for s in strings:
    if ',' in s:
        print(f'"{s}" The words are separated by commas (,).')
    elif ';' in s:
        print(f'"{s}" The words are separated by semicolons (;).')
    elif ' ' in s:
        print(f'"{s}" The words are separated by spaces.')
    else:
        print(f'"{s}" No recognizable separators found.')

# b) If the string uses commas to separate the words, split it into an array, reverse the entries, and then join the array into a new comma separated string.
for s in strings:
    if ',' in s:
        words = s.split(',')
        words.reverse()
        new_s=','.join(words)
        print(f'Original: "{s}" -> Reversed: "{new_s}" The words are separated by commas (,).')
    elif ';' in s:
        print(f'"{s}" The words are separated by semicolons (;).')
    elif ' ' in s:
        print(f'"{s}" The words are separated by spaces.')
    else:
        print(f'"{s}" No recognizable separators found.')


# c) If the string uses semicolons to separate the words, split it into an array, alphabetize the entries, and then join the array into a new comma separated string.
for s in strings:
    if ',' in s:
        words = s.split(',')
        words.reverse()
        new_s=','.join(words)
        print(f'Original: "{s}" -> Reversed: "{new_s}" The words are separated by commas (,).')
    elif ';' in s:
        words = s.split(';')
        words.sort()
        new_s = ','.join(words)
        print(f'Original: "{s}" -> Alphabetized: "{new_s}" The words are separated by semicolons (;).')
    elif ' ' in s:
        print(f'"{s}" The words are separated by spaces.')
    else:
        print(f'"{s}" No recognizable separators found.')


# d) If the string uses spaces to separate the words, split it into an array, reverse alphabetize the entries, and then join the array into a new space separated string.
for s in strings:
    if ',' in s:
        words = s.split(',')
        words.reverse()
        new_s=','.join(words)
        print(f'Original: "{s}" -> Reversed: "{new_s}" The words are separated by commas (,).')
    elif ';' in s:
        words = s.split(';')
        words.sort()
        new_s = ','.join(words)
        print(f'Original: "{s}" -> Alphabetized: "{new_s}" The words are separated by semicolons (;).')
    elif ' ' in s:
        words = s.split(' ')
        words.sort(reverse=True)
        new_s = ' '.join(words)
        print(f'Original: "{s}" -> Reverse Alphabetized: "{new_s}" The words are separated by spaces.')
    else:
        print(f'"{s}" No recognizable separators found.')

# e) If the string uses ‘comma spaces’ to separate the list, modify your code to produce the same result as part “b”, making sure that the extra spaces are NOT part of the final string.
for s in strings:
    if ', ' in s:
        words = s.split(', ')
        words.reverse()
        new_s = ','.join(words)
        print(f'Original: "{s}" -> Reversed: "{new_s}" The words are separated by comma+space (, ).')
    elif ',' in s:
        words = s.split(',')
        words.reverse()
        new_s=','.join(words)
        print(f'Original: "{s}" -> Reversed: "{new_s}" The words are separated by commas (,).')
    elif ';' in s:
        words = s.split(';')
        words.sort()
        new_s = ','.join(words)
        print(f'Original: "{s}" -> Alphabetized: "{new_s}" The words are separated by semicolons (;).')
    elif ' ' in s:
        words = s.split(' ')
        words.sort(reverse=True)
        new_s = ' '.join(words)
        print(f'Original: "{s}" -> Reverse Alphabetized: "{new_s}" The words are separated by spaces.')
    else:
        print(f'"{s}" No recognizable separators found.')