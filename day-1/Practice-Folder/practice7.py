#Topic : Logical operators in Python

#Logical operators evalute multiple conditions (or ,and , not) 
#or = at least one condition must be true
#and = all conditions must be true
#not = reverses the result, returns false if the result is true

temp=25
is_raining=False

if temp>35 or temp <0 or is_raining:
    print("The outdoor event is canceled")
else:
    print("The outdoor event is still scheduled")
    
    
temp=30
is_sunny=True

if temp>=28 and is_sunny:
    print("It is Hot outside🥵")
    print("It is SUNNY ☀")
elif temp>=20 and is_sunny:
    print("It is Warm outside😊")
    print("It is SUNNY ☀")
elif temp>=15 and not is_sunny:
    print("It is Pleasant outside🙂")
    print("It is NOT SUNNY ☁")
        
else:
    print("It is Cold outside🥶")
    print("It is NOT SUNNY ☁")
is_weekend=False
if not is_weekend:
    print("Time to work!💼"
          
    )
else:
    print("Enjoy your weekend!🎉"
          )

    

