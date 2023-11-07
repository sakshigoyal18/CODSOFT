# Prompting the user for input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

# Performing calculation based on the operation choice
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    # Checking for division by zero
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero is not allowed."
else:
    result = "Invalid operation. Please enter +, -, *, or /."

# Displaying the result
print("Result: ", result)