from src.world_state import WorldState
from src.problem import Problem
from src.search_node import SearchNode
from src.tree_search import tree_search

def test_empty_fringe_termination():
    problem = Problem(WorldState([1, 2, 3, 4]), lambda state: state.score == 0)  # Mock problem
    result, fringe = tree_search(problem, lambda fringe: (fringe.pop(0), fringe))
    assert not result
    assert len(fringe) == 0

def test_successful_termination_on_solution():
    # Setup problem with a state that meets the success condition
    winning_state = WorldState([10])  # Assuming score == 0 when only [10] is left
    problem = Problem(winning_state, lambda state: state.score == 0)
    fringe = [SearchNode(winning_state, None, 0)]

    result, path = tree_search(problem, lambda fringe: (fringe.pop(0), fringe))
    assert result
    assert len(path) == 1  # Path should include only the winning node