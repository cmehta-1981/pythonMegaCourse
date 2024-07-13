mylist = ["John", "Joya", "Aman", "Raj"]
mylist.sort()  # default in ascending order
mylist.sort(reverse=False)  # in ascending order
# mylist.sort(reverse=True)  # in descending order

for index, item in enumerate(mylist):
    row = f"{index + 1}.{item.capitalize()}"
    print(row)


for i, j in enumerate("abcd"):
    print(i.capitalize())