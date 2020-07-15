"""
    Created: 29 March 2020 14:30
    Author: Martins Anerua
    Software: PyCharm Community Edition with Anaconda plugin 2019

    Notes:
        1. A state is a particular unique game board
        2. X is the Maximizer and O is the Minimizer
"""

import copy
import math
from time import sleep


def is_draw(state):
    """
    

    Parameters
    ----------
    state : list
        A list of length 10, representing a particular state of the game.

    Returns
    -------
    bool
        Returns True if the game, as represented by state, is a draw and returns False otherwise.

    """
    
    # possible skip: did not check if the game is a win or loss. Try to do this.
    if is_win(state, 'X') or is_win(state, 'O'):
        return False
    else:
        if '-' not in state:
            return True
        else:
            return False

def is_win(state, player):
    """
    

    Parameters
    ----------
    state : list
        A list of length 10, representing a particular state of the game.
    player : str
        A string of one character, representing the player whose win status is to be checked.

    Returns
    -------
    bool
        Returns True if the game results in a win for player, and returns False if it doesn't.

    """
    condition1 = ((player == state[0]) and (player == state[1]) and (player == state[2]))
    condition2 = ((player == state[3]) and (player == state[4]) and (player == state[5]))
    condition3 = ((player == state[6]) and (player == state[7]) and (player == state[8]))
    condition4 = ((player == state[0]) and (player == state[3]) and (player == state[6]))
    condition5 = ((player == state[1]) and (player == state[4]) and (player == state[7]))
    condition6 = ((player == state[2]) and (player == state[5]) and (player == state[8]))
    condition7 = ((player == state[0]) and (player == state[4]) and (player == state[8]))
    condition8 = ((player == state[2]) and (player == state[4]) and (player == state[6]))
    if condition1 or condition2 or condition3 or condition4 or condition5 or condition6 or condition7 or condition8:
        return True
    else:
        return False

def is_a_way(state, player):
    """
    

    Parameters
    ----------
    state : list
        A list of length 10, representing a particular state of the game.
    player : str
        A string of one character, representing the player whose status is to be checked.

    Returns
    -------
    bool
        Returns True if there is ONLY one a way to win for player in the current game state. Returns False otherwise

    """
    if end_state(state) or is_two_ways(state, player):
        return False
    else:
        condition1 = (('-' == state[0]) and (player == state[1]) and (player == state[2])) or (
                (player == state[0]) and ('-' == state[1]) and (player == state[2])) or (
                             (player == state[0]) and (player == state[1]) and ('-' == state[2]))
        condition2 = (('-' == state[3]) and (player == state[4]) and (player == state[5])) or (
                (player == state[3]) and ('-' == state[4]) and (player == state[5])) or (
                             (player == state[3]) and (player == state[4]) and ('-' == state[5]))
        condition3 = (('-' == state[6]) and (player == state[7]) and (player == state[8])) or (
                (player == state[6]) and ('-' == state[7]) and (player == state[8])) or (
                             (player == state[6]) and (player == state[7]) and ('-' == state[8]))
        condition4 = (('-' == state[0]) and (player == state[3]) and (player == state[6])) or (
                (player == state[0]) and ('-' == state[3]) and (player == state[6])) or (
                             (player == state[0]) and (player == state[3]) and ('-' == state[6]))
        condition5 = (('-' == state[1]) and (player == state[4]) and (player == state[7])) or (
                (player == state[1]) and ('-' == state[4]) and (player == state[7])) or (
                             (player == state[1]) and (player == state[4]) and ('-' == state[7]))
        condition6 = (('-' == state[2]) and (player == state[5]) and (player == state[8])) or (
                (player == state[2]) and ('-' == state[5]) and (player == state[8])) or (
                             (player == state[2]) and (player == state[5]) and ('-' == state[8]))
        condition7 = (('-' == state[0]) and (player == state[4]) and (player == state[8])) or (
                (player == state[0]) and ('-' == state[4]) and (player == state[8])) or (
                             (player == state[0]) and (player == state[4]) and ('-' == state[8]))
        condition8 = (('-' == state[2]) and (player == state[4]) and (player == state[6])) or (
                (player == state[2]) and ('-' == state[4]) and (player == state[6])) or (
                             (player == state[2]) and (player == state[4]) and ('-' == state[6]))
        if condition1 or condition2 or condition3 or condition4 or condition5 or condition6 or condition7 or condition8:
            return True
        else:
            return False

