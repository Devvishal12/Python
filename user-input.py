# This program uses input() to ask the user for information 😊🐍
# input() = A function that asks a question, waits for the user to type an answer, and presses Enter 📝
# Whatever the user types comes back as a string (text) ✍️

# Example 1: Asking for the user's name
name = input("What is your name? ")  # Shows "What is your name?" and waits for the user to type and press Enter 😄
print(f"Hello, {name}! 👋")  # Prints a greeting with the user's name

# Example 2: Asking for the user's age
age = input("How old are you? ")  # Asks for age and waits for the user to type (comes as a string) 🎂
print(f"You are {age} years old! 🎂")  # Prints the age as typed

# Example 3: Asking for the user's favorite food
food = input("What is your favorite food? ")  # Asks for favorite food and waits for the user to type 🥟
print(f"Your favorite food is {food} 🥟")  # Prints the favorite food

# Typecasting: input() gives a string, so we convert it to a number for math 🔄
age = int(age)  # Turns the age string (e.g., "25") into an integer (25) 🔢
age_next = age + 1  # Adds 1 to the age (like next year's age) 🎉
print(f"Next year, you will be {age_next} years old! 🎉")  # Shows next year's age
age_last = age - 1  # Subtracts 1 from the age (like last year's age) 🎂
print(f"Last year, you were {age_last} years old! 🎉")  # Shows last year's age

# Example 4: Calculating the area of a rectangle
length = float(input("Enter the length of the area: "))  # Asks for length (converts to float for decimals) 📏
width = float(input("Enter the width of the area: "))  # Asks for width (converts to float for decimals) 📏
area = int(length) * int(width)  # Turns length and width to integers, then multiplies to get area 🔢
print(f"The area is {area} square units. 📐")  # Shows the calculated area

# Exercise: Shopping cart program 🛒
item = input("Enter the item you want to buy: ")  # Asks for the item name (stays a string) 📝
quantity = int(input("Enter the quantity you want to buy: "))  # Asks for quantity (converts to integer) 🔢
price = float(input("Enter the price of the item: "))  # Asks for price (converts to float for decimals) 💰
total_cost = quantity * price  # Multiplies quantity and price to get total cost 💵
print(f"The total cost for {quantity} {item}(s) is {total_cost} Rs. 🛍️")  # Shows the total cost

# More Examples for Practice 🌟
# Example 5: Asking for a temperature and converting it
temp = float(input("Enter the temperature in Celsius: "))  # Asks for temperature (converts to float) 🌡️
temp_fahrenheit = (temp * 9/5) + 32  # Converts Celsius to Fahrenheit using the formula
print(f"The temperature in Fahrenheit is {temp_fahrenheit}°F 🌡️")  # Shows the converted temperature

# Example 6: Asking for a yes/no question
likes_coding = input("Do you like coding? (yes/no): ")  # Asks a yes/no question 📝
if likes_coding.lower() == "yes":  # Checks if the answer is "yes" (ignores uppercase/lowercase)
    print("That's awesome! Keep coding! 🚀")
else:
    print("That's okay, maybe you'll like it later! 😊")