import json

# Parent class
class Student:

    # Constructor: runs when object is created
    def __init__(self, name):
        self.name = name
        self.__marks = []  # Private list to store marks

    # Method to add marks
    def add_mark(self, m):
        if m < 0 or m > 100:
            raise ValueError("Invalid marks")  # Raise error if marks are invalid
        self.__marks.append(m)  # Add marks to list

    # Calculate average marks
    def average(self):
        return sum(self.__marks) / len(self.__marks)


# Child class inheriting Student
class ScholarshipStudent(Student):

    # Override parent average method
    def average(self):
        return min(super().average() + 5, 100)  # Add 5 bonus marks, maximum 100


# Create objects
s1 = Student("Ali")
s2 = ScholarshipStudent("Ahmed")


# Add marks using try-except
for student in [s1, s2]:
    try:
        student.add_mark(80)
        student.add_mark(90)
    except ValueError as e:
        print(e)


# Store names and averages in dictionary
data = {
    s1.name: s1.average(),
    s2.name: s2.average()
}


# Print students' averages
for name, avg in data.items():
    print(name, "Average:", avg)


# Write data into JSON file
try:
    with open("results.json", "w") as file:
        json.dump(data, file, indent=4)
    print("File saved successfully")

# Handle file writing error
except IOError:
    print("File could not be written")