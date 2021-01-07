#Dealing with data in python
pwd #this one is used to see where the python working directery (pwd) is
d = open("test.txt") #this is how we open the datafile before doing any operations on it
print(d.read()) #to read whats in the data
#you cant read the data again without changing the starting postion to the start of the line 
print(d.read())#this will print nothing
d.seek(0) #we return the starting point to 0 in order to be able to read it again
print(d.readlines()) #would return an array with all the lines of the file
#in order to be able to edit a file we should reopen the datafile but this time we would allow writing in it
d = open("test.txt" , "w") #the "w" here allow the writting in the file
d.write("this is a new line") #this will writeover the data and return the numbers of bits wriiten 
