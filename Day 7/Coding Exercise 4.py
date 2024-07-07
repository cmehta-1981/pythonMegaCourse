# Use Python to create a file with name file.txt and write the text snail there.


file = open("file.txt","w")
file.write("snail there")
file.close()
file = open("file.txt","r")
file.read()
file.close()
