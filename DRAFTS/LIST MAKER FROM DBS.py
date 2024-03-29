import re

data = """




951	CINCINNATI REDS GAME #1

P: 10:35AM  C: 12:35PM  E: 1:35PM  
952	PITTSBURGH PIRATES GAME #1






953	ATLANTA BRAVES

P: 4:10PM  C: 6:10PM  E: 7:10PM 
954	NEW YORK METS






955	COLORADO ROCKIES

P: 1:10PM  C: 3:10PM  E: 4:10PM 
956	LOS ANGELES DODGERS






957	SAN DIEGO PADRES

P: 1:10PM  C: 3:10PM  E: 4:10PM 
958	ARIZONA DIAMONDBACKS






AMERICAN LEAGUE  
 
959	DETROIT TIGERS

P: 9:05AM  C: 11:05AM  E: 12:05PM 
960	BOSTON RED SOX






961	CLEVELAND GUARDIANS

P: 10:40AM  C: 12:40PM  E: 1:40PM 
962	TAMPA BAY RAYS






963	LOS ANGELES ANGELS

P: 11:10AM  C: 1:10PM  E: 2:10PM 
964	HOUSTON ASTROS






965	BALTIMORE ORIOLES

P: 1:10PM  C: 3:10PM  E: 4:10PM 
966	SEATTLE MARINERS






INTERLEAGUE  
 
967	OAKLAND ATHLETICS

P: 10:35AM  C: 12:35PM  E: 1:35PM 
968	WASHINGTON NATIONALS






969	MINNESOTA TWINS

P: 10:35AM  C: 12:35PM  E: 1:35PM 
970	PHILADELPHIA PHILLIES






971	CHICAGO CUBS

P: 10:37AM  C: 12:37PM  E: 1:37PM 
972	TORONTO BLUE JAYS






973	NEW YORK YANKEES

P: 10:40AM  C: 12:40PM  E: 1:40PM 
974	MIAMI MARLINS






975	MILWAUKEE BREWERS

P: 11:10AM  C: 1:10PM  E: 2:10PM 
976	CHICAGO WHITE SOX






977	TEXAS RANGERS

P: 1:05PM  C: 3:05PM  E: 4:05PM 
978	SAN FRANCISCO GIANTS






WRITE-IN GAMES  
 
979	CINCINNATI REDS GAME #2

P: 3:05PM  C: 5:05PM  E: 6:05PM  
980	PITTSBURGH PIRATES GAME #2















"""



team_names = re.findall(r"\d+\s+(.*\S)\s*$", data, re.MULTILINE)
team_names = [name.strip() for name in team_names]

print(team_names)