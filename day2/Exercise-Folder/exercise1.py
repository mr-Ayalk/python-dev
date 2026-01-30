#Validate user input excercise 

#1.username is no morethan 10 characters
#2username must not contain any spaces
#3.username must start with an alphabet
#username must not contain digits


username = input("Enter your username: ")

if len(username) > 10:
    print("Username must be no more than 10 characters.")
# elif ' ' in username:
#     print("Username must not contain spaces.")
elif not username.find(" ")==-1:
    print("Username must not contain spaces.")
elif not username[0].isalpha():
    print("Username must start with an alphabet.")
elif any(char.isdigit() for char in username):
    print("Username must not contain digits.")
else:
    print("Username is valid.")