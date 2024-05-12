from src.world_state import WorldState

def test_creation():
    available_numbers = [0, 0, 0, 1]
    x = WorldState(available_numbers)

    assert x.available_numbers == available_numbers

def test_scoring_fun_returns_false():
    available_numbers = [0, 0, 0, 1]
    expected_score = (10 - 1)**2 + 30
    x = WorldState(available_numbers)

    assert x.score == expected_score

def test_winner_fun_False():
    available_numbers = [0, 0, 0, 1]
    x = WorldState(available_numbers)

    assert x.winner == False

def test_winner_fun_False():
    available_numbers = [0, 10, 0, 1]
    x = WorldState(available_numbers)

    assert x.winner == True