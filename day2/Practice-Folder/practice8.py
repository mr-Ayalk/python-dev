#nested loop =A loop within another loop(outer,inner)
#outer loop:
 #    inner  loop
 
 
 
#  #example 1
# for i in range (0,7):
#     for j in range (0,7-i):
#         print("*",end=" ")
#     print()
    
    
# #example-2

# for x in range(3):
#     for y in range(1,10):
#         print(y,end=" ")
#     print()
    
    

# #example -3

# rows=int(input("Enter the # of the rows:  "))

# columns=int(input("Enter the # of the columns:   "))

# symbol=input("Enter a symbol to use:  ")

# for x in range (rows):
#     for y in range(columns):
#         print(symbol,end="")
#     print() 
    
    
#example-4

for i in range(4):
    for j in range (0,3-i):
        print(" ",end=" ")
    for k in range(i+1):
        print("*",end=" ")
    print()