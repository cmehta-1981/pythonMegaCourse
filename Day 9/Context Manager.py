'''
removing the extra one line between the two line , improving the for loop using strip in show case
1-Python is great

2-I Love Python

'''

while True:
    user_action = input("Type add , show , edit , complete or exit:- ")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter the to do:- ") + '\n'
            with open('todo.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)
            
            with open('todo.txt', 'w') as file:
                file.writelines(todos)

        case "show":
            with open('todo.txt', 'r') as file:
                todos = file.readlines()

            new_todos = [item.strip() for item in todos]  # using list comprehensions

            for index, item in enumerate(new_todos):
                row = f"{index + 1}-{item}"
                print(row)
        case 'exit':
            print('exit from program')
            break
print("bye... bye")
