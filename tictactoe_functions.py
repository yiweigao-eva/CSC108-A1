import math

EMPTY = '-'

def is_between(value, min_value, max_value):
    """ (number, number, number) -> bool

    Precondition: min_value <= max_value

    Return True if and only if value is between min_value and max_value,
    or equal to one or both of them.

    >>> is_between(1.0, 0.0, 2)
    True
    >>> is_between(0, 1, 2)
    False
    """
    return value <= max_value and value >= min_value


def game_board_full(game_board):
    """(str) -> bool
    
    Retrun True iff there is no empty characters in the gameboard
    
    >>>game_board_full('1234-678-')
    False
    >>>game_board_full('123456789')
    True
    """
    return EMPTY not in game_board


def get_board_size(game_board):
    """(str) -> int
    
    Return the length of each side of the given game board
    
    >>>get_board_size('123456789')
    3
    >>>get_board_size('1234567890098765432112345')
    5
    """
    return int(math.sqrt(len(game_board)))


def make_empty_board(board_size):
    """(int) -> str
    
    Precondition: 1 <= board_size <= 9
    
    Return a string for storing information about a tic-tac-toe game board whose
    size is given by the board_size
    
    #>>>make_empty_board(9)
    #'---------'
    #>>>make_empty_board(4)
    #'----'
    >>>make_empty_board(6)
    '-----------------------------------'
    >>>make_empty_board(3)
    '---------'
    """
    #You misunderstood requirements of this function. Board_size is the length of one edge of the board.
    #return '-' * board_size
    #Use the constant EMPTY instead of '-'.
    empty = '-' * (board_size ** 2)
    return empty

def get_position(row_index, col_index, board_size):
    """(int, int, int) -> int
    
    Precondition: 0 <= row_indices <= board size, 0 <= column_indices <= board 
    size, 1 <= board_size <= 9
    
    Return the index of the string that corresponding to the given row and 
    column indices
    
    >>>get_position(1, 2 ,3)
    1
    >>>get_position(3, 3, 3)
    8
    >>>get_position(2, 3, 3)
    5
    """
    str_index = (row_index - 1) * board_size + col_index -1
    
    return str_index


def make_move(symbol, row_index, col_index, game_board):
    """(str, int, int, str) -> str
    
    Return the tic-tac-toe game board that results when the given symbol is 
    placed at the given cell position
    
    >>>make_move('X', 1, 2, '---------')
    '-X-------'
    >>>make_move('O', 2, 2, '-X-------')
    '-X--O----'
    """
    board_size = get_board_size(game_board)
    position_to_put = get_position(row_index, col_index, board_size)
    game_board = game_board[:position_to_put] + symbol + game_board[position_to_put + 1:]
    
    return game_board


def extract_line(game_board, direction, row_col_number):
    """(str, str, int) -> str
    
    Precondition: row_or_col_number <= board_size, 1 <= board_size <= 9
    
    Return the characters that make up the specified row, column or diagonal.
    
    >>>extract_line('XXOOOXOXO', 'across', 1)
    'XXO'
    >>>extract_line('XXOOOXOXO', 'down', 3)
    'OXO'
    >>>extract_line('XXOOOXOXO', 'down_diagonal', 1)
    'XOO'
    >>>extract_line('XXOOOXOXO', 'up_diagonal', 1)
    'OOO'
    """
    #
    board_size = get_board_size(game_board)
    across_start = board_size * (row_col_number - 1)
    across_end = across_start + board_size
    down_start = row_col_number - 1
    down_end = down_start + len(game_board)
    start_to_end = board_size * (board_size - 1)
    up_diagonal_end = -2 - (board_size - 1) * board_size
    
    if direction == 'across':
        return game_board[across_start:across_end]
    elif direction == 'down':
        return game_board[down_start:down_end:board_size]
    elif direction == 'down_diagonal':
        return game_board[::board_size + 1]
    elif direction == 'up_diagonal':
        return game_board[-board_size:up_diagonal_end:-(board_size - 1)]
    
    # Students are to complete the body of this function, and then put their
    # solutions for the other required functions below this function.
