#Tempreture conversion

unit=input("Enter the unit you want to convert from (C for Celsius, F for Fahrenheit): ").strip().upper()

temp=float(input("Enter the temperature value to convert: "))

if unit=="C":
    temp=round((temp * 9/5) + 32, 1)
    print(f"The temperature in Fahrenheit is: {temp} F")
elif unit=="F":
    temp=round((temp - 32) * 5/9, 1)
    print(f"The temperature in Celsius is: {temp} C")
else:
    print("Invalid unit entered. Please enter 'C' for Celsius or 'F' for Fahrenheit.")