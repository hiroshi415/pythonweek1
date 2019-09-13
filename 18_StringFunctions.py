# Upper case the first letter in this sentence:
txt = "hello, and welcome to my world."
x = txt.capitalize()
print(x)
print('___________________________')
# Make the string lower case:
txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)
print('___________________________')
# Make the lower case letters upper case and the upper case letters lower case:
txt = "Hello My Name Is PETER"
x = txt.swapcase()
print(x)
print('___________________________')
# Print the word "banana", taking up the space of 20 characters, with "banana" in the middle:
txt = "banana"
x = txt.center(50)
print(x)
print('___________________________')
# Return the number of times the value "apple" appears in the string:
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)
print('___________________________')
# Check if the string ends with a punctuation sign (.):
txt = "Hello, welcome to my world.."
x = txt.endswith("!")
print(x)
print('___________________________')
# Searches the string for a specified value and returns the position of where it was found
txt = "Hello, welcome to my world."
x = txt.index("to")
print(x)
print('___________________________')
# Check if all the characters in the text are alphanumeric:
txt = "Company12!"
x = txt.isalnum()
print(x)
print('___________________________')
# Returns True if all characters in the string are in the alphabet
txt = "CompanyX1"
x = txt.isalpha()
print(x)
print('___________________________')
# Join all items in a tuple into a string, using a hash character as separator:
myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)
print('___________________________')
# Check if all the characters in the text are whitespaces:
txt = "  "
x = txt.isspace()
print(x)
print('___________________________')
