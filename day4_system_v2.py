print("=" * 40)
print("   CS2 PLAYER ASSESSMENT SYSTEM v1.0   ")
print("=" * 40)

while True:
    player_name = input("player name: ")
    rating = float(input("rating: "))

    if rating >= 1.4:
        print(f"{player_name} is one of the best CS2 players in the world!")
    elif rating >= 1.2:
        print(f"{player_name} can be a Solid Starter.")
    elif rating >= 1.0:
        print(f"{player_name} is just an average player.")
    else:
        print(f"{player_name} might not be in good form right now.")

    status = input("Do you want to close the system?\n(YES/NO): ")
    if status.upper().strip() == "YES":
        break

print("   SYSTEM IS CLOSED!   ")
print("=" * 40)