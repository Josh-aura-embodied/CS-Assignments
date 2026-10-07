from score import get_score_rating, update_score
from utils import check_user_guess, generate_secret_number, prompt_valid_guess


def main():
    print("Number Guessing Game")
    print("--------------------")

    secret_number = generate_secret_number()
    current_score = 100

    while True:
        guess = prompt_valid_guess()
        is_correct = check_user_guess(secret_number, guess)

        if is_correct:
            break

        current_score = update_score(current_score)
        print(f"Current score: {current_score}")
        print()

    rating = get_score_rating(current_score)

    print()
    print("--- Game Over ---")
    print(f"Final Score: {current_score}/100")
    print(f"Rating: {rating}")


if __name__ == "__main__":
    main()