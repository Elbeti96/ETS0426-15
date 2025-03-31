This repository delves into fundamental string searching and counting metgit hods, crucial tools for text processing and data analysis. Strings are ubiquitous in programming, and understanding how to efficiently locate substrings or count character occurrences is essential. We'll explore techniques like using Python's built-in string methods (.find(), .count(), .startswith(), .endswith()), regular expressions (for more complex pattern matching), and algorithmic approaches for specific search scenarios. The examples highlight the trade-offs between simplicity, flexibility, and performance when working with string data, enabling you to choose the right method for your task, whether it's validating user input, parsing log files, or analyzing text 
Search Algorithms: Search algorithms efficiently locate specific elements within a dataset. Linear search provides a simple, but often less efficient, approach by iterating through each element until the target is found. Binary search, on the other hand, leverages the sorted nature of a dataset to drastically reduce the search space by repeatedly dividing it in half, achieving logarithmic time complexity. The choice between these (and other more advanced search methods) depends heavily on the characteristics of the data (sorted or unsorted), the size of the dataset, and the frequency with which searches are performed. Choosing the correct algorithm can drastically improve performance, especially for large datasets. Consider a scenario where you need to search for a specific ID in a database of millions of entries; binary search would offer a significant speed advantage if the database is indexed (sorted).
# Linear Search Example
def linear_search(arr, target):
  for i in range(len(arr)):
    if arr[i] == target:
      return i
  return -1  # Target not found

# Example:
my_list = [1, 5, 2, 8, 3]
print(f"Linear Search for 8: {linear_search(my_list, 8)}") # Output: Linear Search for 8: 3

# Binary Search Example (requires a sorted array)
def binary_search(arr, target):
  low = 0
  high = len(arr) - 1
  while low <= high:
    mid = (low + high) // 2
    if arr[mid] == target:
      return mid
    elif arr[mid] < target:
      low = mid + 1
    else:
      high = mid - 1
  return -1  # Target not found

# Example:
sorted_list = [2, 3, 5, 8, 10]
print(f"Binary Search for 5: {binary_search(sorted_list, 5)}") # Output: Binary Search for 5: 2

Counting Algorithms: Counting algorithms focus on determining the occurrence of specific elements or patterns within a dataset. Frequency counting involves tracking the number of times each unique element appears, often used in data analysis and text processing. Histograms provide a visual representation of this frequency distribution, grouping data into bins for easier interpretation. Imagine analyzing website traffic data: a histogram could show the number of visitors within specific age ranges or geographic locations. These counting techniques can be implemented using various data structures, such as hash tables (dictionaries) for efficient lookup and storage. By leveraging these algorithms, you can gain insights into the distribution of data, identify trends, and make informedets decisions based on the frequency of specific events or elements. Understanding these principles provides a solid foundation for tackling more complex data analysis and manipulation tasks.
# Frequency Counting Example
def frequency_count(arr):
  counts = {}
  for item in arr:
    counts[item] = counts.get(item, 0) + 1
  return counts

# Example:
fruit_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
print(f"Frequency Count: {frequency_count(fruit_list)}") # Output: Frequency Count: {'apple': 3, 'banana': 2, 'orange': 1}

#Second Commit

Explanation of .split(delimiter)

The .split(delimiter) method is a fundamental string manipulation technique used to break a string into smaller parts (substrings) based on a designated delimiter. Imagine you have a sentence and you want to extract each word – you'd use a space as the delimiter.

•  Purpose: To divide a single string into an ordered collection of substrings, making it easier to process individual parts of the original string.

•  How it Works:

  1. The method searches the string for instances of the specified delimiter.
  2. Each time the delimiter is found, the string is split at that point.
  3. The substrings between the delimiters are collected into a list (or array, depending on the language).
  4. The delimiter itself is not included in the resulting substrings.

•  Delimiter: The delimiter is the character or sequence of characters that marks the boundaries between the substrings. It can be a single character (like a comma or space) or a longer string.

