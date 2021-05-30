#version 2 of user details component
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
