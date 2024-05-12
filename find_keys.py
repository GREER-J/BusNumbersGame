"""
TITL: Find keys problem
Date: 01.07.23
AUTH: GREER,J
DES:
 - Toy problem for FYP report
"""

# Import
from world_state import WorldState, Locations
from problem import Problem
from search_node import searchNode
import random
from functools import partial
from world_state import Locations

def get_walk_cost(loc1, loc2) -> int:
    cost = False
    if(loc1 == Locations.TA_LOC and loc2 == Locations.SHOPS_LOC):
        cost = 33 # minutes
    elif (loc1 == Locations.TA_LOC and loc2 == Locations.KEY_LOC):
        cost = 1 # minutes
    elif (loc1 == Locations.TA_LOC and loc2 == Locations.CAR_LOC):
        cost = 3 # minutes
    
    elif (loc1 == Locations.CAR_LOC and loc2 == Locations.SHOPS_LOC):
        cost = 30 # minutes
    elif (loc1 == Locations.CAR_LOC and loc2 == Locations.KEY_LOC):
        cost = 2 # minutes
    elif (loc1 == Locations.CAR_LOC and loc2 == Locations.KEY_LOC):
        cost = 1 # minutes

    elif (loc1 == Locations.KEY_LOC and loc2 == Locations.CAR_LOC):
        cost = 2 # minutes
    
    return(cost)

def get_drive_cost(loc1, loc2) -> int:
    cost = False
    if(loc1 == Locations.CAR_LOC and loc2 == Locations.SHOPS_LOC):
        cost = 6 # minutes
    elif(loc1 == Locations.CAR_LOC and loc2 == Locations.TA_LOC):
        cost = 2 # minutes
    elif(loc1 == Locations.CAR_LOC and loc2 == Locations.KEY_LOC):
        cost = 2 # minutes
    
    elif(loc1 == Locations.TA_LOC and loc2 == Locations.SHOPS_LOC):
        cost = 10 # minutes
    elif(loc1 == Locations.TA_LOC and loc2 == Locations.KEY_LOC):
        cost = 1 # minutes

    return(cost)

# Actions
def walk_to(pre_condition: WorldState, location: Locations) -> tuple[bool, WorldState, int]:
    _valid_action = False
    # Check conditions
    if(pre_condition.in_car == False and pre_condition.location != location):
        _valid_action = True
    new_state = WorldState(pre_condition.has_keys, pre_condition.in_car, location)

    # calculate cost
    cost = get_walk_cost(pre_condition.location, new_state.location)

    if(cost == False):
        _valid_action = False # If there's no cost it's not valid
        cost = 100000
    return(_valid_action, new_state, cost)

def drive_to(pre_condition: WorldState, location: Locations) -> tuple[bool, WorldState, int]:
    _valid_action = False
    # Check conditions | I've made it so we can only drive to the shops
    if(pre_condition.in_car == True and pre_condition.location != location and location == Locations.SHOPS_LOC):
        _valid_action = True
    new_state = WorldState(pre_condition.has_keys, pre_condition.in_car, location)

    cost = get_drive_cost(pre_condition.location, new_state.location)
    if(cost == False):
        _valid_action = False # If there's no cost it's not valid
        cost = 100000
    return(_valid_action, new_state, cost)

def get_in_car(pre_condition: WorldState) -> tuple[bool, WorldState, int]:
    _valid_action = False
    # Check conditions
    if(pre_condition.in_car == False and pre_condition.location == Locations.CAR_LOC and pre_condition.has_keys):
        _valid_action = True
    new_state = WorldState(pre_condition.has_keys, True, pre_condition.location)
    cost = 1
    return(_valid_action, new_state, cost)

def get_out_car(pre_condition: WorldState) -> tuple[bool, WorldState, int]:
    _valid_action = False
    # Check conditions
    if(pre_condition.in_car == True):
        _valid_action = True
    new_state = WorldState(pre_condition.has_keys, False, pre_condition.location)
    cost = 10 # Don't do this please
    return(_valid_action, new_state, cost)

