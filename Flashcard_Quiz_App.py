import random

class Flashcard:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

class FlashcardQuizApp:
    def __init__(self):
        self.flashcards = []

    def add_flashcard(self):
        question = input("Enter the question: ")
        answer = input("Enter the answer: ")
        flashcard = Flashcard(question, answer)
        self.flashcards.append(flashcard)
        print("Flashcard added!")

    def quiz_user(self):
        if not self.flashcards:
            print("No flashcards available. Please add some first.")
            return
        
        random.shuffle(self.flashcards)
        score = 0

        for flashcard in self.flashcards:
            user_answer = input(f"Question: {flashcard.question} ")
            if user_answer.lower() == flashcard.answer.lower():
                print("Correct!")
                score += 1
            else:
                print(f"Incorrect! The correct answer is: {flashcard.answer}")

        print(f"You scored {score} out of {len(self.flashcards)}.")

    def run(self):
        while True:
            print("\nFlashcard Quiz App")
            print("1. Add Flashcard")
            print("2. Quiz Me")
            print("3. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                self.add_flashcard()
            elif choice == '2':
                self.quiz_user()
            elif choice == '3':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    app = FlashcardQuizApp()
    app.run()
