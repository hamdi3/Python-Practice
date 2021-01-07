#Formatting in python
str="string"
print("this will type a %s" %(str)) # in %() whatever you write will be changed to a string
print("this will type a %s , %s" %("hello" ,3)) # you can use %s 2 times and more but you use one %() with a comma for diffrient ones
print("this will type a float %1.2f" %(13.4454)) # %1.2f means that the float would have min 1 num before the comma and max 2 after

#Recommended Methods:
print("this will print {p}".format (p = "something")) #by typing {p} then ending the string with a .format(P=) you can put anything as a value of p in it
print("string1 : {p} , string2: {p}, string 3:{p}" .format(p="hi")) #you can p several times
print("object1: {a}, object2:{b}, object3:{c}" .format(a="string", b= 4 , c = 2.3)) #you can use more than one variable
