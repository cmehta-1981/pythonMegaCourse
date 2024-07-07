# experiment for reading the file from external path (outside pycharm)  , stored in local drive

while True:
    user_action = input("Type add , show , edit , complete or exit:- ")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter the to do:- ") + '\n'
            file = open(r'C:\Users\91784\Downloads\testfile.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open(r'C:\Users\91784\Downloads\testfile.txt', 'w')
            file.writelines(todos)
            file.close()
        case "show":
            file = open(r'C:\Users\91784\Downloads\testfile.txt', 'r')
            todos = file.readlines()
            file.close()

            for index, item in enumerate(todos):
                row = f"{index + 1}-{item}"
                print(row)
        case 'exit':
            print('exit from program')
            break
print("bye... bye")
