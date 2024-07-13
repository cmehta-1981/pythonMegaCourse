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
            file = open('todo.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open('todo.txt', 'w')
            file.writelines(todos)
            file.close()
        case "show":

            file = open('todo.txt', 'r')
            todos = file.readlines()
            file.close()

            new_todos = [item.strip() for item in todos]    # using list comprehensions

            for index, item in enumerate(new_todos):
                row = f"{index + 1}-{item}"
                print(row)
        case 'exit':
            print('exit from program')
            break
print("bye... bye")
