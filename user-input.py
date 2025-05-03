#input() = A function that waits for the user to type something and press Enter. It’s like asking a question and waiting for an answer. 
#📝

input("What is your name? ")  # Asks for the user's name and waits for them to type it and press Enter.

# Example: Asking for the user's name
name = input("What is your name? ")  # Waits for the user to type their name and press Enter.
print(f"Hello, {name}! 👋")  # Greets the user with their name.

# Example: Asking for the user's age
age = input("How old are you? ")  # Waits for the user to type their age and press Enter.
print(f"You are {age} years old! 🎂")  # Tells the user their age.
# Example: Asking for the user's favorite food
food = input("what is your favorate food?  ") # Waits for the user to type their favorite food and press Enter.

age = int(age)  # Converts the age from a string to an integer🔢
age = age + 1  # Adds 1 to the age (like saying "next year") 🎂
print(f"Next year, you will be {age} years old! 🎉")  # Tells the user their age next year.
age = age -1 # Subtracts 1 from the age (like saying "last year") 🎂
print(f"Last year, you were {age} years old! 🎉")  # Tells the user their age last year.
print(f"Your favorite food is {food} 🥟")  # Tells the user their favorite food.
# Example: Asking for the area of a rectangle
lenght = float(input("Enter the lenght of the Area: ")) # Waits for the user to type the length of the area and press Enter.
width = float(input("Enter the width of the Area: ")) # Waits for the user to type the width of the area and press Enter.
area = int(lenght) * int(width) # Calculates the area by multiplying the length and width.

print(f"The area is {area} square units.")  # Tells the user the area.

# Exercise 2 : Shooping card program
# Example: Asking for the user's shopping list
item = input("Enter the item you want to buy: ")  # Waits for the user to type the item and press Enter.
quantity = int(input("Enter the quantity you want to buy: "))  # Waits for the user to type the quantity and press Enter.
price = float(input("Enter the price of the item: "))  # Waits for the user to type the price and press Enter.
total_cost = quantity * price  # Calculates the total cost by multiplying the quantity and price.
print(f"The total cost for {quantity} {item}(s) is {total_cost} Rs.")  # Tells the user the total cost.
