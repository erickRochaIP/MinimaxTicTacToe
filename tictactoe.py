"""
Tic Tac Toe Player
"""

import math, copy, time

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    i=0
    for row in board:
        for space in row:
            if space is X:
                i = i+1
            elif space is O:
                i = i-1

    if i > 0:
        return O
    return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] is EMPTY:
                actions.add((i, j))

    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    if board[action[0]][action[1]] is not EMPTY:
        raise NameError('InvalidAction')

    boardAction = copy.deepcopy(board)
    boardAction[action[0]][action[1]] = player(board)

    return boardAction



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not EMPTY:
            return board[i][0]
        if board[0][i] == board [1][i] == board[2][i] and board[0][i] is not EMPTY:
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not EMPTY:
        return board[0][0]
    if board[2][0] == board[1][1] == board[0][2] and board[0][2] is not EMPTY:
        return board[2][0]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    for i in range(3):
        for j in range(3):
            if board[i][j] is EMPTY:
                return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win is X:
        return 1
    if win is O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    begin = time.time()
    
    possibleActions = actions(board)
    gamer = player(board)
    if gamer is X:
        bestScore = -math.inf
    else:
        bestScore = math.inf

    bestMove = None

    for action in possibleActions:
        boardPossible = result(board, action)
        if gamer is O:
            score = way(boardPossible, True)
        else:
            score = way(boardPossible, False)
        

        if gamer is X:
            if score > bestScore:
                bestScore = score
                bestMove = action
        else:
            if score < bestScore:
                bestScore = score
                bestMove = action

    end = time.time()
    print(end - begin)

    return bestMove

def way(board, isMaximizing):
    """
    Returns the value of the board
    """
    checkTerminal = terminal(board)
    if checkTerminal is True:
        score = utility(board)
        return score

    if isMaximizing is True:
        bestScore = -math.inf
        possibleActions = actions(board)
        for action in possibleActions:
            possibleBoard = result(board, action)
            score = way(possibleBoard, False)
            if score > bestScore:
                bestScore = score

        return bestScore
    else:
        bestScore = math.inf
        possibleActions = actions(board)
        for action in possibleActions:
            possibleBoard = result(board, action)
            score = way(possibleBoard, True)
            if score < bestScore:
                bestScore = score

        return bestScore

    return 0