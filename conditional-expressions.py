# conditional- expression = A conditional expression is an expression that evaluates to a value based on a condition.

num = 4

print("Even" if num % 2 == 0 else "Odd")
#         print("✅ It's a bit chilly, wear a jacket! 🧥")
temp_celsius = 50  # Define temp_celsius with a value
wear_a_jacket = "✅ It's a bit chilly, wear a jacket! 🧥" if temp_celsius < 10 else "❌ No need for a jacket"
print(wear_a_jacket)
#         print("❌ No need for a jacket")
#     # ❄️ Cold conditions with 'or'
#     elif temp_celsius < 10 or temp_celsius > 35:
age = 10  # Define age with a value
status = "Adult" if age >= 18 else "Minor"
print(status)