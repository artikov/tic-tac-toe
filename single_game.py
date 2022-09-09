from grid import print_tic_tac_toe
from result import check_win, check_draw


def single_game(current_player):
    # create empty boxes for grid
    values = [' ' for x in range(9)]

    player_position = {
        'X': [],
        'O': []
    }

    while True:
        print_tic_tac_toe(values)

        # try exception for player move
        try:
            print(current_player, "'s turn. Which box? : ")
            move = int(input())
        except ValueError:
            print("Numbers from 1-9 only. Try again...")
            continue

        # sanity check if move in range 1-9
        if move < 1 or move > 9:
            print("Wrong input. 1 to 9 only. Try again...")
            continue

        # check if box is available
        if values[move-1] != ' ':
            print("Place is already filled. Try another box...")
            continue

        # update grid
        values[move-1] = current_player

        # update player positions
        player_position[current_player].append(move)

        # function call to check winning
        if check_win(player_position, current_player):
            print_tic_tac_toe(values)
            print(current_player, 'has won the game!!!\n')
            return current_player

        if check_draw(player_position):
            print_tic_tac_toe(values)
            print('DRAW!!!\n')
            return 'D'

        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'