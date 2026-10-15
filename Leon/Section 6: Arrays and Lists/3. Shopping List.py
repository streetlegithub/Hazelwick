# ask first and initialise variables
option = input("--- Shopping List ---\n1. Add an item\n2. Remove an item\n3. View the list\n4. Count items\n5. Quit\n\nChoose an option: ")
shopping_list = []
inList = False
# start while
while option != "5":
    inList = False
# 1. Add an item
    if option == "1":
        item = input("Item to add: ")
    # check if item in list
        for i in range(len(shopping_list)):
            if shopping_list[i] == item:
                inList = True
            else:
                inList = False
    # add to list if not already there
        if inList == False:
            shopping_list.append(item)
            print(f"{item} added\n")
        else:
            print(f"{item} is already on the list.\n")
# 2. Remove an item
    elif option == "2": 
        item = input("Item to remove: ")
    # check if item in list
        for i in range(len(shopping_list)):
            if shopping_list[i] == item:
                print(f"{item} has been removed from the list.\n")
                shopping_list.pop(i)
                inList = True
            else:
                inList = False
    # add to list if not already there
        if inList == False:
            print(f"{item} is not on the list\n")
# 3. View the list
    elif option == "3":
    # empty error handling
        if shopping_list == []:
            print("Your list is empty.\n")
    # print out list (with better formatting for human readability)
        else:
            for i in range(len(shopping_list)):
                print(f"{i+1}. {shopping_list[i]}")
# 4. Count items
    elif option == "4":
        print(f"Total items: {len(shopping_list)}")
# ending and error handling (edge cases)
    elif option == "5":
        break
    else:
        print("Invalid option, please choose 1-5.")
# ask again
    option = input("--- Shopping List ---\n1. Add an item\n2. Remove an item\n3. View the list\n4. Count items\n5. Quit\n\nChoose an option: ")
# when the loop is over
print("Goodbye!")