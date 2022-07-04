import json
import random 

f = open('quiz.json')
data = json.load(f)

def print_line():
    print("---------------------")

def display_questions(topic):
    choices = ["A.", "B.", "C.", "D."]
    topicData = data["quiz"][topic]
    score = [0, len(topicData)]
    for question in topicData:
        questionData = topicData[question]
        print(questionData["question"])
        for choice, option in zip(choices, questionData["options"]):
            print(choice + option)
        answer = input("> Choose answer: ").upper()
        indexNum = questionData["options"].index(questionData["answer"])
        if (answer +"." == choices[indexNum]):
            print("\nCorrect!")
            score[0] += 1
        else:
            print("\nIncorrect...")
            print("Answer is " + questionData["answer"] + "\n")
        print_line()
    return "you got " + str(score[0]) + " out of " + str(score[1])


while True:
    topic = input("> Choose topic (sport/maths): ").lower()
    score = ""
    if (topic == "sport"):
        print(display_questions(topic))
    
    elif (topic == "maths"):
        print(display_questions(topic))
    else:
        print("topic not found...")
    playAgain = input("Enter (y) to play again: ")
    if (playAgain != "y"):
        break;

f.close()