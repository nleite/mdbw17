# controllers.py

from dao.normalized import PersonDao, PlayerDao,PlayerStatsDao

@app.route('/players/<name>', methods=['GET'])
def get_player(name):

    person_dao = PersonDao(person_collection)
    person = person_dao.get_name_role(name, "player")

    player_dao = PlayerDao(player_collection)
    player = player_dao.get_player(person)

    player_stats_dao = PlayerStatsDao(stats_collection)
    player.add_stats( player_stats_dao.get_by_playerid(player.id) )

    return render_template("player.html", player=player)


# controllers.py
@app.route('/players/<name>', methods=['GET'])
def get_player(name):

    player_dao = PlayerDao(player_collection)
    player = player_dao.get_player(name)

    return render_template("player.html", player=player)


@app.route('/match/', methods=['POST'])
def new_match_stats():
    match = Match(request)
    match_dao.add(match)

    person_dao = Person(dao)
    for p : match.players:
        person = person_dao.add_match_stats(p.name, match)

@app.route('/match/', methods=['POST'])
def new_match_stats():
    match = Match(request)
    match_dao.add(match)

    person_dao = Person(dao)
    for p : match.players:
        person = person_dao.get_name_role(p.name, "player")
        add_player_stats(person.id, p.stats)

    return render_template("result.html", player=player)

def add_player_stats(player_id, stats):
    player_stats_dao = PlayerStatsDao(player_collection)
    player_stats_dao.add_stats(player_id, stats)

# controllers.py
@app.route('/club/<club_id>/coach/', methods=['PUT'])
def club(club_id):
    club_dao = ClubDao(club_collection)
    data =  {"coach": ClubInfo(request).coach}
    club_dao.update_info(club_id, data)
