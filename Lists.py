#Lists in python
l= ["a","s","d","f"]
l = l + ["c"] #you can just add lists to each others
print(l)
l.append("x") #this is how to add an element to alist
print(l)
l.pop(1) #how to remove an elemnt in indx 1
print(l)
l.reverse() #how to reverse a list
print(l)
l.sort() #lists auto-sorting
print(l) 
l2=[1,2,3]
l3=[4,5,6]
matrix = [l,l2,l3] #you can make a list out of lists which is called a linked list
print(matrix[1][2]) #this would print the indx 2 of the list 1 (counting starts with 0 )
erste_spalte = [zeile[0] for zeile in matrix] #this is how to get the first element (indx0) of all the lists in the matrix
print(erste_spalte)
