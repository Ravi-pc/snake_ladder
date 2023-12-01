"""
@Author: Ravi Singh

@Date: 2023-1-12 11:20:30

@Last Modified by:

@Last Modified time: 2023-1-12 12:20:30

@Title : Employee Wage Calculator
"""

import random


def play(dice):
    position = 0
    check_play = random.randint(0, 2)
    if check_play == 1:
        position = position
    elif check_play == 2:
        position += dice
    else:
        position -= dice
    print(f'current position {position}')


def dice_throw():
    """
            Description: dice_throw function to generate number between 0 and 6.

            Parameter: None

            Return: Numbers between

    """

    dice = random.randint(1, 6)
    play(dice)
    return dice


def snake_ladder():
    """
            Description: Snake ladder problem.

            Parameter: None

            Return: Zero

    """
    return 0


if __name__ == "__main__":
    print(f'Starting position is {snake_ladder()}')
    print(f'Dice throw Number {dice_throw()}')
