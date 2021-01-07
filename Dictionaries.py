#Dictionaries in python
d = {"key" : "wert" , "key2" : 34 , "key3" : 2.14 , "key4" : [1,"b",3.1]} # is used for refrence to give a variable an value so its pretty much call by value
print(d["key"].upper()) # in order to call a value of a specific key in a dic you use d["name of the variable"] 
# d here being the name of the dictionarie, you can use operations on the values of the keys
print(d["key4"][2]) #in order to get an element from a list that is defined as a value of a key
#to add an element to a dic
d["key5"] = "new element"
print(d)
dic = {"key" : {"unterkey" : {"unterkey" : "wert"}}} # a dic can contain a dic within a dic
print(dic["key"]["unterkey"]["unterkey"]) #this is how to print the inner dic of an inner dic and the deeper it goes the more [] we get
print(d.keys()) # how to get a tuple of the keys only
print(d.values()) # how to get a tuple of the values only
print(d.items()) # how to get a tuple of the values and keys
