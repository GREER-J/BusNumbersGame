from dataclasses import dataclass
from typing import Union

@dataclass
class WorldState:
    runnning_total: float
    n1: Union[int, bool]
    n2: Union[int, bool]
    n3: Union[int, bool]
    n4: Union[int, bool]

    @property
    def valid_state(self) -> bool:
        return True
    
    @property
    def score(self) -> float:
        target = 10
        if self.runnning_total:
            # We're up and running
            rv = (target - self.runnning_total)**2
            if not self.n1:
                # N1 is there
                rv += 1
            if not self.n2:
                # N1 is there
                rv += 1
            if not self.n3:
                # N1 is there
                rv += 1
            if not self.n4:
                # N1 is there
                rv += 1
            return rv

    
    def __repr__(self) -> str:
        rv = f"{self.runnning_total} ->({self.n1},{self.n2}, {self.n3}, {self.n4}) left"
        return rv