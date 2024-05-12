from dataclasses import dataclass
from enum import Enum, auto

class Locations(Enum):
    KEY_LOC = auto()
    CAR_LOC = auto()
    SHOPS_LOC = auto()
    TA_LOC = auto()

class Objects(Enum):
    Car = auto()

@dataclass
class WorldState:
    has_keys: bool
    in_car: bool
    location: Locations

    @property
    def valid_state(self) -> bool:
        if(self.in_car and self.has_keys == False):
            return(False)
        else:
            return(True)
    
    @property
    def score(self) -> int:
        return(1)
    
    def __repr__(self) -> str:
        rv = f"(l: {self.location.name}, k: {self.has_keys}, c: {self.in_car})"
        return rv