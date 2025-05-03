# This is my first Python program 😊🐍
# print() shows words or numbers on the screen 🖥️
print("I like momos 🥟")  # Prints "I like momos" to the screen

# Variables are like boxes 📦 that store information (text, numbers, etc.)
# Python has 4 main types of data:
# 1. String (str): Words or text inside quotes ✍️
# 2. Integer (int): Whole numbers like 1, 2, 3 🔢
# 3. Float (float): Numbers with decimals like 1.5 📏
# 4. Boolean (bool): Only True or False ✅❌

# Strings: Store text like names or emails 📝
name = "John"  # Saves the name "John" in a box called name 😄
food = "momos"  # Saves "momos" in a box called food 🥟
email = "gjkdhfjkghfjk@email"  # Saves an email in a box called email 📧

# Integers: Store whole numbers 🔢
age = 25  # Saves the number 25 in a box called age 🎂
quantity = 10  # Saves 10 in a box called quantity 🍎

# f-strings: A way to mix text and variables 🖨️
# f"Text {variable}" puts the variable's value into the text
print(f"Hello {name} 😄, you are {age} years old 🎂 and you like {food} 🥟. Your email is {email} 📧. You are buying {quantity} apple 🍎.")
# This prints a sentence using the values of name, age, food, email, and quantity

# Floats: Store numbers with decimals 📊
price = 10.99  # Saves 10.99 in a box called price 💰
gpa = 3.5  # Saves 3.5 in a box called gpa 🎓
distance = 10.5  # Saves 10.5 in a box called distance 🛤️

# Printing floats with f-strings 🖨️
print(f"The price of the apple is {price} 💵.")  # Shows the price
print(f"Your GPA is {gpa} 🎓.")  # Shows the GPA
print(f"The distance is {distance} km 🛣️.")  # Shows the distance

# Booleans: Store True or False ✅❌
is_student = True  # Saves True in a box called is_student 🎒
is_employee = False  # Saves False in a box called is_employee 💼

# if-else: Checks if something is True or False to decide what to print 🤔
# If the box has True, it runs the first part; if False, it runs the else part
if is_student:  # Checks if is_student is True
    print(f"{name} is a student 🎓.")  # Prints if True
else:  # Runs if is_student is False
    print(f"{name} is not a student 🚫.")

if is_employee:  # Checks if is_employee is True
    print(f"{name} is an employee 💼.")  # Prints if True
else:  # Runs if is_employee is False
    print(f"{name} is not an employee 🚫.")

# Printing booleans to see their values ✅
print(f"Is the person a student? {is_student} 🎒.")  # Shows True
print(f"Is the person an employee? {is_employee} 💼.")  # Shows False

# Lists: A way to store many items in one box 📋
# Example (not used here): my_list = ["apple", 5, 3.14, True] 🍎🔢
# Lists are like a shopping list: they hold many things in order