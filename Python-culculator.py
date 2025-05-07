# Python calculator

oprator = input ('👉 Enter the oprator (+ - * /): ')
num1 = float (input ('👉 Enter the first number: '))
num2 = float (input ('👉 Enter the second number: '))

print ('\n--- 🔢 BASIC OPERATIONS ---\n')

if oprator == '+':
    result = num1 + num2
    print (f'➕ {num1} + {num2} = {result}')
elif oprator == '-':
    result = num1 - num2
    print (f'➖ {num1} - {num2} = {result}')
elif oprator == '*':
    result = num1 * num2
    print (f'✖️ {num1} * {num2} = {result}')
elif oprator == '/':
    if num2 != 0:
        result = num1 / num2
        print (f'➗ {num1} / {num2} = {result}')
else:
    print (f'❌ {oprator}is not a valid oprator')  
