"""
State.py

This file will be used to model the state of the puzzle and implement each algorithm.
"""

from queue import Queue

START_STATE = [[1, 4, 2], [5, 3, 0]]
GOAL_STATE = [[0, 1, 2], [5, 4, 3]]
MOVES = ["1R", "1D", "2L", "2R", "2D", "3L", "3D", "4U", "4R", "5L", "5R", "5U", "6L", "6U"]


def pretty_print(state):
    """ This function will print the state given as input.

    :param state: state of six puzzle to print.
    :return:
    """

    print("--------")
    print(state[0])
    print(state[1])
    print("--------")


def execute_move(state, move):
    """This function will execute a valid move. Note that the move is simply to decide which square should be moved,
    so only an integer between 1 and 6 inclusively is needed to make the move. Also note that this function allows
    illegal moves (jumping squares).

    :param state: initial state (2 x 3 matrix)
    :param move: move to be made (just a number from 1 to 6)
    :return: state that results after the move
    """

    return_state = [row[:] for row in state]
    # Determine which row contains the square we wish to move
    square_to_move_row = 0
    if move > 3:
        square_to_move_row = 1
        move -= 3

    empty_spot = find_empty_square(return_state)
    row = empty_spot[0]
    column = empty_spot[1]

    if row == 0:
        return_state[0][column] = return_state[square_to_move_row][move - 1]
        return_state[square_to_move_row][move - 1] = 0
    else:
        return_state[1][column] = return_state[square_to_move_row][move - 1]
        return_state[square_to_move_row][move - 1] = 0

    return return_state


def find_next_moves(state):
    """ This function is key for implementing the algorithms. It will return the next set of possible moves from the
    state given as input. It will ensure the states with a lower number will be prioritized.

    :param state:
    :return: list of next moves with lower numbered pieces having priority
    """

    return_value = []

    empty_spot = find_empty_square(state)
    row = empty_spot[0]
    column = empty_spot[1]

    if row == 0:
        if column == 0:                              # empty spot is in first row, first column
            if state[0][1] > state[1][0]:
                return_value.extend(["4U", "2L"])
            else:
                return_value.extend(["2L", "4U"])
        elif column == 1:                            # empty spot is in first row, second column
            if state[0][0] < state[0][2]:
                if state[0][0] < state[1][1]:
                    return_value.append("1R")
                    if state[0][2] < state[1][1]:
                        return_value.extend(["3L", "5U"])
                    else:
                        return_value.extend(["5U", "3L"])
                else:
                    return_value.extend(["5U", "1R", "3L"])
            else:
                if state[0][2] < state[1][1]:
                    return_value.append("3L")
                    if state[0][0] < state[1][1]:
                        return_value.extend(["1R", "5U"])
                    else:
                        return_value.extend(["5U", "1R"])
                else:
                    return_value.extend(["5U", "3L", "1R"])
        else:                                       # empty spot is in first row, third column
            if state[0][1] > state[1][2]:
                return_value.extend(["6U", "2R"])
            else:
                return_value.extend(["2R", "6U"])

    # Empty slot is in row 2
    else:
        if column == 0:                              # empty spot is in first row, first column
            if state[0][0] > state[1][1]:
                return_value.extend(["5L", "1D"])
            else:
                return_value.extend(["1D", "5L"])
        elif column == 1:                            # empty spot is in first row, second column
            if state[1][0] < state[1][2]:
                if state[1][0] < state[0][1]:
                    return_value.append("4R")
                    if state[1][2] < state[0][1]:
                        return_value.extend(["6L", "2D"])
                    else:
                        return_value.extend(["2D", "6L"])
                else:
                    return_value.extend(["2D", "4R", "6L"])
            else:
                if state[1][2] < state[0][1]:
                    return_value.append("6L")
                    if state[1][0] < state[0][1]:
                        return_value.extend(["4R", "2D"])
                    else:
                        return_value.extend(["2D", "4R"])
                else:
                    return_value.extend(["2D", "6L", "4R"])
        else:                                       # empty spot is in first row, third column
            if state[0][2] > state[1][1]:
                return_value.extend(["5R", "3D"])
            else:
                return_value.extend(["3D", "5R"])
    return return_value


def find_empty_square(state):
    """ This function will take as input an initial state and return a list of two numbers. The first number will
    represent which row the empty spot is, and the second will represent the column.

    :param state: Initial state
    :return: List of two numbers
    """
    try:
        index = state[0].index(0)
        return [0, index]
    except ValueError:
        try:
            index = state[1].index(0)
            return [1, index]
        except ValueError:
            raise EnvironmentError("Error: no empty spot available. State is invalid.")