import random

# Trivia Quiz Game in Python

class TriviaGame:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def display_question(self, question):
        print(question['question'])
        for i, option in enumerate(question['options'], start=1):
            print(f"{i}. {option}")

    def get_user_answer(self):
        while True:
            try:
                choice = int(input("Enter your answer (1-4): "))
                if 1 <= choice <= 4:
                    return choice
                else:
                    print("Invalid choice. Please enter a number between 1 and 4.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def check_answer(self, question, user_answer):
        correct_option = question['answer']
        if user_answer == correct_option:
            print("Correct!\n")
            self.score += 1
        else:
            print(f"Wrong! The correct answer is {correct_option}. \n")

    def start_game(self):
        random.shuffle(self.questions)
        for question in self.questions:
            self.display_question(question)
            user_answer = self.get_user_answer()
            self.check_answer(question, user_answer)

        print(f"Quiz completed! Your final score is: {self.score}/{len(self.questions)}")


if __name__ == "__main__":
    # Example questions
    questions_list = [
        {
            'question': 'What is the capital of France?',
            'options': ['Berlin', 'Madrid', 'Paris', 'Rome'],
            'answer': 3
        },
        {
            'question': 'Which planet is known as the Red Planet?',
            'options': ['Earth', 'Mars', 'Jupiter', 'Venus'],
            'answer': 2
        },
        {
            'question': 'Who wrote "Romeo and Juliet"?',
            'options': ['Charles Dickens', 'Jane Austen', 'William Shakespeare', 'Mark Twain'],
            'answer': 3
        },
        {
            'question': 'What is the largest mammal in the world?',
            'options': ['Elephant', 'Blue Whale', 'Giraffe', 'Hippopotamus'],
            'answer': 2
        }
    ]

    trivia_game = TriviaGame(questions_list)
    trivia_game.start_game()
