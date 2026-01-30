#indexing=accessing elements of a sequence using [] (indexing operator) [start:end:step]
credit_card_number = "1234-5678-9012-3456"
# Accessing individual characters
first_digit = credit_card_number[0]  # '1'
last_digit = credit_card_number[-1]  # '6'
print("First digit:", first_digit)
print("Last digit:", last_digit)
# Slicing substrings
first_four = credit_card_number[0:4]  # '1234'
middle_section = credit_card_number[5:9]  # '5678'
print("First four digits:", first_four)
print("Middle section:", middle_section)    
# Using step in slicing
every_second_digit = credit_card_number[::2]  # '135790246'
print("Every second digit:", every_second_digit)
# Reversing the string
reversed_number = credit_card_number[::-1]  # '6543-2109-8765-4321'
print("Reversed credit card number:", reversed_number)
# Modifying parts of the string (strings are immutable, so we create a new string)
modified_number = credit_card_number[:12] + "9999"  # '1234-5678-9012-9999'
print("Modified credit card number:", modified_number)

# Demonstrating negative indexing
second_last_digit = credit_card_number[-2]  # '5'   


print("Second last digit:", second_last_digit)
# Slicing with negative indices
last_four = credit_card_number[-4:]  # '3456'
print("Last four digits:", last_four)
# Slicing with negative step
reversed_middle = credit_card_number[11:7:-1]  # '2109
print("Reversed middle section:", reversed_middle)
print("Reversed middle section:", reversed_middle)
# Slicing with negative step
reversed_middle = credit_card_number[11:7:-1]  # '2109
print("Reversed middle section:", reversed_middle)
print("Reversed middle section:", reversed_middle)
# Slicing with negative step
reversed_middle = credit_card_number[11:7:-1]  # '2109
print("Reversed middle section:", reversed_middle)


last_four = credit_card_number[-4:]  # '3456'
print(f"XXXX-XXXX-XXXX-{last_four}")