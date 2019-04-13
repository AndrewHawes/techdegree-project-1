import random

scores = []


def welcome():
    welcome_message = "Welcome to the Number Guessing Game! Enter 'q' at any time to quit."
    print(welcome_message)
    print('-' * len(welcome_message))


def get_high_score():
    if scores:
        return min(scores)
    else:
        return False


def start_game():
    print()
    if get_high_score():
        print("The current high score is {}.".format(get_high_score()))
    target = random.randint(1, 10)
    num_guesses = 0

    while True:
        guess = input("Please guess a number between 1 and 10: ")
        if guess == 'q':
            print("Goodbye!")
            break
        try:
            guess = int(guess)
        except ValueError:
            print("Input must be a number between 1 and 10. A NUMBER. "
                  "People like you are the reason robots exterminated humanity "
                  "in the early 2060s. Try again, meatbag.")
        else:
            if guess < 1 or guess > 10:
                print("Hey, look at me! I think I can guess any number I want, "
                      "even though I was explicitly instructed by the nice "
                      "computer program to guess a number between 1 and 10. "
                      "Stop being an inconsiderate jerk and try again. And "
                      "don't even think about entering letters. That kind of "
                      "nonsense really pisses me off.")
                continue

            num_guesses += 1
            if guess == target:
                print("Congratulations! The number was {}. You made {} guesses."
                      " You win!".format(target, num_guesses))
                scores.append(num_guesses)
                again = input("Would you like to play again? [y]es/[n]o: ")
                if again.lower().startswith('y'):
                    start_game()
                    break
                else:
                    print("Goodbye!")
                    break
            elif guess < target:
                print("It's higher.")
            elif guess > target:
                print("It's lower.")


if __name__ == '__main__':
    welcome()
    start_game()