•  No Delimiter Specified (Default): If you don't provide a delimiter, the method typically splits on whitespace (spaces, tabs, newlines). Multiple whitespace characters are treated as a single delimiter.

•  Empty Substrings: If there are consecutive delimiters, or if the delimiter appears at the beginning or end of the string, you might get empty strings in the resulting list. You can filter these out if needed.

Example :

# Splitting by a comma:
data = "name,age,city"
fields = data.split(",")  # fields will be ['name', 'age', 'city']

# Splitting by a space:
sentence = "This is a test sentence."
words = sentence.split()  # words will be ['This', 'is', 'a', 'test', 'sentence.']

# Multiple spaces:
text = "  leading and trailing spaces  "
stripped_words = text.split() # stripped_words will be ['leading', 'and', 'trailing', 'spaces']

# Empty string:
empty_string = ""
result = empty_string.split(",") # result will be ['']

# Consecutive delimiters:
csv_data = "apple,,banana"
csv_parts = csv_data.split(",")  # csv_parts will be ['apple', '', 'banana']

#Third Commit

The .find(substring) (or .indexOf(substring)) method is designed to locate the position of a smaller string (the substring) within a larger string. It's a common and crucial tool for searching text, extracting data, and performing pattern matching.

•   Purpose: To determine the starting index of the first occurrence of a specific substring within a string. If the substring is not found, it returns a special value indicating that the search failed.

•   How it Works:

    1.  The method searches the string from left to right, looking for the first instance where the substring matches a portion of the string.
    2.  If a match is found, the method returns the index (position) of the first character of the matched substring within the larger string. Indices typically start at 0.
    3.  If the substring is not found anywhere in the string, the method returns -1 (in Python and many other languages). Some languages might return a different value, such as null.
    4.  The search stops after the first match is found. To find subsequent occurrences, you may need to use a loop and adjust the starting position of the search.

•   substring: The smaller string you are searching for.

•   Case Sensitivity: The search is generally case-sensitive. "hello" will not match "Hello".  You can use .lower() or .upper() on both strings for a case-insensitive search.

•   Overlapping Matches: The method only finds the first non-overlapping match.  If the substring overlaps with itself, only the initial occurrence is reported.

Example (Python):

# Basic find:
text = "This is a test string"
index = text.find("test")  # index will be 10 (the index of 't' in "test")

# Substring not found:
text = "Hello world"
index = text.find("goodbye")  # index will be -1

# Case sensitivity:
text = "The quick brown fox"
index = text.find("the")  # index will be -1 (because it's lowercase)
index2 = text.find("The") # index2 will be 0

# Finding multiple occurrences (requires a loop):
text = "apple banana apple cherry apple"
substring = "apple"
start = 0
while True:
    index = text.find(substring, start)  # Start the search from 'start'
    if index == -1:
        break  # No more occurrences
    print(f"Found '{substring}' at index {index}")
    start = index + 1  # Move the starting position to after the found substring

#Fourth Commit

Explanation of .join(iterable)

The .join(iterable) method is used to combine elements from an iterable (like a list, tuple, or set) into a single string, using the string on which the method is called as a separator between the elements. It's a versatile way to construct strings from collections of data.

•  Purpose: To concatenate elements of an iterable into a single string, inserting a specified separator between each element.

