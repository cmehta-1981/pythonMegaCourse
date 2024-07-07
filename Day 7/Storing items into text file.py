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
            # "todos" is not recognize when never execute "add" case , if we run "add" case first then 'show' case
            # will work fine , this will fix in reading text from file class
            for index, item in enumerate(todos):
                row = f"{index+1}-{item}"
                print(row)
        case 'exit':
            print('exit from program')
            break
print("bye... bye")
