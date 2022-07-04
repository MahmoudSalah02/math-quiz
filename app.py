import json


def fetch_quiz_question(file_path: str) -> dict:
    """Fetches all quiz questions from a JSON file given the file path"""
    try:
        f = open(file_path)
        quiz_questions = json.load(f)
    except FileNotFoundError:
        print("Wrong file or file path")
    except ValueError:  # includes simplejson.decoder.JSONDecodeError
        print('Decoding JSON has failed')
    finally:
        f.close()
    return quiz_questions


def print_dashed_line():
    """Prints a dashed line"""
    print("---------------------")


def validate_answer(user_answer: str, question_data: dict) -> bool:
    """Accepts the user answer and data on a quetion and returns a boolean of whether the user's answer is correct"""
    actual_answer = question_data["answer"]
    index_of_actual_answer = question_data["options"].index(actual_answer)
    character_of_actual_answer = chr(ord('a') + index_of_actual_answer)
    if character_of_actual_answer == user_answer:
        print("Correct")
        return True
    else:
        print("False, answer is " + character_of_actual_answer.upper())
        return False


def display_topic_questions(topic: str) -> float:
    """Accepts a topic from the user, prints the question along with the corresponding options, and returns the final score of the user"""
    quiz_questions = fetch_quiz_question('quiz.json')
    try:
        topic_questions = quiz_questions["quiz"][topic]
    except KeyError:
        print("Topic not found")
        return None
    score = 0
    # loop through each question in the specified topic
    for question_num in topic_questions:
        question_data = topic_questions[question_num]
        print(question_data["question"])

        # loop through the multiple choice answers
        character_counter = 0
        for option in question_data["options"]:
            current_character = chr(ord('a') + character_counter)
            print(current_character.upper() + ". " + option)
            character_counter += 1

        user_answer = input("> Choose answer: ").lower()
        if validate_answer(user_answer, question_data):
            score += 1

    percentage_score = score / len(topic_questions)
    return percentage_score


def start_quiz() -> None:
    while True:
        topic = input("> Choose topic: ").lower()
        print("Your final score is: " +
              str(display_topic_questions(topic) * 100) + "%")
        playAgain = input("Enter (y) to play again: ").lower()
        if playAgain != "y":
            break


if __name__ == "__main__":
    start_quiz()
