# This is a Python program to learn typecasting 😊🐍
# Typecasting = Changing a variable's data type (e.g., from string to integer) 🔄
# For example, turning "25" (text) into 25 (a number) or 3.5 (decimal) into "3.5" (text)

# Variables: Boxes 📦 that store different types of data
name = "John"  # String: Text like a name ✍️
age = 25  # Integer: Whole number 🔢
height = 5.9  # Float: Number with decimals 📏
is_student = True  # Boolean: True or False ✅❌

# print() shows stuff on the screen 🖥️
# Checking the type of each variable using type() 🕵️‍♂️
print(f"Type of name: {type(name)} ✍️")  # Shows: <class 'str'> (string)
print(f"Type of age: {type(age)} 🔢")  # Shows: <class 'int'> (integer)
print(f"Type of height: {type(height)} 📏")  # Shows: <class 'float'> (float)
print(f"Type of is_student: {type(is_student)} ✅")  # Shows: <class 'bool'> (boolean)

# Typecasting: Changing a variable’s type 🔄
# Example 1: String to Integer
age_str = "25"  # A string that looks like a number "25" ✍️
age_int = int(age_str)  # Turns "25" into the number 25 🔢
print(f"Age as an integer: {age_int} 🎂")  # Shows: 25

# Example 2: Float to Integer
gpa = 3.5  # A float (decimal number) 📏
gpa_int = int(gpa)  # Turns 3.5 into 3 (drops the decimal) 🔢
print(f"GPA as an integer: {gpa_int} 🎓")  # Shows: 3

# Example 3: Integer to String
age_str = str(age)  # Turns 25 (integer) into "25" (string) ✍️
print(f"Age as a string: {age_str} 🎂")  # Shows: "25"

# Example 4: Float to String
height_str = str(height)  # Turns 5.9 (float) into "5.9" (string) ✍️
print(f"Height as a string: {height_str} 📏")  # Shows: "5.9"

# Example 5: Boolean to String
is_student_str = str(is_student)  # Turns True (boolean) into "True" (string) ✍️
print(f"Is student as a string: {is_student_str} 🎒")  # Shows: "True"

# Example 6: String to List
my_string = "Hello"  # A string ✍️
my_list = list(my_string)  # Turns "Hello" into ['H', 'e', 'l', 'l', 'o'] 📋
print(f"String as a list: {my_list} 📝")  # Shows: ['H', 'e', 'l', 'l', 'o']

# More Typecasting Examples for Practice 🌟
# Example 7: String to Float
price_str = "10.99"  # A string that looks like a decimal number ✍️
price_float = float(price_str)  # Turns "10.99" into 10.99 (float) 📏
print(f"Price as a float: {price_float} 💵")  # Shows: 10.99

# Example 8: Integer to Float
quantity = 10  # An integer 🔢
quantity_float = float(quantity)  # Turns 10 into 10.0 (float) 📏
print(f"Quantity as a float: {quantity_float} 🍎")  # Shows: 10.0

# Example 9: String to Boolean
true_str = "True"  # A string that says "True" ✍️
true_bool = bool(true_str)  # Turns "True" into True (boolean) ✅
print(f"String as a boolean: {true_bool} ✅")  # Shows: True

# Example 10: Number to Boolean
number = 0  # An integer 🔢
number_bool = bool(number)  # Turns 0 into False (0 is False, any other number is True) ✅
print(f"Number as a boolean: {number_bool} ❌")  # Shows: False

# Example 11: List to String (using join)
char_list = ['H', 'i']  # A list of characters 📋
char_string = "".join(char_list)  # Turns ['H', 'i'] into "Hi" ✍️
print(f"List as a string: {char_string} 📝")  # Shows: "Hi"