# Suresh Shrestha
# 1/23/2026
# Module 2.2 Assignment

def calculate_total(price, quantity):
    """returns total cost = price * quantity."""
    total = price * quantity
    return total

def main():
    print("Simple Order Total Calculator")

    # Input
    price = float(input("Enter price of item: "))
    quantity = int(input("Enter quantity: "))

    # Function call
    total = calculate_total(price, quantity)

    # Output
    print(f"Total cost: ${total:.2f}")

if __name__ == "__main__":
    main()