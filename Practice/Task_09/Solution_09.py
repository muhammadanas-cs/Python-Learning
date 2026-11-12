x = float(input("Enter first number : "))
y = float(input("Enter second number : "))

print("Addition = ", x+y)
print("Subtraction = ", x-y)
print("Multiplication = ", x*y)

if y != 0:
    print("Division = ", x/y)
    print("Modulus = ", x%y)
else:
    print("Division: Cannot divide by zero")
    print("Modulus: Cannot divide by zero")