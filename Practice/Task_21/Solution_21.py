# Store product records in a list of tuples
products = [
    ("Keyboard", 2500, 10),
    ("Mouse", 1200, 15),
    ("Monitor", 25000, 5),
    ("Headphones", 3500, 8),
    ("USB Drive", 1500, 20)
]

# Variable to store total value of all products
total_value = 0

# Display all product records
print("\n===== PRODUCT RECORDS =====")

for name, price, quantity in products:

    # Calculate stock value of each product
    stock_value = price * quantity

    print("Product Name:", name)
    print("Price: Rs.", price)
    print("Quantity:", quantity)
    print("Stock Value: Rs.", stock_value)
    print()

    # Add product value to total shop value
    total_value += stock_value

# Display total stock value
print("Total Shop Stock Value: Rs.", total_value)


# Search for a product
search = input("\nEnter product name to search: ")

found = False

for name, price, quantity in products:

    # Check whether entered product exists
    if name.lower() == search.lower():

        print("\nProduct Found!")
        print("Product Name:", name)
        print("Price: Rs.", price)
        print("Available Quantity:", quantity)

        found = True
        break

# Display message if product does not exist
if found == False:
    print("Product not found")