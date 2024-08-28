grocery_list = ['Milk', 'Honey', 'Bread', 'Corn flakes']
help = """Help
    A: Add item
    R: Remove item
    D: Delete list
    S: Sort list
    [ENTER]: print list
    SPACE: Quit program"""
run = True

print("*** Grocery List Manager ***")
while run:
    choice = input(">").upper()
    
    if choice == "A":
        item = input("Enter the item to add: ")
        grocery_list.append(item)
        print(f"{item} added to the list.")

    elif choice == "R":
        item = input("Enter the item to remove: ")
        if item in grocery_list:
            grocery_list.remove(item)
            print(f"{item} removed from the list.")
        else:
            print("Item not found in the list.")

    elif choice == "D":
        grocery_list = []
        print("The grocery list is now empty.")

    elif choice == "S":
        if grocery_list:
            grocery_list.sort()
            print("The grocery list has been sorted.")
        else:
            print("The grocery list is empty, no reason to sort it.")

    elif choice in ["P", ""] :
        if grocery_list:
            print("Items: ", ", ".join(grocery_list))
        else:
            print("The grocery list is empty.")

    elif choice == "H":
        print(help)

    elif choice == "Q":
        print("Exiting...")
        run = False

    else:
        print("Invalid choice. Please try again.")
    
    print("---")
    