num1 = float(input("Enter first number= "))
opeartor = input("Choose the operator (+, -, *, /): ")
num2 = float(input("Enter Second number= "))

if opeartor == "+":
    print("Result = ", num1 + num2)

elif opeartor == "-":
    print("Result = ", num1 - num2)
    
elif opeartor == "*":
    print("Result = ", num1 * num2)
    
elif opeartor == "/":
    if num2 != 0:
        print("Result = ", num1 / num2)
    else:
        print("Cannot Divide by zero")
        
else:
    print("Invalid operator")
