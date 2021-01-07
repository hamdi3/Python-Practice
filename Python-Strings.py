#Strings
s = "Hello World!"
print(s[1:]) #this print everything from the first index
print(s[:1]) #this prints everything from the start till the the first index
print(s[-2]) #this would start counting backword(second index from the last)
print(s[::2])#ignores every second index
print(s[1::])# the "::" has no effect here so this will return the same value as s([1:])
print(s[::-1])# this one reverse a string
#you can do operations on string such as mul and add
print(s+" Hello Moon!")
print(s*2)
#operation that could be done on strings
print(s.upper())
print(s.lower())
print(s.split()) #this one is used to split a string to a list of two strings and those are to be divided by the " "
print(s.split("W")) #the string here is to be divided on the "W" or any string that is to be used in the function split()
