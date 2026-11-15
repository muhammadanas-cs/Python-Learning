def is_prime(n):
    if n <= 1:
        return False
    for i in range(2,n):  # Check whether the number is divisible by any number from 2 to n-1
        if n % i == 0:
            return False
    return True

print("Prime number test:")
print(is_prime(7))
print(is_prime(10))

def factorial(n):
    result = 1  # Initialize with 1 because 1 is the identity element of multiplication.
    
    for i in range(1, n+1):
    # We use n + 1 because the ending value in range() is excluded.
    # For example, if n = 5, the loop runs:
    # 1, 2, 3, 4, 5
        result *= i
        
    return result

print("\nFactorial Tests:")
print(factorial(5))
print(factorial(4))

def count_vowels(text):
    count = 0
    
    for char in text:
        if char.lower() in "aeiou": 
        # .lower() converts the character into lowercase.
        # "E".lower() in "aeiou"
            count += 1
        
    return count

print("\nVowel Count Tests:")
print(count_vowels("Hello anas"))
print(count_vowels("Ronaldo"))

