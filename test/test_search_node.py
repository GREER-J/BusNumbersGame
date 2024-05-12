
from src.search_node import SearchNode
from src.world_state import WorldState

def test_successful_expansion():
    start_state = WorldState([1, 2, 3, 4])
    initial_node = SearchNode(start_state, None, 0, 0)
    fringe = [initial_node]
    # Mock or define an action that would be successful
    action = lambda state, n1, n2: (True, WorldState([n1+n2]+[num for num in state.available_numbers if num != n1 and num != n2]), 1)
    
    expanded = initial_node.expand_node([action], fringe)
    assert len(expanded) == 6  # Assuming all pairs work

def test_no_expansion_if_action_fails():
    start_state = WorldState([1, 2, 3, 4])
    initial_node = SearchNode(start_state, None, 0, 0)
    fringe = [initial_node]
    # Define an action that always fails
    action = lambda state, n1, n2: (False, state, 1)
    
    expanded = initial_node.expand_node([action], fringe)
    assert len(expanded) == 0  # No new nodes should be created

def test_no_duplicate_states_in_fringe():
    start_state = WorldState([1, 2, 3, 4])
    initial_node = SearchNode(start_state, None, 0, 0)
    fringe = [initial_node]
    # Action results in the same state
    action = lambda state, n1, n2: (True, state, 1)
    
    expanded = initial_node.expand_node([action], fringe)
    assert len(expanded) == 0  # No new nodes since state is duplicate

def test_correct_path_cost_and_depth_on_expansion():
    start_state = WorldState([1, 2, 3, 4])
    initial_node = SearchNode(start_state, None, 0, 0)
    fringe = [initial_node]
    # Action that changes the state
    action = lambda state, n1, n2: (True, WorldState([n1*n2]+[num for num in state.available_numbers if num != n1 and num != n2]), 3)
    
    expanded = initial_node.expand_node([action], fringe)
    for node in expanded:
        assert node.path_cost == 3  # New path cost should be initial cost + action cost
        assert node.depth == 1  # Depth should increment by 1

def test_duplicate_digits_in_state():
    start_state = WorldState([1, 1, 3, 4])
    initial_node = SearchNode(start_state, None, 0, 0)
    fringe = [initial_node]
    # Mock or define an action that would be successful
    action = lambda state, n1, n2: (True, WorldState([n1+n2]+[num for num in state.available_numbers if num != n1 and num != n2]), 1)
    
    expanded = initial_node.expand_node([action], fringe)
    assert len(expanded) == 6  # Assuming all pairs work