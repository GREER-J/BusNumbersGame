from src.world_state import WorldState
from dataclasses import dataclass

@dataclass
class Problem:
    init_state: WorldState
    available_actions: list
