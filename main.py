from rich import print
import os

def check_word(a, b):
    if len(a) != len(b):
        return 'Words are not the same length!'

    output = ''

    for i in range(len(b)):
        if a[i] == b[i]: 
            output += f'[bold green]|{a[i]}|[/bold green] '
        elif a[i] in b:
            output += f'[bold yellow]|{a[i]}|[/bold yellow] '
        else: 
            output += f'[bold gray]|{a[i]}|[/bold gray] '

    return output

game_board = [[ '| | ', '| | ', '| | ', '| | ', '| | '],
              [ '| | ', '| | ', '| | ', '| | ', '| | '],
              [ '| | ', '| | ', '| | ', '| | ', '| | '],
              [ '| | ', '| | ', '| | ', '| | ', '| | '],
              [ '| | ', '| | ', '| | ', '| | ', '| | '],
              [ '| | ', '| | ', '| | ', '| | ', '| | ']]

running = True
turn = 1
solution = 'raged'

print(check_word('farty', 'faryi'))


while running:
    print('\n[underline bold]      WORDLE[/underline bold]')
    print(f'    Guess: {turn}/6\n')

    for i in game_board:
        print(''.join(i))

    print('\nEnter your guess: ')
    guess = input()

    if len(guess) > 5 or len(guess) < 5 or guess.isalpha() != True:
        print('Guess must be 5 letters')
        continue

    game_board[turn-1] = check_word(guess.lower(), solution)
    turn += 1
