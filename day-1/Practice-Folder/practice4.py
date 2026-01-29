#Topic input()
#The input() function is used to take input from the user. By default, it takes input as a string.
#We can also convert the input to other data types like int, float, etc. using typecasting.
#Taking string input from the user
name = input("Enter your name: ")
print(f"Hello, {name}!")


#Example
name=input("what is your name?:  ")
age=int(input("how old are you?:  "))

age+=1
print(f"Hello {name}, next year you will be {age} years old.")
#Taking integer input from the user
num1 = int(input("Enter an integer: "))
num2 = int(input("Enter another integer: "))
sum_result = num1 + num2
print(f"The sum of {num1} and {num2} is: {sum_result
}")
#Taking float input from the user
float_num1 = float(input("Enter a float number: "))
float_num2 = float(input("Enter another float number: "))
float_sum = float_num1 + float_num2
print(f"The sum of {float_num1} and {float_num2} is: {
float_sum}")
#Taking boolean input from the user
bool_input = input("Enter True or False: ")
bool_value = bool_input.lower() == 'true'
print(f"You entered the boolean value: {bool_value}")


