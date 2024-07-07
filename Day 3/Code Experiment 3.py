'''
modify the cases
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
        case 'show' | 'display':    # show or display both show the result, both show & display out will be same
            #   print(todos)    # output = ['line1', 'line2', 'line3'] print in list format
            for item in todos:
                item = item.title()     # first letter of each word capitalized
                print(item)  # output = line1 , line2 , print in normal string
        case 'exit':
            print('Exit from program')
            break

print('Bye ! Bye1')
