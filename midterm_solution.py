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

total = len(matches)
win_rate = int((wins / total) * 100) if total > 0 else 0

best_index = 0
for i in range(1, total):
    if matches[i][1] > matches[best_index][1]:
        best_index = i
        
print("\n=============================================")
print(f"     {InGame_name} -- MATCH LOG ({current_rank})")
print("=============================================")

for i in range(total):
    hero, kda, result, tag = matches[i]
    result_text = "WIN" if result == 'W' else "LOSS"
    print(f"[{i+1}] {hero:<11} | KDA: {kda:>5.2f} | {result_text:<4} | {tag}")

print("---------------------------------------------")
print(f"Matches Played : {total}")
print(f"Wins : {wins}  |  Losses : {losses}")
print(f"Win Rate       : {win_rate}%")

if total > 0:
    best = matches[best_index]
    print(f"Best Match     : [{best_index+1}] {best[0]}  (KDA: {best[1]:.2f})")

print("=============================================")
