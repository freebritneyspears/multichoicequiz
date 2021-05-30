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
