todos = []

while True:
    user_action = input('Type add or edit or show or exit: ')

    match user_action:
        case 'add':
            todo = input('Enter todo:- ')
            todos.append(todo)
            print(todos)
        case 'show' | 'display':
            for index ,item in enumerate(todos):    # displays number /indexing of the output(0 - clean)
                row = f"{index}-{item}"             # removing the space after number , out =  (0-clean)
                print(row)
        case 'edit':
            number = int(input('enter the number to edit:- '))
            number = number -1
            print(todos[number])
            new_todo = input('Enter new to do ')    # add new item into the list
            todos[number] = new_todo
            print('item has been added into the list')
        case 'exit':
            print('exit from program')
            break

print('Bye ! Bye1')
