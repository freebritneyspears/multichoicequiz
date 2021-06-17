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
