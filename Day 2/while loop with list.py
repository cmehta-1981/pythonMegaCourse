py_string = 'enter the todo: \n'

py_list = []

while True:  # print infinite data, loop never end
    py_todo = input(py_string)
    print(py_todo.capitalize())
    py_list.append(py_todo)
    print(py_list)
