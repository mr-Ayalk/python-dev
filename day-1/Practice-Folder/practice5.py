#Topic : Arithmetic operators and built-in math functions

friends=5
friends=friends+2
friends+=2  #shorthand operator for addition
friends=friends-3
friends-=1  #shorthand operator for subtraction
friends=friends*2
friends*=2  #shorthand operator for multiplication
friends=friends/2
friends//=2  #shorthand operator for floor division
friends=friends**2
friends**=2  #shorthand operator for exponentiation
remainder=friends%3  #modulus operator
print(f"Remainder when total friends divided by 3: {remainder}")
print(f"Total number of friends: {friends}")




#built-in math functions
import math
num=-7.8
x=3.14
y=4
z=5
absolute_value=abs(num)  #absolute value
rounded_value=round(num)  #rounding to nearest integer
ceiling_value=math.ceil(num)  #ceiling value
floor_value=math.floor(num)  #floor value
square_root=math.sqrt(64)  #square root
power=math.pow(2, 3)  #2 raised to the power of 3
max_value=max(x, y, z)  #maximum value among x, y, z
min_value=min(x, y, z)  #minimum value among x, y, z


print(math.pi)  #value of pi
print(math.e)   #value of e
result=math.sin(math.radians(30))  #sine of 30 degrees
result=math.cos(math.radians(60))  #cosine of 60 degrees
result=math.tan(math.radians(45))  #tangent of 45 degrees
result=math.log(100, 10)  #logarithm base 10 of 100
result=math.exp(2)  #e raised to the power of 2
result=math.factorial(5)  #factorial of 5
result=math.gcd(48, 18)  #greatest common divisor of 48 and 18
result=math.lcm(4, 6)  #least common multiple of 4 and 6
result=math.isqrt(50)  #integer square root of 50
result=math.hypot(3, 4)  #hypotenuse of a right-angled triangle with sides 3 and 4
result=math.copysign(-5, 3)  #copy sign of 3 to -5
result=math.fabs(-9.81)  #absolute value as float
result=math.trunc(5.67)  #truncate decimal part
result=math.modf(5.67)  #fractional and integer parts
result=math.prod([1, 2, 3, 4])  #product of elements in an iterable
result=math.perm(5, 2)  #permutations of 5 items taken 2 at a time
result=math.comb(5, 2)  #combinations of 5 items
result=math.ceil(4.2)  #ceiling of 4.2
result=math.floor(4.8)  #floor of 4.8
result=math.dist((1, 2), (4, 6))  #Euclidean distance between two points
result=math.sqrt(49)  #square root of 49
result=math.log2(16)  #logarithm base 2 of 16

