# 📥 Get user input for temperature unit and convert to lowercase for flexibility
unit = input("👉 Is this temperature in Celsius or Fahrenheit (C/F): ").lower()

# 🌡️ Get user input for temperature and convert to float
try:
    temp = float(input("👉 Enter the temperature: "))
except ValueError:
    print("❌ Please enter a valid number for temperature")
    exit()

# 🔍 Check if the unit is Celsius
if unit == "c":
    # 🔄 Convert Celsius to Fahrenheit: °F = (°C * 9/5) + 32
    converted_temp = (temp * 9/5) + 32
    # 🖨️ Print original and converted temperature
    print(f'➕ {temp}°C = {converted_temp}°F')
# 🔍 Check if the unit is Fahrenheit
elif unit == "f":
    # 🔄 Convert Fahrenheit to Celsius: °C = (°F - 32) * 5/9
    converted_temp = (temp - 32) * 5/9
    # 🖨️ Print original and converted temperature
    print(f'➖ {temp}°F = {converted_temp}°C')
# ⚠️ Handle invalid unit input
else:
    # 🖨️ Print error message for unrecognized unit
    print(f'❌ {unit} is not a valid unit')