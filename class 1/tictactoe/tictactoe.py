"""
Tic Tac Toe Player
"""

import math

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
    X_count = sum(row.count(X) for row in board)
    O_count = sum(row.count(O) for row in board)
    return X if X_count <= O_count else O
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    return {(i,j) for i in range(3) for j in range(3) if board[i][j] == EMPTY}
    raise NotImplementedError


def result(board, action):
    """
    返回在指定动作 (i, j) 后生成的新棋盘状态。
    如果动作无效（如越界或位置已被占用），抛出 ValueError。
    """
    if action is None:
        raise ValueError("Action cannot be None")

    i, j = action

    # 检查 i, j 是否在棋盘范围内
    if not (0 <= i < 3 and 0 <= j < 3):
        raise ValueError("Invalid action: Move out of bounds")

    # 检查目标位置是否为空
    if board[i][j] != EMPTY:
        raise ValueError("Invalid action: Position already taken")

    # 创建棋盘深拷贝并执行动作
    new_board = [row[:] for row in board]
    new_board[i][j] = player(board)
    return new_board

    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not EMPTY:
            return row[0]
        
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] and board[0][j] is not EMPTY:
            return board[0][j]
    
    if board[0][0] == board[1][1] == board[2][j] and board[0][j] is not EMPTY:
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not EMPTY:
        return board[0][2]
    
    return None
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    return winner(board) is not None or all (EMPTY not in row for row in board)
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    win = winner(board)

    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    current_player = player(board)

    if current_player == X:
        value,move = max_value(board)
    else:
        value,move = min_value(board)

    return move

    raise NotImplementedError


def max_value(board):
    if terminal(board):
        return utility(board),None
    
    v = -math.inf
    best_move = None
    
    for action in actions(board):
        min_result, _ = min_value(result(board,action))
        if min_result > v:
            v = min_result
            best_move = action
        
    return v , best_move

def min_value(board):
    if terminal(board):
        return utility(board),None
    
    v = math.inf
    best_move = None
    
    for action in actions(board):
        max_result, _ = max_value(result(board,action))
        if max_result < v:
            v = max_result
            best_move = action
        
    return v , best_move