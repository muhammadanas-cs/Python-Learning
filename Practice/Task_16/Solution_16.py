marks = [70, 85, 70, 90, 85, 60, 90]

unique_marks = set(marks)

sorted_marks = sorted(unique_marks , reverse=True)

duplicates_removed = len(marks) - len(unique_marks)

print("Unique marks= ", sorted_marks)
print("Duplicates removed= ", duplicates_removed)