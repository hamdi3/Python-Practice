#Generators are used when dealing with very long lists since theyre are mem. efficent (Lazy object)
def genraum(n):
    for num in range(n):
        yield num**3 #using yield instead of return is by generators since the generators only run once and does'nt sotore anything in the memory meaning its significantly efficent and faster 
#for x in genraum (10): #gen. are to be called lke this
#    print(x)

def genfib(n):
    a = 1
    b = 1
    output = []

    for i in range(n):
        output.append(a)
        yield a
        a,b = b, a+b

def fib(n): #the same code without yield would be (this is a normal func)
    a = 1
    b = 1
    output = []
    for i in range(n):
        output.append(a)
        a,b = b, a+b
    return output
for num in genfib(3):#there are no upper limit since this is only calculated when called and not saved in the memory
    print("this was done by gen",num)
print("done by func",fib(10))# we dont need a for loop here but since it's not a generator this would lead to an exception later on when using bigger number 
def simple_gen():
    for x in range(3):
        yield x
g = simple_gen()
print(g) # this would only say that g is refering to a gen. also an object
print("the first elim in simple_gen is",next(g)) #generator can be used with next(), p.s the first next would only give us the first elim
print("the sec elim in simple_gen is",next(g))#calling it again will give the second elim since generator are only used once
print("the 3d elim in simple_gen is",next(g))#third elim
#print("the first elim in simple_gen is",next(g)) calling it a fourth time would lead to an error since it only give the first 3 values (in range(3))

#iterators
s ="hello"
s_iter = iter(s) #thats how to make an iterator (to use next with) like genrator
print(next(s_iter))

#Assessments
#Generator 1 for quadrates number
def genquadrate(N):
    for i in range(N):
        yield i*i
for i in genquadrate(10):
    print("genquadrate",i)
#Generator 2 for random numbers between to nums
import random
def zuf_zahl(unten,oben,N):
    for i in range(N):
        yield random.randint(unten,oben)
for num in zuf_zahl(1,10,3):
    print("random number",num)
#another way to build gen
l = [1,2,3,4,5,6,7]
gen = (item for item in l if item > 4) #this uses a yield automaticly
for i in gen:
    print(i)
