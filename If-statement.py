# if = Do something if the condition is true
# else = Do something else if the condition is false

age = int(input("Enter your age: "))  # Asks for age and converts to integer 🔢
if age < 18:  # Checks if age is less than 18
    print("You are a minor. 👶")  # Prints if true
elif age >= 18 and age < 65:  # Checks if age is between 18 and 65
    print("You are an adult. 👨‍🦳")  # Prints if true
elif age <0:
    print("Invalid age. Please enter a positive number.")    
else:  # Runs if age is 65 or older
    print("You are a senior citizen. 👴")  # Prints if true

response = input("Do you want to continue? (yes/no): ")  # Asks if the user wants to continue
if response.lower() == "yes":  # Checks if the answer is "yes"
    print("Great! Let's continue. 🚀")  # Prints if true    
else:
    print("Okay, goodbye! 👋")

# This program uses if-else statements to check conditions and print messages accordingly 😊🐍

name = input("Enter your name: ")  # Asks for the user's name
if name == " ":
    print("You didn't enter a name. Please try again.")  # Prints if the name is empty
else:
    print(f"Hello, {name}! 👋")

# Boolean variables: True or False ✅❌
is_student = True  # Saves True in a box called is_student 🎒

if is_student:  # Checks if is_student is True
    print(f"{name} is a student 🎓.")  # Prints if True
else:
    print(f"{name} is not a student 🚫.")

# This program uses if-else statements to check conditions and print messages accordingly 😊🐍
#     
