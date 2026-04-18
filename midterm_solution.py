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

matches = []
wins = 0
losses = 0

for i in range(1, 5):
    print(f"\n--- MATCH {i} ---")
    hero_num = int(input("Hero number (0 to skip): "))
    
    if hero_num == 0:
        continue
    
    if 1 <= hero_num <= 5:
        kills = int(input("Kills: "))
        deaths = int(input("Deaths: "))
        assists = int(input("Assists: "))
        result = input("Results (W/L): ").strip().upper()
    
        formula = deaths if deaths != 0 else 1
        kda = (kills + assists) / formula
        
        if kda >= 5 and result == 'W':
            tag = "DOMINATION!"
        elif kda >= 5 and result == 'L':
            tag = "Carried Hard"
        elif result == 'W':
            tag = "Team Effort"
        else:
            tag = "Better Luck Next Game"
        
        if result == 'W':
            wins += 1
        else:
            losses += 1
            
        matches.append([
            heroes[hero_num][0],
            kda,
            result,
            tag
        ])
    else:
        print("Invalid hero number. Please choose 1-5 (or 0 to skip).")
