#Added inputs for drinks and appetizers and added it to the subtotal.

child_meal = float(input("What is the price of a child's meal? "))

adult_meal = float(input("What is the price of an adult's' meal? "))

appetizers = float(input("What is the price of the appetizers bought? "))

drinks = float(input("What is the price of drinks bought? "))

number_of_children = int(input("How many children are there? "))

number_of_adults = int(input("How many adults are there? "))

subtotal = (child_meal * number_of_children) + (adult_meal * number_of_adults) + appetizers + drinks

print()
print(f"Subtotal: ${subtotal:.2f}")

tax_rate = float(input("What is the sales tax rate? "))
sales_tax = (tax_rate / 100) * subtotal
total = sales_tax + subtotal

print(f"Sales Tax: ${sales_tax:.2f}")
print(f"Total: ${total:.2f}")

print()

payment_amount = float(input("What is the payment amount? "))
change = payment_amount - total

print(f"Change ${change:.2f}")



