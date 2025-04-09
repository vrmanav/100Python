from data import question_data
from quiz_brain import QuizBrain
from question_model import Question
import time


def play_quiz():
    """Start playing quiz"""

    # TODO: Create a question bank
    question_bank = []
    for question in question_data:
        text = question["text"]
        answer = question["answer"]
        question = Question(text, answer)
        question_bank.append(question)

    quiz_brain = QuizBrain(question_bank)

    while quiz_brain.still_has_questions():
        quiz_brain.greet()
        print(quiz_brain.next_question())
        while True:
            user_answer = input(": ").lower()
            if user_answer != "true" and user_answer != "false":
                print(
                    "\t ⚠️ Invalid input given. Try typing in either 'True' or 'False'"
                )
            else:
                break
        quiz_brain.check_answer(user_answer)
        time.sleep(2)


play_quiz()
