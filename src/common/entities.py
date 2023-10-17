import typing as t
from enum import Enum


class Team:
    name: str
    positions: t.Dict[str, "Position"]  # player_name: position


class State(Enum):
    Active = 1
    Reserve = 2
    Retired = 3


class Role(Enum):
    Striker = 1
    Defender = 2
    Goalkeeper = 3
    Messenger = 4
    Coach = 5


class Position:
    player: 'Player'
    state: State
    role: Role


class Treat:
    """Base class for treats"""
    name: str = 'Treat'

    def __str__(self):
        return f'{self.name}'

class Disease:
    """Base class for diseases"""
    name: str = 'Disease'

    def __str__(self):
        return f'{self.name}'

class Player:
    name: str
    treats: t.List[Treat]
    current_disease: Disease


roles_translator = {
    'Striker': Role.Striker,
    'Defender': Role.Defender,
    'Goalkeeper': Role.Goalkeeper,
    'Messenger': Role.Messenger,
    'Coach': Role.Coach
}

states_translator = {
    'Active': State.Active,
    'Reserve': State.Reserve,
    'Retired': State.Retired
}
