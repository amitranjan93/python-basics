print("========= Calculator ======================")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(f"Addition: {num1 + num2}")
print(f"Subtraction: {num1 - num2}")
print(f"Multiplication: {num1 * num2}")
if num2 == 0:
    print("Error: Cannot divide by zero.")
else:
    print(f"Division: {num1 / num2}")