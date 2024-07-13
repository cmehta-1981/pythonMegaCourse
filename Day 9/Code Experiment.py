# open method default have read mode
with open('todo.txt') as file:
    print(file.read())
    print(file.read())  # print nothing because above print function already read the file & and the reading hence
    # this print does not have anything to read

# or

with open('todo.txt', 'r') as file:
    print(file.read())
    content = file.read()
    print(content)  # print nothing because above print function already read the file & and the reading hence
    # this print does not have anything to read

# OR

with open('todo.txt', 'r') as file:
    content = file.read()
print(content)  # print function gives the output
print(content)
