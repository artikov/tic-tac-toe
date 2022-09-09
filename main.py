# Function to create the game board, values represent the cells on the board
def print_tic_tac_toe(values):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[0], values[1], values[2]))
    print('\t_____|_____|_____')

    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[3], values[4], values[5]))
    print('\t_____|_____|_____')

    print("\t     |     |")

    print("\t  {}  |  {}  |  {}".format(values[6], values[7], values[8]))
    print("\t     |     |")
    print("\n")


# main function for a single game
def game():
    user1 = input("User 1, what is your name?\n")
    user2 = input("User 2, what is your name?\n")

    # simple validation for username
    if not user1 or not user2:
        print("Please enter valid name...")
        game()

    print("\nGAME STARTS ! ! !")

    values = [' ' for x in range(9)]

    # object to store position of players
    player_position = {
        'X': [],
        'O': [],
    }

    print_tic_tac_toe(values)


if __name__ == '__main__':
    game()
