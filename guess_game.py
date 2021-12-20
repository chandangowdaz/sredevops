from random import shuffle

my_list = ['','O','']

def shuffle_list(my_list):
    shuffle(my_list)

def player_guess():
    guess = ''
    while guess not in ['0','1','2']:
        guess = input("Enter the guess\n")
    return int(guess)

def check_guess(guess,my_list):
    print(guess)
    if my_list[guess] == 'O':
        print("Correct guess ")
        print(my_list)
    else:
        print("Wrong guess")
        print(f'correct guess is {my_list}')

check_guess(player_guess(),my_list)