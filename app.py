import json
import random 

f = open('quiz.json')
data = json.load(f)

def print_line():
    print("---------------------")

def display_question(topic):
    topicData = data["quiz"][topic]
    questionNum = "q" + str(random.randint(1, len(topicData)))
    print_line()
    print(topicData[questionNum]["question"])
    print_line()
    choices = ["A.", "B.", "C.", "D."]
    for choice, option in zip(choices, topicData[questionNum]["options"]):
        print(choice + option)
    answer = input("> Choose answer: ").upper()
    indexNum = topicData[questionNum]["options"].index(topicData[questionNum]["answer"])
    if (answer +"." == choices[indexNum]):
        print("\nCorrect!")
        print_line()
    else:
        print("\nIncorrect...")
        print("Answer is " + topicData[questionNum]["answer"] + "\n")
        print_line()


while True:
    topic = input("> Choose topic (sport/maths): ").lower()
    if (topic == "sport"):
        display_question(topic)
    elif (topic == "maths"):
        display_question(topic)
    else:
        topic = input("topic not found...")
    playAgain = input("Enter (y) to play again: ")
    if (playAgain != "y"):
        break;

f.close()