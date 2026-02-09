"""
Docstring for week-02-python-basics.main

Data Types: The type of data.

    - Data types: 
        Strings: values inside quotation marks are called strings; e.g: 'George', 'hello my name is wisdom'
        Integers: whole numbers without decimal points; e.g: 10, -5, 0, 123456789, 1000000000
        Floats: Numbers with decimal points; e.g: 3.14, -0.001, 2.0, 0.0

        Booleans: True or False;
        NoneType: no value;
        Complex Numbers: Numbers with real and imaginary parts; e.g: 3i + 4j

    - Data structures: Lists, Dictionaries, Tuples, Sets

- Keywords: These are special reserved words that have specific meanings in Python.
    You don't use keywords as variable, function or class names.

- Conditional Statements (if/else)
- Loops (for, while)
- Functions (basic ones for data manipulation)
- Importing

"""

# ----------------- Data Types -----------------

string_data_type = "Hello, World!"  # String
integer_data_type = -123456789  # Integer
float_data_type = 3.14159  # Float
is_turned_on = True  # Boolean False
none_type =  None # representss no value
complex_data_type = 6 + 4j  # Complex Number

print(string_data_type, type(string_data_type))  # String
print(integer_data_type, type(integer_data_type))  # Integer
print(float_data_type, type(float_data_type))  # Float
print(is_turned_on, type(is_turned_on))  # Boolean
print(none_type, type(none_type))  # NoneType
print(complex_data_type, type(complex_data_type))  # Complex Number

"""
Keywords in Python:
    These are all reserved keyworkds in Python and cannot be used as variable, class, function names:
    False      await      else       import     pass
    None       break      except     in         raise
    True       class      finally    is         return
    and        continue   for        lambda     try
    as         def        from       nonlocal   while
    assert     del        global     not        with
    async      elif       if         or         yield

"""


# ----------------- Data Structures -----------------
"""
Data Structures in Python: 
are used to store collections of data; 
Single structures that can hold multiple values..

Types:
- List: this is used to store sequence of items in a single variable using square brackets [].
    This is ordered, changeable, and allows duplicate values.

- Set: this is used to store multiple items in a single variable using curly braces {}.
    This is unordered, unchangeable, and does not allow duplicate values.

- Tuple:
    This is used to store multiple items in a single variable using parentheses ().
    This is ordered, unchangeable, and allows duplicate values.

- Dictionary:
    This is used to store data in key-value pairs using curly braces {}.
    This is ordered (as of Python 3.7), changeable, and does not allow duplicate keys.



Single structures that can hold multiple values.
"""
list_example = [1, 2, 3, 5656, 7676, 'hello', True, "234567890-", 3434.434]
list_2 = ["90", "hello", "world", 123, 456, 789, 0.1234, False]

# changeable
list_2[0] = "George"
list_2[1] = 1000000

# duplicate values
list_3 = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, {'key': 'value'}, {'key': 'value'}]
print("List: ", list_3)

# ------- SET --------
set_1 = {1, 2, 3, 4, 2345678, 64678, "jsdsnfo", True, 3.14159, 2, 3, 4}  # duplicate values will be removed

# unordered
print("Set: ", set_1)

# unchangeable - you cannot change items after creation
# set_1[5] = "Wisdom"

# adding items
set_1.add(2)

print("set_1: ", set_1)



# ------- TUPLE --------
tuple_1 = (1, 2, 2, 3, 4, 5,)

# ordered
print("tuple_1: ", tuple_1)

# unchangeable - you cannot change items after creation
# tuple_1[0] = "Changed" # error out
# tuple_1.append(100)  # error out
print(tuple_1)

print("tuple_1: ", tuple_1)



# ------ DICTIONARY --------
dict_1 = {
    "name": "George",
    "age": 30,
    "city": "New York"
}

print("Dictionary: ", dict_1)
print("Name: ", dict_1["name"], dict_1["age"])

# changeable
dict_1["name"] = {"first_name": "George", "last_name": "Smith"}
print("Updated Dictionary: ", dict_1)

# --- no duplicate keys allowed ---
dict_1 = {
    "first_name": "George",
    "age": 30,
    "city": "New York",
    "name": "Wisdom"  # this will overwrite the previous 'name' key
}
print("Dictionary with duplicate keys: ", dict_1)

