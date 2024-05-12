from src.world_state import WorldState


# Actions
def add(precondition: WorldState, n1: float, n2: float) -> tuple[bool, WorldState, int]:
    _valid_action = True
    _available_nums = precondition.available_numbers
    new_state = precondition
    if n1 in _available_nums and n2 in _available_nums:
        _available_nums.remove(n1)
        _available_nums.remove(n2)
        _available_nums.append(n1 + n2)
        new_state = WorldState(_available_nums)
    else:
        _valid_action = False
    
    # calculate cost
    cost = 1

    return(_valid_action, new_state, cost)

def sub(precondition: WorldState, n1: float, n2: float) -> tuple[bool, WorldState, int]:
    _valid_action = True
    _available_nums = precondition.available_numbers
    new_state = precondition
    if n1 in _available_nums and n2 in _available_nums:
        _available_nums.remove(n1)
        _available_nums.remove(n2)
        _available_nums.append(n1 - n2)
        new_state = WorldState(_available_nums)
    else:
        _valid_action = False
    
    # calculate cost
    cost = 1

    return(_valid_action, new_state, cost)

def mult(precondition: WorldState, n1: float, n2: float) -> tuple[bool, WorldState, int]:
    _valid_action = True
    _available_nums = precondition.available_numbers
    new_state = precondition
    if n1 in _available_nums and n2 in _available_nums:
        _available_nums.remove(n1)
        _available_nums.remove(n2)
        _available_nums.append(n1 * n2)
        new_state = WorldState(_available_nums)
    else:
        _valid_action = False
    
    # calculate cost
    cost = 1

    return(_valid_action, new_state, cost)

def div(precondition: WorldState, n1: float, n2: float) -> tuple[bool, WorldState, int]:
    _valid_action = not(n2 == 0)
    _available_nums = precondition.available_numbers
    new_state = precondition
    if n1 in _available_nums and n2 in _available_nums and n2 != 0:
        _available_nums.remove(n1)
        _available_nums.remove(n2)
        _available_nums.append(n1 / n2)
        new_state = WorldState(_available_nums)
    else:
        _valid_action = False
    
    # calculate cost
    cost = 1

    return(_valid_action, new_state, cost)