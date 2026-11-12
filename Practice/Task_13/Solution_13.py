num = int(input("Enter a number= "))

if num > 0:
    print("Number is positive")
    if num % 2 == 0:
        print(num ,"is even number")
    else:
        print(num, "is odd")
elif num < 0:
    print("Number is negative")
    
else:
    print("Zero")
    
