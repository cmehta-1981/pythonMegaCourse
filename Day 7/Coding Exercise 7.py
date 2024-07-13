"""
Please download the three text files a.txt, b.txt, and c.txt from the resources and place them in your computer IDE.

Then, create a program that:

1. reads each text file and

2. prints out the content of each file in the command line.

The expected output would be like the following:

"""
filenames = ['files/a.txt','files/b.txt','files/c.txt']

for filename in filenames:
    file = open(filename , 'r')
    contents = file.readlines()
    print(contents)
    file.close()