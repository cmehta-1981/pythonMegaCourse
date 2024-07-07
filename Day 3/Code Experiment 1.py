'''
    if does not match any case then how program works
    in that case need to add one more case statement with any name
'''

todos = []

while True:
    user_action = input('Type add or show or exit: ')
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input('Enter to do: ')
            todos.append(todo)
            print(todos)
        case 'show':
            #   print(todos)    # output = ['line1', 'line2', 'line3'] print in list format
            for item in todos:
                print(item)  # output = line1 , line2 , print in normal string
        case 'exit':
            print('exit from program')
            break
        case _:         # this statement will execute if does not match any above case
            print('hey ,  Entered string are unknown ')


print('Bye ! Bye1')
