from src.common.entities import Treat


class Leadership(Treat):
    name = 'Leadership'


class Teamwork(Treat):
    name = 'Teamwork'


class Communication(Treat):
    name = 'Communication'


class Discipline(Treat):
    name = 'Discipline'


class Adaptability(Treat):
    name = 'Adaptability'


class PoorCommunication(Treat):
    name = 'Poor communication'


class LackOfTeamwork(Treat):
    name = 'Lack of teamwork'


class Selfishness(Treat):
    name = 'Selfishness'


translator = {
    'Leadership': Leadership,
    'Teamwork': Teamwork,
    'Communication': Communication,
    'Discipline': Discipline,
    'Adaptability': Adaptability,
    'Poor communication': PoorCommunication,
    'Lack of teamwork': LackOfTeamwork,
    'Selfishness': Selfishness
}
