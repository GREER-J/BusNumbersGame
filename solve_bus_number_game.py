"""
TITL: Bus number game
Date: 12.05.24
AUTH: GREER,J
DES:
 - Toy problem bus number game solver
"""

# Import
import time
from matplotlib import pyplot as plt

from src.world_state import WorldState
from src.problem import Problem
from src.tree_search import tree_search
from src.actions import add, sub, mult, div
from src.strategies import uniform_cost_strategy



def solve_bus_number_game(numbers:tuple) -> tuple[bool, int]:
    available_actions = [add, sub, mult, div]
    _success, _path_list = tree_search(Problem(WorldState(list(numbers)), available_actions), uniform_cost_strategy)
    _n_moves = len(_path_list)
    return (_success, _n_moves)


def main():
    solved = set()
    total_seen = set()
    start_time = time.time()
    n_errored = 0
    moves = []
    unsuccessful_moves = []
    for i in range(10000):  # Adjust range if you need more or fewer cases
        # Format number as a 4-digit string with leading zeros
        number_str = f"{i:04d}"
        # Convert each character to an integer and sort the digits
        digits = tuple(sorted(int(c) for c in number_str))

        # Skip processing if this tuple has already been processed
        if digits in total_seen:
            continue

        total_seen.add(digits)

        try:
            success, n_moves = solve_bus_number_game(digits)
            if success:
                #print(f"Winner! {digits} solved in {n_moves} moves")
                solved.add(digits)
                moves.append(n_moves)
            else:
                unsuccessful_moves.append(n_moves)
        except Exception as e:
            print(f"Error processing {digits}: {e}")
            n_errored += 1
            continue  # Skip to the next iteration

    # Print the number of unique digit sets found so far
    print(f"\n\nWe solved {len(solved)} of {len(total_seen)} ({len(solved) / len(total_seen):.2f}) problems in {time.time() - start_time:.2f} seconds")
    print(f"Average number of moves: {sum(moves) / len(solved):.2f}")
    print(f"There were {n_errored} troublesome cases")

    print(sum(unsuccessful_moves))
    print(len(unsuccessful_moves))

    #plt.hist(unsuccessful_moves)
    #plt.show()

if __name__ == "__main__":
    main()
