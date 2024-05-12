from src.world_state import WorldState
from typing import List, Callable

def find_combinations(nums):
    #TODO When all the numbers are the same [1,1,1,1] this function returns only one combination which is wrong but I don't think it'll matter here.
    _new_combinations = set()
    for xi, x in enumerate(nums):
        for yi, y in enumerate(nums):
            res = [x,y]
            res.sort()
            res = tuple(res)
            if res not in _new_combinations and xi != yi:
                _new_combinations.add(res)
    return _new_combinations


class SearchNode:
    def __init__(self, state: WorldState, action: callable, path_cost: int, depth: int = 0, parent_node=None) -> None:
        self.state = state
        self.parent_node = parent_node
        self.action = action
        self.path_cost = path_cost
        self.depth = depth

    def __repr__(self) -> str:
        return(self.state.__repr__())
    
    def expand_node(self, action_list: List[Callable], fringe):
        current_world_states = []
        for node in fringe:
            current_world_states.append(node.state)

        new_nodes = []
        # Iterate through each node in the fringe
        #print(f"\nFringe: given {fringe}")

        # Generate all pairs of numbers to apply actions on
        available_numbers = self.state.available_numbers
        new_combinations = find_combinations(available_numbers)
        for n1, n2 in new_combinations:
            for action in action_list:
                success, new_state, action_cost = action(self.state, n1, n2)

                if not success:
                    continue
                if(new_state not in current_world_states):
                    new_path_cost = self.path_cost + action_cost
                    new_depth = self.depth + 1
                    new_nodes.append(SearchNode(new_state, action, new_path_cost, new_depth, self))
                    
        
        # Add on anything in the fringe
        #new_nodes.extend(fringe)
        return new_nodes

    def generate_path_to_node(self) -> list:
        running = True
        path_list = [self]
        selected_node = self
        count = 0
        while(running):
            parent = selected_node.parent_node
            if(parent):
                # parent exists
                path_list.append(parent)
                selected_node = parent
            else:
                running = False
            count += 1
            if(count > 100):
                running = False
                print("Estop!")
        path_list.reverse()
        return(path_list)

    def __str__(self) -> str:
        if(self.action):
            #rv = f"{self.action.__name__} -> {self.state.__str__()}"
            original_func = getattr(self.action, 'func', None)
            if(original_func == None):
                original_func = self.action.__name__
            #kw = self.action.keywords
            rv = f"{original_func} -> {self.state.__str__()}"
        else:
            rv = f"{self.state.__str__()}"
        return(rv)
