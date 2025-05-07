# This program converts weight from kg to lb or keeps it in kg and calculates BMI 😊

def convert_weight(weight: float, unit: str) -> tuple[float, str]:
    """Convert weight between kg and lb 🏋️‍♂️
    
    Args:
        weight: Your weight in kg (a number)
        unit: The unit you want ('lb' or 'kg')
    
    Returns:
        A pair: (converted weight, unit name)
    
    Raises:
        ValueError: If unit is not 'lb' or 'kg'
    """
    # Make unit lowercase to avoid case issues (e.g., 'LB' becomes 'lb')
    unit = unit.lower()
    
    # If user wants pounds, multiply kg by 2.20462
    if unit == "lb":
        return weight * 2.20462, "lb"
    # If user wants kg, no change needed since input is already kg
    elif unit == "kg":
        return weight, "kg"
    # If unit is wrong, show error
    else:
        raise ValueError("Invalid unit. Please enter 'lb' or 'kg'.")

def calculate_bmi(weight: float, height_cm: float) -> float:
    """Calculate BMI using weight in kg and height in cm 📏
    
    Args:
        weight: Weight in kg
        height_cm: Height in cm
    
    Returns:
        BMI value
    
    Raises:
        ValueError: If height is zero or negative
    """
    # Convert height from cm to meters (1 cm = 0.01 m)
    height_m = height_cm / 100
    # Check if height is valid
    if height_m <= 0:
        raise ValueError("Height must be greater than zero.")
    # BMI = weight (kg) / (height (m) * height (m))
    return weight / (height_m * height_m)

def get_valid_float(prompt: str) -> float:
    """Ask user for a number and make sure it's valid 🔢
    
    Args:
        prompt: The question to ask user
    
    Returns:
        A valid number (float)
    
    Raises:
        ValueError: If user enters something that's not a number
    """
    # Keep asking until a valid number is entered
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            # If input is not a number, show error and try again
            print("❌ Please enter a valid number.")

def main():
    """Main part of the program that runs everything 🚀"""
    try:
        # Ask for weight and height, make sure they're numbers
        weight = get_valid_float("👉 Enter your weight in kg: ")
        height = get_valid_float("👉 Enter your height in cm: ")
        # Ask for unit (lb or kg)
        unit = input("👉 Enter the unit you want to convert to (lb or kg): ").strip()

        # Convert the weight and get the result
        converted_weight, unit = convert_weight(weight, unit)
        # Calculate BMI
        bmi = calculate_bmi(weight, height)
        # Show the weight result with 2 decimal places
        print(f"Your weight in {unit} is: {converted_weight:.2f} {unit} 😊")
        # Show BMI with 2 decimal places
        print(f"Your BMI is: {bmi:.2f} 📏")

    except ValueError as e:
        # If something goes wrong (like wrong unit or zero height), show error
        print(f"❌ Error: {e}")

# Run the program if this file is run directly
if __name__ == "__main__":
    main()