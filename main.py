#rock paper scissors game
import math
import random


def play():
    user = input('Enter your choice (r)ock, (p)aper, (s)cissors: ')
    #while invalid input
    while user not in ['r', 'p', 's']:
        user = input('Try again! Enter your choice (r)ock, (p)aper, (s)cissors: ')

    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return (0, user, computer)

    if is_win(user, computer):
        return (1, user, computer)
    return (-1, user, computer)


def is_win(player, computer):
    #check when players wins
    if (player == 'r' and computer == 's') or (player == 's' and computer == 'p') or (player == 'p' and computer == 'r'):
        return True
    return False


def best_of(n):
    #you must win most of n games
    nessesary_wins = math.ceil(n/2)
    user_wins = 0
    computer_wins = 0
    while user_wins < nessesary_wins and computer_wins < nessesary_wins:
        result, user, computer = play()

        if result == 0:
            print('It\'s a tie')
        elif result == 1:
            user_wins += 1
            print(f'You chose {user} and computer chose {computer}, you won!')
        else:
            computer_wins += 1
            print(f'You chose {user} and computer chose {computer}, sorry you lost')

    if user_wins >= nessesary_wins:
        print(f'You won {user_wins} out of {n} games, you won! ')
    elif computer_wins >= nessesary_wins:
        print(f'Sory computer won {computer_wins} out of {n} games, you lost ;( ')


if __name__ == '__main__':
    best_of(3)