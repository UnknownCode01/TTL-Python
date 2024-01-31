import random

def generate_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    return num1, num2

def ask_question(num1, num2):
    user_answer = int(input(f" {num1} times {num2}? "))
    return user_answer == num1 * num2

def main():
    print("Welcome to the Multiplication Game!")

    correct_count = 0
    total_questions = 10

    for _ in range(total_questions):
        num1, num2 = generate_question()
        is_correct = ask_question(num1, num2)

        if is_correct:
            print("Correct! Great job!\n")
            correct_count += 1
        else:
            print(f"That's incorrect, the correct answer is {num1 * num2}.\n")

    if correct_count==10:
        print('Congratulations, you scored a perfect 10/10')
    else:
        print(f"Game Over! You got {correct_count} out of {total_questions} questions correct.")

if __name__ == "__main__":
    main()
