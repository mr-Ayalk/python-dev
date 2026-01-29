#Topic :Variables and Data Types
#In Python we don't need to declare variables with data types-we can directly assign values to variables and Python will automatically detect the data type

#Variable =A container for a value (string, integer, float, boolean, etc.). A variable behaves as if it is the value that it contains.

#Different data types in Python: Integer, Float, String, Boolean
var1 = 10          #Integer
var2 = 3.14       #Float
var3 = "Hello"    #String
var4 = True       #Boolean
print(var1)
print(var2)
print(var3)
print(var4)
print(type(var1))



first_name="Ayalk"
last_name='Teketel'
full_name= first_name + " " + last_name
print(full_name)
print(f"My full name is: {full_name}")
print(len(full_name))

print(type(full_name))


#Strings can be defined using single quotes(' '), double quotes(" "), or triple quotes(''' ''' or """ """) for multi-line strings
multi_line_string = '''This is a string
that spans multiple
lines.'''
print(multi_line_string)

#Integers (whole numbers) and floats (decimal numbers) can be used for mathematical operations
a = 5
b = 2.5
sum_result = a + b
print(f"The sum of {a} and {b} is: {sum_result}")

print(type(sum_result))

#Booleans represent True or False values and are often used in conditional statements
is_sunny = True
is_raining = False
print(f"Is it sunny today? : {is_sunny}")
print(f"Is it raining today?  : {is_raining}")

if is_sunny and not is_raining:
    print("It's a nice day!")
else:
    print("Stay indoors!")