def pick_up_keys(pre_condition: WorldState) -> tuple[bool, WorldState, int]:
    _valid_action = False
    # Check conditions
    if(pre_condition.has_keys == False and pre_condition.location == Locations.KEY_LOC):
        _valid_action = True
    new_state = WorldState(True, pre_condition.in_car, pre_condition.location)
    cost = 1
    return(_valid_action, new_state, cost)

available_actions = [get_in_car, get_out_car, pick_up_keys]


def tree_search(problem: Problem, strategy: callable):
    fringe = [searchNode(problem.init_state, None, 0)]
    running = True
    count = 0
    while(running):
        if(len(fringe) == 0):
            # We've searched everything!
            print("Stopping!")
            running = False
            return(False, fringe)
        selected_node, fringe = strategy(fringe)
        #print(selected_node)
        #print(fringe) # This is interesting to see for testing
        if(selected_node.state.location == Locations.SHOPS_LOC):
            # Winner!
            path_list = selected_node.generate_path_to_node()
            return(True, path_list)
        expanded_nodes = selected_node.expand_node(problem.available_actions, fringe)
        fringe.extend(expanded_nodes)

        # Output
        print(f"{count}: fringe length: {len(fringe)}")
        count += 1

        if(count > 500):
            print("Cutoff!")
            running = False
            return(False, selected_node.generate_path_to_node())

def FIFO_strategy(fringe: list):
    selected_node = fringe[0]
    fringe.remove(selected_node)
    return(selected_node, fringe)


def FILO_strategy(fringe: list):
    selected_node = fringe[-1]
    fringe.remove(selected_node)
    return(selected_node, fringe)


def random_select_strategy(fringe: list):
    selected_node = random.choice(fringe)
    fringe.remove(selected_node)
    return(selected_node, fringe)

def uniform_cost_strategy(fringe: list):
    lowest_score = 90000
    selected_node = fringe[0]
    for node in fringe:
        if(node.path_cost < lowest_score):
            lowest_score = node.path_cost
            selected_node = node
    fringe.remove(selected_node)
    return(selected_node, fringe)


def show_output(rv, data, strategy):
    if(rv):
        print(f"Found goal node with {strategy.__name__}")
        print(f"Path to goal node with cost {data[-1].path_cost}")
        for node in data:
            if(node.parent_node):
                print(f"{node.depth * '    '}|--{node}")
            else:
                print(node)
    else:
        print("Naww")


def main():
    problem = Problem(WorldState(False, False, Locations.TA_LOC), WorldState(False, True, Locations.TA_LOC), available_actions)
    for strategy in [FIFO_strategy, FILO_strategy, random_select_strategy, uniform_cost_strategy]:
        print(f"\nSolve problem with {strategy.__name__}:")
        rv, data = tree_search(problem, strategy)
        show_output(rv, data, strategy)
        print("\n")
        


def expand_walk_action():
    for l in Locations.__iter__():
        available_actions.append(partial(walk_to, location=l))

def expand_drive_action():
    for l in Locations.__iter__():
        available_actions.append(partial(drive_to, location=l))

if(__name__ == '__main__'):

    
    expand_walk_action()
    expand_drive_action()


    main()
    '''
    init = WorldState(False, False, Locations.HOME_LOC)
    goal = WorldState(True, True, Locations.SHOPS_LOC)
    t1, s1, cost1 = walk_to(init, Locations.KEY_LOC)
    t2, s2, cost2 = pick_up_keys(s1)
    t3, s3, cost3 = walk_to(s2, Locations.CAR_LOC)
    t4, s4, cost4 = get_in_car(s3)
    t5, s5, cost5 = drive_to(s4, Locations.SHOPS_LOC)
    print(t5,s5, (cost1+cost2+cost3+cost4+cost5))
    '''
    print("Done")
