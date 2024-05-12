import random
from src.search_node import SearchNode

def FIFO_strategy(fringe: list[SearchNode]):
    selected_node = fringe[0]
    fringe.remove(selected_node)
    return(selected_node, fringe)


def FILO_strategy(fringe: list[SearchNode]):
    selected_node = fringe[-1]
    fringe.remove(selected_node)
    return(selected_node, fringe)


def random_select_strategy(fringe: list[SearchNode]):
    selected_node = random.choice(fringe)
    fringe.remove(selected_node)
    return(selected_node, fringe)

def uniform_cost_strategy(fringe: list[SearchNode]):
    lowest_score = 90000
    selected_node = fringe[0]
    for node in fringe:
        if(node.path_cost < lowest_score):
            lowest_score = node.path_cost
            selected_node = node
    fringe.remove(selected_node)
    return(selected_node, fringe)