•  How it Works:

  1. The method iterates through the iterable.
  2. For each element in the iterable, it converts the element to a string (if it isn't already).
  3. It then appends the string representation of the element to the accumulating result string.
  4. Between each element (except for the first), it inserts the string on which the .join() method was called (the separator).
  5. A new string is returned, containing all the joined elements.

•  iterable: A collection of items, such as a list, tuple, set, or any other object that can be iterated over. All elements of the iterable must be convertible to strings.
•  Separator: The string that is inserted between each element of the iterable. This is the string on which the .join() method is called. If you want no separator, use an empty string "".

•  Type Conversion: The join() method expects the iterable to contain only strings (or objects that can be easily converted to strings). If you have non-string elements (e.g., numbers), you'll need to convert them to strings before using join().

Example (Python):

# Joining with a space:
words = ["This", "is", "a", "sentence"]
joined_text = " ".join(words)  # joined_text will be "This is a sentence"

# Joining with a comma:
parts = ["apple", "banana", "cherry"]
csv_string = ",".join(parts)  # csv_string will be "apple,banana,cherry"

# Joining with no separator:
characters = ['H', 'e', 'l', 'l', 'o']
word = "".join(characters)  # word will be "Hello"

# Joining numbers (requires conversion to strings):
numbers = [1, 2, 3, 4, 5]
string_numbers = [str(x) for x in numbers]  # Convert to strings first
joined_numbers = "-".join(string_numbers) # joined_numbers will be "1-2-3-4-5"

# Joining a tuple:
colors = ("red", "green", "blue")
color_string = " and ".join(colors) # color_string will be "red and green and blue"

#Fifth commit
. .startswith(prefix) (Starts With)

•   Description: Checks if a string starts with a prefix.
•   Example (Python):
    
    text = "Hello world"
    starts = text.startswith("Hello")  # starts is True
    

. .endswith(suffix) (Ends With)

•   Description: Checks if a string ends with a suffix.
•   Example (Python):
    
    text = "Hello world"
    ends = text.endswith("world")  # ends is True
 .lstrip() (Left Strip)

•   Description: Removes leading whitespace.
•   Example (Python):
    
    text = "   Hello"
    stripped = text.lstrip()  # stripped is "Hello"
    

.rstrip() (Right Strip)

•   Description: Removes trailing whitespace.
•   Example (Python):
    
    text = "Hello   "
    stripped = text.rstrip()  # stripped is "Hello"
#Sixth commit

 .partition(separator)

•  Explanation: The .partition(separator) method divides a string into three parts based on the first occurrence of a specified separator. It returns a tuple containing: (1) the part before the separator, (2) the separator itself, and (3) the part after the separator. If the separator is not found, it returns a tuple containing the original string, followed by two empty strings.

•  Purpose: To split a string into three distinct parts using a separator, making it easy to extract specific segments of the string.

•  How it Works:

  1. The method searches for the first occurrence of the separator within the string.
  2. If the separator is found:
    *  The string before the separator is the first element of the tuple.
    *  The separator itself is the second element of the tuple.
    *  The string after the separator is the third element of the tuple.
  3. If the separator is not found:
    *  The original string is the first element of the tuple.
    *  The second and third elements of the tuple are empty strings.

•  Important: It only splits at the first occurrence. For splitting at all occurrences, use .split().

•  Example (Python):

    text = "Hello, world!"
    parts = text.partition(", ")  # parts will be ('Hello', ', ', 'world!')

    text2 = "filename.txt"
    parts2 = text2.partition(".") # parts2 will be ('filename', '.', 'txt')

    text3 = "No separator here"
    parts3 = text3.partition(",")  # parts3 will be ('No separator here', '', '')

 .center(width, fillchar)

•  Explanation: The .center(width, fillchar) method centers a string within a field of a specified width. It pads the string with the specified fill character (default is space) on both sides to reach the desired width.

•  Purpose: To format a string by centering it within a fixed-width field, often used for creating formatted output or aligning text.

•  How it Works:

  1. Calculates the amount of padding needed on each side of the string to reach the specified width.
  2. If width is less than or equal to the length of the string, it returns the original string unchanged.
  3. Otherwise, it creates a new string by padding the original string with the fillchar on both sides, attempting to distribute the padding equally. If the padding can't be perfectly equal, the extra character is typically added to the right side.

•  fillchar (optional): The character used for padding. If omitted, it defaults to a space (" ").

•  Example (Python):

    text = "Hello"
    centered_text = text.center(10)  # centered_text will be "  Hello   "
    centered_text2 = text.center(15, "*") # centered_text2 will be "****Hello*****"
    centered_text3 = text.center(3)  # centered_text3 will be "Hello" (width is too small)

 .zfill(width)

•  Explanation: The .zfill(width) method pads a numeric string on the left with leading zeros to reach a specified width. It's typically used for formatting numbers with a consistent number of digits.

•  Purpose: To pad a numeric string with leading zeros, ensuring a fixed width for consistent formatting.

•  How it Works:

  1. If the string starts with a plus or minus sign, it preserves the sign.
  2. Calculates the amount of padding needed to reach the specified width.
  3. Adds leading zeros to the left of the number (or to the right of the sign, if present) until the string reaches the desired width.
  4. If the width is less than or equal to the length of the string, it returns the original string.

•  Example (Python):

    number = "5"
    padded_number = number.zfill(3)  # padded_number will be "005"

    number2 = "123"
    padded_number2 = number2.zfill(5) # padded_number2 will be "00123"

    number3 = "-42"
    padded_number3 = number3.zfill(5) # padded_number3 will be "-0042"

    number4 = "+10"
    padded_number4 = number4.zfill(4) # padded_number4 will be "+010"

    number5 = "12345"
    padded_number5 = number5.zfill(3) # padded_number5 will be "12345" (width too small)

#Seventh Commit
Alright, here are three more string methods, complete with explanations and README entries:

1. isnumeric()

•   Explanation: The isnumeric() method checks whether all characters in a string are numeric characters. Numeric characters include digits, fractions, superscripts, subscripts, and other characters that represent numeric values. This method is more inclusive than isdigit().

•   Purpose: To validate if a string represents a numeric value, considering a broader range of numeric characters beyond simple digits.

•   How it Works:

    1.  The method iterates through each character in the string.
    2.  It checks if each character is a numeric character as defined by Unicode. This includes digits ('0' - '9'), as well as characters like fraction symbols (e.g., '½'), superscript digits (e.g., '²'), and other Unicode numeric characters.
    3.  If all characters are numeric, it returns True.
    4.  If any character is not numeric, it returns False.
    5.  Empty strings return False.

•   Important Notes:
    •   This method does not consider characters like '.' (decimal point) or '-' (negative sign) as numeric. So, "12.3" and "-42" will return False.
    •   isnumeric() is different from isdigit(). isdigit() only returns True for characters that are simple digits (0-9).

•   Example (Python):

    text1 = "12345"
    result1 = text1.isnumeric()  # result1 will be True

    text2 = "½"  # Fraction one-half
    result2 = text2.isnumeric()  # result2 will be True

    text3 = "12.3"
    result3 = text3.isnumeric()  # result3 will be False

    text4 = "abc"
    result4 = text4.isnumeric()  # result4 will be False

    text5 = ""
    result5 = text5.isnumeric()  # result5 will be False

2. isdecimal()

•   Explanation: The isdecimal() method checks if all characters in a string are decimal characters. Decimal characters are those that can be used to form numbers in base-10, such as digits 0-9. This method is more restrictive than isnumeric() and isdigit().

•   Purpose: To specifically validate if a string contains only characters that are part of the standard decimal number system.

•   How it Works:

    1.  The method iterates through each character in the string.
    2.  It checks if each character is a decimal character according to Unicode. This primarily includes the digits '0' through '9'.
    3.  If all characters are decimal, it returns True.
    4.  If any character is not a decimal, it returns False.
    5.  Empty strings return False.

•   Important Notes:

    •   This method returns False for characters like fraction symbols, superscript digits, and other characters that isnumeric() might consider numeric.
    •   isdecimal() is different from isdigit() which also return True for special digits like superscripted numbers.

•   Example (Python):

    text1 = "12345"
    result1 = text1.isdecimal()  # result1 will be True

    text2 = "½"  # Fraction one-half
    result2 = text2.isdecimal()  # result2 will be False

    text3 = "12.3"
    result3 = text3.isdecimal()  # result3 will be False

    text4 = "abc"
    result4 = text4.isdecimal()  # result4 will be False

    text5 = ""
    result5 = text5.isdecimal()  # result5 will be False

3. expandtabs(tabsize=8)

•  Explanation: The expandtabs(tabsize=8) method replaces tab characters (\t) in a string with spaces. The tabsize argument specifies the number of spaces that each tab character should be expanded to. If tabsize is not provided, it defaults to 8.

•  Purpose: To convert tab characters into spaces, enabling consistent formatting and alignment in strings, especially when dealing with text that might have been created with different tab settings.

•  How it Works:

  1. The method scans the string for tab characters (\t).
  2. For each tab character found:
    *  It calculates the number of spaces needed to reach the next tab stop. Tab stops are typically set at intervals of tabsize.
    *  It replaces the tab character with the calculated number of spaces.

•  tabsize (optional): An integer specifying the tab size (number of spaces per tab). Defaults to 8.

•  Example (Python):

    text1 = "Hello\tworld"
    result1 = text1.expandtabs()  # result1 will be "Hello   world" (tabsize=8)

    text2 = "Column1\tColumn2\tColumn3"
    result2 = text2.expandtabs(4) # result2 will be "Column1 Column2 Column3" (tabsize=4)

    text3 = "A\tB\nC\tD" #multiline string
    result3 = text3.expandtabs(2)
    print(result3)
    #A B
    #C D

#Eighth commit
. isdigit()

•   Explanation: The isdigit() method checks if all characters in a string are digits (0-9). It is more restrictive than isnumeric() and includes only basic digit characters.

•   Purpose: To validate if a string contains only the basic numeric digits (0 through 9).

•   How it Works:

    1.  The method iterates through each character in the string.
    2.  It checks if each character is one of the digits '0', '1', '2', '3', '4', '5', '6', '7', '8', or '9'.
    3.  If all characters are digits, it returns True.
    4.  If any character is not a digit, it returns False.
    5.  Empty strings return False.

•   Important Notes:

    •   This method returns False for characters like fraction symbols, superscript digits, decimal points, or negative signs.
    •   isdigit() is different from isnumeric() and isdecimal(). isdigit() returns True for superscripted numbers which isdecimal does not.

•   Example (Python):

    text1 = "12345"
    result1 = text1.isdigit()  # result1 will be True

    text2 = "123²" # Contains a superscript digit
    result2 = text2.isdigit()  # result2 will be True

    text3 = "½"  # Fraction one-half
    result3 = text3.isdigit()  # result3 will be False

    text4 = "12.3"
    result4 = text4.isdigit()  # result4 will be False

    text5 = "abc"
    result5 = text5.isdigit()  # result5 will be False

    text6 = ""
    result6 = text6.isdigit()  # result6 will be False

 isalnum()

•  Explanation: The isalnum() method checks if all characters in a string are alphanumeric, meaning either letters or digits. It returns True if the string is not empty and all characters are alphanumeric; otherwise, it returns False.

•  Purpose: To validate if a string contains only letters and numbers.

•  How it Works:

  1. The method iterates through each character in the string.
  2. It checks if each character is either a letter (a-z, A-Z) or a digit (0-9).
  3. If all characters are alphanumeric, it returns True.
  4. If any character is not alphanumeric, or if the string is empty, it returns False.

•  Important Notes:

  •  This method returns False for strings containing whitespace, punctuation, or symbols.

•  Example (Python):

    text1 = "HelloWorld123"
    result1 = text1.isalnum()  # result1 will be True

    text2 = "HelloWorld 123" # Contains space
    result2 = text2.isalnum()  # result2 will be False

    text3 = "HelloWorld!" # Contains a symbol
    result3 = text3.isalnum()  # result3 will be False

    text4 = "12345"
    result4 = text4.isalnum()  # result4 will be True

    text5 = "abc"
    result5 = text5.isalnum()  # result5 will be True

    text6 = ""
    result6 = text6.isalnum()  # result6 will be False

 isidentifier()

•  Explanation: The isidentifier() method checks if a string is a valid identifier according to the rules of the programming language. In Python, a valid identifier must start with a letter (a-z, A-Z) or an underscore (_), and can contain letters, digits, or underscores.

•  Purpose: To validate if a string can be used as a variable name, function name, or other identifier in your code.

•  How it Works:

  1. The method checks if the string starts with a letter or an underscore.
  2. It then checks if all remaining characters are letters, digits, or underscores.
  3. If both conditions are met, it returns True.
  4.  It also checks whether the string is a reserved keyword, in which case it returns False.
  5. If the string is empty or does not meet the identifier rules, it returns False.

•  Important Notes:

  •  The rules for valid identifiers can vary slightly between programming languages. This explanation and the example are based on Python's identifier rules.

•  Example (Python):

    text1 = "my_variable"
    result1 = text1.isidentifier()  # result1 will be True

    text2 = "_my_variable"
    result2 = text2.isidentifier()  # result2 will be True

    text3 = "123variable" # Starts with a digit
    result3 = text3.isidentifier()  # result3 will be False

    text4 = "my-variable" # Contains a hyphen
    result4 = text4.isidentifier()  # result4 will be False

    text5 = "if" # Reserved Keyword
    result5 = text5.isidentifier() # result5 will be False

    text6 = ""
    result6 = text6.isidentifier()  # result6 will be False
#Ninth commit
?, [3/31/2025 9:14 PM]
Okay, here are three more string methods with explanations and README entries, bringing us closer to covering a wide range of string manipulation techniques:

1. isdigit()

•   Explanation: The isdigit() method checks if all characters in a string are digits (0-9). It is more restrictive than isnumeric() and includes only basic digit characters.

•   Purpose: To validate if a string contains only the basic numeric digits (0 through 9).

•   How it Works:

    1.  The method iterates through each character in the string.
    2.  It checks if each character is one of the digits '0', '1', '2', '3', '4', '5', '6', '7', '8', or '9'.
    3.  If all characters are digits, it returns True.
    4.  If any character is not a digit, it returns False.
    5.  Empty strings return False.

•   Important Notes:

    •   This method returns False for characters like fraction symbols, superscript digits, decimal points, or negative signs.
    •   isdigit() is different from isnumeric() and isdecimal(). isdigit() returns True for superscripted numbers which isdecimal does not.

•   Example (Python):

?, [3/31/2025 9:14 PM]
    text1 = "12345"
    result1 = text1.isdigit()  # result1 will be True

    text2 = "123²" # Contains a superscript digit
    result2 = text2.isdigit()  # result2 will be True

    text3 = "½"  # Fraction one-half
    result3 = text3.isdigit()  # result3 will be False

    text4 = "12.3"
    result4 = text4.isdigit()  # result4 will be False

    text5 = "abc"
    result5 = text5.isdigit()  # result5 will be False

    text6 = ""
    result6 = text6.isdigit()  # result6 will be False

?, [3/31/2025 9:14 PM]
2. isalnum()

•  Explanation: The isalnum() method checks if all characters in a string are alphanumeric, meaning either letters or digits. It returns True if the string is not empty and all characters are alphanumeric; otherwise, it returns False.

•  Purpose: To validate if a string contains only letters and numbers.

•  How it Works:

  1. The method iterates through each character in the string.
  2. It checks if each character is either a letter (a-z, A-Z) or a digit (0-9).
  3. If all characters are alphanumeric, it returns True.
  4. If any character is not alphanumeric, or if the string is empty, it returns False.

•  Important Notes:

  •  This method returns False for strings containing whitespace, punctuation, or symbols.

•  Example (Python):

?, [3/31/2025 9:14 PM]
    text1 = "HelloWorld123"
    result1 = text1.isalnum()  # result1 will be True

    text2 = "HelloWorld 123" # Contains space
    result2 = text2.isalnum()  # result2 will be False

    text3 = "HelloWorld!" # Contains a symbol
    result3 = text3.isalnum()  # result3 will be False

    text4 = "12345"
    result4 = text4.isalnum()  # result4 will be True

    text5 = "abc"
    result5 = text5.isalnum()  # result5 will be True

    text6 = ""
    result6 = text6.isalnum()  # result6 will be False

?, [3/31/2025 9:14 PM]
3. isidentifier()

•  Explanation: The isidentifier() method checks if a string is a valid identifier according to the rules of the programming language. In Python, a valid identifier must start with a letter (a-z, A-Z) or an underscore (_), and can contain letters, digits, or underscores.

•  Purpose: To validate if a string can be used as a variable name, function name, or other identifier in your code.

•  How it Works:

  1. The method checks if the string starts with a letter or an underscore.
  2. It then checks if all remaining characters are letters, digits, or underscores.
  3. If both conditions are met, it returns True.
  4.  It also checks whether the string is a reserved keyword, in which case it returns False.
  5. If the string is empty or does not meet the identifier rules, it returns False.

•  Important Notes:

  •  The rules for valid identifiers can vary slightly between programming languages. This explanation and the example are based on Python's identifier rules.

•  Example (Python):

#Ninth commit
1. casefold()

•  Explanation: The casefold() method is similar to lower(), but it's more aggressive in converting strings to lowercase. It's intended for caseless comparisons where you want to remove all case distinctions, even those that lower() might miss. This is especially important when dealing with Unicode characters from different languages.

•  Purpose: To perform a more comprehensive lowercase conversion for case-insensitive comparisons, particularly with Unicode strings.

•  How it Works:
  1. It converts the string to lowercase.
  2. It handles special Unicode characters that have more complex case mappings than simple English letters. casefold() aims to eliminate all case distinctions.

•  Key Difference from lower(): lower() is sufficient for most English-language case-insensitive comparisons. casefold() is more robust for internationalized applications.

•  Example (Python):
    text1 = "ß"  # German Eszett (sharp S)
    lower_text = text1.lower()   # lower_text will be "ß" (unchanged)
    casefold_text = text1.casefold() # casefold_text will be "ss"

    text2 = "Hello World"
    lower_text2 = text2.lower() #lower_text2 will be "hello world"
    casefold_text2 = text2.casefold() #casefold_text2 will be "hello world"

2. title()

•  Explanation: The title() method converts a string to title case, where the first letter of each word is capitalized, and all other letters are lowercase.

•  Purpose: To format strings in a title-like style, making them more readable and visually appealing.

•  How it Works:

  1. The method identifies word boundaries (typically whitespace or punctuation).
  2. It capitalizes the first letter of each word.
  3. It converts all other letters in each word to lowercase.

•  Important Notes: The definition of a "word" can depend on the presence of punctuation.

•  Example (Python):

    text1 = "hello world"
    title_text = text1.title()  # title_text will be "Hello World"

    text2 = "this is a sentence."
    title_text2 = text2.title() # title_text2 will be "This Is A Sentence."

    text3 = "aBcDeFg"
    title_text3 = text3.title() # title_text3 will be "Abcdefg"

3. swapcase()

•  Explanation: The swapcase() method swaps the case of each character in a string. Uppercase letters become lowercase, and lowercase letters become uppercase.

•  Purpose: To invert the case of letters in a string.

•  How it Works:

  1. The method iterates through each character in the string.
  2. If a character is uppercase, it's converted to lowercase.
  3. If a character is lowercase, it's converted to uppercase.
  4. Characters that are not letters (e.g., digits, symbols, whitespace) are left unchanged.

•  Example (Python):
    text1 = "Hello World"
    swapped_text = text1.swapcase()  # swapped_text will be "hELLO wORLD"

    text2 = "aBcDeFg123"
    swapped_text2 = text2.swapcase() # swapped_text2 will be "AbCdEfG123"