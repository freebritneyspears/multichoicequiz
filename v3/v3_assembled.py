
#rough draft for final version

score = 0
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

#Ask if they want to hear the instructions
instructions = input("Would you like to hear the instructions {}? \na. Yes \nb. No \n=>".format( name)).lower()

#What if the user doesnt want to hear the instructions
if instructions == 'no' or instructions == 'No' or instructions == 'B' or instructions == 'b':
    print("Alright lets continue with the quiz")
#What if the user does want to hear the instructions
if instructions == 'Yes' or instructions == 'yes' or instructions == 'A' or instructions == 'a':
    print("Here are the instructions to the quiz!")
    print("you will be given 10 questions, and three options")
    print("one of the options is correct and the other two are incorrect")
    print("for each question you get correct you will get one point")
    print("try to get as many points as you can!")
#Ask if they are ready to take the quiz
status = input("Are you ready to take this capitals of the world quiz {}? \na. Yes \nb. No \n=>".format( name)).lower()

#What if the user is not ready
if status == 'no' or status == 'n':
    print("okay, see you next time.")
    exit()
   
#what if the user is ready
if status == 'yes' or status == 'y' or status == 'a':
    print("Welcome to the quiz! goodluck and try your best!")

#set of questions that are asked
#question 1

    print("\nQuestion: 1|score:{}".format(score))
    ans=input("What is the capital of New Zealand?\na.London\nb.Wellington\nc.Auckland \nYour answer:  ").lower()
    if ans == 'Wellington' or ans == 'b' or ans == 'wellington' or ans == 'B':
        print("Correct")
        score+=1
        print("Your score is",score)
    else:
        print("Incorrect!! the correct answer is Wellington")
        if score <=0:
            score = 0
            print("Your score is",score)

#question 2

    print("\nQuestion: 2|score:{}".format(score))
    ans=input("Which countries capital is Jakarta?\na.Cuba\nb.Indonesia\nc.Japan \nYour answer:  ").lower()
    if ans == 'Indonesia' or ans == 'b' or ans == 'indonesia' or ans == 'B':
        print("Correct")
        score+=1
        print("Your score is",score)
    else:
        print("Incorrect!! the correct answer is Indonesia!")
        if score <=0:
            score = 0
            print("Your score is",score)

#question 3

    print("\nQuestion: 3|score:{}".format(score))
    ans=input("what is the capital of Iraq?\na.Madagascar\nb.Baghdad\nc.Barcelona \nYour answer:  ").lower()
    if ans == 'Baghdad' or ans == 'b' or ans == 'baghdad' or ans == 'B':
        print("Correct")
        score+=1
        print("Your score is",score)
    else:
        print("incorrect! the correct answer is Baghdad!")
        if score <=0:
            score = 0
            print("Your score is",score)
#question 4

    print("\nQuestion: 4|score:{}".format(score))
    ans=input("which countries capital is Berlin?\na.Rome\nb.Germany\nc.America\nYour answer:  ").lower()
    if ans == 'germany' or ans == 'b' or ans == 'Germany' or ans == 'B':
        print("Correct")
        score+=1
        print("Your score is",score)
    else:
        print("incorrect the correct answer is Germany! better luck next time...")
        if score <=0:
            score = 0
            print("Your score is",score)

   
#question 5

    print("\nQuestion: 5|score:{}".format(score))
    ans=input("What is the capital of Italy?\na.Canberra\nb.Rome\nc.Suva\nYour answer:  ").lower()
    if ans == 'Rome' or ans == 'B' or ans == 'b' or ans == 'rome':
        print("Correct")
        score+=1
        print("Your score is",score)
    else:
        print("Oops incorrect the correct answer is Rome!")
        if score <=0:
            score = 0
            print("Your score is",score)


#question 6

    print("\nQuestion: 6|score:{}".format(score))
    ans=input("What countries capital is New Delhi??\na.Russia\nb.India.\nc.China\nYour answer:  ").lower()
    if ans == 'India' or ans == 'b' or ans == 'B' or ans == 'india':
        print("Correct")
        score+=1
        print("Your score is",score)
    else:
        print("Oops incorrect the correct answer is India!")
        if score <=0:
            score = 0
            print("Your score is",score)


#question 7

    print("\nQuestion: 7|score:{}".format(score))
    ans=input("What is the capital of Australia??\na.Auckland\nb.Canberra.\nc.Sydney\nYour answer:  ").lower()
    if ans == 'Canberra' or ans == 'b' or ans == 'B' or ans == 'canberra':
        print("Correct")
        score+=1
        print("Your score is",score)
    else:
        print("incorrect! the correct answer is Canberra!")
        if score <=0:
            score = 0
            print("Your score is",score)


#question 8

    print("\nQuestion: 8|score:{}".format(score))
    ans=input("What countries capital is Cairo??\na.Madagascar\nb.Egypt.\nc.India\nYour answer:  ").lower()
    if ans == 'Egypt' or ans == 'b' or ans == 'B' or ans == 'egypt':
        print("Correct")
        score+=1
        print("Your score is",score)
    else:
        print("Oops incorrect the correct answer is Egypt!")
        if score <=0:
            score = 0
            print("Your score is",score)


#question 9

    print("\nQuestion: 9|score:{}".format(score))
    ans=input("What is the capital of Fiji??\na.Compton\nb.Suva.\nc.Apia\nYour answer:  ").lower()
    if ans == 'Suva' or ans == 'b' or ans == 'B' or ans == 'suva':
        print("Correct")
        score+=1
        print("Your score is",score)
    else:
        print("Oops incorrect the correct answer is Suva!")
        if score <=0:
            score = 0
            print("Your score is",score)

#question 10

    print("\nQuestion: 10|score:{}".format(score))
    ans=input("What countries capital is Paris??\na.Russia\nb.France.\nc.China\nYour answer:  ").lower()
    if ans == 'France' or ans == 'b' or ans == 'B' or ans == 'france':
        print("Correct")
        score+=1
        print("Your score is", score)
    else:
        print("Oops incorrect the correct answer is France!")
        if score <=0:
            score = 0
            print("Your score is", score)

print("thanks for playing my quiz! i hope you enjoyed")
print("Your final score was", score)

