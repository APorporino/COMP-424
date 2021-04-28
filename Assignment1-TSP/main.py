from tsp import Tsp, hill_climbing
from math import isclose

NUM_INSTANCES = 100
NUM_CITIES = 7

NUM_INSTANCES_QUESTION_D = 1
NUM_CITIES_QUESTION_D = 100


def main():
    """ Entry point to the program. Will print to the console desired output.
    """
    tsp_instances = make_tsp_instances(NUM_INSTANCES, NUM_CITIES)

    print("----- STATS FOR BRUTE FORCE ON {} INSTANCES OF {} CITIES -----".format(NUM_INSTANCES, NUM_CITIES))
    brute_force_lengths = optimal_length(tsp_instances)
    print_stats(brute_force_lengths)
    random_tours_and_lengths = random_lengths(tsp_instances)
    random_tour_lengths = random_tours_and_lengths[1]
    random_tours = random_tours_and_lengths[0]

    print("\n----- STATS FOR RANDOM TOUR ON {} INSTANCES OF {} CITIES -----".format(NUM_INSTANCES, NUM_CITIES))
    print_stats(random_tour_lengths)
    num_equal_el = count_num_equal_elements(random_tour_lengths, brute_force_lengths)
    print(str(num_equal_el) + " number of times random tour was the same as the optimal tour.")

    print("\n----- STATS FOR HILL CLIMBING ON {} INSTANCES OF {} CITIES -----".format(NUM_INSTANCES, NUM_CITIES))
    hill_climbing_lengths = []
    for tour in random_tours:
        hill_climbing_lengths.append(hill_climbing(tour))
    print_stats(hill_climbing_lengths)
    num_equal_el = count_num_equal_elements(hill_climbing_lengths, brute_force_lengths)
    print(str(num_equal_el) + " number of times hill climbing algorithm gave the optimal tour.")

    question_d()


def question_d():
    tsp_instances = make_tsp_instances(NUM_INSTANCES_QUESTION_D, NUM_CITIES_QUESTION_D)
    print("\n\n------------ QUESTION D ------------\n\n")
    print("\n----- STATS FOR RANDOM TOUR ON {} INSTANCES OF {} CITIES -----"
          .format(NUM_INSTANCES_QUESTION_D, NUM_CITIES_QUESTION_D))
    random_tours_and_lengths = random_lengths(tsp_instances)
    random_tour_lengths = random_tours_and_lengths[1]
    random_tours = random_tours_and_lengths[0]
    print_stats(random_tour_lengths)

    print("\n----- STATS FOR HILL CLIMBING ON {} INSTANCES OF {} CITIES -----"
          .format(NUM_INSTANCES_QUESTION_D, NUM_CITIES_QUESTION_D))
    hill_climbing_lengths = []
    for tour in random_tours:
        hill_climbing_lengths.append(hill_climbing(tour))
    print_stats(hill_climbing_lengths)


def make_tsp_instances(num_instances, num_cities_in_instance):
    tsp_instances = []
    for i in range(num_instances):
        instance = Tsp()
        instance.add_random_cities(num_cities_in_instance)
        tsp_instances.append(instance)
    return tsp_instances


def optimal_length(tsp_instances):
    lengths = []
    for i in tsp_instances:
        optimal = i.brute_force_search()
        lengths.append(optimal)
    return lengths


def random_lengths(tsp_instances):
    lengths = []
    tours = []
    for i in tsp_instances:
        random_tour_and_length = i.random_tour()
        random = random_tour_and_length[1]
        tour = random_tour_and_length[0]
        lengths.append(random)
        tours.append(tour)
    return [tours, lengths]


def print_stats(list_lengths):
    mean_value = mean(list_lengths)
    print("Mean: " + str(mean_value))
    print("Standard deviation: " + str(st_dv(list_lengths, mean_value)))
    print("Max: " + str(max(list_lengths)))
    print("Min: " + str(min(list_lengths)))


def mean(list_num):
    total = 0
    for i in list_num:
        total += i
    return total / len(list_num)


def st_dv(list_num, mean_value):
    sum_squares = 0
    for i in list_num:
        sum_squares += (i - mean_value) ** 2
    return (sum_squares / len(list_num)) ** .5


def count_num_equal_elements(l1, l2):
    """ Will return the number of instances where the lists have the same value at the same index.

    The input lists must be the same length or an "index out of bounds error will be thrown."

    :param l1: The first list.
    :param l2: The second list.
    :return: Integer representing number of times where the lists had the same value at the same index.
    """
    count = 0
    for i in range(0, len(l1)):
        if isclose(l1[i], l2[i]):
            count += 1
    return count


main()
