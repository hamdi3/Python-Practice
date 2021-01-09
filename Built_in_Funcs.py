#eingebaute funktionen
#map(funktion,sequance)
def fahrenheit(T):
    return ((float(9)/5)*T +32)

def celceius(T):
    return (5/9 * (T-32))

temp = [0,22.5,50,100]
f_temp = list(map(fahrenheit,temp)) #to use a list elements as parameters in a function
print(f_temp)
print(list(map(lambda x : (5/9)*(x-32),f_temp)))# can be done using a lambda function
a = [1,2,3,4]
b = [5,6,7,8]
c = [9,10,11,12]
print(list(map(lambda x,y:  x+y, a,b)))
print(list (map(lambda x,y,z : x+y+z, a,b,c)))

#reduce (function,sequenz) / das gibt im Unterschied zur Map nur einen Wert zuruck
from functools import reduce
lst = [47,11,42,13]
print(reduce(lambda x,y : x+y , lst)) # so wird'S gerechnet 47+11 = 58 + 42 = 100 + 13 = 113 
lst = [34, 23, 45, 1000, 32, 2000]
print(max(lst))
max_ber = lambda a,b : a if (a>b) else b 
def max_find(a,b):
    if (a>b):
        return a
    else:
        return b
print(max_find(12,100))

print(reduce(max_find,lst))

#filter(func, sequenz) gibt die Möglichkeit zu filtern, ergibt True oder false (bool func)
def gerade_check (num):
    if num % 2 == 0:
        return True
    else:
        return False
lst = range (20)
print(list(filter(gerade_check,lst))) #would only return the number from the list that are True in that function 
print(list(filter(lambda x : x % 2 == 0, lst)))
print(list(filter(lambda x : x > 10, lst)))
#zip is for izerrating 2 lists or tuples
x = [1,2,3]
y = [4,5,6,7]
print(list(zip(x,y))) #the 4th elm will be ignored from y 
#using zip on dic
x = {"a" : 1 , "b" : 2}
y = {"c" : 3 , "d" : 4}
print(list(zip(x,y)))
print(list(zip(x,y.values()))) #this would work each way
#trying it in a func
def switcharo(x,y):
    dout = {}
    for xkey,yval in zip(x,y.values()):
        dout[xkey] = yval
    return dout
print(switcharo(x,y))
a = [ 12,45,7,8,12]
b = [45,3,20,3,45,4]
print(list(map(lambda paar : max (paar) , zip(a,b)))) #map gives the elements that are returned from lambda from that list

#enumerate() is basicly a counter
lst = ["a","b","c","d"]
for nummer , elem in enumerate(lst):
    print(nummer,elem)
#all which return true if all elements were ture (or exist in it) and any returns true when min. one elem is True (or at least one element exists)
l = [True,True,False,True]
print(all(l)) #would return false since not all elements are true
print(any(l)) ##would return True since at lease one element is true   
#complex() would give a komplexe Zahl 
#for 2+3i
print(complex(2,3)) #the first one is the real part while the second is the imagenry (notice that it says j instead of i which is not a problem)
print(complex("21.1")) #a string is also accepted as long as its a number or has the j (for the imaginary part) in it

#assigments
#first a func using map to give the lenth of each word in a list
test="this is a test"
def word_count(lst):
    return list(map(len,lst.split(" ")))
print(word_count(test))
#converting a list into a full number using reduce
from functools import reduce
def stellen_zu_zahlen(stellen):
    num = reduce(lambda x,y : x*10 + y , stellen)
    return num
print(stellen_zu_zahlen([1,2,3,4,5,6]))
#filtering a wordlist using filter
def filter_words(word_list, letter):
    x= list(filter(lambda x : x.startswith(letter),word_list))
    return x 
print(filter_words(["Hello","list"], "H"))
#using zip to connect elements of lists with a connector
def verbinden(L1,L2,konnektor):
    return [word1 + konnektor + word2 for(word1,word2) in zip(L1,L2)]
print(verbinden(["a","b"],["c","d"],"-"))
#using enumerate to turn a list into a dic
def dict_list(L):
    return {key:value for (key,value) in enumerate(L)}
print(dict_list(["a","b"]))
#using enumerate to check how many elim in a list equal their indx
def count_treffer(L):
    return len([wert for wert,indx in enumerate(L) if wert == indx])
print(count_treffer([0,1,3]))
