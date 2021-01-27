import state


def breadth_first_search(start):
    """ Implementation for breadth first search.

    :param start: Starting state matrix
    :return: Will return a list, first element contains another list of all states visited along the solution path,
    and the second element is an integer representing the number of total states visited (different than the number of
    states in the solution path).
    """

    # queue will contain a list of elements to be searched. Each element is a list where the state configuration is
    # at index 0. Index 1 will contain a list of other states representing the path to get to the state (one at index
    # 0) from the start state.
    queue = [[start, [start]]]
    states_visited = []

    def inner_fn():
        next_node = queue.pop(0)
        curr_state = next_node[0]
        path_to_curr_state = next_node[1]

        states_visited.append(curr_state)

        if curr_state == state.GOAL_STATE:
            return [path_to_curr_state, len(states_visited)]

        new_moves = state.find_next_moves(curr_state)

        for move in new_moves:
            next_state = state.execute_move(curr_state, int(move[0]))
            if not (next_state in states_visited):
                queue.append([next_state, path_to_curr_state + [next_state]])
        return inner_fn()

    answer = inner_fn()

    print("---------------- Breadth First Search ------------------")
    for s in answer[0]:
        state.pretty_print(s)
    print("--------------------------------------------------------")
    print(str(answer[1]) + " states visited")

    return answer


def depth_first_search(start):
    """ Implementation for depth first search.

    :param start: Starting state matrix
    :return: Will return a list, first element contains another list of all states visited along the solution path,
    and the second element is an integer representing the number of total states visited (different than the number of
    states in the solution path).
    """

    # Only change is from queue to stack. So we now pop from back of list, instead of the front.
    stack = [[start, [start]]]
    states_visited = []

    def inner_fn():
        next_node = stack.pop()  # Now taking from back of list (stack)
        curr_state = next_node[0]
        path_to_curr_state = next_node[1]

        states_visited.append(curr_state)

        if curr_state == state.GOAL_STATE:
            return [path_to_curr_state, len(states_visited)]

        new_moves = state.find_next_moves(curr_state)
        # new_moves must now be reversed because the algorithm takes from the back of list first instead of the front
        new_moves.reverse()
        for move in new_moves:
            next_state = state.execute_move(curr_state, int(move[0]))
            if not (next_state in states_visited):
                stack.append([next_state, path_to_curr_state + [next_state]])
        return inner_fn()

    answer = inner_fn()

    print("---------------- Depth First Search ------------------")
    for s in answer[0]:
        state.pretty_print(s)
    print("--------------------------------------------------------")
    print(str(answer[1]) + " states visited")

    return answer


def uniform_cost_search(start):
    """ Implementation for uniform cost search.

    :param start: Starting state matrix
    :return: Will return a list, first element contains another list of all states visited along the solution path,
    and the second element is an integer representing the number of total states visited (different than the number of
    states in the solution path).
    """

    # must make this a priority queue based on the length of path. Since each step is same cost, we just need to
    # keep track of the level (path length) of the state.
    priority_queue = [[start, [start]]]
    states_visited = []

    def inner_fn():
        next_node = priority_queue.pop(0)  # Take from front (priority)
        curr_state = next_node[0]
        path_to_curr_state = next_node[1]

        states_visited.append(curr_state)

        if curr_state == state.GOAL_STATE:
            return [path_to_curr_state, len(states_visited)]

        new_moves = state.find_next_moves(curr_state)

        for move in new_moves:
            # Since each move has an equal "cost" of 1, it does not matter which order
            # we add them in the queue since they will all still be the same overall "cost"
            next_state = state.execute_move(curr_state, int(move[0]))
            if not (next_state in states_visited):
                priority_queue.append([next_state, path_to_curr_state + [next_state]])
        return inner_fn()

    answer = inner_fn()

    print("---------------- Uniform Cost Search ------------------")
    for s in answer[0]:
        state.pretty_print(s)
    print("--------------------------------------------------------")
    print(str(answer[1]) + " states visited")

    return answer


1


def iterative_deepening(start):
    """ Implementation for iterative deepening search.

    :param start: Starting state matrix
    :return: Will return a list, first element contains another list of all states visited along the solution path,
    and the second element is an integer representing the number of total states visited (different than the number of
    states in the solution path). The third element will be the depth of the solution.
    """

    depth_level = 0

    while True:
        stack = [[start, [start], 0]]  # stack will now hold depth level of node as third element
        states_visited = []
        while True:
            if len(stack) == 0:  # We will break and not find an answer once stack is empty
                break

            next_node = stack.pop(0)  # Take from front of list (stack)
            curr_state = next_node[0]
            path_to_curr_state = next_node[1]
            depth_level_curr_state = next_node[2]

            states_visited.append(curr_state)

            if curr_state == state.GOAL_STATE:
                print("---------------- Iterative Deepening Search ------------------")
                for s in next_node[1]:
                    state.pretty_print(s)
                print("--------------------------------------------------------")
                print(str(len(states_visited)) + " states visited")
                print(str(next_node[2]) + " was the depth level (counting 0 as root)")
                return [path_to_curr_state, len(states_visited), depth_level_curr_state]

            new_moves = state.find_next_moves(curr_state)
            # new_moves must now be reversed because the algorithm takes from the back of list first instead of the
            # front
            new_moves.reverse()
            for move in new_moves:
                next_state = state.execute_move(curr_state, int(move[0]))
                if not (next_state in states_visited):
                    # ONLY ADD NEW STATE IF ITS UNDER OR EQUAL TO DEPTH LEVEL!!
                    if not (depth_level_curr_state + 1 > depth_level):
                        stack.append([next_state, path_to_curr_state + [next_state], depth_level_curr_state + 1])
        depth_level += 1

