"""
@Author: Ravi Singh

@Date: 2023-1-12 11:20:30

@Last Modified by:

@Last Modified time: 2023-4-12 1:25:30

@Title : Employee Wage Calculator
"""

import random


def player():
    """
            Description: Player function for the snake ladder problem to lay between two players.

             Parameter: start_position

            Return: Nothing

    """
    player1_pos = 0
    player2_pos = 0
    player_no = 1
    while player1_pos < 100 and player2_pos < 100:
        match player_no:
            case 1:
                dice = play()
                if dice > 0:
                    if player1_pos + dice > 100:
                        pass
                    else:
                        player1_pos += dice
                        player_no = 1
                        continue
                else:
                    player1_pos += dice
                    if player1_pos < 0:
                        player1_pos = 0
                    player_no = 2
                print(f"Player 1 is at position: {player2_pos}")

            case 2:
                dice = play()
                if dice > 0:
                    if player2_pos + dice > 100:
                        pass
                    else:
                        player2_pos += dice
                        player_no = 2
                        continue
                else:
                    player2_pos += dice
                    if player2_pos < 0:
                        player2_pos = 0
                    player_no = 1
                print(f"Player 2 is at position: {player2_pos}")

    if player1_pos == 100:
        print(f"Player 1 is win!! at position {player1_pos}\n")
    else:
        print(f"Player 2 is win!! at position {player2_pos}\n")


def play():
    """
        Description: Play function to execute different cases of snake ladder problem.

         Parameter: start_position

        Return: Nothing

    """
    dice = random.randint(1, 6)
    play_condition = random.randint(0, 2)
    if play_condition == 0:
        print(f'Player stays at the same position.')
        return 0
    elif play_condition == 1:
        print(f'Player gets the ladder.')
        return dice
    else:
        print(f'Player gets the snake.')
        return -dice


if __name__ == "__main__":
    start_position = 0
    player()
