#version one full
#Ask for name
def greet():
    global name
    while True:
        name = input("Please enter your name:  ")
        if name.isalpha():
            break
        print("Enter a - z only")
greet()

print("you will be given 10 questions, and three options")
print("one of the options is correct")
print("for each question you get correct you will get one point")

#question 1

    print("\nQuestion: 1|score:{}".format(score))
    ans=input("What is the capital of New Zealand?\na.London\nb.Wellington\nc.Auckland \nYour answer:  ").lower()

if ans == 'b' or ans == 'B' or ans == 'wellington' or ans == 'Wellington':
        print("Correct")
        score+=1
        print("Your score is", score)
    else:
        print("Oops incorrect the correct answer is _____!")
        if score <=0:
            score = 0
            print("Your score is", score)

print("final score is", score)
