heroes = {
    1: ("Layla", "Marksman"),
    2: ("Tigreal", "Tank"),
    3: ("Gusion", "Assassin"),
    4: ("Kagura", "Mage"),
    5: ("Chou", "Fighter")
}

InGame_name = input("In-game name (IGN): ").strip()
current_rank = input("Current rank: ").strip().title()

print("\n==========================================")
print("   MOBILE LEGENDS -- HERO ROSTER")
print("==========================================")

for num, (hero, role) in heroes.items():
    print(f" {num}. {hero:<10} [{role}]")

print("==========================================")
