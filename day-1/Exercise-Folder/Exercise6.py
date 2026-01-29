#Python weight converter
weight_in_kg = float(input("Enter your weight in kilograms: "))

unit=input("kilograms or Pounds (K or L): ").upper()

if unit == "K":
    weight_in_pounds = weight_in_kg * 2.20462
    print(f"Your weight in Pounds is: {weight_in_pounds:.2f} lbs")
    
elif unit == "L":
    weight_in_kg_converted = weight_in_kg / 2.20462
    print(f"Your weight in Kilograms is: {weight_in_kg_converted:.2f} kg")
else:
    print("Invalid unit. Please enter 'K' for kilograms or 'L' for pounds.")# This program converts weight between kilograms and pounds based on user input.