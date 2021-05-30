#final version of instructions component
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
