def get_price():
    while True:
        try:
            price = float(input("Enter price:   "))
            return price
        except ValueError:
            print("Invalid decimal number. Please try again.")

def get_quantity():
    while True:
        try:
            quantity = int(input("Enter quantity:   "))
            return quantity
        except ValueError:
            print("Invalid integer. Please try again.")

def main():
    print("The Invoice Line Item Calculator\n")

    choice = "y"
    while choice == "y":
        price = get_price()
        quantity = get_quantity()
        total = price * quantity

        print()
        print(f"PRICE:     {price: .2f}")
        print(f"QUANTITY:  {quantity}")
        print(f"TOTAL:     {total: .2f}\n")

        choice = input("Enter another line item? (y/n): ").strip().lower()
        print()

    print("Bye!")
    input("Press any key to continue . . .")

if __name__ == "__main__":
    main() 


