from rich import print
import random

def check_word(a, b):
    if len(a) != len(b):
        return 'Words are not the same length!'

    output = ''
    winCount = 0
    win = False

    for i in range(len(b)):
        if a[i] == b[i]: 
            output += f'[bold green]|{a[i].upper()}|[/bold green] '
            winCount += 1
        elif a[i] in b:
            output += f'[bold yellow]|{a[i].upper()}|[/bold yellow] '
        else: 
            output += f'[bold gray]|{a[i].upper()}|[/bold gray] '
    
    if winCount >= 5:
         win = True

    return output, win

def print_board(gb):
    print('\n[underline bold]      WORDLE[/underline bold]')
    print(f'    Guess: {turn}/6\n')

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
# solution = 'raged'
solution = random.choice(open('words.txt').readlines())[:-1]
print(f'|{solution}|')

while running:
    print_board(game_board)

    print('\nEnter your guess (q! to exit): ')
    guess = input()
    print('\n')

    if(guess == "q!"):
        break

    if len(guess) > 5 or len(guess) < 5 or guess.isalpha() != True:
        print('Guess must be 5 letters')
        continue

    game_board[turn-1] = check_word(guess.lower(), solution)[0]
    turn += 1

    if(check_word(guess.lower(), solution)[1]):
        print_board(game_board)
        print(f'\nCongratulations! [bold green]{solution.upper()}[/bold green] was the word!')
        break

    if turn > 6:
        turns = 6
        print_board(game_board)
        print(f'\nThe game is over. The word was: [bold red]{solution.upper()}[/bold red]!')
        break
