"""
replace . by - using replace method ,
"""

filenames = ["1.Row data.txt", "2.Row data.txt", "3.Row data.txt"]

for filename in filenames:
    # filename[1] = '-'  # TypeError: 'str' object does not support item assignment
    filename = filename.replace('.', '-', 1)
    print(filename)
