import random

MIN = 1
MAX = 100


def generate_secret_number():
    return random.randint(MIN, MAX)


def prompt_valid_guess():
    while True:
        print(f"Guess a number between {MIN} and {MAX}:")
        try:
            guess = int(input().strip())
        except ValueError:
            print("Invalid input. Must be a number.")
            print()
            continue

        if guess < MIN or guess > MAX:
            print(f"Out of range. Must be between {MIN} and {MAX}.")
            print()
            continue

        return guess


def check_user_guess(secret_number, guess):
    if guess == secret_number:
        print("Correct!")
        return True
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")

    print()
    return False


if __name__ == "__main__":
    print("Testing utils module...")
    test_num = generate_secret_number()
    print(f"Generated test secret number: {test_num}")