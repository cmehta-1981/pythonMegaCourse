# exampl 1
new = []

for i in [1, 2, 3]:
    new.append(i + 10)

print(new)          # output [11, 12, 13]


# exampl 2
# List comprehensions examples
old = [1, 2, 3]
new = [i + 10 for i in old]
print(new)  # same as above # output [11, 12, 13]


# exampl 3

new = [i for i in ['a', 'b', 'c']]
print(new)      #out is ['a', 'b', 'c']