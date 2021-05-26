# Python has functions for creating, reading, updating, and deleting files.

# open a file
myFile = open('myfile.txt', 'w')
# creates myfile.txt in file structure

# get some info
print('Name: ', myFile.name)
print('Is Closed: ', myFile.closed) 
print('Opening Mode: ', myFile.mode)

# write to file
myFile.write("i love Python")
myFile.write(' and JS.')
myFile.close()

# append to file
myFile = open('myfile.txt', 'a')
myFile.write('. I also enjoy PHP')
myFile.close()

# read from a file
myFile = open('myfile.txt', 'r+')
text = myFile.read(100)
print(text)
