from rich import print
from collections import defaultdict
import random

def check_word(a, b):
    if len(a) != len(b):
        return 'Words are not the same length!'
    a = a.lower()
    output = ''
    winCount = 0
    win = False

    letters = defaultdict(int)
    letters_used = defaultdict(int)

    for i in b:
        letters[i] += 1

    print(letters)

    for i in range(len(b)):
        if a[i] == b[i]:
            output += f'[bold green]|{a[i].upper()}|[/bold green] '
            winCount += 1
            letters_used[a[i]] += 1
        elif a[i] in b and letters_used[a[i]] < letters[a[i]]:
            output += f'[bold yellow]|{a[i].upper()}|[/bold yellow] '
            letters_used[a[i]] += 1
        else: 
            output += f'[bold gray]|{a[i].upper()}|[/bold gray] '
    
    if winCount >= 5:
         win = True

    return output, win

def print_board(gb):
    print('\n[underline bold]      WORDLE[/underline bold]')
    print(f'    Guess: {turn}/6\n')

    print(' 1   2   3   4   5')
    for i in gb:
        print(''.join(i))

game_board = [[ '| | ', '| | ', '| | ', '| | ', '| | '],
              [ '| | ', '| | ', '| | ', '| | ', '| | '],
              [ '| | ', '| | ', '| | ', '| | ', '| | '],
              [ '| | ', '| | ', '| | ', '| | ', '| | '],
              [ '| | ', '| | ', '| | ', '| | ', '| | '],
              [ '| | ', '| | ', '| | ', '| | ', '| | ']]

running = True
turn = 1
# solution = random.choice(open('words.txt').readlines())[:-1]
solution = 'aaabb'
print(f'\n Solution: {solution}')

while running:
    print_board(game_board)

    print('\nEnter your guess (q! to exit):')
    print('12345')
    guess = input()
    print('\n')

    if(guess == "q!"):
        break

    if len(guess) > 5 or len(guess) < 5 or guess.isalpha() != True:
        print('Guess must be 5 letters')
        continue

    game_board[turn-1] = check_word(guess, solution)[0]
    turn += 1

    if(check_word(guess, solution)[1]):
        print_board(game_board)
        print(f'\nCongratulations! [bold green]{solution.upper()}[/bold green] was the word!')
        break

    if turn > 6:
        turns = 6
        print_board(game_board)
        print(f'\nThe game is over. The word was: [bold red]{solution.upper()}[/bold red]!')
        break
