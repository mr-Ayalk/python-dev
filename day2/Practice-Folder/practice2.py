#Topic : Built-in String Functions

name=input("Enter your name:    ")
result=name.capitalize()  # Capitalizes the first character of the string
result=name.upper()       # Converts all characters to uppercase
result=name.lower()       # Converts all characters to lowercase
result=name.title()       # Capitalizes the first character of each word
result=name.strip()      # Removes leading and trailing whitespace
result=name.replace("a","@")  # Replaces all occurrences of 'a' with '@'
result=name.split()      # Splits the string into a list of words
result=len(name)        # Returns the length of the string
result=name.find("a")   # Finds the first occurrence of 'a' and returns its index, -1 if not found
result=name.count("a")  # Counts the occurrences of 'a' in the string
result=name.startswith("A")  # Checks if the string starts with 'A', returns True or False
result=name.endswith("z")    # Checks if the string ends with 'z', returns True
result=name.isalpha()   # Checks if all characters in the string are alphabetic, returns True or False
result=name.isdigit()   # Checks if all characters in the string are digits, returns True
result=name.isalnum()   # Checks if all characters in the string are alphanumeric, returns True or False
result=name.center(50)  # Centers the string within a field of given width (50 here)
result=name.zfill(50)  # Pads the string on the left with zeros to fill a width of 50
result=name.encode()   # Encodes the string into bytes using default encoding (utf-8)
result=name.count(" ")  # Counts the number of spaces in the string
result=name.swapcase()  # Swaps the case of each character in the string
result=name.partition(" ")  # Splits the string at the first occurrence of space into a tuple (before, separator, after)
result=name.rfind("a")   # Finds the last occurrence of 'a' and returns its index, -1 if not found
result=name.rsplit(" ")  # Splits the string into a list of words from the right side
result=name.lstrip()   # Removes leading whitespace
result=name.rstrip()   # Removes trailing whitespace



print(result)



print(type(result))
print(help(str))  # Displays the documentation for string methods