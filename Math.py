import math

print("🔮 WELCOME TO THE ULTIMATE MATH TEMPLE 🧠💥")
print("This program does... basically everything mathy 😅\n")

# Inputs with error handling
try:
    a = float(input("👉 Enter the first number (a): "))
    b = float(input("👉 Enter the second number (b): "))
except EOFError:
    print("❌ Error: No input provided. Using default values a=1, b=2.")
    a, b = 1.0, 2.0

print("\n--- 🔢 BASIC OPERATIONS ---\n")
print(f"➕ {a} + {b} = {a + b}")
print(f"➖ {a} - {b} = {a - b}")
print(f"✖️ {a} * {b} = {a * b}")
print(f"➗ {a} / {b} = {a / b if b != 0 else '∞'}")
print(f"📏 Floor division: {a} // {b} = {a // b if b != 0 else 'undefined'}")
print(f"🧩 Modulo: {a} % {b} = {a % b if b != 0 else 'undefined'}")
print(f"🔼 Power: {a} ** {b} = {a ** b}")
print(f"⚡ math.pow({a}, {b}) = {math.pow(a, b)}")

print("\n--- 🧠 ADVANCED MATH ---\n")
print(f"📐 sqrt({a}) = {math.sqrt(a) if a >= 0 else 'imaginary'}")
print(f"📘 log({a}) = {math.log(a) if a > 0 else 'undefined'}")
print(f"📗 log10({a}) = {math.log10(a) if a > 0 else 'undefined'}")
print(f"📙 log2({a}) = {math.log2(a) if a > 0 else 'undefined'}")
print(f"🧮 ceil({a}) = {math.ceil(a)}")
print(f"🧮 floor({a}) = {math.floor(a)}")
print(f"✂️ trunc({a}) = {math.trunc(a)}")
print(f"🔁 round({a}, 2) = {round(a, 2)}")
print(f"🎯 fabs({a}) = {math.fabs(a)}")

print("\n--- 🔢 MATH CONSTANTS ---")
print(f"π (pi) = {math.pi}")
print(f"e (Euler’s number) = {math.e}")
print(f"τ (tau) = {math.tau}")
print(f"Infinity = {math.inf}")
print(f"NaN = {math.nan}")

print("\n--- 🌍 TRIGONOMETRY ---\n")
print(f"🌀 sin({a}) = {math.sin(a)}")
print(f"🌊 cos({a}) = {math.cos(a)}")
print(f"🏹 tan({a}) = {math.tan(a)}")
print(f"🔁 radians({a}) = {math.radians(a)}")
print(f"↩️ degrees({a}) = {math.degrees(a)}")

print("\n--- 🌐 HYPERBOLIC FUNCTIONS ---\n")
print(f"sinh({a}) = {math.sinh(a)}")
print(f"cosh({a}) = {math.cosh(a)}")
print(f"tanh({a}) = {math.tanh(a)}")

print("\n--- 🎲 COMBINATORICS & MISC ---\n")
if a.is_integer() and a >= 0:
    print(f"🎲 factorial({int(a)}) = {math.factorial(int(a))}")
    if b.is_integer() and b >= 0:
        print(f"📦 comb({int(a)}, {int(b)}) = {math.comb(int(a), int(b))}")
        print(f"📂 perm({int(a)}, {int(b)}) = {math.perm(int(a), int(b))}")
else:
    print("❌ Cannot compute factorial/comb/perm unless both numbers are non-negative integers.")

print(f"📐 hypot({a}, {b}) = {math.hypot(a, b)}")

if a.is_integer() and b.is_integer():
    print(f"📏 GCD({int(a)}, {int(b)}) = {math.gcd(int(a), int(b))}")
    print(f"📐 LCM({int(a)}, {int(b)}) = {math.lcm(int(a), int(b))}")
else:
    print("❌ GCD/LCM only work with integers.")

print("\n--- 🧪 CHECKS & COMPARISONS ---\n")
print(f"Is {a} finite? {math.isfinite(a)}")
print(f"Is {a} infinite? {math.isinf(a)}")
print(f"Is {a} NaN? {math.isnan(a)}")
print(f"copysign({a}, {b}) = {math.copysign(a, b)}")

print("\n🎉 That’s it! You’ve just unlocked the full power of Python math 🧙‍♂️💻")

print("\n--- 🟢 EXTRA: CIRCLE CALCULATIONS ---")
try:
    radius = float(input("👉 Enter the radius of a circle: "))
except EOFError:
    print("❌ Error: No input provided. Using default radius=1.")
    radius = 1.0
area = math.pi * radius ** 2
circumference = 2 * math.pi * radius
print(f"🟢 Area of the circle = {area:.2f} square units")
print(f"🟢 Circumference of the circle = {circumference:.2f} units")