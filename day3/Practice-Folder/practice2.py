#Topics : 2D collections


#We can use tuples,lists or sets
fruits=["apple","orange","banana","coconut"]

vegetables=["celery","carrots","potatoes"]

meats= ["chicken","fish","turkey"]

groceries=[fruits,vegetables,meats]

print(groceries)
print(groceries[1])
print(groceries[2][2])

for collection in groceries:
    for food in collection:
        print(food,end=" ")
    print()
    
    
    
#Example-key pad

num_pad=((1,2,3),(4,5,6),(7,8,9),("*",0,"#"))

for row in num_pad:
    for num in row:
        print(num,end=" ")
    print()
          