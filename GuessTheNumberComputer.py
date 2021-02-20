import random


def guess_num(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 anf {x}'))
        if guess < random_number:
            print("sorry, guess again. Too low.")
        elif guess > random_number:
            print('Sorry, guess again. Too high')

    print(f'Congrats!! You guess the number {random_number} correctly.')


guess_num(10)
