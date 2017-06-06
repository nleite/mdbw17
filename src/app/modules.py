

class Player(object):

    def __init__(self, name, clubs, matches, awards):
        self.name = name
        self.clubs = clubs
        self.matches = matches
        self.awards = awards
        self.current_club = clubs[-1] if clubs[-1].current else None ;

class Club(object):

    def __init__(self, name, moto, city, field, supporters):
        self.name = name
        self.city = name
        self.field = field
        self.supporters = supporters

class Match(object):

    def __init__(self, home, away, score, facts):
        self.home = home
        self.away - away
        self.score = score
        self.facts = facts


class Award(object):

    def __init__(self, name, year, org):
        self.name = name
        self.year = year
        self.org = org
