"""
Assign a list to the variable temperatures. The list should contain three items, a float, an integer, and a string.

"""

temperatures = ['10.1','11','Python']

temperatures.remove('11')

menu = ["pasta", "pizza", "salad"]

for i, j in enumerate(menu):
    print(f"{i}.{j}")


menu = ["pasta", "pizza", "salad"]

user_choice = int(input("Enter the index of the item: "))

message = f"You chose {menu[user_choice]}."
print(message)
