import math

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

# a function for user turn
def turn():
    try:
        move = input(f"Pick turn as {player}: ")

        if move == "stop":
            return "stop"
        else:
            move = int(move)

        if (move > 9) or (move < 1):
            print("Input can't be bigger than 9 or less than 1!")
            raise

        if type(board[math.floor((move - 1) / 3)][(move % 3) - 1]) == int:
            board[math.floor((move - 1) / 3)][(move % 3) - 1] = player
        else:
            print("You can't choose a spot that has been already selected!")
            raise
    except:
        return turn()


def winner():
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


def minimax(maxing: bool):
    opponent = "O" if player == "X" else "X"

    scores = {"player": 1, "opponent": -1, "tie": 0}
    win_result = winner()

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
                    score = minimax(False)
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
                    score = minimax(True)
                    board[i][j] = (i * 3) + (j + 1)
                    if score < best_score:
                        best_score = score
                        if best_score == -1:
                            break

            if best_score == -1:
                break

        return best_score


def ai_turn():
    opponent = "O" if player == "X" else "X"

    best_score = -2
    best_move = []

    for i in range(3):
        for j in range(3):
            if type(board[i][j]) == int:
                board[i][j] = player
                score = minimax(False)
                board[i][j] = (i * 3) + (j + 1)
                if score > best_score:
                    best_score = score
                    best_move = [i, j]
                    if best_score == 1:
                        break

        if best_score == 1:
            break

    board[best_move[0]][best_move[1]] = player
    return best_move


def win_display(result: str):
    if result == "tie":
        print(
            f"\n+———+———+———+\n| {board[0][0]} | {board[0][1]} | {board[0][2]} |\n+———+———+———+\n| {board[1][0]} | {board[1][1]} | {board[1][2]} |\n+———+———+———+\n| {board[2][0]} | {board[2][1]} | {board[2][2]} |\n+———+———+———+"
        )
        print("Nobody won it's a TIE!")
        return True
    elif result:
        print(
            f"\n+———+———+———+\n| {board[0][0]} | {board[0][1]} | {board[0][2]} |\n+———+———+———+\n| {board[1][0]} | {board[1][1]} | {board[1][2]} |\n+———+———+———+\n| {board[2][0]} | {board[2][1]} | {board[2][2]} |\n+———+———+———+"
        )
        print(f"🎉{player} is the WINNER!🎉")
        return True
    else:
        return False


while True:
    print(
        f"\n+———+———+———+\n| {board[0][0]} | {board[0][1]} | {board[0][2]} |\n+———+———+———+\n| {board[1][0]} | {board[1][1]} | {board[1][2]} |\n+———+———+———+\n| {board[2][0]} | {board[2][1]} | {board[2][2]} |\n+———+———+———+"
    )

    if ai_first:
        ai_move = ai_turn()
        print(
            f"AI has taken it's turn as {player} at spot {(ai_move[0] * 3) + (ai_move[1] + 1)}"
        )

        if win_display(winner()):
            break
        else:
            print(
                f"\n+———+———+———+\n| {board[0][0]} | {board[0][1]} | {board[0][2]} |\n+———+———+———+\n| {board[1][0]} | {board[1][1]} | {board[1][2]} |\n+———+———+———+\n| {board[2][0]} | {board[2][1]} | {board[2][2]} |\n+———+———+———+"
            )

        player = "O" if player == "X" else "X"
        if turn() == "stop":
            break

        if win_display(winner()):
            break
    else:
        if turn() == "stop":
            break

        if win_display(winner()):
            break

        if ai:
            print(
                f"\n+———+———+———+\n| {board[0][0]} | {board[0][1]} | {board[0][2]} |\n+———+———+———+\n| {board[1][0]} | {board[1][1]} | {board[1][2]} |\n+———+———+———+\n| {board[2][0]} | {board[2][1]} | {board[2][2]} |\n+———+———+———+"
            )
            player = "O" if player == "X" else "X"
            ai_move = ai_turn()
            print(
                f"AI has taken it's turn as {player} at spot {(ai_move[0] * 3) + (ai_move[1] + 1)}"
            )

            if win_display(winner()):
                break

    player = "O" if player == "X" else "X"
