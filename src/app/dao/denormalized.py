# dao.denormalized.py
class PlayerDao(object):

    def __init__(self, collection):
        self._coll = collection

    def get_player(self, name):
        # db.players.find({"name": name})
        query = {"name": name}
        player_doc = self._coll.find_one(query)

        return Player(player_doc)

    # dao.denormalized.py
    def add_match_stats(self, player_name, match):
        # db.players.update( {"name": player_name}, {"$push": {"matches": match}} )
        query = {"name": player_name}
        update = {"$push": {"match": match}}
        self._coll.update_one(query, update)


    def update_club_info(self, club_name, club_info):
        # db.players.update( {"current_club.name": name}, {"$set": club_info} )
        query = {"current_club.name": club_name}
        update = {"$set": club_info}
        self._coll.update_many(query, update)
