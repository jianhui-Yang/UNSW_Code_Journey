import sys

print("=" * 40)
print("   CS2 PLAYER ASSESSMENT SYSTEM v5.1   ")
print("=" * 40)
print("(You can log out of the system by entering 'Q' at any time!)")

VITALITY = [
    {"name":"ZywOo", "role":"AWPer", "nation":"France"}, 
    {"name":"apEx", "role":"IGL", "nation":"France"}, 
    {"name":"flameZ", "role":"Opener", "nation":"Israel"}, 
    {"name":"ropz", "role":"Lurker", "nation":"Estonia"}, 
    {"name":"mezii", "role":"Support", "nation":"U.K."}, 
] 

FURIA = [
    {"name":"molodoy", "role":"AWPer", "nation":"Kazakhstan"}, 
    {"name":"FalleN", "role":"IGL", "nation":"Brazil"}, 
    {"name":"YEKINDAR", "role":"Opener", "nation":"Latvia"}, 
    {"name":"yuurih", "role":"Lurker", "nation":"Brazil"}, 
    {"name":"KSCERATO", "role":"Support", "nation":"Brazil"}, 
] 
SPIRIT = [
    {"name":"sh1ro", "role":"AWPer", "nation":"Russia"}, 
    {"name":"magixx", "role":"IGL", "nation":"Russia"}, 
    {"name":"donk", "role":"Opener", "nation":"Russia"}, 
    {"name":"zont1x", "role":"Lurker", "nation":"Ukraine"}, 
    {"name":"tN1R", "role":"Support", "nation":"Belarus"}, 
] 

def select_player(team_name, roster_list):
    print(f"---{team_name} ROSTER---")
    team_power = get_team_power(team_name)
    print(f"The team power of this team is {team_power}.")
    for i in range(5):
        player_name = roster_list[i]["name"]
        player_role = roster_list[i]["role"]
        player_nation = roster_list[i]["nation"]
        print(f"{i}: {player_name} (Role: {player_role}, Nation: {player_nation})")
    while True:
        try:
            user_input = input(f"Enter a number from 0 to 4 to select a player: ").upper().strip()
            if user_input == "Q":
                print("  SYSTEM IS CLOSED!  ")
                print("=" * 40)
                sys.exit()

            index = int(user_input)

            if 0 <= index <= 4:
                print(f"You have selected {roster_list[index]['name']}.")
                return roster_list[index]
            else:
                print(f"Index out of range! Please enter 0, 1, 2, 3, 4 or 'Q'.")
        except ValueError:
            print(f"Invalid input! Please enter a number or 'Q'.")
            continue
    
def get_team_power(team_name):
    if team_name == "VITALITY":
        return 100
    elif team_name == "SPIRIT":
        return 95
    elif team_name == "FURIA":
        return 92
    else:
        return 80

while True:
    team_name = input("Please select a team from Vitality, FURIA and SPIRIT: ").upper().strip()
    if team_name == "Q":
        print("  SYSTEM IS CLOSED!  ")
        print("=" * 40)
        sys.exit()

    if team_name == "VITALITY":
        player_data = select_player("VITALITY",VITALITY)
        real_name = player_data["name"]
    elif team_name == "FURIA":
        player_data = select_player("FURIA",FURIA)
        real_name = player_data["name"]
    elif team_name == "SPIRIT":
        player_data = select_player("SPIRIT",SPIRIT)
        real_name = player_data["name"]
    else:
        print("Invalid team! Please try again!")
        continue

    while True:
        try:
            rate_input = input("Please enter the average rating of this player: ").upper().strip()
            if rate_input == "Q":
                print("  SYSTEM IS CLOSED!  ")
                print("=" * 40)
                sys.exit()

            rating = float(rate_input)

            if rating >= 1.75 or rating <= 0:
                print(f"This average rating is unreasonable, please enter a valid rating (0.01 - 1.75)!")
            else:
                break
        except ValueError:
            print("This average rating is unreasonable, please enter a valid number or 'Q'!")
            continue

    if rating >= 1.4:
        print(f"{real_name} is one of the best CS2 players all over the world!")
    elif rating >= 1.2:
        print(f"{real_name} can be a Solid Starter.")
    elif rating >= 1.0:
        print(f"{real_name} is just an average player.")
    else:
        print(f"{real_name} might not be in good form right now.")