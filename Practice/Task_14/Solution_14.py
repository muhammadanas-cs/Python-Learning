items = []

for i in range(5):
    item = input("enter an item: ")
    items.append(item)
    
items.sort()

print("Sorted list:", items)
print("Total number of items:", len(items))