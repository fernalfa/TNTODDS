with open('../0.INFO', 'r') as file:
    data = file.read()



def parse_data(data):
    lines = data.strip().split('\n')
    top5_start = lines.index("Top 5") + 1
    top10_start = lines.index("Top 10") + 1
    top20_start = lines.index("Top 20") + 1

    top5_odds = lines[top5_start:top10_start - 1]
    top10_odds = lines[top10_start:top20_start - 1]
    top20_odds = lines[top20_start:]

    players = lines[1:top5_start - 1]

    top5_list = []
    top10_list = []
    top20_list = []

    for i, player in enumerate(players):
        top5_list.append({"Player": player, "Odds": top5_odds[i]})
        top10_list.append({"Player": player, "Odds": top10_odds[i]})
        top20_list.append({"Player": player, "Odds": top20_odds[i]})

    return top5_list, top10_list, top20_list

top5_players, top10_players, top20_players = parse_data(data)

# Output for Top 5
print("Top 5:")
for player_info in top5_players:
    print("Player:", player_info["Player"])
    print("Odds:", player_info["Odds"])
    print()

# Output for Top 10
print("Top 10:")
for player_info in top10_players:
    print("Player:", player_info["Player"])
    print("Odds:", player_info["Odds"])
    print()

# Output for Top 20
print("Top 20:")
for player_info in top20_players:
    print("Player:", player_info["Player"])
    print("Odds:", player_info["Odds"])
    print()