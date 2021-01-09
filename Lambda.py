#Lambda Statments
def square(num): return num**2
square(14)
square2 = lambda num : num**2 #this works exactly like the function
square2(3)
#Examples
even = lambda x : x % 2 == 0 #finding if the number is even
even(4)
first = lambda s : s[0] #this gives the first element of a string
first("hello") 
reverse = lambda s : s[::-1] # reversing a string
reverse("hello")
add = lambda x,y: x+y
add(4,3)
#Funktionen und Methoden Assessment Aufgabe (trying to use lambda)
#1. Volumen einer Kugel
import math
vol = lambda r : (4/3)*math.pi*(r**3)
print(vol(4))
#2. Range Check Funktion
check = lambda i,lst : i in lst
print(check(17,[1,2,3,4,8,5]))
#3. Groß- and Kleinschreibung Strings (selfnote : read about map and join to do for in lamvda)
def count (str):
    upper = 0
    lower = 0
    for i in list(str):
        if i.isupper():
            upper+=1
        elif i.islower():
            lower+=1
    return [upper, lower]
print(count("Hello This Is a Test"))
#4. Einzigartige Zahl in einer Liste (while trying to use set())h 
uniqe = lambda lst : list(set(lst)) #a set is like a dic but without indxs and without repeataions. 
np.array(uniqe([1,2,3,3,3,4,4]))
#5. Alle Zahlen einer Liste multiplizieren (i was yet again unable to use a for-statment in a lambda)
def lstmul(lst):
    mul=1
    for i in (lst):
        mul*=i
    return mul
print(lstmul([1,2,3,4]))
#6. Palindrom Check
pcheck = lambda lst : lst.lower() == lst.lower()[::-1]
print(pcheck("Otto"))
#7. Pangramm Check
import string
pacheck = lambda lst2 : set(lst2.replace(" ", "").lower()) == set(string.ascii_lowercase)
print(pacheck("The quick brown fox jumps over the lazy dog"))
