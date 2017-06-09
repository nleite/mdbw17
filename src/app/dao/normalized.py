# dao/normalized.py
from app.modules import Player, Person, PlayerStats

class PersonDao(object):
    def __init__(self, collection):
        self._coll = collection

    def get_name_role(self, person_name, role):
        # db.person.find({"name": person_name, "role": role})
        query = {
            "name": person_name,
            "role": role
        }
        person_doc = self._coll.find_one(query);

        return Person(person_doc)

class PlayerDao(object):

    def __init__(self, collection):
        self._coll = collection

    def get_player(self, person):
        # db.person.find({"person_id": person.get_id()})
        query = {
            "person_id" : person.get_id()
        }
        player_doc = self._coll.find_one(query)

        player = Player(person, player_doc)

class PlayerStatsDao(object):

    def __init__(self, collection):
        self._coll = collection

    def get_by_playerid(self, player_id, matches):
        # db.player_stats.find({"player_id": player_id, match_id: {"$in": matches}})
        query = {
            "player_id": player_id,
            "match_id": { "$in": matches}
        }
        cursor = self._coll.find(query)
        player_stats = PlayerStats()

        for stats_doc in cursor:
            player_stats.append( stats_doc)

        player_stats.aggregate()

        return player_stats

# dao/normalized.py
class ClubDao(object):

    def __init__(self, collection):
        self._coll = collection

    def update_info(self,club_id, club_info):
        # db.club.updateOne({"_id": club_info.id}, {"$set": club_info})
        query = {"_id": club_id}
        update = {"$set": club_info}
        self._coll.update_one(query, update)
