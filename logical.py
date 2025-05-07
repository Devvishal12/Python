# 🌟 Temperature Converter and Weather Advisor Project 🌟
# 📝 Combines temperature conversion (Celsius/Fahrenheit) and weather-based activity recommendations
# 📚 Uses logical operators (and, or, not) and emojis for clarity

# --- Temperature Conversion ---
# 📥 Get user input for temperature unit
unit = input("👉 Is this temperature in Celsius or Fahrenheit (C/F): 🌡️ ").lower()

# 📥 Get user input for temperature value
try:
    temp = float(input("👉 Enter the temperature: 🔢 "))
except ValueError:
    print("❌ Please enter a valid number for temperature")
    exit()

# 🔄 Perform temperature conversion
if unit == "c":
    # 🔄 Convert Celsius to Fahrenheit: °F = (°C * 9/5) + 32
    converted_temp = (temp * 9/5) + 32
    print(f"➕ {temp}°C = {converted_temp}°F 🌡️")
    # 📌 Store original unit and converted temp for weather check
    original_unit = "C"
    temp_celsius = temp  # Already in Celsius
elif unit == "f":
    # 🔄 Convert Fahrenheit to Celsius: °C = (°F - 32) * 5/9
    converted_temp = (temp - 32) * 5/9
    print(f"➖ {temp}°F = {converted_temp}°C 🌡️")
    # 📌 Store original unit and converted temp for weather check
    original_unit = "F"
    temp_celsius = converted_temp  # Converted to Celsius
else:
    print(f"❌ '{unit}' is not a valid unit (use C or F)")
    exit()

# --- Weather Condition Check ---
# 📥 Get user input for sunny condition
is_sunny_input = input("👉 Is it sunny? (yes/no): ☀️ ").lower()
is_sunny = is_sunny_input in ["yes", "y"]

# 📥 Get user input for raining condition
is_raining_input = input("👉 Is it raining? (yes/no): ☔ ").lower()
is_raining = is_raining_input in ["yes", "y"]

# 🔍 Check weather conditions using logical operators
if is_raining:
    # ☔ Raining: stay indoors regardless of temperature
    print("❌ It's raining, stay indoors! ☔")
elif temp_celsius > 35:
    # 🔥 Too hot: stay indoors
    print("❌ It's extremely hot, stay indoors! 🔥")
elif temp_celsius < 0:
    # ❄️ Too cold: stay indoors
    print("❌ It's extremely low and cold, stay indoors! ❄️")
elif is_sunny:
    # ☀️ Sunny conditions with 'and'
    if temp_celsius >= 28:
        print("✅ It's a great day for a picnic! 🧺")
    elif temp_celsius >= 20:
        print("✅ It's a nice day for a walk! 🚶")
    elif temp_celsius >= 10:
        print("✅ It's a bit chilly, but you can still enjoy the outdoors. 🧥")
    else:
        print("✅ It's cold but sunny, so you can still go outside. 🥶")
else:
    # 🌥️ Not sunny conditions with 'not'
    if temp_celsius >= 20:
        print("✅ It's warm but not sunny, good for a walk! 🚶")
    elif temp_celsius >= 10:
        print("✅ It's a bit chilly and cloudy, but you can still go outside. ☁️")
    else:
        print("❌ It's too cold and gloomy for outdoor activities. 😔")

# 🎉 Display final note
print(f"🌟 Weather advice based on {temp}°{original_unit} and current conditions.")