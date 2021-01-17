import constants
import copy


players_copy = copy.deepcopy(constants.PLAYERS)
teams_copy = copy.deepcopy(constants.TEAMS)

exp_players = []
inexp_players = []


def clean_data():
	#to clean height, convert to int and save new data as value in dictionary
    for player in players_copy:
        height_int, inches = player['height'].split(" ")
        height_int = int(height_int)
        player['height'] = height_int

	#to turn experience into boolean and seperate players by experience
    for player in players_copy:
        if player['experience'] == 'YES':
            player['experience'] = True
            exp_players.append(player)
        elif player['experience'] == "NO":
            player['experience'] = False
            inexp_players.append(player)
				
	#to split guardians to remove "and"
    for player in players_copy:
        player['guardians'] = player['guardians'].split(" and ")
		
					
def balance_team():
	#splits teams evenly w/even inexp and exp players.
	teams_copy[0] = inexp_players[0:3] + exp_players[0:3]
	teams_copy[1] = inexp_players[3:6] + exp_players[3:6]
	teams_copy[2] = inexp_players[6:9] + exp_players[6:9]	
	


def print_stats(team, team_list):
    #displays stats for team selected
    print("\nTeam: {} Stats".format(team))
    print("Total players: 6  \nTotal experienced: 3  \nTotal inexperienced: 3")
    height_list = 0
    players_on_team = []
    guardians_on_team = []

    for player in team_list:
        height_list += player['height']
        avg_height = round(float(height_list/6),2)
        players_on_team.append(player['name'])
        guardians_on_team += player['guardians']
        
    print("Average height: {}".format(avg_height))
    print("Players on Team: \n" + ", ".join(players_on_team))
    print("Guardians:  \n" + ", ".join(guardians_on_team)) 
    
    
def team_menu():
    print("\nPlease select a team")
    try:
        team_choice = int(input("1) Panthers  \n2) Bandits  \n3) Warriors \n\nEnter an option (1-3):  "))
    except ValueError:
        print("Oh no! That's not a valid number.")
    else:
        if team_choice < 1 or team_choice > 3:
            print("Oh no! That's not a valid number.")
        elif team_choice == 1:
            print_stats("Panthers", teams_copy[0])
        elif team_choice == 2:
            print_stats("Bandits", teams_copy[1])
        elif team_choice == 3:
            print_stats("Warriors", teams_copy[2])
        continue_selection = input("Press Enter to continue...  ")
    

def start_menu():
    print("BASKETBALL TEAM STATS TOOL \n\n ===MENU===")
    while True:
        try:
            choice = int(input("\n\n===MAIN MENU===\n\n1) Display Team Stats  \n2) Quit \n\nEnter an option (1 or 2):  "))
            if choice == 1:
                team_menu()
            if choice == 2:
                print("Thanks for using the stat tool!")
                break
        except ValueError:
            print("Oh no! That's not a valid number.")
        else:
            if choice < 1 or choice > 2:
                print("Oh no! That's not a valid number.") 

    
    
	
if __name__ == "__main__":
    clean_data()
    balance_team()
    start_menu()
