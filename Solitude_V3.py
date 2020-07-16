"""
    Created: 29 March 2020 14:30
    Author: Martins Anerua

    Notes:
        1. A state is a particular unique game board
        2. state[9] represents the player whose turn it is to play (not the one whose play resulted in the current game state)
        3. Solitude is the Maximizer and human player is the Minimizer
"""

import copy
import math

MAXI = ''
MINI = ''

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
   
    if is_win(state, MAXI) or is_win(state, MINI):
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
    if is_draw(state) or is_win(state, MAXI) or is_win(state, MINI):
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

def static_value(state, MAXI, MINI):
    """
    

    Parameters
    ----------
    state : list
        A list of length 10, representing a particular state of the game.
    MAXI : str
        The Maximizer player.
    MINI : str
        The Minimizer player.

    Returns
    -------
    value : int
        Returns the static value of 'state'. This ranges from +100 to -100 inclusively.

    """
    value = 0
    if is_win(state, MAXI):
        value = 100
    else:
        if is_win(state, MINI):
            value = -100
        else:
            if is_draw(state):
                value = 0
            else:
                if is_two_ways(state, MAXI):
                    value += 50
                if is_a_way(state, MAXI):
                    value += 10
                if has_center(state, MAXI):
                    value += 5
                if has_corner(state, MAXI):
                    value += 1
                
                if is_two_ways(state, MINI):
                    value -= 50
                if is_a_way(state, MINI):
                    value -= 10
                if has_center(state, MINI):
                    value -= 5
                if has_corner(state, MINI):
                    value -= 1
    return value

