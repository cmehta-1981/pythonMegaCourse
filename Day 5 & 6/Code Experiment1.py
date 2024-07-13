for i, j in enumerate("Python"):
    print(i, j)

a = enumerate("Python")
print(a)  # represent an enumerate object hence python does not understand how to print the value
print(list(a)) # we can print list objet , output  = [(0, 'P'), (1, 'y'), (2, 't'), (3, 'h'), (4, 'o'), (5, 'n')]
