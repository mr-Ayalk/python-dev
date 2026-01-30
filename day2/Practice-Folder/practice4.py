# format specifiers = {value:flags} format a value based on what
#                      flags are inserted

# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator

price1= 3.14159
price2= 1234567.891011
price3= -42.5444
print(f"Price1: {price1:.2f}")
print(f"Price2: {price2:,.2f}")
print(f"Price3: {price3:+.2f}")
print(f"Price1: {price1:>10.2f}")
print(f"Price2: {price2:<15,.2f}")
print(f"Price3: {price3:=+10.2f}")
print(f"Price1: {price1:^10.2f}")
print(f"Price2: {price2: 15,.2f}")
print(f"Price3: {price3:0>10.2f}")
# Experiment with different format specifiers below
value= 98765.4321
print(f"Value: {value:.3f}")
print(f"Value: {value:>12.3f}")
print(f"Value: {value:<12,.2f}")
print(f"Value: {value:^15,.2f}")
print(f"Value: {value:+,.2f}")
print(f"Value: {value:=+12,.2f}")
print(f"Value: {value:0>12,.2f}")
print(f"Value: {value: 15,.2f}")
print(f"Value: {value:0<12,.2f}")
print(f"Value: {value:,.1f}")
print(f"Value: {value:0^15,.2f}")
print(f"Value: {value:0=+12,.2f}")
print(f"Value: {value:0>15,.3f}")
print(f"Value: {value: 0<15,.2f}")
print(f"Value: {value:0^12,.3f}")
print(f"Value: {value:0= 12,.2f}")
print(f"Value: {value:0>15,.2f}")
print(f"Value: {value: 0^12,.2f}")
print(f"Value: {value:0<15,.3f}")
print(f"Value: {value:0=+15,.3f}")
print(f"Value: {value: 0>12,.3f}")
print(f"Value: {value:0^15,.3f}")
print(f"Value: {value:0= 15,.3f}")
print(f"Value: {value:0<12,.3f}")
print(f"Value: {value: 0>15,.3f}")
print(f"Value: {value:0^12,.2f}")
print(f"Value: {value:0=+15,.2f}")
print(f"Value: {value: 0<12,.3f}")
print(f"Value: {value:0>15,.2f}")