def get_all_next_moves(state, MAXI, MINI):
    """
    

    Parameters
    ----------
    state : list
        A list of length 10, representing a particular state of the game.
    MAXI : str
        The Maximizer player.
    MINI : str
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
            if player == MAXI:
                temp_state[9] = MINI
            elif player == MINI:
                temp_state[9] = MAXI
            moves.append(temp_state)
        return moves

def minimax(state, depth, alpha, beta, MAXI, MINI):
    """
    

    Parameters
    ----------
    state : list
        A list of length 10, representing a particular state of the game.
    depth : int
        The depth of the search tree.
    alpha : int
        Alpha value.
    beta : TYPE
        Beta value.
    MAXI : str
        The Maximizer player.
    MINI : str
        The Minimizer player.

    Returns
    -------
    list
        Implements the minimax algorithm with alpha-beta pruning and 
        returns a list whose first index is the alpha/beta value of the game state 
        and the second index is another list representing the next state recommended
        by the algorithm.

    """
    if end_state(state) or depth == 0:
        return [static_value(state, MAXI, MINI), ""]
    next_moves = get_all_next_moves(state, MAXI, MINI)
    move = []
    if state[9] == MAXI:
        for s in next_moves:
            score = minimax(s, depth - 1, alpha, beta, MAXI, MINI)[0]
            if score > alpha:
                move = copy.deepcopy(s)
                alpha = score
            if alpha >= beta:
                break
        return [alpha, move]
    elif state[9] == MINI:
        for s in next_moves:
            score = minimax(s, depth - 1, alpha, beta, MAXI, MINI)[0]
            if score < beta:
                move = copy.deepcopy(s)
                beta = score
            if alpha >= beta:
                break
        return [beta, move]

def avail_position(state):
    """
    

    Parameters
    ----------
    game : list
        A list of length 10, representing a particular state of the game.

    Returns
    -------
    avail : list
        Returns a list of all available positions in state.

    """
    avail = []
    for _ in range(0,9):
        if state[_] == '-':
            avail.append(_)
    return avail

def display_game(state):
    """
    

    Parameters
    ----------
    state : list
        A list of length 10, representing a particular state of the game.

    Returns
    -------
    None
        Displays game in a readable form and returns None.

    """
    gp = copy.deepcopy(state)
    for g in range(0, 9):
        if gp[g] == '-':
            gp[g] = ' '
    print(gp[0], "  |  ", gp[1], "  |  ", gp[2])
    print("-----------------")
    print(gp[3], "  |  ", gp[4], "  |  ", gp[5])
    print("-----------------")
    print(gp[6], "  |  ", gp[7], "  |  ", gp[8])   

def instruction():
    print("------------------------------------------------------------------")
    print("-------------------------How to Play------------------------------")
    print("------------------------------------------------------------------")
    print()
    print("Tic-Tac-Toe is a game in which two players take turns putting")
    print("their tokens (usually X and O) on a 3x3 grid and try to get three")
    print("of the same symbol in a line")
    print()
    print("Solitude is a brave, bold and beautiful minimax algorithm, and she")
    print("is ready to defeat any of her adversaries.")
    print()
    print("To play, simply follow the game prompts. When prompted for an input")
    print("please follow her majesty's rule below:")
    demo_game = ['1','2','3','4','5','6','7','8','9']
    display_game(demo_game)
    print()
    print("For example, to play in the top left corner, simply input 1 when")
    print("prompted.")
    print()
    print("Her majesty wishes you a pleasant experience! Goodluck.")
    print()
    print("------------------------------------------------------------------")
    print("------------------------------------------------------------------")

def about():
    print("------------------------------------------------------------------")
    print("-----------------------------About--------------------------------")
    print("------------------------------------------------------------------")
    print()
    print("                         Solitude v1.0                            ")
    print("                    Written by Martins Anerua                     ")
    print("                           July 2020                              ")
    print()
    print("            https://www.github.com/anerua/Solitude_v3             ")
    print()
    print("------------------------------------------------------------------")
    print("------------------------------------------------------------------")    
    
def play():
    global MAXI, MINI    
    while(True):
        try:
            MAXI = input("Choose an alphabet character for me e.g. 'X' or 'O': ")[0].upper()
        except IndexError:
            MAXI = 'X'
            print("Lazy uh? I choose X then.")
        if MAXI.isalpha():
            while(True):
                try:
                    MINI = input("Enter your alphabet character e.g. 'X' or 'O': ")[0].upper()
                except IndexError:
                    MINI = 'O'
                    print("Lazy uh? I choose O for you then.")
                if MINI.isalpha() and MINI != MAXI:
                    break
                elif MINI == MAXI:
                    print("Didn't tell you? I'm a selfish damsel. I don't share my character with anyone.")
                    continue
                else:
                    print("Interesting, never knew", MINI, "was an English alphabet!")
                    continue
            break
        else:
            print("Ever heard of alphabets, like ABCDEF...? I don't think so.")
            continue
        
    game = ['-', '-', '-', '-', '-', '-', '-', '-', '-', MAXI]
    try:
        human_first = input("Do you want to be the first player, Y/n? ")[0].lower()
    except IndexError:
        human_first = 'y'
        print("I mean you're a god, you shouldn't have to type right? Well newsflash, even gods aren't this proud!")
        print("Anyway, I'll just assume you want to play first.")
        
    
    if human_first == 'y':
        display_game(game)
        while(True):
            try:
                opponent = int(input("Your turn: ")) - 1
            except ValueError:
                print("Really? Like that's not even a numeric character!")
                continue
            if opponent not in avail_position(game):
                print("Not a valid move. Pick a valid position")
                continue
            else:
                break
            
        game[opponent] = MINI
    
    print("Hmm...")
    ai_move = minimax(game, 9, -math.inf, math.inf, MAXI, MINI)
    game = copy.deepcopy(ai_move[1])
    
    display_game(game)
    print("I'm done")
    print("")
    
    while (not is_win(game, MAXI)) and (not is_win(game, MINI)) and (not is_draw(game)):
        while(True):
            try:
                opponent = int(input("Your turn: ")) - 1
            except ValueError:
                print("Really? Like that's not even a numeric character!")
                continue
            if opponent not in avail_position(game):
                print("Not a valid move. Pick a valid position")
                continue
            else:
                break
        game[opponent] = MINI
        game[9] = MAXI
        
        if (not is_win(game, MAXI)) and (not is_win(game, MINI)) and (not is_draw(game)):
            print("Hmm...")
            ai_move = minimax(game, 9, -math.inf, math.inf, MAXI, MINI)
            game = copy.deepcopy(ai_move[1])
            game[9] = MAXI
            
        display_game(game)
        print("I'm done")
        print("")
    
    if is_win(game, MAXI):
        print("I won the game, duh!")
    elif is_win(game, MINI):
        print("Wow, you won! I owe you a kiss.")
    else:
        print("A draw! You just might be my perfect partner.")
    
    print("------------------------------------------------------------------")
    print("------------------------------------------------------------------")

def game_home():
    print("------------------------------------------------------------------")
    print("-----------------------Welcome to Solitude------------------------")
    print("------------------------------------------------------------------")
    while(True):
        print("Type 'help' for help")
        print("Type 'about' for additional game information")
        print("Type 'play' to play the game")
        print("Type 'exit' to exit the game")
        command = input("> ").strip().lower()
        if command == 'help':
            instruction()
        elif command == 'about':
            about()
        elif command == 'play':
            play()
        elif command == 'exit':
            break
        else:
            print("I don't speak that language. I do hope you understand mine")
            continue
    print()
    print("------------------------------------------------------------------")
    print("--------------------Solitude says goodbye-------------------------")
    print("------------------------------------------------------------------")
    
if __name__ == '__main__':
    game_home()