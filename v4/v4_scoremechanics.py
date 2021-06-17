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
           
