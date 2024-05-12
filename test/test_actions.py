from src.actions import add, sub, mult, div
from src.world_state import WorldState

def test_add_numbers_available():
    start = WorldState([1,1, 2, 3])
    success, new_state, cost = add(start, start.available_numbers[0], start.available_numbers[1])
    
    assert success
    assert cost == 1
    assert sorted(new_state.available_numbers) == sorted([2, 2, 3])

def test_add_numbers_n1_not_available():
    start = WorldState([1,1, 2, 3])
    success, new_state, cost = add(start, 5, start.available_numbers[1])
    
    assert success == False
    assert cost == 1

def test_add_numbers_n2_not_available():
    start = WorldState([1,1, 2, 3])
    success, new_state, cost = add(start, 1, 6)
    
    assert success == False
    assert cost == 1

def test_sub_numbers_available():
    start = WorldState([1,1, 2, 3])
    success, new_state, cost = sub(start, start.available_numbers[0], start.available_numbers[1])
    
    assert success
    assert cost == 1
    assert sorted(new_state.available_numbers) == sorted([0, 2, 3])

def test_sub_numbers_n1_not_available():
    start = WorldState([1,1, 2, 3])
    success, new_state, cost = sub(start, 5, start.available_numbers[1])
    
    assert success == False
    assert cost == 1

def test_sub_numbers_n2_not_available():
    start = WorldState([1,1, 2, 3])
    success, new_state, cost = sub(start, 1, 6)
    
    assert success == False
    assert cost == 1

def test_mult_numbers_available():
    start = WorldState([1,1, 2, 3])
    success, new_state, cost = mult(start, 2, 3)
    
    assert success
    assert cost == 1
    assert sorted(new_state.available_numbers) == sorted([1, 1, 6])

def test_mult_numbers_n1_not_available():
    start = WorldState([1,1, 2, 3])
    success, new_state, cost = mult(start, 5, start.available_numbers[1])
    
    assert success == False
    assert cost == 1

def test_mult_numbers_n2_not_available():
    start = WorldState([1,1, 2, 3])
    success, new_state, cost = mult(start, 1, 6)
    
    assert success == False
    assert cost == 1

def test_div_numbers_available():
    start = WorldState([1,1, 2, 3])
    success, new_state, cost = div(start, 1, 2)
    
    assert success
    assert cost == 1
    assert sorted(new_state.available_numbers) == sorted([1, 0.5, 3])

def test_div_numbers_n1_not_available():
    start = WorldState([1,1, 2, 3])
    success, new_state, cost = div(start, 5, start.available_numbers[1])
    
    assert success == False
    assert cost == 1

def test_div_numbers_n2_not_available():
    start = WorldState([1,1, 2, 3])
    success, new_state, cost = div(start, 1, 6)
    
    assert success == False
    assert cost == 1

def test_div_numbers_n2_is_zero():
    start = WorldState([1,1, 0, 3])
    success, new_state, cost = div(start, 1, 0)
    
    assert success == False
    assert cost == 1

#TODO I haven't implemented this yet but I know it's there.

# def test_add_numbers_not_enough_instances():
#     start = WorldState([2, 3, 4])  # Only one instance of 2
#     success, new_state, cost = add(start, 2, 2)  # Attempt to add 2 + 2
    
#     assert not success  # Should not succeed as there's only one 2
#     assert cost == 1    # Cost should still be reported as 1
#     assert start.available_numbers == [2, 3, 4]  # State should remain unchanged

# def test_sub_numbers_not_enough_instances():
#     start = WorldState([3, 5, 6])  # Only one instance of 3
#     success, new_state, cost = sub(start, 3, 3)
    
#     assert not success
#     assert cost == 1
#     assert start.available_numbers == [3, 5, 6]

# def test_mult_numbers_not_enough_instances():
#     start = WorldState([4, 5, 6])  # Only one instance of 4
#     success, new_state, cost = mult(start, 4, 4)
    
#     assert not success
#     assert cost == 1
#     assert start.available_numbers == [4, 5, 6]

# def test_div_numbers_not_enough_instances():
#     start = WorldState([4, 5, 6])  # Only one instance of 4
#     success, new_state, cost = div(start, 4, 4)
    
#     assert not success
#     assert cost == 1
#     assert start.available_numbers == [4, 5, 6]
