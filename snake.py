"""
@Author: Ravi Singh

@Date: 2023-1-12 11:20:30

@Last Modified by:

@Last Modified time: 2023-4-12 1:25:30

@Title : Employee Wage Calculator
"""

import random


def play(position):
    while position < 100:
        dice = random.randint(1, 6)
        play_condition = random.randint(0, 2)
        if play_condition == 0:
            position += 0
            print(f'Player stays at the same position.')
        elif play_condition == 1:
            position += dice
            if position < 100:
                print(f'Player moves {dice} position ahead.')
            elif position > 100:
                print(f'Extra numbers player cannot move move. ')
                position -= dice
            else:
                print(f'Player moves {dice} position ahead.')
                print(f'Player Wins!!!!!')
        else:
            if position >= 0 and position >= dice:
                position -= dice
                print(f'Player moves {dice} position backward.')
                if position <= 0:
                    print(f'Sorry!! You need to restart.')
                    position = 0
        print(f'Player is at {position} position.')

if __name__ == "__main__":
    start_position = 0
    play(start_position)
