#dictionay =a collection of {key:value} pairs ordered and changable .No duplicates

capitals={"USA":"Washington D.C.",
          "India":"New Delhi",
          "China":"Beijing",
          "Russia":"Moscow"}

# print(dir(capitals))
# print(help(capitals))
# print(capitals.get("Japan") ) #None

if capitals.get("Russia"):
    print("That capital exists")
else:
    print("That capital doesn't exist")
    
    
capitals.update({"Germany":"Berlin"})
capitals.pop("China")
capitals.popitem() #removes the latest item

keys=capitals.keys()
print(keys)

for key in capitals.keys():
    print(key)


values=capitals.values()
print(values)

for value in capitals.values():
    print(value)
print(capitals)


items=capitals.items()
for key,value in capitals.items():
    print(f"{key}:{value}")
