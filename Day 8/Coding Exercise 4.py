"""


Extend the given code so it prints out the sum of the numbers.

The output of your code should be as below:

49.1
"""

user_entries = ['10', '19.1', '20']

sum = 0
for i in user_entries:
    sum = sum + float(i)

print(sum)