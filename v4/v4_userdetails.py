print("=================================================================")
print("         WELCOME TO THE CAPITALS OF THE WORLD QUIZ")
print("=================================================================")


#Ask for name by using greet function
def greet():
    global name
    while True:
        name = input("Please enter your name:  ")
        if name.replace(' ','').isalpha():
            break
        print("Please enter your name in alphabets only.")
greet()#calling the greet function



#Ask for age
while True:
    age = input("Please enter your age : ")
    if age.replace(' ','').isnumeric():
        break
    print("please enter numbers only")

#Ask if they are ready to take the quiz
status = input("Are you ready to take the quiz :{}?: \na. Yes \nb. No \n=>".format( name))


#what if the user is ready
if status == 'yes' or status == 'Yes' or status == 'y' or status == 'Y' or status == 'a' or status == 'A':
    print("Welcome to the quiz.")
else:
    print("thank you trying this quiz ")
    exit()
   
