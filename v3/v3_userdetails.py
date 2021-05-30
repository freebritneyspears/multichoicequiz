#final version for user details component
#Ask for name
def greet():
    global name
    while True:
        name = input("Please enter your name:  ")
        if name.isalpha():
            break
        print("Enter a - z only")
greet()

#Ask for age
while True:
    age = input("Please enter your age:  ")
    if age.isnumeric():
        break
    print("Enter numbers only")

#Ask if they are ready to take the quiz
status = input("Are you ready to take this capitals of the world quiz {}? \na. Yes \nb. No \n=>".format( name)).lower()

#What if the user is not ready
if status == 'no' or status == 'n':
    print("okay, see you next time.")
    exit()
   
#what if the user is ready
if status == 'yes' or status == 'y' or status == 'a':
    print("Welcome to the quiz! goodluck and try your best!")