def is_two_ways(state, player):
    """
    

    Parameters
    ----------
    state : list
        A list of length 10, representing a particular state of the game.
    player : str
        A string of one character, representing the player whose status is to be checked.

    Returns
    -------
    bool
        Returns True if there are AT LEAST two ways to win for player in the current game state. Returns False otherwise

    """
    if end_state(state):
        return False
    else:
        condition1 = (('-' == state[0]) and (player == state[1]) and (player == state[2])) or (
                (player == state[0]) and ('-' == state[1]) and (player == state[2])) or (
                             (player == state[0]) and (player == state[1]) and ('-' == state[2]))
        condition2 = (('-' == state[3]) and (player == state[4]) and (player == state[5])) or (
                (player == state[3]) and ('-' == state[4]) and (player == state[5])) or (
                             (player == state[3]) and (player == state[4]) and ('-' == state[5]))
        condition3 = (('-' == state[6]) and (player == state[7]) and (player == state[8])) or (
                (player == state[6]) and ('-' == state[7]) and (player == state[8])) or (
                             (player == state[6]) and (player == state[7]) and ('-' == state[8]))
        condition4 = (('-' == state[0]) and (player == state[3]) and (player == state[6])) or (
                (player == state[0]) and ('-' == state[3]) and (player == state[6])) or (
                             (player == state[0]) and (player == state[3]) and ('-' == state[6]))
        condition5 = (('-' == state[1]) and (player == state[4]) and (player == state[7])) or (
                (player == state[1]) and ('-' == state[4]) and (player == state[7])) or (
                             (player == state[1]) and (player == state[4]) and ('-' == state[7]))
        condition6 = (('-' == state[2]) and (player == state[5]) and (player == state[8])) or (
                (player == state[2]) and ('-' == state[5]) and (player == state[8])) or (
                             (player == state[2]) and (player == state[5]) and ('-' == state[8]))
        condition7 = (('-' == state[0]) and (player == state[4]) and (player == state[8])) or (
                (player == state[0]) and ('-' == state[4]) and (player == state[8])) or (
                             (player == state[0]) and (player == state[4]) and ('-' == state[8]))
        condition8 = (('-' == state[2]) and (player == state[4]) and (player == state[6])) or (
                (player == state[2]) and ('-' == state[4]) and (player == state[6])) or (
                             (player == state[2]) and (player == state[4]) and ('-' == state[6]))
        conditions = [condition1, condition2, condition3, condition4, condition5, condition6, condition7, condition8]
        if conditions.count(True) > 1:
            return True
        else:
            return False

def end_state(state):
    """
    

    Parameters
    ----------
    state : list
        A list of length 10, representing a particular state of the game.

    Returns
    -------
    bool
        Returns True if the state is a win state for any player or a draw state. Returns False otherwise.

    """
    if is_draw(state) or is_win(state, 'X') or is_win(state, 'O'):
        return True
    else:
        return False

def has_center(state, focus):
    """
    

    Parameters
    ----------
    state : list
        A list of length 10, representing a particular state of the game.
    focus : str
        A string of one character, representing the player whose status is to be checked.

    Returns
    -------
    bool
        Returns True if 'focus' is present in the center position of 'state'. Returns False otherwise.

    """
    if state[4] == focus:
        return True
    else:
        return False

def has_corner(state, focus):
    """
    

    Parameters
    ----------
    state : list
        A list of length 10, representing a particular state of the game.
    focus : str
        A string of one character, representing the player whose status is to be checked.

    Returns
    -------
    bool
        Returns True if 'focus' is present in at least one of the corner positions of 'state'. Returns False otherwise.

    """
    if (state[0] == focus) or (state[2] == focus) or (state[6] == focus) or (state[8] == focus):
        return True
    else:
        return False

def has_edge(state, focus):
    """
    

    Parameters
    ----------
    state : list
        A list of length 10, representing a particular state of the game.
    focus : str
        A string of one character, representing the player whose status is to be checked.

    Returns
    -------
    bool
        Returns True if 'focus' is present in at least one of the four edge positions of 'state'. Returns False otherwise.

    """
    if (state[1] == focus) or (state[3] == focus) or (state[5] == focus) or (state[7] == focus):
        return True
    else:
        return False

