with open('../0.INFO', 'r') as file:
    data = file.read()



def parse_data(data):
    lines = data.strip().split('\n')
    top5_start = lines.index("Top 5") + 1
    top10_start = lines.index("Top 10") + 1
    top20_start = lines.index("Top 20") + 1
    top30_start = lines.index("Top 30") + 1

    top5_odds = lines[top5_start:top10_start - 1]
    top10_odds = lines[top10_start:top20_start - 1]
    top20_odds = lines[top20_start:top30_start - 1]
    top30_odds = lines[top30_start:]

    odds_info = {
        "Top 5": top5_odds,
        "Top 10": top10_odds,
        "Top 20": top20_odds,
        "Top 30": top30_odds,
    }

    players = lines[1:top5_start - 1]

    player_odds = {}
    for i, player in enumerate(players):
        player_odds[player] = {
            "Top 5": odds_info["Top 5"][i],
            "Top 10": odds_info["Top 10"][i],
            "Top 20": odds_info["Top 20"][i],
            "Top 30": odds_info["Top 30"][i],
        }

    return player_odds, odds_info

parsed_players, parsed_odds = parse_data(data)

# Now, you can access the odds for each player like this:
for player, odds in parsed_players.items():
    print(player)
    print("Top 5:", odds["Top 5"])
    print("Top 10:", odds["Top 10"])
    print("Top 20:", odds["Top 20"])
    print("Top 30:", odds["Top 30"])
    print()

# You can also access the overall odds information:
print("Overall Odds:")
print("Top 5:", parsed_odds["Top 5"])
print("Top 10:", parsed_odds["Top 10"])
print("Top 20:", parsed_odds["Top 20"])
print("Top 30:", parsed_odds["Top 30"])