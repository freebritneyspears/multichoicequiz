#version 1 of user details component
#Ask for name
def greet():
    global name
    while True:
        name = input("Please enter your name:  ")
        if name.isalpha():
            break
        print("Enter a - z only")
greet()

