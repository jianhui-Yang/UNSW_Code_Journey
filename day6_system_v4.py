print("=" * 40)
print("   CS2 PLAYER ASSESSMENT SYSTEM v4.0   ")
print("=" * 40)

VITALITY = ["ZywOo", "apEx", "flameZ", "ropz", "mezii"] 
FURIA = ["FalleN", "KSCERATO", "yuurih", "YEKINDAR", "molodoy"]
SPIRIT = ["donk","magixx","zont1x","tN1R","sh1ro"]

def select_player(team_name, roster_list):
    print(f"\n---{team_name} ROSTER---")
    print(f"0:{roster_list[0]}\n1:{roster_list[1]}\n2:{roster_list[2]}\n3:{roster_list[3]}\n4:{roster_list[4]}")
    while True:
        try:

            index = int(input(f"Enter a number from 0 to 4 to select a player: "))
            if 0 <= index <= 4:
                print(f"You have selected {roster_list[index]}")
                return roster_list[index]
            else:
                print(f"Index out of range! Please enter 0, 1, 2, 3, or 4.")

        except ValueError:
            print(f"Invalid input! Please enter a number.")
            continue
    

while True:
    team_name = input("Please select a team from Vitality, FURIA and SPIRIT: ").upper().strip()
    if team_name == "VITALITY":
        player_name = select_player("VITALITY",VITALITY)
    elif team_name == "FURIA":
        player_name = select_player("FURIA",FURIA)
    elif team_name == "SPIRIT":
        player_name = select_player("SPIRIT",SPIRIT)
    else:
        print("Invalid team! Please try again!")
        continue

    while True:
        try:
            rating = float(input("Please enter the average rating of this player: "))
            if rating >= 1.75 or rating <= 0:
                print(f"This average rating is unreasonable, please enter a valid rating (0.01 - 1.75)!")
            else:
                break
        except ValueError:
            print("This average rating is unreasonable, please enter a valid number!")
            continue

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