
while True:
    print("\n===== Expense Tracker =====")
    print("1. Add an expense")
    print("2.  total")
    print("3. Exit")
    choice = input("select ")

    if choice == "1":
        item = input("item ")
        
        item = item.replace(",", " ")
        try:
            amount = float(input(" Rs. "))
            with open("expenses.txt", "a") as f:
                f.write(f"{item},{amount}\n")
            print(" expense saved!")
        except ValueError:
            print("type a number")
    elif choice == "2":
        total = 0
        try:
            with open("expenses.txt", "r") as f:
                for line in f:
                    item, amount = line.strip().split(",")
                    print(f"{item:<15} Rs. {amount}")
                    total += float(amount)
            print(f"\nTotal: Rs. {total}")
        except FileNotFoundError:
            print("Nothing here ")

    elif choice == "3":
        print("byy")
        break

    else:
        print(" type 1, 2 or 3.")
