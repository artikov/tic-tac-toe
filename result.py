# function to check winning conditions
def check_win(player_position, current_player):
    # all possible winning combinations
    combinations = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

    for x in combinations:

        if all(y in player_position[current_player] for y in x):
            return True

    return False


# check if draw
def check_draw(player_pos):
    if len(player_pos['X']) + len(player_pos['O']) == 9:
        return True

    return False

