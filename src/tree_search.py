from src.problem import Problem
from src.search_node import SearchNode

def tree_search(problem: Problem, strategy: callable):
    fringe = [SearchNode(problem.init_state, None, 0)]
    running = True
    count = 0
    while(running):

        # Check exit conditions
        if(len(fringe) == 0):
            # We've searched everything!
            #print(f"We've run out of options after {count} moves")
            running = False
            return(False, fringe)
        
        # If we're still good then select a node to expand
        selected_node, fringe = strategy(fringe)
        # print(f"Selected node: {selected_node}")
        # print(f"Fringe: {fringe}") # This is interesting to see for testing

        # If it's the goal node ... stop
        if selected_node.state.winner:
            # Winner!
            path_list = selected_node.generate_path_to_node()
            return(True, path_list)
        
        # Otherwise we keep searching, expand the node
        expanded_nodes = selected_node.expand_node(problem.available_actions, fringe)
        # print(f"Expanded nodes: {expanded_nodes}")
        # print(f"actions: {problem.available_actions}")
        fringe.extend(expanded_nodes)

        # Output
        #print(f"{count}: fringe length: {len(fringe)}")
        count += 1

        if(count > 500):
            print("We've hit our move cap. Here's where we got up to.")
            running = False
            return(False, selected_node.generate_path_to_node())