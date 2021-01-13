import constants
import copy


players_copy = copy.deepcopy(constants.PLAYERS)
teams_copy = copy.deepcopy(constants.TEAMS)

exp_players = []
inexp_players = []

def clean_data():
	#to clean height and convert to int
	for player in players_copy:
		height_int, inches = player['height'].split(" ")
		height_int = int(height_int)
		
	#to turn experience into boolean and seperate players by experience
	for player in players_copy:
		if player['experience'] == 'YES':
			player['experience'] = "True"
			exp_players.append(player)
		elif player['experience'] == "NO":
			player['experience'] = "False"
			inexp_players.append(player)
				
	#to split guardians to remove "and"
	for player in players_copy:
		player['guardians'] = player['guardians'].split(" and ")
		
					
def balance_team():
	num_players_team = len(players_copy) / len(teams_copy)
	
	#splits teams evenly w/even inexp and exp players. while allowing team to be refernced by name or list index
	teams_copy[0] = Panthers = inexp_players[0:3] + exp_players[0:3]
	teams_copy[1] = Bandits = inexp_players[3:6] + exp_players[3:6]
	teams_copy[2] = Warriors = inexp_players[6:9] + exp_players[6:9]	
	

def start_menu():
    print("BASKETBALL TEAM STATS TOOL \n\n ===MENU===")
    

        

	
	
if __name__ == "__main__":
    clean_data()
    balance_team()
    start_menu()