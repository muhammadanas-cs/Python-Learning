
Students_class = {
    "S101": {"name": "Ali", "marks": [70, 80, 90]},
    "S102": {"name": "Anas", "marks": [100, 82, 90]},
    "S103": {"name": "Ahmed", "marks": [72, 84, 90]},
    "S104": {"name": "Adnan", "marks": [60, 100, 90]},
    "S105": {"name": "Afnan", "marks": [20, 40, 90]}
}

print("STUDENT RESULTS")

for student_id, details in Students_class.items(): # .items() returns both keys and values from a dictionary.
    name = details["name"] # Access the student's name from the nested dictionary.
    marks = details["marks"] # Access the student's marks list.
    
    total = sum(marks)
    average = total / len(marks)
    
    print("ID: ", student_id)
    print("Name: ", name)
    print("Total Marks: ", total)
    print("Average Marks: ", round(average,4) ) # Round the average to four decimal places.
    print()
    
top_student = max(
    Students_class.values(), # .values() returns all student records without their IDs.
    key =lambda s: sum(s["marks"]) # Lambda calculates the total marks of a student.
)
 
lowest_student = min(
    Students_class.values(),
    key =lambda s: sum(s["marks"])
)   

print("Top Student: ", top_student["name"],
      "Total:", sum(top_student["marks"]))

print("Lowest Student: ", lowest_student["name"],
      "Total:", sum(lowest_student["marks"]))

print("\nAdd a new student")

new_id = input("Enter student_ID:")

if new_id in Students_class:
    print("Student ID already exists.")
    
else:
    new_name= input("Enter the name:")
    
    new_marks = [] # Create an empty list to store the student's marks.
    for i in range (3):
        mark = int(input(f"Enter marks for subject {i+1}: "))
        new_marks.append(mark)
    
    Students_class[new_id] = {
    "name": new_name,
    "marks": new_marks
}    

    print("Student added")

print("\nEdit Student Marks")

edit_id = input("Enter student ID: ")

if edit_id in Students_class:
    print("Student: ", Students_class[edit_id]["name"])
    
    for i in range(3):
        
        mark = int(input(f"Enter new marks for subject {i+1}: "))
        Students_class[edit_id]["marks"][i]= mark # Update the marks at the current list index.
    
    print("Marks updated successfully.")
else:
    print("student not found.")
    
print("\nDelete Student")

delete_id = input("enter student id to be deleted: ")

if delete_id in Students_class:
    deleted_student = Students_class.pop(delete_id)
    print(deleted_student["name"], "deleted successfully. ")
else:
    print("Student not found")
    
print("\nFINAL STUDENT RECORDS")

for student_id, details in Students_class.items():
    total = sum(details["marks"])
    average = total / len(details["marks"])

    print(
        student_id,
        details["name"],
        "Marks:", details["marks"],
        "Total:", total,
        "Average:", round(average, 2)
    )