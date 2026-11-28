subjects = []
marks = []

# Get number of subjects
while True:
    try:
        n = int(input("Enter the number of subjects: "))
        if n > 0:
            break
        print("Enter at least 1 subject.")
    except ValueError:
        print("Please enter a valid number.")

# Get subject names and marks
for i in range(n):
    sub = input(f"\nEnter subject {i+1} name: ")

    while True:
        try:
            score = float(input(f"Enter marks for {sub}: "))

            if 0 <= score <= 100:
                break
            print("Marks must be between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")

    subjects.append(sub)
    marks.append(score)

# Calculate result
total = sum(marks)
percentage = total / n

# Calculate grade
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

# Display result
print("\n========== RESULT CARD ==========")

# Display subject name left aligned (20 spaces) and marks right aligned with 2 decimal places
for i in range(n):
    print(f"{subjects[i]:<20} {marks[i]:>.2f}")

print("---------------------------------")
print(f"Total Marks : {total:.2f} / {n*100}")
print(f"Percentage  : {percentage:.2f}%")
print(f"Grade       : {grade}")
print("=================================")
