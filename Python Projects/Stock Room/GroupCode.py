# Acklam Sports - Stock Room
# Part 1 reads and adds to the order book (orders.txt)
# Part 2 reads, checks and saves the stock list (stock.csv)

# os lets us find the folder this program is saved in, so the files are
# always found even if the program is run from a different folder
import os

FOLDER = os.path.dirname(os.path.abspath(__file__))
ORDERS_FILE = os.path.join(FOLDER, "orders.txt")
SUMMARY_FILE = os.path.join(FOLDER, "summary.txt")
STOCK_FILE = os.path.join(FOLDER, "stock.csv")


# ==================================================================
# PART 1: THE ORDER BOOK
# ==================================================================
print("--- Order book ---")

# CORE: read every order from the file
# "r" means read. Each line comes with a hidden "\n" (new line) on the end,
# so strip() takes it off - otherwise "Football\n" would never equal "Football"
orders = []
with open(ORDERS_FILE, "r") as file:
    for line in file:
        order = line.strip()
        if order != "":              # skip any empty lines
            orders.append(order)

# Show every order, numbered from 1 (not 0 like list positions)
number = 1
for order in orders:
    print(f"{number}. {order}")
    number += 1

# CORE + STRETCH: count the orders for one item
# .lower() on both sides means "football" still matches "Football"
item = input("\nItem: ").strip()
count = 0
for order in orders:
    if order.lower() == item.lower():
        count += 1
print(f"Orders for {item}: {count}")

# SECURE: add a new order to the end of the file
# "a" means append - it adds to the end and keeps what is already there
# ("w" would wipe the whole file first)
new_order = input("\nNew order: ").strip()
if new_order == "":
    print("A blank order can't be added, so nothing was added.")
else:
    with open(ORDERS_FILE, "a") as file:
        file.write(new_order + "\n")
    print(f"Added: {new_order}")

# Read the file again to prove the new order really got saved
orders = []
with open(ORDERS_FILE, "r") as file:
    for line in file:
        if line.strip() != "":
            orders.append(line.strip())
print(f"The order book now holds {len(orders)} orders")

# STRETCH: the summary
# A dictionary stores each item once, with its count as the value
# e.g. {"Football": 3, "Shin pads": 2, ...}
totals = {}
for order in orders:
    if order in totals:
        totals[order] += 1           # seen before: add one
    else:
        totals[order] = 1            # first time: start at one

# "w" means write - summary.txt is made fresh each time
with open(SUMMARY_FILE, "w") as file:
    for order, amount in totals.items():
        file.write(f"{order}: {amount}\n")

# Read summary.txt back and show it
print("\nSummary")
with open(SUMMARY_FILE, "r") as file:
    for line in file:
        print(line.strip())


# ==================================================================
# PART 2: THE STOCK LIST
# ==================================================================
print("\n--- Stock list ---")

# CORE: read the stock
# Each line looks like "Football,12.99,8". split(",") breaks it into
# ["Football", "12.99", "8"] - but they are all text (strings),
# so price becomes a float (decimal) and stock becomes an int (whole number)
stock_list = []
with open(STOCK_FILE, "r") as file:
    headings = file.readline().strip()     # first line: item,price,stock
    for line in file:                      # carries on from line 2
        if line.strip() == "":
            continue
        parts = line.strip().split(",")
        name = parts[0]
        price = float(parts[1])
        stock = int(parts[2])
        stock_list.append([name, price, stock])

# Show each item and add up the stock in all
# :.2f shows a number to two decimal places, so 6.5 shows as 6.50
total_stock = 0
for record in stock_list:
    print(f"{record[0]}: £{record[1]:.2f}, {record[2]} in stock")
    total_stock += record[2]
print(f"In stock in all: {total_stock}")

# Look up one item - found stays None if the item is not in the list
item = input("\nItem: ").strip()
found = None
for record in stock_list:
    if record[0].lower() == item.lower():
        found = record

if found is None:
    print(f"{item} is not sold here")
else:
    print(f"{found[0]}: {found[2]} in stock at £{found[1]:.2f}")

    # SECURE: does the shop have enough?
    # input() always gives text, so it must become an int before it can be
    # compared with the stock. try/except catches typing like "two" or "abc"
    while True:
        try:
            wanted = int(input("How many does the customer want? "))
        except ValueError:
            print("Please type a whole number.")
            continue
        if wanted < 1:
            print("The number must be 1 or more.")
        else:
            break

    if wanted <= found[2]:
        print(f"Yes, there are enough {found[0]} in stock")

        # STRETCH: save the sale
        # Take them off the stock, then write the WHOLE file again,
        # headings first, joining each record back into one line with commas
        found[2] -= wanted
        with open(STOCK_FILE, "w") as file:
            file.write(headings + "\n")
            for record in stock_list:
                file.write(f"{record[0]},{record[1]:.2f},{record[2]}\n")
        print(f"Sold {wanted}. {found[0]} now has {found[2]} in stock")
    else:
        print(f"No, there are only {found[2]} {found[0]} in stock")

# STRETCH: the stock's value - each price times its stock, all added up
stock_value = 0
for record in stock_list:
    stock_value += record[1] * record[2]
print(f"\nStock value: £{stock_value:.2f}")
