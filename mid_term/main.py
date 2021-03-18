# Trivia
# Joseph Simper
# imports
import sys
from datetime import datetime

test_file = "JosephHamiltonTestCorrect.txt"

# functions
def open_file(file_name, mode):
    """open and return a open file with the given premissions"""
    try:
        file = open("assets/test_files/"+file_name, mode)
    except IOError as e:
        print("Unable to open the file", file_name, "Ending program. \n", e)
        try:
            time = datetime.now()
            error_time = time.strftime("%m/%d/%y %H:%M:%S")
            file = open("assets/error_log/error_log.txt", "a")
            file.write(str(e)+" "+str(error_time)+"\n")
            input("\n\npress the enter key to exit.")
            sys.exit()
        except:
            sys.exit()


    return file

def get_name():
    """ Gets name from the user and a start data and time for the tests"""
    time = datetime.now()
    test_time = time.strftime("%m/%d %H:%M")
    while True:
        name = input("Enter your first and last name")
        if len(name) >= 3 and " " in name:
            name = name.title()
            return name, test_time
        else:
            print("Not a good name")

def next_line(file):
    try:
        line = file.readline()
        line = line.replace("/","\n")
        return line
    except:
        print("Somthing went wrong while reading a line from a file")
        sys.exit()

def question_block(file):
    category = next_line(file)
    question = next_line(file)
    choices = []
    for i in range(4):
        choices.append(next_line(file))
    
    correct = str(next_line(file))
    if correct:
        correct = correct[0]

    explanation = next_line(file)

    return category, question, choices, correct, explanation


def welcome(name,title,time):
    """Welcome the player."""
    print("welcome "+name+" to your Mid Term\n")
    print("your test was created by"+title)
    print("the test was started at "+time)

def report_card(name,score,totalQue,time):
    try:
        file = open("assets/scores/"+name,"w")
        #getting current time
        time = datetime.now()
        endtime = time.strftime("%m/%d/%y %H:%M:%S")

        file.write("name: "+name)
        file.write("time test was started: "+str(time))
        file.write("End Time: "+str(endtime))
        file.write("score (total correct): "+str(score))
        file.write("total questions: "+str(totalQue))

        percent = score/totalQue*100
        
        if percent >= 90:
            letter = "A"
        elif percent >= 80:
            letter = "B"
        elif percent >= 70:
            letter = "C"
        elif percent >= 60:
            letter = "D"
        else:
            letter = "F"

        #writing to file...
        file.write("percentage:",str(percent))
        file.write("letter grade:"+letter)

        file.close()
    except:
        print("There was an error while making your report card")


test_file = "JosephHamiltonTestCorrect.txt"#you must change "example_test.txt" to the actual test



def main():
    score = 0
    totalQue = 0
    #get the name and test time from user
    name, time = get_name()
    #open the file
    file = open_file(test_file,"r")
    title = next_line(file)
    #start the test
    welcome(name, title,time)
    #get the first question
    category, question, choices, correct, explanation=question_block(file)
    #start the game loop
    while category:
        #add one to total questions every time we get a new question
        totalQue +=1
        print("\t\t",category,"\n")
        print(question)
        for i in range(len(choices)):
            print(str.format("\t{}:  {}",i+1,choices[i]))
        answer = input("what is your answer?")
        #check answer
        if answer == correct:
            print("\nRight!", end=" ")
            score +=1
        else:
            print("\nWrong.",end=" ")
        print(explanation)
        print("Score:", score, "\n\n")
        category, question, choices, correct, explanation=question_block(file)
    #close the file
    file.close()
    # finish up the game
    print("That was the last question!")
    print("Your final score is",score)
    print("assets/report_cards/"+name+".txt")
    #create a report card for the user
    report_card(name,score,totalQue,time)


#main
main()
