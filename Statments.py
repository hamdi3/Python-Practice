#for statments
l = [1,2,3,4,5]
sum = 0
for num in l :
    sum += num
print(sum)  

string = "This is a String"
for s in string:
    print(s)

l2= [(1,2),(3,4),(5,6)]
for t in l2 :
    print (t)
for (t1,t2) in l2:
    print(t1,t2)
    
#Excersises 
#ex1: giving only the words that start with an S in a long string.
s1 = "say stuff that starts wiht an s"
for word in s1.split():
    if word[0]=="s" or word[0]=="S":
        print(word) 
        
#using range() to give odd number from 1 to 10
range(0,11,2)

#creating a list with cond.
[x for x in range (1,51) if x%3 == 0]

#ex:
#selecting words with an odd length from a string
s = "hello there im a string to use for testing your functions"
for word in s.split():
    if len(word) % 2 != 0:
        print(word + "-> this word has an odd length")
        
#making a list from the first letters of a string
s = "hello you can test me as much as you want"
[word[0] for word in s.split()]
