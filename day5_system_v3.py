print("=" * 40)
print("   CS2 PLAYER ASSESSMENT SYSTEM v3.0   ")
print("=" * 40)

VITALITY = ["ZywOo", "apEx", "flameZ", "ropz", "mezii"] 
FURIA = ["FalleN", "KSCERATO", "yuurih", "YEKINDAR", "molodoy"]
SPIRIT = ["donk","magixx","zont1x","tN1R","sh1ro"]

def select_player(team_name, roster_list):
    print(f"\n---{team_name} ROSTER---")
    print(f"0:{roster_list[0]}\n1:{roster_list[1]}\n2:{roster_list[2]}\n3:{roster_list[3]}\n4:{roster_list[4]}")
    index = int(input(f"Enter a number from 0 to 4 to select a player: "))
    print(f"You have selected {roster_list[index]}")
    return roster_list[index]

while True:
    team_name = input("Please select a team from Vitality, FURIA and SPIRIT: ").upper().strip()
    if team_name == "VITALITY":
        player_name = select_player("VITALITY",VITALITY)
    elif team_name == "FURIA":
        player_name = select_player("FURIA",FURIA)
    elif team_name == "SPIRIT":
        player_name = select_player("SPIRIT",SPIRIT)
    else:
        print("Invalid team! Try again!")
        continue

    rating = float(input("Please enter the rating of this player: "))
    if rating >= 1.4:
        print(f"{player_name} is one of the best CS2 players all over the world!")
    elif rating >= 1.2:
        print(f"{player_name} can be a Solid Starter.")
    elif rating >= 1.0:
        print(f"{player_name} is just an average player.")
    else:
        print(f"{player_name} might not be in good form right now.")
    status = input("Do you want to close the system?\n(YES/NO): ").upper().strip()
    if status == "YES":
        break

print("   SYSTEM IS CLOSED!   ")
print("=" * 40)