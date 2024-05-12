from dataclasses import dataclass

@dataclass
class WorldState:
    _available_numbers: list[float]

    @property
    def valid_state(self) -> bool:
        return True
    
    @property
    def score(self) -> float:
        target = 10
        _running_cost = sum(self.available_numbers)
        rv = (target - _running_cost)**2
        rv += 10*(len(self._available_numbers)-1)
        return rv

    @property 
    def available_numbers(self) -> list:
        rv = self._available_numbers
        return rv
    
    @property
    def winner(self) -> bool:
        for i in self._available_numbers:
            if i == 10:
                return True
        return False

    
    def __repr__(self) -> str:
        rv = f"{self.score} -> Numbers remaining: ({self._available_numbers})"
        return rv