import re

data = """


951	LOS ANGELES DODGERS

P: 1:10PM  C: 3:10PM  E: 4:10PM 
952	SAN DIEGO PADRES






953	WASHINGTON NATIONALS

P: 3:40PM  C: 5:40PM  E: 6:40PM 
954	PHILADELPHIA PHILLIES






955	MIAMI MARLINS

P: 3:40PM  C: 5:40PM  E: 6:40PM 
956	CINCINNATI REDS






957	ATLANTA BRAVES

P: 4:05PM  C: 6:05PM  E: 7:05PM 
958	PITTSBURGH PIRATES






959	CHICAGO CUBS

P: 4:10PM  C: 6:10PM  E: 7:10PM 
960	NEW YORK METS






961	COLORADO ROCKIES

P: 5:10PM  C: 7:10PM  E: 8:10PM 
962	MILWAUKEE BREWERS






AMERICAN LEAGUE  
 
963	MINNESOTA TWINS

P: 3:40PM  C: 5:40PM  E: 6:40PM 
964	DETROIT TIGERS






965	KANSAS CITY ROYALS

P: 4:10PM  C: 6:10PM  E: 7:10PM 
966	BOSTON RED SOX






967	TORONTO BLUE JAYS

P: 4:10PM  C: 6:10PM  E: 7:10PM 
968	CLEVELAND GUARDIANS






969	NEW YORK YANKEES

P: 5:10PM  C: 7:10PM  E: 8:10PM 
970	CHICAGO WHITE SOX






971	TEXAS RANGERS

P: 6:40PM  C: 8:40PM  E: 9:40PM 
972	OAKLAND ATHLETICS






INTERLEAGUE  
 
973	SAN FRANCISCO GIANTS

P: 6:38PM  C: 8:38PM  E: 9:38PM 
974	LOS ANGELES ANGELS











"""



team_names = re.findall(r"\d+\s+(.*\S)\s*$", data, re.MULTILINE)
team_names = [name.strip() for name in team_names]

print(team_names)