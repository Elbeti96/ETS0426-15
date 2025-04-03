Case Conversion

•  str.lower(): Converts all characters in the string to lowercase. This is useful for case-insensitive comparisons or standardizing input.

    text = "HeLLo"
    lowercase = text.lower()  # lowercase is "hello"

*  str.upper(): Converts all characters in the string to uppercase. Commonly used for emphasizing text or for system-level commands that require uppercase input.

    text = "hello"
    uppercase = text.upper()  # uppercase is "HELLO"

*  str.title(): Converts the string to title case, where the first letter of each word is capitalized, and the rest are lowercase. This is often used for formatting titles or headings. The method identifies word boundaries by spaces.

    text = "this is a sentence"
    title_case = text.title()  # title_case is "This Is A Sentence"

*  str.capitalize(): Capitalizes only the first character of the entire string, converting the rest to lowercase. This is useful for ensuring the first letter of a sentence is capitalized while standardizing the rest of the text.

    text = "hELLO world"
    capitalized = text.capitalize()  # capitalized is "Hello world"

*  str.swapcase(): Swaps the case of each character in the string. Uppercase becomes lowercase, and lowercase becomes uppercase. This can be useful for creating visual effects or obfuscating text.

    text = "HeLLo wORLd"
    swapped = text.swapcase()  # swapped is "hEllO WorlD"

Searching and Counting

•  str.find(substring): Returns the index (position) of the first occurrence of a specified substring within the string. If the substring is not found, it returns -1. Useful for finding if a string contains a specific sequence of characters and locating its starting point.

    text = "Hello world"
    index = text.find("world")  # index is 6
    index2 = text.find("xyz") # index2 is -1

*  str.index(substring): Similar to find(), but it raises a ValueError if the substring is not found. Use this when you expect the substring to be present and want the program to throw an error if it's not.

    text = "Hello world"
    index = text.index("world")  # index is 6
    #text.index("xyz")  # Raises ValueError

*  str.startswith(prefix): Checks if a string starts with a given prefix and returns True or False. This is helpful for validating input or filtering strings based on their beginnings.

    text = "Hello world"
    starts = text.startswith("Hello")  # starts is True

*  str.endswith(suffix): Checks if a string ends with a given suffix and returns True or False. This is helpful for validating file extensions or processing text based on its ending characters.

    text = "Hello world"
    ends = text.endswith("world")  # ends is True

*  str.count(substring): Counts the number of non-overlapping occurrences of a substring within the string. Useful for analyzing text to see how often a specific word or phrase appears.

    text = "apple banana apple"
    count = text.count("apple")  # count is 2

Modification

•  str.replace(old, new): Replaces all occurrences of a specified substring (old) with another substring (new). Returns a new string with the replacements. Used for correcting errors, standardizing text, or transforming data.

    text = "Hello world"
    new_text = text.replace("Hello", "Hi")  # new_text is "Hi world"

*  str.strip(): Removes leading and trailing whitespace (spaces, tabs, newlines) from a string. This is commonly used to clean up user input or data read from files.

    text = "  Hello world  "
    stripped = text.strip()  # stripped is "Hello world"

*  str.lstrip(): Removes only the leading whitespace from a string. Useful for cleaning up input when you want to preserve trailing whitespace.

    text = "   Hello"
    stripped = text.lstrip()  # stripped is "Hello"

*  str.rstrip(): Removes only the trailing whitespace from a string. Useful for cleaning up data when you want to preserve leading whitespace.

    text = "Hello   "
    stripped = text.rstrip()  # stripped is "Hello"

*  str.split(delimiter): Splits the string into a list of substrings based on a specified delimiter. If no delimiter is provided, it splits on whitespace. Used for parsing data from a string into individual components.

    text = "apple,banana"
    fruits = text.split(",")  # fruits is ['apple', 'banana']

*  str.join(iterable): Joins the elements of an iterable (like a list, tuple, or set) into a single string, using the string on which the method is called as a separator. This is useful for constructing strings from collections of data.

    words = ["a", "b"]
    joined = ",".join(words)  # joined is "a,b"

Checking Content Type

•  str.isalpha(): Checks if all characters in the string are letters (a-z, A-Z). Returns True if the string is not empty and all characters are letters; otherwise, returns False. Useful for validating input fields that should only contain letters.

    text = "HelloWorld"
    is_alpha = text.isalpha()  # is_alpha is True

    text2 = "Hello World"
    is_alpha2 = text2.isalpha() #is_alpha2 is False

*  str.isdigit(): Checks if all characters in the string are digits (0-9). Returns True if the string is not empty and all characters are digits; otherwise, returns False. Useful for validating input fields that should only contain numbers.

    text = "12345"
    is_digit = text.isdigit()  # is_digit is True

*  str.isalnum(): Checks if all characters in the string are alphanumeric (letters or digits). Returns True if the string is not empty and all characters are alphanumeric; otherwise, returns False. Useful for validating input that should contain only letters and numbers.

    text = "HelloWorld123"
    is_alnum = text.isalnum()  # is_alnum is True

*  str.isspace(): Checks if all characters in the string are whitespace characters (spaces, tabs, newlines, etc.). Returns True if the string is not empty and all characters are whitespace; otherwise, returns False. Useful for validating empty or blank input fields.

    text = "  \t\n"
    is_space = text.isspace()  # is_space is True

*  str.islower(): Checks if all cased characters in the string are lowercase and there is at least one cased character. A cased character means that it can be both upper and lowercase (a letter).

    text = "hello world"
    is_lower = text.islower()  # is_lower is True

    text2 = "hello 123"
    is_lower2 = text2.islower() # is_lower2 is True

    text3 = "123"
    is_lower3 = text3.islower() #is_lower3 is False

*  str.isupper(): Checks if all cased characters in the string are uppercase and there is at least one cased character. A cased character means that it can be both upper and lowercase (a letter).

    text = "HELLO WORLD"
    is_upper = text.isupper()  # is_upper is True

     text2 = "HELLO 123"
    is_upper2 = text2.isupper() # is_upper2 is True

    text3 = "123"
    is_upper3 = text3.isupper() #is_upper3 is False

Formatting

•   str.format(*args, *kwargs): Formats a string by replacing placeholders with the provided positional and keyword arguments. Provides a flexible way to construct complex strings with dynamic values.

    name = "Alice"
    age = 30
    formatted_text = "Name: {}, Age: {}".format(name, age) # formatted_text is "Name: Alice, Age: 30"

*  f-strings (Formatted string literals): A concise and readable way to embed expressions directly inside string literals. Introduced in Python 3.6, they provide a more intuitive way to format strings.

    name = "Bob"
    age = 25
    formatted_text = f"Name: {name}, Age: {age}"  # formatted_text is "Name: Bob, Age: 25"

•  len(string): Returns the length (number of characters) of the string. This is a built-in function, not a string method, but it's commonly used with strings.

    text = "Hello"
    length = len(text)  # length is 5

*  str.encode(encoding='utf-8', errors='strict'): Encodes the string using the specified encoding (e.g., 'utf-8', 'ascii'). This converts the string into a sequence of bytes. Used for working with files, network communication, or data storage where bytes are required. The errors parameter specifies how to handle encoding errors (e.g., 'strict', 'ignore', 'replace').

    text = "Hello"
    encoded_text = text.encode('utf-8')  # encoded_text is b'Hello'