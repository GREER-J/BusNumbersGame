import pytest
from src.strategies import FIFO_strategy, FILO_strategy, random_select_strategy, uniform_cost_strategy
import random

class DummyNode:
    def __init__(self, path_cost):
        self.path_cost = path_cost

def test_FIFO_strategy():
    start_fringe = [DummyNode(10), DummyNode(20), DummyNode(30)]
    selected_node, updated_fringe = FIFO_strategy(start_fringe.copy())
    assert selected_node in start_fringe
    assert selected_node.path_cost == 10  # First in
    assert len(updated_fringe) == 2
    assert updated_fringe[0].path_cost == 20  # Check next in line

def test_FILO_strategy():
    start_fringe = [DummyNode(10), DummyNode(20), DummyNode(30)]
    selected_node, updated_fringe = FILO_strategy(start_fringe.copy())
    assert selected_node in start_fringe
    assert selected_node.path_cost == 30  # Last in
    assert len(updated_fringe) == 2
    assert updated_fringe[-1].path_cost == 20  # New last should be the previous last

def test_random_select_strategy():
    start_fringe = [DummyNode(10), DummyNode(20), DummyNode(30)]
    random.seed(0)  # Seed for reproducibility
    selected_node, updated_fringe = random_select_strategy(start_fringe.copy())
    # Expected selection may vary, check selected is removed
    assert selected_node in start_fringe
    assert len(updated_fringe) == 2
    assert selected_node not in updated_fringe

def test_uniform_cost_strategy():
    start_fringe = [DummyNode(10), DummyNode(20), DummyNode(30)]
    selected_node, updated_fringe = uniform_cost_strategy(start_fringe.copy())
    assert selected_node in start_fringe
    assert selected_node.path_cost == 10  # Should select node with lowest cost
    assert len(updated_fringe) == 2
    assert all(node.path_cost != 10 for node in updated_fringe)  # Check lowest cost node is removed

