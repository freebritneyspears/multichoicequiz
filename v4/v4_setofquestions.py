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
