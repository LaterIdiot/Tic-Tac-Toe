from math import *

print("""
Tic-tac-toe

 • This program allows you to play Tic-tac-toe against a player or a computer.
 • To select a spot on the board you have to type in the number corresponding to that spot.
 """)

# sets up the board as 2 dimensional array
board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# initalizes the player as X
player = "X"
# asks the user if they want to play against an AI
ai = input(
    "Do you want to play against an AI (yes/no by default it's no and anything other than yes is also no)? "
)
# turns user input into boolean
ai = True if ai == "yes" else False
# a variable to represent if AI is going first or not and is by default False
ai_first = False
if ai:
    # asks the user if they want AI to go first or not
    ai_first = input(
        "Do you want the AI to go first (yes/no by default it's no and anything other than yes is also no)? "
    )
    # turns user input into boolean
    ai_first = True if ai_first == "yes" else False


def display_board(board: list):
    print(
        f"\n+———+———+———+\n| {board[0][0]} | {board[0][1]} | {board[0][2]} |\n+———+———+———+\n| {board[1][0]} | {board[1][1]} | {board[1][2]} |\n+———+———+———+\n| {board[2][0]} | {board[2][1]} | {board[2][2]} |\n+———+———+———+"
    )


# a function for user turn
def turn(board: list, player: str):
    # converts user input into a move on the board
    try:
        move = input(f"Pick turn as {player}: ")

        if move == "stop":
            return "stop"
        else:
            move = int(move)

        if (move > 9) or (move < 1):
            print("Input can't be bigger than 9 or less than 1!")
            raise

        if type(board[floor((move - 1) / 3)][(move % 3) - 1]) == int:
            board[floor((move - 1) / 3)][(move % 3) - 1] = player
        else:
            print("You can't choose a spot that has been already selected!")
            raise
    except:
        print("")
        return turn(board, player)


# checks if there is a winner or a tie
def winner(board: list):
    opponent = "O" if player == "X" else "X"

    if (
        (board[0].count(player) == 3)
        or (board[1].count(player) == 3)
        or (board[2].count(player) == 3)
        or ([board[0][0], board[1][0], board[2][0]].count(player) == 3)
        or ([board[0][1], board[1][1], board[2][1]].count(player) == 3)
        or ([board[0][2], board[1][2], board[2][2]].count(player) == 3)
        or ([board[0][0], board[1][1], board[2][2]].count(player) == 3)
        or ([board[0][2], board[1][1], board[2][0]].count(player) == 3)
    ):
        return player
    elif (
        (board[0].count(opponent) == 3)
        or (board[1].count(opponent) == 3)
        or (board[2].count(opponent) == 3)
        or ([board[0][0], board[1][0], board[2][0]].count(opponent) == 3)
        or ([board[0][1], board[1][1], board[2][1]].count(opponent) == 3)
        or ([board[0][2], board[1][2], board[2][2]].count(opponent) == 3)
        or ([board[0][0], board[1][1], board[2][2]].count(opponent) == 3)
        or ([board[0][2], board[1][1], board[2][0]].count(opponent) == 3)
    ):
        return opponent
    elif [
        list(map(type, board[0])).count(int) == 0,
        list(map(type, board[1])).count(int) == 0,
        list(map(type, board[2])).count(int) == 0,
    ].count(False) == 0:
        return "tie"
    else:
        return False


# function based on minimax algorithm this is a recursive algorithm
def minimax(maxing: bool, board: list, player: str):
    """
    This is a algorithm that helps choose the best move of a stage in
    the game. It does this by looping through each possible stage from
    the current stage and figures out which one is the best on scoring
    system and picking the on with the highest score.
    """

    opponent = "O" if player == "X" else "X"

    scores = {"player": 1, "opponent": -1, "tie": 0}
    win_result = winner(board)

    if win_result:
        return (
            scores["tie"]
            if win_result == "tie"
            else scores["player" if player == win_result else "opponent"]
        )

    if maxing:
        best_score = -2
        for i in range(3):
            for j in range(3):
                if type(board[i][j]) == int:
                    board[i][j] = player
                    score = minimax(False, board, player)
                    board[i][j] = (i * 3) + (j + 1)
                    if score > best_score:
                        best_score = score
                        if best_score == 1:
                            break

            if best_score == 1:
                break

        return best_score
    else:
        best_score = 2
        for i in range(3):
            for j in range(3):
                if type(board[i][j]) == int:
                    board[i][j] = opponent
                    score = minimax(True, board, player)
                    board[i][j] = (i * 3) + (j + 1)
                    if score < best_score:
                        best_score = score
                        if best_score == -1:
                            break

            if best_score == -1:
                break

        return best_score


# picks AI turn
def ai_turn(board: list, player: str):
    opponent = "O" if player == "X" else "X"

    best_score = -2
    best_move = []

    # this set of for loops assigns best move to the variable "best_move"
    for i in range(3):
        for j in range(3):
            if type(board[i][j]) == int:
                board[i][j] = player
                score = minimax(False, board, player)
                board[i][j] = (i * 3) + (j + 1)
                if score > best_score:
                    best_score = score
                    best_move = [i, j]
                    if best_score == 1:
                        break

        if best_score == 1:
            break

    board[best_move[0]][best_move[1]] = player
    return ((best_move[0] * 3) + (best_move[1] + 1))


# displays winner or a tie if game end occurs and also returns if the game ended or not in boolean
def win_display(result: str, board: list):
    if result == "tie":
        display_board(board)
        print("Nobody won it's a TIE!")
        return True
    elif result:
        display_board(board)
        print(f"🎉{player} is the WINNER!🎉")
        return True
    else:
        return False


# main loop to run the game until game end
while True:
    display_board(board)

    if ai_first:
        ai_move = ai_turn(board, player)
        print(
            f"AI picked its turn as {player} at spot {ai_move}"
        )

        if win_display(winner(board), board):
            break
        else:
            display_board(board)

        player = "O" if player == "X" else "X"
        if turn(board, player) == "stop":
            break

        if win_display(winner(board), board):
            break
    else:
        if turn(board, player) == "stop":
            break

        if win_display(winner(board), board):
            break

        if ai:
            display_board(board)
            player = "O" if player == "X" else "X"
            ai_move = ai_turn(board, player)
            print(
                f"AI picked its turn as {player} at spot {ai_move}"
            )

            if win_display(winner(board), board):
                break

    player = "O" if player == "X" else "X"

input("\nPress any button to exit this window!")