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
    elif option == "3":
        if shopping_list == []:
            print("Your list is empty.\n")
    option = input("--- Shopping List ---\n1. Add an item\n2. Remove an item\n3. View the list\n4. Count items\n5. Quit\n\nChoose an option: ")