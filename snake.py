"""
@Author: Ravi Singh

@Date: 2023-1-12 11:20:30

@Last Modified by:

@Last Modified time: 2023-1-12 12:20:30

@Title : Employee Wage Calculator
"""

import random


def dice_throw():
    """
            Description: dice_throw function to generate number between 0 and 6.

            Parameter: None

            Return: Numbers between

    """
    return random.randint(1, 6)


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
