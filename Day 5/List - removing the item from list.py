mylsit = ['a', 'b', 'c']
print(mylsit)  # ['a', 'b', 'c']

'''
pop(self, index=-1, /)
    Remove and return item at index (default last).
'''

mylsit.pop()  # pop last item
mylsit.pop(1)  # pop first item from list

'''
help(list.clear)
Help on method_descriptor:
clear(self, /)
    Remove all items from list.
    
mylsit.clear()
mylsit
[] -  return empty list 
'''
mylsit.clear()

'''
remove(self, value, /)
    Remove first occurrence of value.
    Raises ValueError if the value is not present.
'''

mylsit.remove('a')
