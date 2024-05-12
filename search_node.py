from world_state import WorldState


class searchNode:
    def __init__(self, state: WorldState, action: callable, path_cost: int, depth: int = 0, parent_node=None) -> None:
        self.state = state
        self.parent_node = parent_node
        self.action = action
        self.path_cost = path_cost
        self.depth = depth

    def __repr__(self) -> str:
        return(self.state.__repr__())
    
    def expand_node(self, action_list: list, fringe: list):
        current_world_states = []
        for node in fringe:
            current_world_states.append(node.state)
        new_nodes = []
        for action in action_list:
            succes, ns, action_cost = action(self.state)
            if(succes == False):
               continue
            # It works!
            if(ns not in current_world_states):
                new_path_cost = self.path_cost + action_cost
                new_depth = self.depth + 1
                new_nodes.append(searchNode(
                    ns, action, new_path_cost, new_depth, self))
        return(new_nodes)

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
            if(count > 10):
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
