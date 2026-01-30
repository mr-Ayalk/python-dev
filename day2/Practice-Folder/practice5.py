#Topic : While Loop=executes some code as long as a condition is true

# Example 1: Print numbers from 1 to 5 using a while loop

count=1
while count<6:
    print(count)
    count+=1
    
    
name=input("Enter your name:  ")

while name== "":
    print("You did not enter your name")
    name=input("Enter your name: ")
print(f"Hello {name}")

#example

food=input("Enter a food you like (q to quit):  ")

while not food == "q":
    print(f"You like {food}")
    food=input("Enter an other  food you like (q to quit):  ")
    
print("bye")


#example

num=int(input("Enter a # between 1-10:  "))

while num <1 or num > 10:
    print(f"{num} is not valid")
    num=int(input("Enter a # between 1-10 :    "))
    
print(f"Your number is {num}")