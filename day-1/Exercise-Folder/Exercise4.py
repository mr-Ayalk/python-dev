#Circumference of a Circle Calculator
import math

radius=float(input("Enter the radius of the circle:  "))
circumference=2*math.pi*radius
print(f"The circumference of the circle with radius {radius} is {round(circumference,2)}cm")


#Area of a Circle Calculator
import math
radius=float(input("Enter the radius of the circle:  "))
area=math.pi*radius**2
print(f"The area of the circle with radius {radius} is {round(area,2)}cm²")

#Volume of a Sphere Calculator
import math
radius=float(input("Enter the radius of the sphere:  "))
volume=(4/3)*math.pi*radius**3
print(f"The volume of the sphere with radius {radius} is {round(volume,2)}cm³")

#Surface Area of a Sphere Calculator
import math
radius=float(input("Enter the radius of the sphere:  "))
surface_area=4*math.pi*radius**2
print(f"The surface area of the sphere with radius {radius} is {round(surface_area,2)}cm²")

#Hypotenuse Calculator using Pythagorean Theorem
import math
a=float(input("Enter the length of side a:  "))
b=float(input("Enter the length of side b:  "))
# hypotenuse=math.sqrt(a**2 + b**2)
c=math.sqrt(pow(a,2) + pow(b,2))
print(f"The length of the hypotenuse is {round(c,2)}cm")