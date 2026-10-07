# For each of these string methods, run the code and work out what they do!
# add a comment using # to each one to explain what it does

user_string = input("Enter a string: ")

print(f"\nOriginal String: {user_string}")
print(f"Modified String 1: {user_string.lower()}")
# converts all characters in the string to lowercase
print(f"Modified String 2: {user_string.upper()}")
# converts all characters in the string to uppercase
print(f"Modified String 3: {user_string.strip()}")
# removes leading and trailing whitespace
print(f"Modified String 4: {user_string.replace('a', '@')}")
# replaces all occurrences of 'a' with '@'
print(f"Modified String 5: {user_string.capitalize()}")
# converts the first character to uppercase and the rest to lowercase
print(f"Modified String 6: {user_string[::-1]}")
# reverses the string
print(f"Modified String 7: {user_string.title()}")
# converts the first character of each word to uppercase and the rest to lowercase
print(f"Modified String 8: {len(user_string)}")
# returns the length of the string
print(f"Modified String 9: {user_string.find('a')}")
# returns the index of the first occurrence of 'a'
print(f"Modified String 10: {user_string.count('a')}")
# returns the number of occurrences of 'a'
print(f"Modified String 11: {user_string.startswith('Hello')}")
#returns True if the string starts with 'Hello', otherwise False
print(f"Modified String 12: {user_string.endswith('!')}")
# returns True if the string ends with '!', otherwise False
print(f"Modified String 13: {user_string.isalnum()}")
# returns True if all characters in the string are alphanumeric (letters and numbers), otherwise False
print(f"Modified String 14: {user_string.isalpha()}")
# returns True if all characters in the string are alphabetic (letters), otherwise False
print(f"Modified String 15: {user_string.isdigit()}")
# returns True if all characters in the string are digits (numbers), otherwise False



######
# if you finish, you can look at some more: https://www.w3schools.com/python/python_ref_string.asp
# and add some extras to this selection!
# You can also combine these functions - have a play around and see what you can do!