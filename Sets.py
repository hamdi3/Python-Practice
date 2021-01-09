#sets is a collections of nonredundant elements that are'nt in order 
s = set() #this is how to create a set
s.add(1) #how to add an element to a set
print(s)
s.add(2)
print(s)
s.add(1) #this one will do nothing because in a set there cant be a repeatation of elements
print(s)
#how to change a list into a set
l=[1,2,3,2,1,3,2,1,3,2,1,2,1,2,5,4]
print(set(l)) #this is how :) in otherwords it does eliminate all the redundant elements
print(set("Missippi")) #to make a set out of a string the set would contain the letters
