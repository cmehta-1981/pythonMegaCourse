mylist = ['a','b','c']
type(mylist)
mylist[0] = 'e'
print(mylist[1])
d = mylist[1]
print(type(d))
print(dir(list))

mylist.__setitem__(1,'d')
print(mylist)
print(mylist.__getitem__(1))


