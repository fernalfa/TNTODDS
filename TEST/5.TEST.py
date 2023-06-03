scenarios = [
    "MIA Heat 100:106 BOS Celtics",
    "+15000",
    "MIA Heat 101:107 BOS Celtics",
    "+15000",
    "MIA Heat 107:110 BOS Celtics",
    "+15000",
    "MIA Heat 101:106 BOS Celtics",
    "+16000",
    "MIA Heat 105:99 BOS Celtics",
    "+16000",
    "MIA Heat 104:107 BOS Celtics",
    "+16000",
    "MIA Heat 101:104 BOS Celtics",
    "+16000",
    "MIA Heat 99:105 BOS Celtics",
    "+16000",
    "MIA Heat 99:104 BOS Celtics",
    "+16000"
]

for i in range(0, len(scenarios), 2):
    scenario = scenarios[i]
    additional_info = scenarios[i + 1]
    parts = scenario.split()
    team1 = ' '.join(parts[:2])  # Join the first two parts as team 1
    score1, score2 = parts[2].split(':')  # Split the third part on ":" to get the scores
    team2 = ' '.join(parts[3:])  # Join the remaining parts as team 2
    print(f"{team1} {score1} - {team2} {score2}")
    print(additional_info)
    print()