# This function may have become obsolete
def my_pieces(state, focus):
    """
    

    Parameters
    ----------
    state : list
        A list of length 10, representing a particular state of the game.
    focus : str
        A string of one character, representing the player whose status is to be checked.

    Returns
    -------
    int
        Returns the number of places in which 'focus' is present in 'state'.

    """
    return state.count(focus)

def corner_avail(state):
    """
    

    Parameters
    ----------
    state : list
        A list of length 10, representing a particular state of the game.

    Returns
    -------
    bool
        Returns True if there is at least one corner position available in state. Returns False otherwise

    """
    if (state[0] == '-') or (state[2] == '-') or (state[6] == '-') or (state[8] == '-'):
        return True
    else:
        return False

def center_avail(state):
    """
    

    Parameters
    ----------
    state : list
        A list of length 10, representing a particular state of the game.

    Returns
    -------
    bool
        Returns True if the center position is available in state. Returns False otherwise

    """
    if state[4] == '-':
        return True
    else:
        return False

def static_value(state, maxi='X', mini='O'):
    """
    

    Parameters
    ----------
    state : list
        A list of length 10, representing a particular state of the game.
    maxi : str
        The Maximizer player.
    mini : str
        The Minimizer player.

    Returns
    -------
    value : int
        Returns the static value of 'state'. This ranges from +100 to -100 inclusively.

    """
    value = 0
    if is_win(state, maxi):
        value = 100
    else:
        if is_win(state, mini):
            value = -100
        else:
            if is_draw(state):
                value = 0
            else:
                if is_two_ways(state, maxi):
                    value += 50
                if is_a_way(state, maxi):
                    value += 10
                if has_center(state, maxi):
                    value += 5
                if has_corner(state, maxi):
                    value += 1
                
                if is_two_ways(state, mini):
                    value -= 50
                if is_a_way(state, mini):
                    value -= 10
                if has_center(state, mini):
                    value -= 5
                if has_corner(state, mini):
                    value -= 1
    return value

def get_all_next_moves(state, maxi, mini):
    """
    

    Parameters
    ----------
    state : list
        A list of length 10, representing a particular state of the game.
    maxi : str
        The Maximizer player.
    mini : str
        The Minimizer player.

    Returns
    -------
    moves : list
        Returns a list of all valid possible states that differ from 'state' by one move.

    """
    moves = []
    if end_state(state):
        return moves
    else:
        indices = []
        if state[4] == '-':
            indices.append(4)
        for _ in [0,2,6,8]:
            if state[_] == '-':
                indices.append(_)
        for _ in [1,3,5,7]:
            if state[_] == '-':
                indices.append(_)
        player = copy.deepcopy(state[9])
        for index in indices:
            temp_state = copy.deepcopy(state)
            temp_state[index] = player
            if player == maxi:
                temp_state[9] = mini
            elif player == mini:
                temp_state[9] = maxi
            moves.append(temp_state)
        return moves


##def max_value(state, depth, alpha, beta):
##    if end_state(state) or depth == 0:
##        print(state, " ", static_value(state))
##        return static_value(state)
##    v = -math.inf
##    for s in get_all_next_moves(state):
##        v = max(v, min_value(s, depth - 1, alpha, beta))
##        # Alpha-Beta flavour
##        alpha = max(alpha, v)
##        if alpha >= beta:
##            return alpha
##    return v
##
##
##def min_value(state, depth, alpha, beta):
##    if end_state(state) or depth == 0:
##        print(state, " ", static_value(state))
##        return static_value(state)
##    v = math.inf
##    for s in get_all_next_moves(state):
##        v = min(v, max_value(s, depth - 1, alpha, beta))
##        # Alpha-Beta flavour
##        beta = min(beta, v)
##        if alpha >= beta:
##            return beta
##    return v
##
##
##def top_level_max_value(state, depth, alpha, beta):
##    if end_state(state) or depth == 0:
##        return static_value(state)
##    [v, move] = [-math.inf, None]
##    a_move = None
##    for s in get_all_next_moves(state):
##        [v, move] = max([v, move], [min_value(s, depth - 1, alpha, beta), s])
##        print(state, " ", static_value(state))
##        # Alpha-Beta flavour
##        [alpha, a_move] = max([alpha, a_move], [v, move])
##        if alpha >= beta:
##            return [alpha, a_move]
##    return [v, move]

