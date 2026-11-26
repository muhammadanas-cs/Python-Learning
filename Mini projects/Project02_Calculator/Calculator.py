def calculator():
    print("Simple Calculations")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponential")
    print("6. Modulus")
    
    choice = input("Choose the operation(1-6): ")
    num1 = float(input("Enter first number= "))
    num2 = float(input("Enter second number= "))
    
    if choice == '1':
        print("Result= ", num1 + num2)
    elif choice == '2':
            print("Result= ", num1 - num2)
    elif choice == '3':
            print("Result= ", num1 * num2)
    elif choice == '4':
        if num2 != 0:
            print("Result= ", num1 / num2)
        else:
            print("Error! Can not divide by zero")
    elif choice == '5':
        print("Result= ", num1 ** num2)
    elif choice == '6':
        print("Result= ", num1 % num2)    
    else:
        print("Invalid choice")
calculator()        
    
        
    
    