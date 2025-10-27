# W05 Project: Shopping Cart 
# Creativity: Added quantity support so users can buy multiples of the same item,
# and prices are neatly aligned for readability.

def main():
    print("Welcome to the Shopping Cart Program!")

    # Lists to store item names, prices, and quantities
    items = []
    prices = []
    quantities = []

    # Menu loop
    while True:
        print("\nPlease select one of the following: ")
        print("1. Add item")
        print("2. View cart")
        print("3. Remove item")
        print("4. Compute total")
        print("5. Quit")

        choice = input("Please enter an action: ")

        if choice == "1":
            # Add item
            item = input("What item would you like to add? ").strip()
            try:
                price = float(input(f"What is the price of '{item}'? "))
                qty = int(input(f"How many '{item}' would you like to add? "))
            except ValueError:
                print("Invalid input. Please enter numeric values for price and quantity.")
                continue

            items.append(item)
            prices.append(price)
            quantities.append(qty)
            print(f"'{qty} x {item}' at ${price:.2f} each has been added to the cart.")

        elif choice == "2":
            # View cart
            if len(items) == 0:
                print("Your shopping cart is empty.")
            else:
                print("The contents of the shopping cart are:")
                for i, (item, price, qty) in enumerate(zip(items, prices, quantities), start=1):
                    total_item_price = price * qty
                    print(f"{i}. {item} (x{qty}) - ${price:.2f} each | Total: ${total_item_price:.2f}")

        elif choice == "3":
            # Remove item
            if len(items) == 0:
                print("Your shopping cart is empty. Nothing to remove.")
            else:
                print("The contents of the shopping cart are:")
                for i, (item, price, qty) in enumerate(zip(items, prices, quantities), start=1):
                    print(f"{i}. {item} (x{qty}) - ${price:.2f}")

                try:
                    remove_index = int(input("Which item would you like to remove? ")) - 1
                    if 0 <= remove_index < len(items):
                        removed_item = items.pop(remove_index)
                        prices.pop(remove_index)
                        quantities.pop(remove_index)
                        print(f"'{removed_item}' has been removed from the cart.")
                    else:
                        print("Sorry, that is not a valid item number.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

        elif choice == "4":
            # Compute total
            if len(items) == 0:
                print("Your shopping cart is empty. Total = $0.00")
            else:
                total = sum(price * qty for price, qty in zip(prices, quantities))
                print(f"The total price of the items in the shopping cart is ${total:.2f}")

        elif choice == "5":
            print("Thank you for shopping with us. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

# Run the program
main()
