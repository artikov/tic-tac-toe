from single_game import single_game


# main function to play the game
def game():
    print("# Tic Tac Toe #")
    user1 = input("User 1, what is your name?\n")
    user2 = input("User 2, what is your name?\n")

    # simple validation for username
    if not user1 or not user2:
        print("Please enter valid name...")
        game()

    # by default make user 1 as current player
    current_player = user1

    # save player choice
    player_choice = {'X': '', 'O': ''}

    # needed to determine the current player
    options = ['X', 'O']

    scores = {
        user1: 0,
        user2: 0
    }

    while True:
        print("Chose your figure", current_player)
        print("Enter 1 for 'X'\n"
              "Enter 2 for '0'\n"
              "Enter 3 to Quit the game.")

        try:
            choice = int(input())
        except ValueError:
            print("Wrong input. Numbers 1-3 only, try again...")
            continue

        if choice == 1:
            player_choice['X'] = current_player
            if current_player == user1:
                player_choice['O'] = user2
            else:
                player_choice['O'] = user1

        elif choice == 2:
            player_choice['O'] = current_player
            if current_player == user1:
                player_choice['X'] = user2
            else:
                player_choice['X'] = user1

        elif choice == 3:
            print('Final Scores Are:')
            print(scores)
            break

        else:
            print('Wrong input. Please try again...')
            continue

        # store the winner in a single game
        winner = single_game(options[choice-1], player_choice)

        if winner != 'D':
            player_won = player_choice[winner]
            scores[player_won] += 1

        print(scores)

        if current_player == user1:
            current_player = user2
        else:
            current_player = user1


if __name__ == '__main__':
    game()
