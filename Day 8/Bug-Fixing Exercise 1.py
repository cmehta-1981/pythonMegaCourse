"""

Bug-Fixing Exercise 1
The code below tries to write the items of temperatures each in one line in the file.txt list. However, the code has an error. Try to fix the error.

temperatures = [10, 12, 14]

file = open("file.txt", 'w')

file.writelines(temperatures)

"""
'''
Explanation

A new line was added to the code to convert the numbers of the list to strings so they can be written to the text file:

temperatures = [str(i) + '\n' for i in temperatures]
'''
temperatures = [10, 12, 14]
temperatures = [str(i) + '\n' for i in temperatures]
file = open("file.txt", 'w')

file.writelines(temperatures)