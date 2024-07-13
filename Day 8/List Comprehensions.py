"""

replace . with - & add .txt at the end of the below list items in .txt using list comprehensions

output should be like below
['1-doc.txt', '2-report.txt', '3-presentation.txt']

"""
filenames = ['1.doc','2.report','3.presentation']

filenames = [filename.replace('.','-')+ '.txt' for filename in filenames]
print(filenames)