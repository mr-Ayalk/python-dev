#if=Do some code only if some condition is true
#else do some thing else

# num=10
# num1=22

# if num>=num1:
#     print(num)
# else:
#     print(num1)






age=int(input("Enter your age: "))
if age>=100:
    print("You are too old to vote.")
elif age>18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")