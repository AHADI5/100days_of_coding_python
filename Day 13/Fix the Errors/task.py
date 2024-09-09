
try:
    age = int(input("How old are you?"))
except ValueError :
    print("You typed in an invalid value , please try again with a correct value")
    age = int(input("How old are you?"))

if age > 18:
    print(f"You can drive at age {age}.")
