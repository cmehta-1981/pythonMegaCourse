# create the list & file name & store list contents in respective file

# list having strings
contents = ["Describe the python",
            "Python is very interesting",
            "I love python "]
# list having file names ,need to strore string in respective below file name
filesnames = ["doc.txt","report.txt","demo.txt"]


for content , filename in zip(contents,filesnames):
    file = open(f"files/{filename}",'w')
    file.write(content)
    file.close()