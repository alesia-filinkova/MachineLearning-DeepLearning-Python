import json

def load_flashcards(file_path="flashcards.json"):
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileExistsError:
        return []

def save_flashcards(flashcards, file_path="flashcards.json"):
    with open(file_path, "w") as file:
        json.dump(flashcards, file, indent=4)

def add_flashcard():
    question = input("Enter the question: ")
    answer = input("Enter the answer: ")
    flashcards = load_flashcards()
    flashcards.append({"question": question, "answer": answer, "learned": False})
    save_flashcards(flashcards)
    print("Flashcard added successfully!")

def mark_as_learned():
    flashcards = load_flashcards()
    for card in flashcards:
        if not card["learned"]:
            print(f"Question: {card['question']}")
            mark = input("Mark this card as learned? (yes/no): ").lower()
            if mark == "yes":
                card["learned"] = True
                save_flashcards(flashcards)
                print("Marked as learned!")
                return
    print("No more flashcards to mark as learned!")
    
def review_flashcards():
    flashcards = load_flashcards()
    for card in flashcards:
        if not card["learned"]:
            print(f"Question: {card['question']}")
            user_answer = input("Your answer: ")
            if user_answer.lower() == card["answer"].lower():
                print("Correct!")
            else:
                print(f"Incorrect. The correct answer is: {card['answer']}")
            return
    print("No more flashcards to review!")

def main():
    print("Welcome to the Flashcards Learning App!")
    while True:
        print("\nOptions:")
        print("1. Add Flashcard")
        print("2. Review Flashcards")
        print("3. Mark Flashcards as Learned")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_flashcard()
        elif choice == "2":
            review_flashcards()
        elif choice == "3":
            mark_as_learned()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()