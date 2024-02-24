import re

data = """
Damian Lillard
Over 4.5
−120
U
 
4.5
−110
Donovan Mitchell
Over 4.5
−110
U
 
4.5
−125
Giannis Antetokounmpo
Over 4.5
−110
U
 
4.5
−120
Jayson Tatum
Over 5.5
−105
U
 
5.5
−130
Kevin Durant
Over 3.5
−125
U
 
3.5
−105
LeBron James
Over 5.5
+100
U
 
5.5
−135
Luka Doncic
Over 5.5
+100
U
 
5.5
−135
Nikola Jokic
Over 6.5
−115
U
 
6.5
−115
Shai Gilgeous-Alexander
Over 7.5
−115
U
 
7.5
−115
Stephen Curry
Over 4.5
−120
U
 
4.5
−110
Tyrese Haliburton
Over 9.5
−145
U
 
9.5
+110
"""

# Define a regular expression pattern to find "Over" followed by a number
pattern = r'Over\s+(\d+\.\d+)'

# Find all matches of the pattern in the data
matches = re.findall(pattern, data)

# Print the extracted numbers
for match in matches:
    print(match)
