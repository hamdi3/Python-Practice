#OOP (Object oriented programming)
print(type(1)) #this pretty much gives the type of the object
#defining an oject
class Beispiel(object): # class names starts with a capital litter.abs
    pass
x = Beispiel()
print(type(x))
#Methodes (methods are insinde classes)
class Hund (object):
    def __init__(self,rasse): #instiallizing the class should always
        self.rasse = rasse
sam = Hund(rasse = "lab")
frank = Hund(rasse = "Huskey")
print(type(frank))
print(frank.rasse) #is not a method, its an attribute.
class Hund (object):
    spezies = "Säugetertier"
    def __init__ (self,rasse,name): #it's important to always write self
        self.rasse=rasse #this how to define an attribute
        self.name=NameError
sam = Hund("Lab","Sam")
print(sam.spezies)#spezies is an attribte for the entire class 
class Kreis (object):
    pi= 3.14

    def __init__ (self,radius = 1 ): # radius = 1 is a standard value when we dont define otherwise
        self.radius= radius
    def flaeche(self):
        return self.radius * self.radius * Kreis.pi
    def radiusEinstellen(self,radius):
        self.radius = radius
    def radiusErhalten (self):
        return self.radius

k = Kreis(radius=100) # when we need to define something else
print(k.flaeche())
k.radiusEinstellen(10)
print(k.flaeche())
print(k.radiusErhalten())

# inheritance by oop
class Tier (object):
    def __init__ (self):
        print("Tier erschaffen")
    def werBinIch(self):
        print("Tier ")
    def essen (self):
        print("Essen")

class Hund(Tier): #refrensing Tier as a father(base)class.
    def __init__(self):
        Tier.__init__(self) #call initial mehtod from Tier 
        print("Hund erstellt")
    def werBinIch(self): #the methode was 
        print("Hund")
    def bellen(self):
        print("wuf!")
t= Tier()
print(t.werBinIch())
print(t.essen())
h=Hund()
print(h.werBinIch())
print(h.bellen())
print(h.essen()) # we didnt need to redfine that since we have it in Tier

#Speical Methods
class Buch (object):
    def __init__ (self,title, autor, seiten):
        print("Ein Buch wird geschrieben!")
        self.titel = title
        self.autor = autor
        self.seiten = seiten

    def __str__ (self):
        return "Title: %s, Autor: %s, Seiten %s"%(self.titel, self.autor, self.seiten) 
    def __len__ (self):
        return self.seiten
    def __del__ (self):
        print("Ein buch wird gelöcht")

buch = Buch("Pyton Rock", "Hamdi Khalil" , 590)
print(buch)
print(len(buch))
print(str(buch))
del buch
print(buch) #we realize that this prints an error since we already deleted the data

#OOP Assessment
class Linie(object):
    def __init__(self,koor1,koor2):
        print("eine Linie wurde erstellt")
        self.koor1 = koor1
        self.koor2 = koor2
    def distanz (self):
        x1, y1 = self.koor1
        x2, y2 = self.koor2
        return ((x2-x1)**2 + (y2-y1)**2)**0.5
    def steigung(self):
        return ((self.koor2[1]-self.koor1[1])/(self.koor2[0]-self.koor1[0])) #or just deal with them as if they were a list 

koordinate1 = (3,2)
koordinate2 = (8,10)
li = Linie(koordinate1,koordinate2)
print(li.distanz())
print(li.steigung())

import math
class Zylinder (object):
    def __init__(self, hohe = 1, radius = 1):
        print("eine Zylinder wurde erstellt")
        self.hohe = hohe
        self.radius = radius
    def vol (self):
        return math.pi * self.radius**2 * self.hohe
    def oberflaeche (self):
        return 2 * math.pi * self.radius * (self.radius + self.hohe)

c = Zylinder(2,3)
print(c.vol())
print(c.oberflaeche())
