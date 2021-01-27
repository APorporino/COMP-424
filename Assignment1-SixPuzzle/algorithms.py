import state
from queue import Queue


def breadth_first_search(start):
    states_visited = []

    q = Queue(maxsize=20)
    q.put(start)

    def inner_fn():
        if not (q.empty()):
            next_node = q.get()

            states_visited.append(next_node)

            if next_node == state.GOAL_STATE:
                return

            new_moves = state.find_next_moves(next_node)

            for move in new_moves:
                new_state = state.execute_move(next_node, int(move[0]))
                if not (new_state in states_visited):
                    q.put(new_state)
            inner_fn()
        else:
            print("Nothing left in queue")
            return

    inner_fn()

    print("---------------- Breadth First Search ------------------")
    for s in states_visited:
        state.pretty_print(s)
    print("--------------------------------------------------------")
    return states_visited

