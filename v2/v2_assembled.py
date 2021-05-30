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

#version 2 of instructions component
#Ask if they want to hear the instructions
instructions = input("Would you like to hear the instructions {}? \na. Yes \nb. No \n=>".format( name)).lower()

#What if the user doesnt want to hear the instructions
if instructions == 'no' or instructions == 'No' or instructions == 'B' or instructions == 'b':
    print("lets continue with the quiz")
#What if the user does want to hear the instructions
if instructions == 'Yes' or instructions == 'yes' or instructions == 'A' or instructions == 'a':
    print("you will be given 10 questions, and three options")
    print("one of the options is correct")
    print("for each question you get correct you will get one point")

#set of questions that are asked v2
#question 1

    print("\nQuestion: 1|score:{}".format(score))
    ans=input("What is the capital of New Zealand?\na.London\nb.Wellington\nc.Auckland \nYour answer:  ").lower()
if ans == 'b' or ans == 'B' or ans == 'wellington' or ans == 'Wellington':
        print("Correct")
        score+=1
        print("Your score is", score)
    else:
        print("Oops incorrect the correct answer is Wellington!")
        if score <=0:
            score = 0
            print("Your score is", score)
    
#question 2

    print("\nQuestion: 2|score:{}".format(score))
    ans=input("Which countries capital is Jakarta?\na.Cuba\nb.Indonesia\nc.Japan \nYour answer:  ").lower()
if ans == 'Indonesia' or ans == 'indonesia' or ans == 'b' or ans == 'B':
        print("Correct")
        score+=1
        print("Your score is", score)
    else:
        print("Oops incorrect the correct answer is Indonesia!")
        if score <=0:
            score = 0
            print("Your score is", score)

#question 3

    print("\nQuestion: 3|score:{}".format(score))
    ans=input("what is the capital of Iraq?\na.Madagascar\nb.Baghdad\nc.Barcelona \nYour answer:  ").lower()
if ans == 'b' or ans == 'B' or ans == 'Baghdad' or ans == 'baghdad':
        print("Correct")
        score+=1
        print("Your score is", score)
    else:
        print("Oops incorrect the correct answer is _____!")
        if score <=0:
            score = 0
            print("Your score is", score)
#question 4

    print("\nQuestion: 4|score:{}".format(score))
    ans=input("which countries capital is Berlin?\na.Rome\nb.Germany\nc.America\nYour answer:  ").lower()
if ans == 'germany' or ans == 'Germany' or ans == 'B' or ans == 'b':
        print("Correct")
        score+=1
        print("Your score is", score)
    else:
        print("Oops incorrect the correct answer is Germany!")
        if score <=0:
            score = 0
            print("Your score is", score)   
#question 5
    print("\nQuestion: 5|score:{}".format(score))
    ans=input("What is the capital of Italy?\na.Canberra\nb.Rome\nc.Suva\nYour answer:  ").lower()
if ans == 'rome' or ans == 'Rome' or ans == 'b' or ans == 'B' :
        print("Correct")
        score+=1
        print("Your score is", score)
    else:
        print("Oops incorrect the correct answer is Rome!")
        if score <=0:
            score = 0
            print("Your score is", score)    

print("thanks for playing my quiz!")
print("final score is", score)


