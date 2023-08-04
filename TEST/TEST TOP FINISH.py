data = """

Cameron Smith
Brooks Koepka
Bryson DeChambeau
Dustin Johnson
Patrick Reed
Talor Gooch
Joaquin Niemann
Sebastian Munoz
Harold Varner III
Sergio Garcia
Cameron Tringale
Mito Pereira
Jason Kokrak
Louis Oosthuizen
Kevin Na
Branden Grace
Henrik Stenson
Thomas Pieters
Peter Uihlein
Abraham Ancer
Dean Burmester
Anirban Lahiri
Paul Casey
Ian Poulter
Marc Leishman
Charles Howell III
Brendan Steele
Carlos Ortiz
Pat Perez
Richard Bland
Danny Lee
Laurie Canter
Eugenio Lopez-Chacarra
Bubba Watson
Matt Jones
David Puig
Matthew Wolff
Phil Mickelson
Lee Westwood
Scott Vincent
Charl Schwartzel
Bernd Wiesberger
Graeme McDowell
Martin Kaymer
James Piot
Chase Koepka
Jediah Morgan
Sihwan Kim
Top 5
+160
+240
+240
+260
+260
+280
+280
+320
+375
+375
+425
+425
+475
+500
+500
+500
+550
+550
+550
+550
+650
+650
+700
+700
+700
+700
+700
+700
+850
+850
+850
+1000
+1100
+1100
+1200
+1400
+1600
+1800
+1800
+2000
+2000
+2200
+3000
+4500
+7000
+7000
+14000
+19000
Top 10
-150
+100
+100
+110
+110
+120
+120
+137
+160
+160
+175
+175
+190
+200
+200
+200
+210
+210
+220
+220
+250
+250
+275
+275
+275
+275
+275
+275
+320
+320
+320
+350
+400
+400
+425
+475
+550
+600
+600
+650
+650
+750
+900
+1200
+2000
+2000
+3000
+4000
Top 20
-500
-334
-334
-300
-300
-280
-280
-260
-210
-210
-200
-200
-180
-175
-175
-175
-163
-163
-160
-160
-140
-140
-134
-130
-134
-130
-134
-130
-115
-110
-115
-105
+110
+110
+115
+125
+137
+150
+150
+160
+162
+187
+210
+250
+400
+400
+550
+600
Top 30
-2200
-1400
-1400
-1400
-1400
-1200
-1200
-1100
-900
-900
-850
-850
-800
-750
-750
-750
-700
-700
-650
-650
-600
-600
-550
-550
-550
-550
-550
-550
-475
-475
-475
-425
-375
-375
-375
-334
-300
-275
-275
-260
-260
-230
-210
-180
-125
-125
+105
+105


"""



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