def minimax(state, depth, alpha, beta, maxi, mini):
    if end_state(state) or depth == 0:
        return [static_value(state, maxi, mini), ""]
    next_moves = get_all_next_moves(state, maxi, mini)
    move = []
    if state[9] == maxi:
        for s in next_moves:
            score = minimax(s, depth - 1, alpha, beta, maxi, mini)[0]
            if score > alpha:
                move = copy.deepcopy(s)
                alpha = score
            if alpha >= beta:
                break
        # print('# maximizer')
        # print(move)
        return [alpha, move]
    elif state[9] == mini:
        for s in next_moves:
            score = minimax(s, depth - 1, alpha, beta, maxi, mini)[0]
            if score < beta:
                move = copy.deepcopy(s)
                beta = score
            if alpha >= beta:
                break
        # print('# minimizer')
        # print(move)
        return [beta, move]


def animation():
    short_delay = 1
    long_delay = 3
    print("------------------------------------------------------------------")
    sleep(short_delay)
    print("-----------------------Welcome to Solitude------------------------")
    sleep(short_delay)
    print("------------------------------------------------------------------")
    sleep(short_delay)
    print("MY RULE:")
    sleep(short_delay)
    print("      I am X and you are O. If you're not comfortable with that...")
    sleep(long_delay)
    print("                               FUCK OFF!")
    sleep(short_delay)
    print("Let's begin!")
    sleep(short_delay)


if __name__ == '__main__':
    # animation()
    maxi = 'X'
    mini = 'O'
    game = ['-', '-', '-', '-', '-', '-', '-', '-', '-', 'X']
    # gp = copy.deepcopy(game)
    # for g in range(0, 10):
    #     if gp[g] == '-':
    #         gp[g] = ' '
    # print(gp[0], "  |  ", gp[1], "  |  ", gp[2])
    # print("-----------------")
    # print(gp[3], "  |  ", gp[4], "  |  ", gp[5])
    # print("-----------------")
    # print(gp[6], "  |  ", gp[7], "  |  ", gp[8])
    # opponent = int(input("Your turn: "))
    # game[opponent] = 'O'
    print("Hmm...")
    arr = minimax(game, 9, -math.inf, math.inf, maxi, mini)
    game = copy.deepcopy(arr[1])
    # print(arr[0])
    game[9] = 'X'
    gp = copy.deepcopy(game)
    for g in range(0, 10):
        if gp[g] == '-':
            gp[g] = ' '
    print(gp[0], "  |  ", gp[1], "  |  ", gp[2])
    print("-----------------")
    print(gp[3], "  |  ", gp[4], "  |  ", gp[5])
    print("-----------------")
    print(gp[6], "  |  ", gp[7], "  |  ", gp[8])
    print("I'm done")
    print("")
    while (not is_win(game, 'X')) and (not is_win(game, 'O')) and (not is_draw(game)):
        opponent = int(input("Your turn: "))
        if game[opponent] == '-':
            game[opponent] = 'O'
        else:
            print("    Open your eyes, dummy! Can't you see that's not a valid move?")
            continue
        if (not is_win(game, 'X')) and (not is_win(game, 'O')) and (not is_draw(game)):
            print("Hmm...")
            arr = minimax(game, 9, -math.inf, math.inf, maxi, mini)
            game = copy.deepcopy(arr[1])
            # print(arr[0])
            game[9] = 'X'
        gp = copy.deepcopy(game)
        for g in range(0, 10):
            if gp[g] == '-':
                gp[g] = ' '
        print(gp[0], "  |  ", gp[1], "  |  ", gp[2])
        print("-----------------")
        print(gp[3], "  |  ", gp[4], "  |  ", gp[5])
        print("-----------------")
        print(gp[6], "  |  ", gp[7], "  |  ", gp[8])
        print("I'm done")
        print("")
    
    if is_win(game, 'X'):
        print("I won the game you dumbass!")
    elif is_win(game, 'O'):
        print("You won, hats off! I guess I underestimated you.")
    else:
        print("You dare draw me!")
