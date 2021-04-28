import random
from itertools import permutations

LOWER_BOUND = 0
UPPER_BOUND = 1


def euclidean_distance(index1, index2):
    temp1 = (index1[0] - index2[0]) ** 2
    temp2 = (index1[1] - index2[1]) ** 2
    return (temp1 + temp2) ** .5


def tour_length(tour):
    total_distance = 0
    for i in range(0, len(tour) - 1):
        total_distance += euclidean_distance(tour[i], tour[i + 1])
    total_distance += euclidean_distance(tour[-1], tour[0])
    return total_distance


def hill_climbing(tour):
    """ This function implements hill climbing algorithm using two change function to find neighboring nodes.

    The way that the 2 edges to be swapped are chosen is by considering all possible tuples from (0,0) to
    (size_of_city, size_of_city). This will create (size_of_city*size_of_city) tuples, however 1/size_of_city of them
    will have identical numbers and can thus be ignored. We can reduce the remaining tuples by half since they will
    just be duplicates.

    It helps to think of an example and in our first case we have city of size 7. This results in 21 valid tuples, and
    thus 21 neighbors.

    :param tour: The tour that we use to find neighbors for.
    :return: Returns an estimate of the optimal solution (which is the min length of travelling to all cities)
    """
    check_length = tour_length(tour)
    current_tour = tour
    current_length = check_length
    for i in range(len(tour)):
        for k in range(len(tour)):
            if i < k:       # Used to avoid duplicates
                result = two_opt_swap(tour, i, k)
                if result:
                    new_length = result[0]
                    new_tour = result[1]
                    if new_length < current_length:
                        current_length = new_length
                        current_tour = new_tour

    if current_length == check_length:
        # All neighbors have higher values, so we return
        return current_length
    else:
        # We must find neighbors of our new tour and run hill_climbing again
        return hill_climbing(current_tour)


def two_opt_swap(tour, i, k):
    """ This function performs a similar functionality as the wikipedia function shown to us in the Teams messages by
    the professor.

    It handles creating neighboring tours by swapping edges.

    Note: The input i must be greater than the input k.

    :param tour: The input tour represented as a list of cities. Each city is a list of 2 coordinates.
    :param i: Will represent the first edge. It is the index value for the input tour and represents the first node
    in the first edge to be chosen.
    :param k: Will represent the second edge. It is the index value for the input tour and represents the first node
    in the second edge to be chosen.
    :return: The return value is a list where the first element is length of the new neighbor tour and the second
    element is the length of that new neighbor tour.
    """

    new_tsp_instance = []

    # Make sure the edges removed do not share a node because no valid swap can be made in this case.
    if abs(i - k) == 1:
        return []
    if (i == len(tour) & k == 0) | (k == len(tour) & i == 0):
        # This statement is needed since the last and first element of the list don't differ by a value of 1 but
        # are still connected.
        return []

    new_tsp_instance.extend(tour[0:i + 1])
    nodes_to_reverse = tour[i + 1:k + 1]
    nodes_to_reverse.reverse()
    new_tsp_instance.extend(nodes_to_reverse)
    new_tsp_instance.extend(tour[k + 1:])

    new_length = tour_length(new_tsp_instance)
    return [new_length, new_tsp_instance]


def make_random_permutation(start, end):
    random_tour = []
    for i in range(start, end):
        random_tour.append(i)
    random.shuffle(random_tour)
    return random_tour


class Tsp:
    """ This class is used to store information relating to a TSP problem instance.

    """
    def __init__(self):
        self.cities = []

    def add_random_cities(self, num_cities):
        for i in range(num_cities):
            self.cities.append([random.uniform(LOWER_BOUND, UPPER_BOUND), random.uniform(LOWER_BOUND, UPPER_BOUND)])

    def size(self):
        return len(self.cities)

    def brute_force_search(self):
        min_value = 0
        perm = list(permutations(range(0, self.size())))
        for p in perm:
            tour = self.map_permutation_to_tour(p)
            length = tour_length(tour)
            if min_value == 0:
                min_value = length
            elif length < min_value:
                min_value = length
        return min_value

    def random_tour(self):
        perm = make_random_permutation(0, self.size())
        tour = self.map_permutation_to_tour(perm)
        return [tour, tour_length(tour)]

    def map_permutation_to_tour(self, permutation):
        tour = []
        for p in permutation:
            tour.append(self.cities[p])
        return tour
