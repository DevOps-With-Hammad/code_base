# Step 1: Create the initial shopping list
shopping_list = ["Milk", "Eggs", "Bread", "Bananas"]
# Step 2: Add "Apples" to the list
shopping_list.append("Apples")
print(shopping_list)
# Step 3: Remove "Bread" from the list
shopping_list.remove("Bread")
print(shopping_list)


# Step 4: Create the show_list function
def show_list(shopping_list) :
    for item in shopping_list :
        print(item)


show_list(shopping_list)

# Step 5: Create the total_items function
def total_items(shopping_list):
# Step 6: Display the shopping list and the total number of items
        print(len(shopping_list))

total_items(shopping_list)
