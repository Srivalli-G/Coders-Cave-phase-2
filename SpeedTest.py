import random
import time
def generate_random_text():
    texts = [
        "The quick brown fox jumps over the lazy dog.",
        "Python is a versatile programming language.",
        "Practice makes perfect.",
        "Typing speed matters in the digital age.",
        "Coding is fun and challenging at the same time.",]
    return random.choice(texts)
def calculate_wpm(text, time_taken):
    words = len(text.split())
    minutes = time_taken / 60
    wpm = words / minutes
    return round(wpm, 2)
def main():
    input("Welcome to the Typing Speed Tester! Press Enter to start...")
    text_to_type = generate_random_text()
    print("Type the following text:")
    print(text_to_type)
    input("Press Enter to begin typing...")
    start_time = time.time()
    user_input = input("Start typing: ")
    end_time = time.time()
    time_taken = end_time - start_time
    wpm = calculate_wpm(text_to_type, time_taken)
    print(f"Time taken: {time_taken:.2f} seconds")
    print(f"Your typing speed: {wpm} WPM")
    accuracy = sum(a == b for a, b in zip(text_to_type, user_input)) / len(text_to_type)
    print(f"Accuracy: {accuracy * 100:.2f}%")
if __name__ == "__main__":
    main()