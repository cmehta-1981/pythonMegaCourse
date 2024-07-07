# Write a program that reads the story.txt file and returns the number of characters contained in the file.

file = open("story.txt", "w")
file.writelines(["I love python\n" , "Python is great"])
file = open("story.txt", "r")
textfile = file.read()
print(len(textfile))
print(f"Number of characters in file is {len(textfile)}")



