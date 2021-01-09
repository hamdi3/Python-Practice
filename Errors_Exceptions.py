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
#Errors und exceptions handeling
try:
    2+"s"
except TypeError:
    print ("da war ein TypError")

try:
    f = open("testdatei", "w")
    f.write("schreibe in die Datei")
except IOError :
    print("Error : könnte Datei nicht finden oder schrein")
else :
    print("erfolgreich geschrieben0")
    f.close()

try:
    f = open("eineDatei")

#test
def intfrage():
    while True:
        try :
            val = int(input("Bitte geb eine Zahl ein : "))
        except :
            print ("keine Zahl bitte geb eine Ganzzahl ein !")
            continue
        else:
            print("ja das ist eine Zahl!")
            break
        finally :
            print("aber immerhin wurde ich ausgeführt!")
        print (val)

#intfrage()

def Aufgabe1():
    try:
        for i in ["a","b","c"]:
            print(i**2)
    except TypeError:
        print("you can't use pow() for strings")

Aufgabe1()

def Aufgabe2():
    x = 5
    y = 0
    try :
        z = x/y
    except ZeroDivisionError:
        print ("you can't devide by zero")
    finally :
        print ("Alles erledigt!")

Aufgabe2()

def ask():
    while True:
        try:
            val = int(input("Please give a number"))
            return val ** 2
        except:
            print("Please give a number")
            continue
        else:
            break
        
ask()
