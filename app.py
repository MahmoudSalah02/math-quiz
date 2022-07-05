import json


def fetch_quiz_question(file_path: str) -> dict:
    '''
    Returns a dictionary of questions on all topics

            Parameters:
                    file_path (str): A string representing the file path of quiz questions


            Returns:
                    quiz_questions (dict): dictionary of questions on all topics
    '''
    with open(file_path, 'r') as file:
        quiz_questions = json.load(file)
        return quiz_questions


def print_dashed_line() -> None:
    '''
    Prints a dashed line

            Parameters:
                    None


            Returns:
                    None
    '''
    print("---------------------")


def validate_answer(user_answer: str, question_data: dict) -> bool:
    '''
    Returns whether the user's answer matches the actual answer of a question

            Parameters:
                    user_answer (str): A string representing the user's answer 
                    question_data (dict): A dictionary with all the information about the question

            Returns:
                    bool: True if the user's answer is correct. False otherwise
    '''
    actual_answer = question_data["answer"]
    index_of_actual_answer = question_data["options"].index(actual_answer)
    character_of_actual_answer = chr(ord('a') + index_of_actual_answer)
    if character_of_actual_answer == user_answer:
        print("Correct")
        return True
    else:
        print("False, answer is " + character_of_actual_answer.upper())
        return False


def display_topic_questions(topic: str, file_path: str) -> float:
    '''
    Displays all questions and their corresponding options in a clear format and returns the user's score

            Parameters:
                    topic (str): A string representing the question's topic
                    file_path (str): A string representing the file path of quiz questions

            Returns:
                    percentage_score (float): A float with two decimels representing the ratio of the number of correct answers to the total number of questions
    '''
    quiz_questions = fetch_quiz_question(file_path)
    topic_questions = quiz_questions["quiz"][topic]
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
    '''
    Starts the quiz by generating the queestions allowing the user to answer questions on multiple topics

            Parameters:
                    None

            Returns:
                    None
    '''
    while True:
        topic = input("> Choose topic: ").lower()
        try:
            percentage_score = display_topic_questions(topic, 'quiz.json') * 100
            percentage_score = round(percentage_score, 2)
            print("Your final score is: " + str(percentage_score) + "%")
        except FileNotFoundError:
            print("Wrong file or file path")
        except ValueError:
            print('Decoding JSON has failed')
        except KeyError:
            print("Topic not found")

        finally:
            playAgain = input("Enter (y) to play again: ").lower()
            if playAgain != "y":
                break

if __name__ == "__main__":
    start_quiz()
