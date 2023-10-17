"""convert data from file to entities"""

import typing as t
from src.common import entities, treats, diseases
import src.backend.data_patterns as data_patterns
import pandas as pd


def convert_teams(teams: t.List[t.Tuple]) -> t.List[entities.Team]:
    df = pd.DataFrame(teams, columns=data_patterns.teams_pattern)
    team_names = df['team_name'].unique()
    new_teams = []
    for team_name in team_names:
        team = entities.Team()
        team.name = team_name
        team.positions = dict()

        players = df[df['team_name'] == team_name]['player_name'].unique()
        for player_name in players:
            player = entities.Player()
            player.treats = []
            player.name = player_name

            position = entities.Position()
            position.player = player

            data = df[df['team_name'] == team_name][df['player_name'] == player_name]
            treats_str = data['treat'].unique()
            for treat_str in treats_str:
                player.treats.append(_convert_treat(treat_str))
            player.current_disease = _convert_disease(data['disease'].unique()[0])

            position.role = _convert_role(data['role'].unique()[0])
            position.state = _convert_state(data['state'].unique()[0])

            team.positions.update({player_name: position})
        new_teams.append(team)
    return new_teams

    return None


def _convert_treat(treat: str):
    return treats.translator.get(treat, entities.Treat)()


def _convert_disease(disease: str):
    return diseases.translator.get(disease, diseases.NoDisease)()


def _convert_role(role: str):
    return entities.roles_translator.get(role, entities.Role.Striker)


def _convert_state(state: str):
    return entities.states_translator.get(state, entities.State.Active)


def convert_role_to_str(role: entities.Role):
    for s, role_ in entities.roles_translator.items():
        if role_ == role:
            return s


def convert_state_to_str(state: entities.State):
    for s, state_ in entities.states_translator.items():
        if state_ == state:
            return s
