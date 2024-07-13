'''
Question 2:
When the interpreter runs the read() method more than one time, the method returns the content of the file only the first time because:

Ans:
Yes, the first read() method will put the cursor at the end of the text file.


Question 3:
What would be the content of the text file if you were to run the code below?

with open("file.txt", 'w') as file:
    file.write("Hello")

with open("file.txt", 'w') as file:
    file.write("Hi")

Ans : Hi
This is correct because the second open function will overwrite the file created by the first open function.

'''

with open("file.txt", 'w') as file:
    file.write("Hello")

with open("file.txt", 'w') as file:
    file.write("Hi")




'''
Question 4:
What would be the content of the file this time if you were to run the code below?

with open("file.txt", 'w') as file:
    file.write("Hello")
    file.write("Hi")
    
Ans  =  HelloHi
'''

with open("file.txt", 'w') as file:
    file.write("Hello")
    file.write("Hi")




