#collection = single "variable" used to store multiple values

#List = [] ordered and changeable .Duplicates OK

#Set ={} unordered and immutable ,but Add / Remove OK. No duplications

#Tuple =() ordered and unchangeable .Duplicates OK.Faster


#Example for lists

fruits=["apple","orange","banana","coconut"]
print(dir(fruits))
print(help(fruits))
print(len(fruits))
print("apple" in fruits)
print(fruits[2])
print(fruits[::2])
print(fruits[::-1])
fruits[0]="pineapple"


fruits.append("pineapple")
fruits.remove("apple")
fruits.insert(0,"mango")
fruits.sort()
fruits.reverse()
fruits.clear()
print(fruits.index("apple"))
print(fruits.count("pineapple"))
for fruit in fruits:
    print(fruit)
    
    
#Examples for set

fruits={"apple","orange","banana","coconut"}
#print(dir(fruits))
print(help(fruits))
print(len(fruits))
print("pineapple" in fruits)

fruits.add("pineapple")
fruits.remove("apple")
fruits.pop()
fruits.clear()




#Examples for set

fruits=("apple","orange","banana","coconut")
#print(dir(fruits))
print(help(fruits))
print(len(fruits))
print("pineapple" in fruits)

fruits.index("apple")

print(fruits.index("apple"))
print(fruits.count("pineapple"))
for fruit in fruits:
    print(fruit)