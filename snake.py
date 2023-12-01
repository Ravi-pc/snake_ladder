"""
@Author: Ravi Singh

@Date: 2023-1-12 11:20:30

@Last Modified by:

@Last Modified time: 2023-1-12 12:20:30

@Title : Employee Wage Calculator
"""

import random


def play(position):
    while position <= 100:
        dice = random.randint(1, 6)
        while position < 100:
            play_condition = random.randint(0, 2)
            match play_condition:
                case 0:
                    position += 0
                    print(f'Player stays at the position ')
                case 1:
                    position += dice
                    print(f'Player moves {dice} position ahead and is at {position} position')
                case 2:
                    if position != 0:
                        position -= dice
                        print(f'Player moves {dice} position backward is at {position} position')



if __name__ == "__main__":
    start_position = 0
    play(start_position)
