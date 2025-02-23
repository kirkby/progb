from grocery_list import GroceryList

grocery_list = []
grocery_list = GroceryList()

while True:
    print("Choose an action:")
    print("1. Add to list")
    print("2. Remove from list")
    print("3. Print list")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter the item to add: ")
        item_count = int(input("Enter the number of items to add: "))
        grocery_list.add_item(item, item_count)
    elif choice == "2":
        item = input("Enter the item to remove: ")
        item_count = int(input("Enter the number of items to remove: "))
        grocery_list.remove_item(item, item_count)
    elif choice == "3":
        grocery_list.print_list()
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
while True:
    print("Choose an action:")
    print("1. Add to list")
    print("2. Remove from list")
    print("3. Print list")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter the item to add: ")
        grocery_list.append(item)
        print(f"{item} added to the list.")
    elif choice == "2":
        item = input("Enter the item to remove: ")
        if item in grocery_list:
            grocery_list.remove(item)
            print(f"{item} removed from the list.")
        else:
            print("Item not found in the list.")
    elif choice == "3":
        if grocery_list:
            print("Grocery List:")
            for item in grocery_list:
                print(item)
        else:
            print("The grocery list is empty.")
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")