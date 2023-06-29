import re

# Lines data
lines_data = """
Houston Astros
C. Javier -R
O 26½
-135
1978
St. Louis Cardinals
M. Mikolas -R
U 26½
+105
08:05 PM
1955
Philadelphia Phillies
A. Nola -R
O 25
-135
1956
Chicago Cubs
D. Smyly -L
U 25
+105
08:05 PM
1959
Detroit Tigers
J. Wentz -L
O 28
-115
1960
Texas Rangers
D. Dunning -R
U 28
-115
08:10 PM
1961
Cleveland Guardians
L. Allen -L
O 27
-140
1962
Kansas City Royals
A. Cox-L
U 27
+110
09:38 PM
1963
Chicago White Sox
L. Giolito -R
O 26
-140
1964
Los Angeles Angels
J. Barria -R
U 26
+110
09:40 PM
1965
New York Yankees
D. German -R
O 25½
+105
1966
Oakland Athletics
J. Sears -L
U 25½
-135
09:40 PM
1979
Tampa Bay Rays
Z. Eflin -R
O 27½
-130
1980
Arizona Diamondbacks
Z. Davies -R
U 27½
+100
"""

# Define the regex pattern
pattern = r"(O|U)\s+((\d+)(½)?)\n(-?\d+)"

# Find all matches in the lines data
matches = re.findall(pattern, lines_data)

# Iterate over the matches and extract the relevant information
over_price = None
under_price = None

for match in matches:
    over_under = match[0]
    number = match[1]
    line = match[4]

    if over_under == 'O':
        over_price = line
    elif over_under == 'U':
        under_price = line
        # Process the Over and Under prices together
        print(f"Over/Under: {number}")
        print(f"Over Price: {over_price}")
        print(f"Under Price: {under_price}\n")
