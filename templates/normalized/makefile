persons := 105000
matches := 80000
teams := 4000
stats := 1200000000
reports := 240000

generate: prep
	mgeneratejs photos_template.json -n 1 > "data/photos.json"
	mgeneratejs person_template.json -n 1 > "data/persons.json"
	mgeneratejs player_template.json -n 1 > "data/players.json"
	mgeneratejs player_stats_template.json -n 1 > "data/stats.json"
	mgeneratejs team_template.json -n 1 > "data/teams.json"
	mgeneratejs match_template.json -n 1 > "data/matches.json"
	mgeneratejs scout_notes_template.json -n 1 > "data/reports.json"

prep:
	mkdir -p data
