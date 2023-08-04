import re

text = """
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
"""

lines_with_odds = re.findall(r'(?i)(\w+(\s+\w+)*\s)([+-]?\d+(\.\d+)?)', text)

for line in lines_with_odds:
    player_name = line[0].strip()
    odds = line[2]
    print(f"{player_name}: {odds}")
