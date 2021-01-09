#functions in python
#adding a comment to a function
def dosomething(par) :
    ' this code does something ' #writting this here will show as a description of this function by hovering the mouse over it when it's used somewhere else
    return "done"
help(dosomething) #pretty much with help we can get our comment on the code
#now to test a simple function "is prime"
def isprime (num):
    for n in range (2,num):
        if num%n==0:
            return "keine Primzahl"
            break
    else:
        print("primzahl")
print(isprime(69))
#Self note it could be optimized like this: (we got rid of the "break")
import math
def istprim(num):
    if num % 2 == 0 and num > 2:
        return False
    for i in range (3, int(math.sqrt(num))+1 , 2):
        if num % i == 0 :
            return False
    return True
print(istprim(69))
