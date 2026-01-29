#Topic :Typecasting





#Typecasting is the process of converting a variable from one data type to another data type str(), int(), float(), bool()
#Implicit typecasting: Python automatically converts one data type to another without user intervention
var_int = 10          #Integer
var_float = 3.14     #Float
var_str = "20"       #String
#Implicit typecasting from integer to float
result1 = var_int + var_float
print(f"Implicit Typecasting: The result of adding integer and float is: {result1}")
print(f"Type of result1: {type(result1)}")  #result1 is
#Explicit typecasting: User manually converts one data type to another using built-in functions
#Explicit typecasting from string to integer
var_str_to_int = int(var_str)
result2 = var_int + var_str_to_int
print(f"Explicit Typecasting: The result of adding integer and converted string to integer is: {result2}")
print(f"Type of result2: {type(result2)}")  #result2 is an integer
#Explicit typecasting from integer to string
var_int_to_str = str(var_int)
print(f"Explicit Typecasting: The integer converted to string is: {var_int_to_str
}")
print(f"Type of var_int_to_str: {type(var_int_to_str)}")  #var_int_to_str is a string
#Explicit typecasting from float to integer
var_float_to_int = int(var_float)
print(f"Explicit Typecasting: The float converted to integer is: {var_float_to_int
}")
print(f"Type of var_float_to_int: {type(var_float_to_int)}")
#Explicit typecasting from integer to float
var_int_to_float = float(var_int)
print(f"Explicit Typecasting: The integer converted to float is: {var_int_to_float
}")
print(f"Type of var_int_to_float: {type(var_int_to_float)}")
#Explicit typecasting from integer to boolean
var_int_to_bool = bool(var_int)
print(f"Explicit Typecasting: The integer converted to boolean is: {var_int_to_bool
}")
print(f"Type of var_int_to_bool: {type(var_int_to_bool)}")
#Explicit typecasting from boolean to integer
var_bool = False
var_bool_to_int = int(var_bool)
print(f"Explicit Typecasting: The boolean converted to integer is: {var_bool_to_int
}")
print(f"Type of var_bool_to_int: {type(var_bool_to_int)}")
#Explicit typecasting from string to float
var_str_float = "5.67"
var_str_to_float = float(var_str_float)
print(f"Explicit Typecasting: The string converted to float is: {var_str_to_float
}")
print(f"Type of var_str_to_float: {type(var_str_to_float)}")
#Explicit typecasting from float to string
var_float_to_str = str(var_float)
print(f"Explicit Typecasting: The float converted to string is: {var_float_to_str
}")
print(f"Type of var_float_to_str: {type(var_float_to_str)}")
#Explicit typecasting from boolean to string
var_bool_to_str = str(var_bool)
print(f"Explicit Typecasting: The boolean converted to string is: {var_bool_to_str
}")
print(f"Type of var_bool_to_str: {type(var_bool_to_str)}")
#Explicit typecasting from string to boolean
var_str_bool = "True"
var_str_to_bool = bool(var_str_bool)
print(f"Explicit Typecasting: The string converted to boolean is: {var_str_to_bool
}")
print(f"Type of var_str_to_bool: {type(var_str_to_bool)}")
#Note: In Python, non-empty strings are considered True when converted to boolean, while empty strings are considered False.

#Explicit typecasting from float to boolean
var_float_to_bool = bool(var_float)
print(f"Explicit Typecasting: The float converted to boolean is: {var_float_to_bool
}")
print(f"Type of var_float_to_bool: {type(var_float_to_bool)}")
#Explicit typecasting from boolean to float
var_bool_to_float = float(var_bool)
print(f"Explicit Typecasting: The boolean converted to float is: {var_bool_to_float
}")
print(f"Type of var_bool_to_float: {type(var_bool_to_float)}")
print("x")
#In Python, typecasting is straightforward and can be done using built-in functions. It is important to ensure that the conversion is valid to avoid runtime errors.

