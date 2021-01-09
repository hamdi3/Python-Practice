#Dekoratoren (Decoratores) (Design-Möglichkeiten)
def funk():
    return 1
funk()
s = "Global Variables"
def funk1():
    print(locals())# this would just show us all the local functions within the func1
#print(globals().keys()) #this shows all the global vars
#print(funk1())
def hallo(name="David"):
    return("Hallo " + name) #P.s writing wiht a coma would give a tupel
print(hallo())
gruss = hallo #no need for "()" here 
print(gruss) # this would give us an object showing that this get the main method from .hallo
print(gruss())#adding "()" will run the func
del hallo #to delete a mehode
#hallo() #calling a methode after deleting would give an error since we deleted it
print(gruss()) #notice how this would run the method even after deleting it
#Functione inside of a function
def hallo(name="david"):
    print("hallo()")
    def gruss():
        return "\t das ist innerhalb der gruss"
    def willkomen():
        return "\t das ist innerhalb der Willkommen"
    print(gruss())
    print(willkomen())
    print("jetzt sind wir wieder in der Hallo")
print(hallo())
#functions as parameter
del hallo
def hallo():
    return "hallo there"
del funk
def anrede (funk):
    print("Anrede Funktion")
    print(funk())
anrede(hallo) #since we use it as parameter (object) we don't need any "()"
def neu_dekorator(funk):

    def huellen_funktion():
        print("code würde hier stehen(vor)")
        funk()
        print("code nach der funktion")
    return huellen_funktion #again an object so no need for ()

def funk_braucht_dek():
    print("this function needs a dicorator")
funk_braucht_dek = neu_dekorator(funk_braucht_dek)# this will be used pretty much for when we have something we want to change in a func while still wanting the beginnig and the endig to remain the same
print(funk_braucht_dek())
#or it could be used like this first we call the funktion that will take a func as a parameter with an @ then we define the new function
@neu_dekorator
def funk_braucht_dek():
    print("this funk bracht ein dek")
funk_braucht_dek()
