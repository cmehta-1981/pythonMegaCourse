# experiment for changing the text file path & keeping in another directory

while True:
    user_action = input("Type add , show , edit , complete or exit:- ")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter the to do:- ") + '\n'
            file = open('files/testing.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open('files/testing.txt', 'w')
            file.writelines(todos)
            file.close()
        case "show":
            file = open('files/testing.txt', 'r')
            todos = file.readlines()
            file.close()

            for index, item in enumerate(todos):
                row = f"{index + 1}-{item}"
                print(row)
        case 'exit':
            print('exit from program')
            break
print("bye... bye")
