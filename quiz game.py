import random

class QuizGame:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def display_welcome_message(self):
        print("Welcome to the Quiz Game!")
        print("Answer the following questions to test your knowledge.")
        print("Each correct answer earns you 1 point.")
        print("Let's get started!\n")

    def present_quiz_questions(self):
        random.shuffle(self.questions)
        for question in self.questions:
            print(question['question'])
            if 'options' in question:
                for index, option in enumerate(question['options'], start=1):
                    print(f"{index}. {option}")
            user_answer = input("Your answer: ").strip().lower()
            self.evaluate_answer(user_answer, question['answer'])
            print()

    def evaluate_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            print("Correct! You earned 1 point.")
            self.score += 1
        else:
            print("Incorrect.")
            print(f"The correct answer is: {correct_answer}")

    def display_final_results(self):
        print("\nQuiz completed!")
        print(f"Your final score is: {self.score}/{len(self.questions)}")

    def play_again(self):
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        return play_again == 'yes'


def main():
    questions = [
        {
            'question': "Who invented python programing language?",
            'answer': "Guido Van Rossum"
        },
        {
            'question': "Who is the father of the computer?",
            'answer': "Charles Babage"
        },
        {
            'question': "Who wrote 'Romeo and Juliet'?",
            'answer': "shakespeare"
        },
        {
            'question': "What is the chemical symbol for gold?",
            'answer': "Au"
        }
    ]

    while True:
        quiz = QuizGame(questions)
        quiz.display_welcome_message()
        quiz.present_quiz_questions()
        quiz.display_final_results()

        if not quiz.play_again():
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    main()
