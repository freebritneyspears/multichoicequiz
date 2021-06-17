from random import shuffle
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
   
##Asking if user wants instructions
def inst():
    inst = input("do you want to read the instructions if you enter anything except for yes or a the instructions will not be shown  :{}?: \na. Yes \nb. No \n=>")
    if inst == 'yes' or inst == 'Yes' or inst == 'y' or inst == 'Y' or inst == 'a' or inst == 'A':
     
        print("==================================INSTRUCTIONS==========================================")
        print("This quiz will ask you questions about the subject of countries and their capitals")
        print("There will be one correct answer per question. Each Question will have")
        print("three possible answers for each question.")
        print("========================================================================================")
    else:
        print("welcome to the quiz")
       
                           
inst()## calling the functions
## number of questions to be asked
def rounds():
    global r
    while True:
        try:
            r = int(input("\nPlease enter how many rounds you want to play: "))##asking the user how many rounds they want to play
            if 0<r<=10:
                break
            else:
                print("please enter the rounds in 1 to 10 only")
        except:
            print('please enter rounds in numbers only (The max is 10)')



rounds()
print("                                                    ")
#set of questions that are asked
#question 1
## questions and right answers

#initial score

incorrect = 0
correct = 0
score = 0
questions=[
[
    "What is the capital of New Zealand?:  ",##Q1
    {'answer':'b','option':'\na.England\nb.wellington \nc.Russia '}
    ],

[
    "Which countries capital is Jakarta?:  ",##Q2
    {'answer':'b','option':'\na.Cuba \nb.Indoneisa \nc.Japan '}
    ],


[
    "What is the capital of Iraq?:  ",
    {'answer':'b','option':'\na.Madagascar \nb. Baghdad \nc. Barcelona '}##Q3
    ],    
   
[
    "Which countries capital is Berlin?:  ",
    {'answer':'b','option':'\na.Rome \nb.Germany \nc.USA '}##Q4
    ],    
   

[
    "What is the capital of Italy?:  ",
    {'answer':'b','option':'\na.Canberra \nb.Rome \nc.Suva '}##Q5
    ],    
     


[
    "What countries capital is New Delhi?:  ",
    {'answer':'b','option':'\na.Russia \nb.India \nc.China '}##Q6
    ],    
     
[
    "What is the capital of Australia ?",
    {'answer':'b','option':'\na.Auckland\nb.Canberra \nc.Sydney '}##Q7
    ],    

[
    "Which countries capital is Cairo?:  ",
    {'answer':'b','option':'\na.Madagascar \nb.Egypt \nc.India '}##Q8
    ],    
[
    "What is the capital of Fiji?",
    {'answer':'b','option':'\na.Compton \nb. Suva \nc. Apia '}##Q9
    ],    

[
    "Which countries capital is Paris?:  ",
    {'answer': 'b','option':'\na.Russia \nb.France \nc. China '}##Q10
    ],
]
shuffle(questions)
## score mechanics
print("Main Routine")
while r>0:
    data = questions[0]
    q = data[0]
    data =data[1]
    answer = data['answer']
    option = data['option']

    print(q)
    print(option)
    while True:
        user_answers = input("Please enter your answer here : ").lower().replace(' ','')
        if user_answers =='a' or user_answers == 'b' or user_answers == 'c' or user_answers == 'd':
            if user_answers == answer:
                print("***************************")
                print("nice you got it correct!!!")
                print("***************************")
                score +=1 #when user answers correctly
                correct +=1 #when user answers correctly
                print("=======")
                print("your score is",score)
                print("=======")
            else:
                print("**********************************************************")
                print("oops the answer you have chosen is not correct. The right answer is ",answer)    
                print("**********************************************************")
                print("=======")
                print("your score is",score)
                print("=======")
                incorrect +=1


            del questions[0]
            r-=1
            break
        else:
            print("please enter the alphabet for the chosen option")
           

           
print("Thanks for playing",name)
print("Your final score is", score)
