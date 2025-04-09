import os


class QuizBrain:
    def __init__(self, question_bank):
        self.question_list = question_bank
        self.question_number = 0
        self.score = 0

    def greet(self):
        "Greet the user and display the rules"
        os.system("clear")
        print("Welcome to Kaun Banega Crorepati")
        print("You have to answer every question by typing in either 'True' or 'False'")

    def next_question(self):
        """Ask the next question to user"""
        text = self.question_list[self.question_number].text
        self.question_number += 1
        return f"\nQ.{self.question_number} {text}"

    def still_has_questions(self):
        """Returns True if questions are remaining, else False"""
        total_questions = len(self.question_list)
        return self.question_number < total_questions

    def check_answer(self, user_answer):
        """Checks user's guess with the correct answer"""
        correct_answer = self.question_list[(self.question_number) - 1].answer
        if user_answer == correct_answer:
            self.score += 1
            print("🎉 That's correct ", end="")
        else:
            print("😕 Wrong answer ", end="")
        print(f"your current score is {self.score}/{self.question_number}")

    def show_final_score(self):
        """Display the final score after the game is over"""
        return f"Your final score is {self.score}/{self.question_number}"
