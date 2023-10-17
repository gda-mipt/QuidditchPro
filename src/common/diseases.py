from src.common.entities import Disease


class LegInjury(Disease):
    name = 'Leg is injured'


class ArmInjury(Disease):
    name = 'Arm is injured'


class NoDisease(Disease):
    name = 'No diseases'


translator = {
    'Leg is injured': LegInjury,
    'Arm is injured': ArmInjury,
    'No diseases': NoDisease
}
