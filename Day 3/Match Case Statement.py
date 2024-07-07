todos = []

while True:
    user_action = input('Type add or show or exit: ')

    match user_action:
        case 'add':
            todo = input('Enter to do: ')
            todos.append(todo)
            print(todos)
        case 'show':
            print(todos)
        case 'exit':
            print('exit from program')
            break

print('Bye ! Bye1')

