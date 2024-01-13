import re

def extract_data(text):
    # Extract games
    games = re.findall(r'\((.*?)\)', text)

    # Extract type of props
    prop_types = [
        'PLAYER TRIPLE DOUBLE',
        'PLAYER DOUBLE DOUBLE',
        'UNDER/OVER PLAYER POINTS AND ASSISTS',
        'UNDER/OVER PLAYER POINTS AND REBOUNDS',
        'UNDER/OVER PLAYER ASSISTS AND REBOUNDS',
        'UNDER/OVER PLAYER POINTS, ASSISTS AND REBOUNDS',
        'UNDER/OVER PLAYER STEALS AND BLOCKS',
        'UNDER/OVER PLAYER 3 POINTS MADE',
        'UNDER/OVER PLAYER TURNOVERS',
        'UNDER/OVER PLAYER STEALS',
        'UNDER/OVER PLAYER BLOCKS',
        'UNDER/OVER PLAYER POINTS',
        'UNDER/OVER PLAYER ASSISTS',
        'UNDER/OVER PLAYER REBOUNDS'
    ]

    # Extract type of props for each game
    # Count total number of props for each type
    total_props_per_type = {prop_type: len(re.findall(f'{prop_type}.*?(?=\(|$)', text)) for prop_type in prop_types}

    return len(games), prop_types, total_props_per_type

# Example usage
text = """


All Props: 	Fixture ID	Prop Description	Prop Type	Wager Type	Is TNT	Market ID	Game Date
	12055116	DONOVAN MITCHELL - PLAYER TRIPLE DOUBLE (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - ML	No	1095	2024-01-07 13:00:00
	12055121	BRANDON INGRAM - PLAYER TRIPLE DOUBLE (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - ML	No	1095	2024-01-07 18:00:00
	12055121	DOMANTAS SABONIS - PLAYER TRIPLE DOUBLE (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - ML	No	1095	2024-01-07 18:00:00
	12055122	PAOLO BANCHERO - PLAYER TRIPLE DOUBLE (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - ML	No	1095	2024-01-07 18:00:00
	12055133	ANTHONY EDWARDS - PLAYER TRIPLE DOUBLE (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - ML	No	1095	2024-01-07 19:30:00
	12055133	LUKA DONCIC - PLAYER TRIPLE DOUBLE (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - ML	No	1095	2024-01-07 19:30:00
	12055132	DEVIN BOOKER - PLAYER TRIPLE DOUBLE (Phoenix Suns vs Memphis Grizzlies) (Phoenix Suns vs Memphis Grizzlies)	Player Prop	GAME - ML	No	1095	2024-01-07 20:00:00
	12055132	JA MORANT - PLAYER TRIPLE DOUBLE (Phoenix Suns vs Memphis Grizzlies) (Phoenix Suns vs Memphis Grizzlies)	Player Prop	GAME - ML	No	1095	2024-01-07 20:00:00
	12055141	NIKOLA JOKIC - PLAYER TRIPLE DOUBLE (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - ML	No	1095	2024-01-07 20:00:00
	12055140	BRANDIN PODZIEMSKI - PLAYER TRIPLE DOUBLE (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - ML	No	1095	2024-01-07 20:30:00
	12055140	PASCAL SIAKAM - PLAYER TRIPLE DOUBLE (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - ML	No	1095	2024-01-07 20:30:00
	12055140	SCOTTIE BARNES - PLAYER TRIPLE DOUBLE (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - ML	No	1095	2024-01-07 20:30:00
	12055115	JAMES HARDEN - PLAYER TRIPLE DOUBLE (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - ML	No	1095	2024-01-07 21:30:00
	12055115	LEBRON JAMES - PLAYER TRIPLE DOUBLE (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - ML	No	1095	2024-01-07 21:30:00
	12055116	KELDON JOHNSON - PLAYER DOUBLE DOUBLE (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - ML	No	1094	2024-01-07 13:00:00
	12055116	JARRETT ALLEN - PLAYER DOUBLE DOUBLE (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - ML	No	1094	2024-01-07 13:00:00
	12055116	WEMBANYAMA VICTOR - PLAYER DOUBLE DOUBLE (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - ML	No	1094	2024-01-07 13:00:00
	12055116	CARIS LEVERT - PLAYER DOUBLE DOUBLE (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - ML	No	1094	2024-01-07 13:00:00
	12055116	TRE JONES - PLAYER DOUBLE DOUBLE (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - ML	No	1094	2024-01-07 13:00:00
	12055116	MAX STRUS - PLAYER DOUBLE DOUBLE (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - ML	No	1094	2024-01-07 13:00:00
	12055116	DONOVAN MITCHELL - PLAYER DOUBLE DOUBLE (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - ML	No	1094	2024-01-07 13:00:00
	12055116	JEREMY SOCHAN - PLAYER DOUBLE DOUBLE (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - ML	No	1094	2024-01-07 13:00:00
	12055117	ANFERNEE SIMONS - PLAYER DOUBLE DOUBLE (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - ML	No	1094	2024-01-07 15:00:00
	12055117	CAMERON JOHNSON - PLAYER DOUBLE DOUBLE (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - ML	No	1094	2024-01-07 15:00:00
	12055117	NICOLAS CLAXTON - PLAYER DOUBLE DOUBLE (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - ML	No	1094	2024-01-07 15:00:00
	12055117	DAY'RON SHARPE - PLAYER DOUBLE DOUBLE (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - ML	No	1094	2024-01-07 15:00:00
	12055117	MIKAL BRIDGES - PLAYER DOUBLE DOUBLE (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - ML	No	1094	2024-01-07 15:00:00
	12055117	SPENCER DINWIDDIE - PLAYER DOUBLE DOUBLE (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - ML	No	1094	2024-01-07 15:00:00
	12055121	KEEGAN MURRAY - PLAYER DOUBLE DOUBLE (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - ML	No	1094	2024-01-07 18:00:00
	12055121	MALIK MONK - PLAYER DOUBLE DOUBLE (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - ML	No	1094	2024-01-07 18:00:00
	12055121	DOMANTAS SABONIS - PLAYER DOUBLE DOUBLE (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - ML	No	1094	2024-01-07 18:00:00
	12055121	DE'AARON FOX - PLAYER DOUBLE DOUBLE (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - ML	No	1094	2024-01-07 18:00:00
	12055121	ZION WILLIAMSON - PLAYER DOUBLE DOUBLE (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - ML	No	1094	2024-01-07 18:00:00
	12055121	CHRISTIAN JAMES MCCOLLUM - PLAYER DOUBLE DOUBLE (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - ML	No	1094	2024-01-07 18:00:00
	12055121	BRANDON INGRAM - PLAYER DOUBLE DOUBLE (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - ML	No	1094	2024-01-07 18:00:00
	12055122	PAOLO BANCHERO - PLAYER DOUBLE DOUBLE (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - ML	No	1094	2024-01-07 18:00:00
	12055122	MURRAY DEJOUNTE - PLAYER DOUBLE DOUBLE (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - ML	No	1094	2024-01-07 18:00:00
	12055122	TRAE YOUNG - PLAYER DOUBLE DOUBLE (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - ML	No	1094	2024-01-07 18:00:00
	12055122	ONYEKA OKONGWU - PLAYER DOUBLE DOUBLE (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - ML	No	1094	2024-01-07 18:00:00
	12055122	CLINT CAPELA - PLAYER DOUBLE DOUBLE (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - ML	No	1094	2024-01-07 18:00:00
	12055122	JALEN JOHNSON - PLAYER DOUBLE DOUBLE (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - ML	No	1094	2024-01-07 18:00:00
	12055122	SADDIQ BEY - PLAYER DOUBLE DOUBLE (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - ML	No	1094	2024-01-07 18:00:00
	12055133	LUKA DONCIC - PLAYER DOUBLE DOUBLE (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - ML	No	1094	2024-01-07 19:30:00
	12055133	MIKE CONLEY JR. - PLAYER DOUBLE DOUBLE (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - ML	No	1094	2024-01-07 19:30:00
	12055133	NAZ REID - PLAYER DOUBLE DOUBLE (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - ML	No	1094	2024-01-07 19:30:00
	12055133	ANTHONY EDWARDS - PLAYER DOUBLE DOUBLE (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - ML	No	1094	2024-01-07 19:30:00
	12055133	KARL-ANTHONY TOWNS JR. - PLAYER DOUBLE DOUBLE (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - ML	No	1094	2024-01-07 19:30:00
	12055133	RUDY GOBERT - PLAYER DOUBLE DOUBLE (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - ML	No	1094	2024-01-07 19:30:00
	12055132	JA MORANT - PLAYER DOUBLE DOUBLE (Phoenix Suns vs Memphis Grizzlies) (Phoenix Suns vs Memphis Grizzlies)	Player Prop	GAME - ML	No	1094	2024-01-07 20:00:00
	12055132	DEVIN BOOKER - PLAYER DOUBLE DOUBLE (Phoenix Suns vs Memphis Grizzlies) (Phoenix Suns vs Memphis Grizzlies)	Player Prop	GAME - ML	No	1094	2024-01-07 20:00:00
	12055141	JAMAL MURRAY - PLAYER DOUBLE DOUBLE (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - ML	No	1094	2024-01-07 20:00:00
	12055141	MICHAEL PORTER JR. - PLAYER DOUBLE DOUBLE (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - ML	No	1094	2024-01-07 20:00:00
	12055141	NIKOLA JOKIC - PLAYER DOUBLE DOUBLE (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - ML	No	1094	2024-01-07 20:00:00
	12055141	JALEN DUREN - PLAYER DOUBLE DOUBLE (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - ML	No	1094	2024-01-07 20:00:00
	12055141	AARON GORDON - PLAYER DOUBLE DOUBLE (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - ML	No	1094	2024-01-07 20:00:00
	12055141	CADE CUNNINGHAM - PLAYER DOUBLE DOUBLE (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - ML	No	1094	2024-01-07 20:00:00
	12055140	PASCAL SIAKAM - PLAYER DOUBLE DOUBLE (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - ML	No	1094	2024-01-07 20:30:00
	12055140	SCOTTIE BARNES - PLAYER DOUBLE DOUBLE (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - ML	No	1094	2024-01-07 20:30:00
	12055140	STEPHEN CURRY - PLAYER DOUBLE DOUBLE (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - ML	No	1094	2024-01-07 20:30:00
	12055140	BRANDIN PODZIEMSKI - PLAYER DOUBLE DOUBLE (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - ML	No	1094	2024-01-07 20:30:00
	12055140	JAKOB POELTL - PLAYER DOUBLE DOUBLE (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - ML	No	1094	2024-01-07 20:30:00
	12055140	IMMANUEL QUICKLEY - PLAYER DOUBLE DOUBLE (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - ML	No	1094	2024-01-07 20:30:00
	12055140	JONATHAN KUMINGA - PLAYER DOUBLE DOUBLE (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - ML	No	1094	2024-01-07 20:30:00
	12055140	RJ BARRETT JR. - PLAYER DOUBLE DOUBLE (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - ML	No	1094	2024-01-07 20:30:00
	12055115	IVICA ZUBAC - PLAYER DOUBLE DOUBLE (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - ML	No	1094	2024-01-07 21:30:00
	12055115	LEBRON JAMES - PLAYER DOUBLE DOUBLE (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - ML	No	1094	2024-01-07 21:30:00
	12055115	KAWHI LEONARD - PLAYER DOUBLE DOUBLE (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - ML	No	1094	2024-01-07 21:30:00
	12055115	PAUL GEORGE - PLAYER DOUBLE DOUBLE (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - ML	No	1094	2024-01-07 21:30:00
	12055115	ANTHONY DAVIS JR. - PLAYER DOUBLE DOUBLE (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - ML	No	1094	2024-01-07 21:30:00
	12055115	JAMES HARDEN - PLAYER DOUBLE DOUBLE (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - ML	No	1094	2024-01-07 21:30:00
	12055116	JEREMY SOCHAN - UNDER/OVER PLAYER POINTS AND ASSISTS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1093	2024-01-07 13:00:00
	12055116	DEAN WADE - UNDER/OVER PLAYER POINTS AND ASSISTS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1093	2024-01-07 13:00:00
	12055116	DONOVAN MITCHELL - UNDER/OVER PLAYER POINTS AND ASSISTS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1093	2024-01-07 13:00:00
	12055116	ISAAC OKORO - UNDER/OVER PLAYER POINTS AND ASSISTS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1093	2024-01-07 13:00:00
	12055116	DEVIN VASSELL - UNDER/OVER PLAYER POINTS AND ASSISTS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1093	2024-01-07 13:00:00
	12055116	TRE JONES - UNDER/OVER PLAYER POINTS AND ASSISTS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1093	2024-01-07 13:00:00
	12055116	MALAKI BRANHAM - UNDER/OVER PLAYER POINTS AND ASSISTS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1093	2024-01-07 13:00:00
	12055116	SAM MERRILL - UNDER/OVER PLAYER POINTS AND ASSISTS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1093	2024-01-07 13:00:00
	12055116	GEORGES NIANG - UNDER/OVER PLAYER POINTS AND ASSISTS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1093	2024-01-07 13:00:00
	12055116	CARIS LEVERT - UNDER/OVER PLAYER POINTS AND ASSISTS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1093	2024-01-07 13:00:00
	12055116	JULIAN CHAMPAGNIE - UNDER/OVER PLAYER POINTS AND ASSISTS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1093	2024-01-07 13:00:00
	12055116	JARRETT ALLEN - UNDER/OVER PLAYER POINTS AND ASSISTS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1093	2024-01-07 13:00:00
	12055116	KELDON JOHNSON - UNDER/OVER PLAYER POINTS AND ASSISTS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1093	2024-01-07 13:00:00
	12055116	MAX STRUS - UNDER/OVER PLAYER POINTS AND ASSISTS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1093	2024-01-07 13:00:00
	12055116	WEMBANYAMA VICTOR - UNDER/OVER PLAYER POINTS AND ASSISTS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1093	2024-01-07 13:00:00
	12055117	ROYCE O'NEALE - UNDER/OVER PLAYER POINTS AND ASSISTS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1093	2024-01-07 15:00:00
	12055117	ANFERNEE SIMONS - UNDER/OVER PLAYER POINTS AND ASSISTS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1093	2024-01-07 15:00:00
	12055117	GRANT JERAMI - UNDER/OVER PLAYER POINTS AND ASSISTS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1093	2024-01-07 15:00:00
	12055117	SPENCER DINWIDDIE - UNDER/OVER PLAYER POINTS AND ASSISTS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1093	2024-01-07 15:00:00
	12055117	CAMERON THOMAS - UNDER/OVER PLAYER POINTS AND ASSISTS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1093	2024-01-07 15:00:00
	12055117	CAMERON JOHNSON - UNDER/OVER PLAYER POINTS AND ASSISTS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1093	2024-01-07 15:00:00
	12055117	DORIAN FINNEY SMITH - UNDER/OVER PLAYER POINTS AND ASSISTS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1093	2024-01-07 15:00:00
	12055117	NICOLAS CLAXTON - UNDER/OVER PLAYER POINTS AND ASSISTS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1093	2024-01-07 15:00:00
	12055117	DENNIS SMITH JR. - UNDER/OVER PLAYER POINTS AND ASSISTS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1093	2024-01-07 15:00:00
	12055117	DAY'RON SHARPE - UNDER/OVER PLAYER POINTS AND ASSISTS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1093	2024-01-07 15:00:00
	12055117	MIKAL BRIDGES - UNDER/OVER PLAYER POINTS AND ASSISTS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1093	2024-01-07 15:00:00
	12055121	KEEGAN MURRAY - UNDER/OVER PLAYER POINTS AND ASSISTS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1093	2024-01-07 18:00:00
	12055121	BRANDON INGRAM - UNDER/OVER PLAYER POINTS AND ASSISTS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1093	2024-01-07 18:00:00
	12055121	MALIK MONK - UNDER/OVER PLAYER POINTS AND ASSISTS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1093	2024-01-07 18:00:00
	12055121	HARRISON BARNES - UNDER/OVER PLAYER POINTS AND ASSISTS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1093	2024-01-07 18:00:00
	12055121	DE'AARON FOX - UNDER/OVER PLAYER POINTS AND ASSISTS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1093	2024-01-07 18:00:00
	12055121	HERBERT JONES - UNDER/OVER PLAYER POINTS AND ASSISTS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1093	2024-01-07 18:00:00
	12055121	CHRISTIAN JAMES MCCOLLUM - UNDER/OVER PLAYER POINTS AND ASSISTS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1093	2024-01-07 18:00:00
	12055121	DOMANTAS SABONIS - UNDER/OVER PLAYER POINTS AND ASSISTS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1093	2024-01-07 18:00:00
	12055121	ZION WILLIAMSON - UNDER/OVER PLAYER POINTS AND ASSISTS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1093	2024-01-07 18:00:00
	12055122	TRAE YOUNG - UNDER/OVER PLAYER POINTS AND ASSISTS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1093	2024-01-07 18:00:00
	12055122	CLINT CAPELA - UNDER/OVER PLAYER POINTS AND ASSISTS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1093	2024-01-07 18:00:00
	12055122	JALEN SUGGS - UNDER/OVER PLAYER POINTS AND ASSISTS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1093	2024-01-07 18:00:00
	12055122	BOGDAN BOGDANOVIC - UNDER/OVER PLAYER POINTS AND ASSISTS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1093	2024-01-07 18:00:00
	12055122	SADDIQ BEY - UNDER/OVER PLAYER POINTS AND ASSISTS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1093	2024-01-07 18:00:00
	12055122	PAOLO BANCHERO - UNDER/OVER PLAYER POINTS AND ASSISTS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1093	2024-01-07 18:00:00
	12055122	ONYEKA OKONGWU - UNDER/OVER PLAYER POINTS AND ASSISTS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1093	2024-01-07 18:00:00
	12055122	MURRAY DEJOUNTE - UNDER/OVER PLAYER POINTS AND ASSISTS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1093	2024-01-07 18:00:00
	12055122	JALEN JOHNSON - UNDER/OVER PLAYER POINTS AND ASSISTS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1093	2024-01-07 18:00:00
	12055133	KYLE ANDERSON - UNDER/OVER PLAYER POINTS AND ASSISTS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1093	2024-01-07 19:30:00
	12055133	RUDY GOBERT - UNDER/OVER PLAYER POINTS AND ASSISTS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1093	2024-01-07 19:30:00
	12055133	ANTHONY EDWARDS - UNDER/OVER PLAYER POINTS AND ASSISTS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1093	2024-01-07 19:30:00
	12055133	NAZ REID - UNDER/OVER PLAYER POINTS AND ASSISTS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1093	2024-01-07 19:30:00
	12055133	MIKE CONLEY JR. - UNDER/OVER PLAYER POINTS AND ASSISTS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1093	2024-01-07 19:30:00
	12055133	KARL-ANTHONY TOWNS JR. - UNDER/OVER PLAYER POINTS AND ASSISTS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1093	2024-01-07 19:30:00
	12055133	JADEN MCDANIELS - UNDER/OVER PLAYER POINTS AND ASSISTS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1093	2024-01-07 19:30:00
	12055133	LUKA DONCIC - UNDER/OVER PLAYER POINTS AND ASSISTS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1093	2024-01-07 19:30:00
	12055133	NICKEIL ALEXANDER-WALKER - UNDER/OVER PLAYER POINTS AND ASSISTS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1093	2024-01-07 19:30:00
	12055132	JA MORANT - UNDER/OVER PLAYER POINTS AND ASSISTS (Phoenix Suns vs Memphis Grizzlies) (Phoenix Suns vs Memphis Grizzlies)	Player Prop	GAME - TOTAL	No	1093	2024-01-07 20:00:00
	12055132	DEVIN BOOKER - UNDER/OVER PLAYER POINTS AND ASSISTS (Phoenix Suns vs Memphis Grizzlies) (Phoenix Suns vs Memphis Grizzlies)	Player Prop	GAME - TOTAL	No	1093	2024-01-07 20:00:00
	12055141	CADE CUNNINGHAM - UNDER/OVER PLAYER POINTS AND ASSISTS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1093	2024-01-07 20:00:00
	12055141	AARON GORDON - UNDER/OVER PLAYER POINTS AND ASSISTS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1093	2024-01-07 20:00:00
	12055141	NIKOLA JOKIC - UNDER/OVER PLAYER POINTS AND ASSISTS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1093	2024-01-07 20:00:00
	12055141	BOJAN BOGDANOVIC - UNDER/OVER PLAYER POINTS AND ASSISTS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1093	2024-01-07 20:00:00
	12055141	MICHAEL PORTER JR. - UNDER/OVER PLAYER POINTS AND ASSISTS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1093	2024-01-07 20:00:00
	12055141	CALDWELL POPE KENTAVIOUS - UNDER/OVER PLAYER POINTS AND ASSISTS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1093	2024-01-07 20:00:00
	12055141	JALEN DUREN - UNDER/OVER PLAYER POINTS AND ASSISTS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1093	2024-01-07 20:00:00
	12055141	JAMAL MURRAY - UNDER/OVER PLAYER POINTS AND ASSISTS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1093	2024-01-07 20:00:00
	12055140	IMMANUEL QUICKLEY - UNDER/OVER PLAYER POINTS AND ASSISTS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1093	2024-01-07 20:30:00
	12055140	PASCAL SIAKAM - UNDER/OVER PLAYER POINTS AND ASSISTS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1093	2024-01-07 20:30:00
	12055140	STEPHEN CURRY - UNDER/OVER PLAYER POINTS AND ASSISTS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1093	2024-01-07 20:30:00
	12055140	JAKOB POELTL - UNDER/OVER PLAYER POINTS AND ASSISTS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1093	2024-01-07 20:30:00
	12055140	JONATHAN KUMINGA - UNDER/OVER PLAYER POINTS AND ASSISTS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1093	2024-01-07 20:30:00
	12055140	KLAY THOMPSON - UNDER/OVER PLAYER POINTS AND ASSISTS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1093	2024-01-07 20:30:00
	12055140	RJ BARRETT JR. - UNDER/OVER PLAYER POINTS AND ASSISTS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1093	2024-01-07 20:30:00
	12055140	BRANDIN PODZIEMSKI - UNDER/OVER PLAYER POINTS AND ASSISTS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1093	2024-01-07 20:30:00
	12055140	SCOTTIE BARNES - UNDER/OVER PLAYER POINTS AND ASSISTS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1093	2024-01-07 20:30:00
	12055115	JAMES HARDEN - UNDER/OVER PLAYER POINTS AND ASSISTS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1093	2024-01-07 21:30:00
	12055115	TAUREAN PRINCE - UNDER/OVER PLAYER POINTS AND ASSISTS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1093	2024-01-07 21:30:00
	12055115	PAUL GEORGE - UNDER/OVER PLAYER POINTS AND ASSISTS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1093	2024-01-07 21:30:00
	12055115	KAWHI LEONARD - UNDER/OVER PLAYER POINTS AND ASSISTS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1093	2024-01-07 21:30:00
	12055115	ANTHONY DAVIS JR. - UNDER/OVER PLAYER POINTS AND ASSISTS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1093	2024-01-07 21:30:00
	12055115	TERANCE MANN - UNDER/OVER PLAYER POINTS AND ASSISTS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1093	2024-01-07 21:30:00
	12055115	IVICA ZUBAC - UNDER/OVER PLAYER POINTS AND ASSISTS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1093	2024-01-07 21:30:00
	12055115	LEBRON JAMES - UNDER/OVER PLAYER POINTS AND ASSISTS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1093	2024-01-07 21:30:00
	12055116	SAM MERRILL - UNDER/OVER PLAYER POINTS AND REBOUNDS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1092	2024-01-07 13:00:00
	12055116	WEMBANYAMA VICTOR - UNDER/OVER PLAYER POINTS AND REBOUNDS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1092	2024-01-07 13:00:00
	12055116	JEREMY SOCHAN - UNDER/OVER PLAYER POINTS AND REBOUNDS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1092	2024-01-07 13:00:00
	12055116	JARRETT ALLEN - UNDER/OVER PLAYER POINTS AND REBOUNDS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1092	2024-01-07 13:00:00
	12055116	CARIS LEVERT - UNDER/OVER PLAYER POINTS AND REBOUNDS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1092	2024-01-07 13:00:00
	12055116	MAX STRUS - UNDER/OVER PLAYER POINTS AND REBOUNDS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1092	2024-01-07 13:00:00
	12055116	DONOVAN MITCHELL - UNDER/OVER PLAYER POINTS AND REBOUNDS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1092	2024-01-07 13:00:00
	12055116	GEORGES NIANG - UNDER/OVER PLAYER POINTS AND REBOUNDS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1092	2024-01-07 13:00:00
	12055116	KELDON JOHNSON - UNDER/OVER PLAYER POINTS AND REBOUNDS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1092	2024-01-07 13:00:00
	12055116	DEVIN VASSELL - UNDER/OVER PLAYER POINTS AND REBOUNDS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1092	2024-01-07 13:00:00
	12055116	ISAAC OKORO - UNDER/OVER PLAYER POINTS AND REBOUNDS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1092	2024-01-07 13:00:00
	12055116	JULIAN CHAMPAGNIE - UNDER/OVER PLAYER POINTS AND REBOUNDS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1092	2024-01-07 13:00:00
	12055116	TRE JONES - UNDER/OVER PLAYER POINTS AND REBOUNDS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1092	2024-01-07 13:00:00
	12055116	DEAN WADE - UNDER/OVER PLAYER POINTS AND REBOUNDS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1092	2024-01-07 13:00:00
	12055117	SPENCER DINWIDDIE - UNDER/OVER PLAYER POINTS AND REBOUNDS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1092	2024-01-07 15:00:00
	12055117	ANFERNEE SIMONS - UNDER/OVER PLAYER POINTS AND REBOUNDS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1092	2024-01-07 15:00:00
	12055117	NICOLAS CLAXTON - UNDER/OVER PLAYER POINTS AND REBOUNDS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1092	2024-01-07 15:00:00
	12055117	DORIAN FINNEY SMITH - UNDER/OVER PLAYER POINTS AND REBOUNDS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1092	2024-01-07 15:00:00
	12055117	MIKAL BRIDGES - UNDER/OVER PLAYER POINTS AND REBOUNDS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1092	2024-01-07 15:00:00
	12055117	DAY'RON SHARPE - UNDER/OVER PLAYER POINTS AND REBOUNDS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1092	2024-01-07 15:00:00
	12055117	DENNIS SMITH JR. - UNDER/OVER PLAYER POINTS AND REBOUNDS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1092	2024-01-07 15:00:00
	12055117	GRANT JERAMI - UNDER/OVER PLAYER POINTS AND REBOUNDS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1092	2024-01-07 15:00:00
	12055117	CAMERON JOHNSON - UNDER/OVER PLAYER POINTS AND REBOUNDS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1092	2024-01-07 15:00:00
	12055117	CAMERON THOMAS - UNDER/OVER PLAYER POINTS AND REBOUNDS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1092	2024-01-07 15:00:00
	12055117	ROYCE O'NEALE - UNDER/OVER PLAYER POINTS AND REBOUNDS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1092	2024-01-07 15:00:00
	12055121	DOMANTAS SABONIS - UNDER/OVER PLAYER POINTS AND REBOUNDS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1092	2024-01-07 18:00:00
	12055121	ZION WILLIAMSON - UNDER/OVER PLAYER POINTS AND REBOUNDS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1092	2024-01-07 18:00:00
	12055121	CHRISTIAN JAMES MCCOLLUM - UNDER/OVER PLAYER POINTS AND REBOUNDS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1092	2024-01-07 18:00:00
	12055121	HERBERT JONES - UNDER/OVER PLAYER POINTS AND REBOUNDS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1092	2024-01-07 18:00:00
	12055121	BRANDON INGRAM - UNDER/OVER PLAYER POINTS AND REBOUNDS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1092	2024-01-07 18:00:00
	12055121	DE'AARON FOX - UNDER/OVER PLAYER POINTS AND REBOUNDS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1092	2024-01-07 18:00:00
	12055121	HARRISON BARNES - UNDER/OVER PLAYER POINTS AND REBOUNDS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1092	2024-01-07 18:00:00
	12055121	KEEGAN MURRAY - UNDER/OVER PLAYER POINTS AND REBOUNDS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1092	2024-01-07 18:00:00
	12055121	MALIK MONK - UNDER/OVER PLAYER POINTS AND REBOUNDS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1092	2024-01-07 18:00:00
	12055122	SADDIQ BEY - UNDER/OVER PLAYER POINTS AND REBOUNDS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1092	2024-01-07 18:00:00
	12055122	JALEN SUGGS - UNDER/OVER PLAYER POINTS AND REBOUNDS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1092	2024-01-07 18:00:00
	12055122	BOGDAN BOGDANOVIC - UNDER/OVER PLAYER POINTS AND REBOUNDS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1092	2024-01-07 18:00:00
	12055122	MURRAY DEJOUNTE - UNDER/OVER PLAYER POINTS AND REBOUNDS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1092	2024-01-07 18:00:00
	12055122	CLINT CAPELA - UNDER/OVER PLAYER POINTS AND REBOUNDS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1092	2024-01-07 18:00:00
	12055122	PAOLO BANCHERO - UNDER/OVER PLAYER POINTS AND REBOUNDS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1092	2024-01-07 18:00:00
	12055122	TRAE YOUNG - UNDER/OVER PLAYER POINTS AND REBOUNDS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1092	2024-01-07 18:00:00
	12055122	ONYEKA OKONGWU - UNDER/OVER PLAYER POINTS AND REBOUNDS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1092	2024-01-07 18:00:00
	12055122	JALEN JOHNSON - UNDER/OVER PLAYER POINTS AND REBOUNDS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1092	2024-01-07 18:00:00
	12055133	NAZ REID - UNDER/OVER PLAYER POINTS AND REBOUNDS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1092	2024-01-07 19:30:00
	12055133	KARL-ANTHONY TOWNS JR. - UNDER/OVER PLAYER POINTS AND REBOUNDS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1092	2024-01-07 19:30:00
	12055133	RUDY GOBERT - UNDER/OVER PLAYER POINTS AND REBOUNDS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1092	2024-01-07 19:30:00
	12055133	MIKE CONLEY JR. - UNDER/OVER PLAYER POINTS AND REBOUNDS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1092	2024-01-07 19:30:00
	12055133	JADEN MCDANIELS - UNDER/OVER PLAYER POINTS AND REBOUNDS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1092	2024-01-07 19:30:00
	12055133	KYLE ANDERSON - UNDER/OVER PLAYER POINTS AND REBOUNDS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1092	2024-01-07 19:30:00
	12055133	ANTHONY EDWARDS - UNDER/OVER PLAYER POINTS AND REBOUNDS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1092	2024-01-07 19:30:00
	12055133	NICKEIL ALEXANDER-WALKER - UNDER/OVER PLAYER POINTS AND REBOUNDS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1092	2024-01-07 19:30:00
	12055133	LUKA DONCIC - UNDER/OVER PLAYER POINTS AND REBOUNDS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1092	2024-01-07 19:30:00
	12055132	JA MORANT - UNDER/OVER PLAYER POINTS AND REBOUNDS (Phoenix Suns vs Memphis Grizzlies) (Phoenix Suns vs Memphis Grizzlies)	Player Prop	GAME - TOTAL	No	1092	2024-01-07 20:00:00
	12055132	DEVIN BOOKER - UNDER/OVER PLAYER POINTS AND REBOUNDS (Phoenix Suns vs Memphis Grizzlies) (Phoenix Suns vs Memphis Grizzlies)	Player Prop	GAME - TOTAL	No	1092	2024-01-07 20:00:00
	12055141	CALDWELL POPE KENTAVIOUS - UNDER/OVER PLAYER POINTS AND REBOUNDS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1092	2024-01-07 20:00:00
	12055141	MICHAEL PORTER JR. - UNDER/OVER PLAYER POINTS AND REBOUNDS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1092	2024-01-07 20:00:00
	12055141	CADE CUNNINGHAM - UNDER/OVER PLAYER POINTS AND REBOUNDS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1092	2024-01-07 20:00:00
	12055141	BOJAN BOGDANOVIC - UNDER/OVER PLAYER POINTS AND REBOUNDS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1092	2024-01-07 20:00:00
	12055141	NIKOLA JOKIC - UNDER/OVER PLAYER POINTS AND REBOUNDS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1092	2024-01-07 20:00:00
	12055141	JALEN DUREN - UNDER/OVER PLAYER POINTS AND REBOUNDS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1092	2024-01-07 20:00:00
	12055141	AARON GORDON - UNDER/OVER PLAYER POINTS AND REBOUNDS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1092	2024-01-07 20:00:00
	12055141	JAMAL MURRAY - UNDER/OVER PLAYER POINTS AND REBOUNDS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1092	2024-01-07 20:00:00
	12055140	SCOTTIE BARNES - UNDER/OVER PLAYER POINTS AND REBOUNDS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1092	2024-01-07 20:30:00
	12055140	JONATHAN KUMINGA - UNDER/OVER PLAYER POINTS AND REBOUNDS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1092	2024-01-07 20:30:00
	12055140	RJ BARRETT JR. - UNDER/OVER PLAYER POINTS AND REBOUNDS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1092	2024-01-07 20:30:00
	12055140	BRANDIN PODZIEMSKI - UNDER/OVER PLAYER POINTS AND REBOUNDS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1092	2024-01-07 20:30:00
	12055140	KLAY THOMPSON - UNDER/OVER PLAYER POINTS AND REBOUNDS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1092	2024-01-07 20:30:00
	12055140	JAKOB POELTL - UNDER/OVER PLAYER POINTS AND REBOUNDS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1092	2024-01-07 20:30:00
	12055140	PASCAL SIAKAM - UNDER/OVER PLAYER POINTS AND REBOUNDS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1092	2024-01-07 20:30:00
	12055140	STEPHEN CURRY - UNDER/OVER PLAYER POINTS AND REBOUNDS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1092	2024-01-07 20:30:00
	12055140	IMMANUEL QUICKLEY - UNDER/OVER PLAYER POINTS AND REBOUNDS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1092	2024-01-07 20:30:00
	12055115	PAUL GEORGE - UNDER/OVER PLAYER POINTS AND REBOUNDS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1092	2024-01-07 21:30:00
	12055115	IVICA ZUBAC - UNDER/OVER PLAYER POINTS AND REBOUNDS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1092	2024-01-07 21:30:00
	12055115	TAUREAN PRINCE - UNDER/OVER PLAYER POINTS AND REBOUNDS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1092	2024-01-07 21:30:00
	12055115	ANTHONY DAVIS JR. - UNDER/OVER PLAYER POINTS AND REBOUNDS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1092	2024-01-07 21:30:00
	12055115	LEBRON JAMES - UNDER/OVER PLAYER POINTS AND REBOUNDS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1092	2024-01-07 21:30:00
	12055115	KAWHI LEONARD - UNDER/OVER PLAYER POINTS AND REBOUNDS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1092	2024-01-07 21:30:00
	12055115	JAMES HARDEN - UNDER/OVER PLAYER POINTS AND REBOUNDS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1092	2024-01-07 21:30:00
	12055115	TERANCE MANN - UNDER/OVER PLAYER POINTS AND REBOUNDS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1092	2024-01-07 21:30:00
	12055116	CARIS LEVERT - UNDER/OVER PLAYER ASSISTS AND REBOUNDS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1091	2024-01-07 13:00:00
	12055116	KELDON JOHNSON - UNDER/OVER PLAYER ASSISTS AND REBOUNDS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1091	2024-01-07 13:00:00
	12055116	SAM MERRILL - UNDER/OVER PLAYER ASSISTS AND REBOUNDS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1091	2024-01-07 13:00:00
	12055116	JULIAN CHAMPAGNIE - UNDER/OVER PLAYER ASSISTS AND REBOUNDS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1091	2024-01-07 13:00:00
	12055116	DEVIN VASSELL - UNDER/OVER PLAYER ASSISTS AND REBOUNDS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1091	2024-01-07 13:00:00
	12055116	ISAAC OKORO - UNDER/OVER PLAYER ASSISTS AND REBOUNDS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1091	2024-01-07 13:00:00
	12055116	MAX STRUS - UNDER/OVER PLAYER ASSISTS AND REBOUNDS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1091	2024-01-07 13:00:00
	12055116	DONOVAN MITCHELL - UNDER/OVER PLAYER ASSISTS AND REBOUNDS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1091	2024-01-07 13:00:00
	12055116	JARRETT ALLEN - UNDER/OVER PLAYER ASSISTS AND REBOUNDS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1091	2024-01-07 13:00:00
	12055116	DEAN WADE - UNDER/OVER PLAYER ASSISTS AND REBOUNDS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1091	2024-01-07 13:00:00
	12055116	WEMBANYAMA VICTOR - UNDER/OVER PLAYER ASSISTS AND REBOUNDS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1091	2024-01-07 13:00:00
	12055116	MALAKI BRANHAM - UNDER/OVER PLAYER ASSISTS AND REBOUNDS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1091	2024-01-07 13:00:00
	12055116	GEORGES NIANG - UNDER/OVER PLAYER ASSISTS AND REBOUNDS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1091	2024-01-07 13:00:00
	12055116	JEREMY SOCHAN - UNDER/OVER PLAYER ASSISTS AND REBOUNDS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1091	2024-01-07 13:00:00
	12055116	TRE JONES - UNDER/OVER PLAYER ASSISTS AND REBOUNDS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1091	2024-01-07 13:00:00
	12055117	SPENCER DINWIDDIE - UNDER/OVER PLAYER ASSISTS AND REBOUNDS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1091	2024-01-07 15:00:00
	12055117	DAY'RON SHARPE - UNDER/OVER PLAYER ASSISTS AND REBOUNDS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1091	2024-01-07 15:00:00
	12055117	CAMERON JOHNSON - UNDER/OVER PLAYER ASSISTS AND REBOUNDS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1091	2024-01-07 15:00:00
	12055117	ROYCE O'NEALE - UNDER/OVER PLAYER ASSISTS AND REBOUNDS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1091	2024-01-07 15:00:00
	12055117	NICOLAS CLAXTON - UNDER/OVER PLAYER ASSISTS AND REBOUNDS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1091	2024-01-07 15:00:00
	12055117	ANFERNEE SIMONS - UNDER/OVER PLAYER ASSISTS AND REBOUNDS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1091	2024-01-07 15:00:00
	12055117	MIKAL BRIDGES - UNDER/OVER PLAYER ASSISTS AND REBOUNDS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1091	2024-01-07 15:00:00
	12055117	GRANT JERAMI - UNDER/OVER PLAYER ASSISTS AND REBOUNDS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1091	2024-01-07 15:00:00
	12055117	DENNIS SMITH JR. - UNDER/OVER PLAYER ASSISTS AND REBOUNDS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1091	2024-01-07 15:00:00
	12055117	CAMERON THOMAS - UNDER/OVER PLAYER ASSISTS AND REBOUNDS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1091	2024-01-07 15:00:00
	12055117	DORIAN FINNEY SMITH - UNDER/OVER PLAYER ASSISTS AND REBOUNDS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1091	2024-01-07 15:00:00
	12055121	HERBERT JONES - UNDER/OVER PLAYER ASSISTS AND REBOUNDS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1091	2024-01-07 18:00:00
	12055121	KEEGAN MURRAY - UNDER/OVER PLAYER ASSISTS AND REBOUNDS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1091	2024-01-07 18:00:00
	12055121	HARRISON BARNES - UNDER/OVER PLAYER ASSISTS AND REBOUNDS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1091	2024-01-07 18:00:00
	12055121	DE'AARON FOX - UNDER/OVER PLAYER ASSISTS AND REBOUNDS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1091	2024-01-07 18:00:00
	12055121	CHRISTIAN JAMES MCCOLLUM - UNDER/OVER PLAYER ASSISTS AND REBOUNDS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1091	2024-01-07 18:00:00
	12055121	MALIK MONK - UNDER/OVER PLAYER ASSISTS AND REBOUNDS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1091	2024-01-07 18:00:00
	12055121	ZION WILLIAMSON - UNDER/OVER PLAYER ASSISTS AND REBOUNDS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1091	2024-01-07 18:00:00
	12055121	DOMANTAS SABONIS - UNDER/OVER PLAYER ASSISTS AND REBOUNDS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1091	2024-01-07 18:00:00
	12055121	BRANDON INGRAM - UNDER/OVER PLAYER ASSISTS AND REBOUNDS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1091	2024-01-07 18:00:00
	12055122	SADDIQ BEY - UNDER/OVER PLAYER ASSISTS AND REBOUNDS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1091	2024-01-07 18:00:00
	12055122	JALEN SUGGS - UNDER/OVER PLAYER ASSISTS AND REBOUNDS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1091	2024-01-07 18:00:00
	12055122	CLINT CAPELA - UNDER/OVER PLAYER ASSISTS AND REBOUNDS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1091	2024-01-07 18:00:00
	12055122	MURRAY DEJOUNTE - UNDER/OVER PLAYER ASSISTS AND REBOUNDS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1091	2024-01-07 18:00:00
	12055122	BOGDAN BOGDANOVIC - UNDER/OVER PLAYER ASSISTS AND REBOUNDS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1091	2024-01-07 18:00:00
	12055122	PAOLO BANCHERO - UNDER/OVER PLAYER ASSISTS AND REBOUNDS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1091	2024-01-07 18:00:00
	12055122	TRAE YOUNG - UNDER/OVER PLAYER ASSISTS AND REBOUNDS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1091	2024-01-07 18:00:00
	12055122	ONYEKA OKONGWU - UNDER/OVER PLAYER ASSISTS AND REBOUNDS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1091	2024-01-07 18:00:00
	12055122	JALEN JOHNSON - UNDER/OVER PLAYER ASSISTS AND REBOUNDS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1091	2024-01-07 18:00:00
	12055133	NICKEIL ALEXANDER-WALKER - UNDER/OVER PLAYER ASSISTS AND REBOUNDS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1091	2024-01-07 19:30:00
	12055133	KYLE ANDERSON - UNDER/OVER PLAYER ASSISTS AND REBOUNDS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1091	2024-01-07 19:30:00
	12055133	RUDY GOBERT - UNDER/OVER PLAYER ASSISTS AND REBOUNDS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1091	2024-01-07 19:30:00
	12055133	LUKA DONCIC - UNDER/OVER PLAYER ASSISTS AND REBOUNDS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1091	2024-01-07 19:30:00
	12055133	JADEN MCDANIELS - UNDER/OVER PLAYER ASSISTS AND REBOUNDS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1091	2024-01-07 19:30:00
	12055133	NAZ REID - UNDER/OVER PLAYER ASSISTS AND REBOUNDS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1091	2024-01-07 19:30:00
	12055133	KARL-ANTHONY TOWNS JR. - UNDER/OVER PLAYER ASSISTS AND REBOUNDS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1091	2024-01-07 19:30:00
	12055133	MIKE CONLEY JR. - UNDER/OVER PLAYER ASSISTS AND REBOUNDS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1091	2024-01-07 19:30:00
	12055133	ANTHONY EDWARDS - UNDER/OVER PLAYER ASSISTS AND REBOUNDS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1091	2024-01-07 19:30:00
	12055132	JA MORANT - UNDER/OVER PLAYER ASSISTS AND REBOUNDS (Phoenix Suns vs Memphis Grizzlies) (Phoenix Suns vs Memphis Grizzlies)	Player Prop	GAME - TOTAL	No	1091	2024-01-07 20:00:00
	12055132	DEVIN BOOKER - UNDER/OVER PLAYER ASSISTS AND REBOUNDS (Phoenix Suns vs Memphis Grizzlies) (Phoenix Suns vs Memphis Grizzlies)	Player Prop	GAME - TOTAL	No	1091	2024-01-07 20:00:00
	12055141	AARON GORDON - UNDER/OVER PLAYER ASSISTS AND REBOUNDS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1091	2024-01-07 20:00:00
	12055141	MICHAEL PORTER JR. - UNDER/OVER PLAYER ASSISTS AND REBOUNDS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1091	2024-01-07 20:00:00
	12055141	NIKOLA JOKIC - UNDER/OVER PLAYER ASSISTS AND REBOUNDS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1091	2024-01-07 20:00:00
	12055141	CALDWELL POPE KENTAVIOUS - UNDER/OVER PLAYER ASSISTS AND REBOUNDS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1091	2024-01-07 20:00:00
	12055141	CADE CUNNINGHAM - UNDER/OVER PLAYER ASSISTS AND REBOUNDS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1091	2024-01-07 20:00:00
	12055141	BOJAN BOGDANOVIC - UNDER/OVER PLAYER ASSISTS AND REBOUNDS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1091	2024-01-07 20:00:00
	12055141	JALEN DUREN - UNDER/OVER PLAYER ASSISTS AND REBOUNDS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1091	2024-01-07 20:00:00
	12055141	JAMAL MURRAY - UNDER/OVER PLAYER ASSISTS AND REBOUNDS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1091	2024-01-07 20:00:00
	12055140	STEPHEN CURRY - UNDER/OVER PLAYER ASSISTS AND REBOUNDS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1091	2024-01-07 20:30:00
	12055140	IMMANUEL QUICKLEY - UNDER/OVER PLAYER ASSISTS AND REBOUNDS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1091	2024-01-07 20:30:00
	12055140	SCOTTIE BARNES - UNDER/OVER PLAYER ASSISTS AND REBOUNDS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1091	2024-01-07 20:30:00
	12055140	RJ BARRETT JR. - UNDER/OVER PLAYER ASSISTS AND REBOUNDS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1091	2024-01-07 20:30:00
	12055140	JONATHAN KUMINGA - UNDER/OVER PLAYER ASSISTS AND REBOUNDS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1091	2024-01-07 20:30:00
	12055140	PASCAL SIAKAM - UNDER/OVER PLAYER ASSISTS AND REBOUNDS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1091	2024-01-07 20:30:00
	12055140	JAKOB POELTL - UNDER/OVER PLAYER ASSISTS AND REBOUNDS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1091	2024-01-07 20:30:00
	12055140	KLAY THOMPSON - UNDER/OVER PLAYER ASSISTS AND REBOUNDS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1091	2024-01-07 20:30:00
	12055140	BRANDIN PODZIEMSKI - UNDER/OVER PLAYER ASSISTS AND REBOUNDS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1091	2024-01-07 20:30:00
	12055115	JAMES HARDEN - UNDER/OVER PLAYER ASSISTS AND REBOUNDS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1091	2024-01-07 21:30:00
	12055115	TAUREAN PRINCE - UNDER/OVER PLAYER ASSISTS AND REBOUNDS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1091	2024-01-07 21:30:00
	12055115	PAUL GEORGE - UNDER/OVER PLAYER ASSISTS AND REBOUNDS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1091	2024-01-07 21:30:00
	12055115	IVICA ZUBAC - UNDER/OVER PLAYER ASSISTS AND REBOUNDS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1091	2024-01-07 21:30:00
	12055115	ANTHONY DAVIS JR. - UNDER/OVER PLAYER ASSISTS AND REBOUNDS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1091	2024-01-07 21:30:00
	12055115	TERANCE MANN - UNDER/OVER PLAYER ASSISTS AND REBOUNDS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1091	2024-01-07 21:30:00
	12055115	KAWHI LEONARD - UNDER/OVER PLAYER ASSISTS AND REBOUNDS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1091	2024-01-07 21:30:00
	12055115	LEBRON JAMES - UNDER/OVER PLAYER ASSISTS AND REBOUNDS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1091	2024-01-07 21:30:00
	12055116	DEVIN VASSELL - UNDER/OVER PLAYER POINTS, ASSISTS AND REBOUNDS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1090	2024-01-07 13:00:00
	12055116	CARIS LEVERT - UNDER/OVER PLAYER POINTS, ASSISTS AND REBOUNDS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1090	2024-01-07 13:00:00
	12055116	JULIAN CHAMPAGNIE - UNDER/OVER PLAYER POINTS, ASSISTS AND REBOUNDS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1090	2024-01-07 13:00:00
	12055116	DEAN WADE - UNDER/OVER PLAYER POINTS, ASSISTS AND REBOUNDS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1090	2024-01-07 13:00:00
	12055116	ISAAC OKORO - UNDER/OVER PLAYER POINTS, ASSISTS AND REBOUNDS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1090	2024-01-07 13:00:00
	12055116	DONOVAN MITCHELL - UNDER/OVER PLAYER POINTS, ASSISTS AND REBOUNDS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1090	2024-01-07 13:00:00
	12055116	MALAKI BRANHAM - UNDER/OVER PLAYER POINTS, ASSISTS AND REBOUNDS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1090	2024-01-07 13:00:00
	12055116	KELDON JOHNSON - UNDER/OVER PLAYER POINTS, ASSISTS AND REBOUNDS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1090	2024-01-07 13:00:00
	12055116	JEREMY SOCHAN - UNDER/OVER PLAYER POINTS, ASSISTS AND REBOUNDS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1090	2024-01-07 13:00:00
	12055116	MAX STRUS - UNDER/OVER PLAYER POINTS, ASSISTS AND REBOUNDS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1090	2024-01-07 13:00:00
	12055116	SAM MERRILL - UNDER/OVER PLAYER POINTS, ASSISTS AND REBOUNDS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1090	2024-01-07 13:00:00
	12055116	JARRETT ALLEN - UNDER/OVER PLAYER POINTS, ASSISTS AND REBOUNDS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1090	2024-01-07 13:00:00
	12055116	WEMBANYAMA VICTOR - UNDER/OVER PLAYER POINTS, ASSISTS AND REBOUNDS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1090	2024-01-07 13:00:00
	12055116	TRE JONES - UNDER/OVER PLAYER POINTS, ASSISTS AND REBOUNDS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1090	2024-01-07 13:00:00
	12055116	GEORGES NIANG - UNDER/OVER PLAYER POINTS, ASSISTS AND REBOUNDS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1090	2024-01-07 13:00:00
	12055117	ROYCE O'NEALE - UNDER/OVER PLAYER POINTS, ASSISTS AND REBOUNDS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1090	2024-01-07 15:00:00
	12055117	DAY'RON SHARPE - UNDER/OVER PLAYER POINTS, ASSISTS AND REBOUNDS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1090	2024-01-07 15:00:00
	12055117	ANFERNEE SIMONS - UNDER/OVER PLAYER POINTS, ASSISTS AND REBOUNDS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1090	2024-01-07 15:00:00
	12055117	CAMERON JOHNSON - UNDER/OVER PLAYER POINTS, ASSISTS AND REBOUNDS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1090	2024-01-07 15:00:00
	12055117	MIKAL BRIDGES - UNDER/OVER PLAYER POINTS, ASSISTS AND REBOUNDS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1090	2024-01-07 15:00:00
	12055117	DENNIS SMITH JR. - UNDER/OVER PLAYER POINTS, ASSISTS AND REBOUNDS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1090	2024-01-07 15:00:00
	12055117	CAMERON THOMAS - UNDER/OVER PLAYER POINTS, ASSISTS AND REBOUNDS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1090	2024-01-07 15:00:00
	12055117	NICOLAS CLAXTON - UNDER/OVER PLAYER POINTS, ASSISTS AND REBOUNDS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1090	2024-01-07 15:00:00
	12055117	DORIAN FINNEY SMITH - UNDER/OVER PLAYER POINTS, ASSISTS AND REBOUNDS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1090	2024-01-07 15:00:00
	12055117	GRANT JERAMI - UNDER/OVER PLAYER POINTS, ASSISTS AND REBOUNDS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1090	2024-01-07 15:00:00
	12055117	SPENCER DINWIDDIE - UNDER/OVER PLAYER POINTS, ASSISTS AND REBOUNDS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1090	2024-01-07 15:00:00
	12055121	CHRISTIAN JAMES MCCOLLUM - UNDER/OVER PLAYER POINTS, ASSISTS AND REBOUNDS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1090	2024-01-07 18:00:00
	12055121	DE'AARON FOX - UNDER/OVER PLAYER POINTS, ASSISTS AND REBOUNDS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1090	2024-01-07 18:00:00
	12055121	MALIK MONK - UNDER/OVER PLAYER POINTS, ASSISTS AND REBOUNDS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1090	2024-01-07 18:00:00
	12055121	DOMANTAS SABONIS - UNDER/OVER PLAYER POINTS, ASSISTS AND REBOUNDS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1090	2024-01-07 18:00:00
	12055121	ZION WILLIAMSON - UNDER/OVER PLAYER POINTS, ASSISTS AND REBOUNDS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1090	2024-01-07 18:00:00
	12055121	HERBERT JONES - UNDER/OVER PLAYER POINTS, ASSISTS AND REBOUNDS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1090	2024-01-07 18:00:00
	12055121	BRANDON INGRAM - UNDER/OVER PLAYER POINTS, ASSISTS AND REBOUNDS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1090	2024-01-07 18:00:00
	12055121	KEEGAN MURRAY - UNDER/OVER PLAYER POINTS, ASSISTS AND REBOUNDS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1090	2024-01-07 18:00:00
	12055121	HARRISON BARNES - UNDER/OVER PLAYER POINTS, ASSISTS AND REBOUNDS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1090	2024-01-07 18:00:00
	12055122	BOGDAN BOGDANOVIC - UNDER/OVER PLAYER POINTS, ASSISTS AND REBOUNDS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1090	2024-01-07 18:00:00
	12055122	CLINT CAPELA - UNDER/OVER PLAYER POINTS, ASSISTS AND REBOUNDS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1090	2024-01-07 18:00:00
	12055122	TRAE YOUNG - UNDER/OVER PLAYER POINTS, ASSISTS AND REBOUNDS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1090	2024-01-07 18:00:00
	12055122	JALEN JOHNSON - UNDER/OVER PLAYER POINTS, ASSISTS AND REBOUNDS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1090	2024-01-07 18:00:00
	12055122	ONYEKA OKONGWU - UNDER/OVER PLAYER POINTS, ASSISTS AND REBOUNDS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1090	2024-01-07 18:00:00
	12055122	JALEN SUGGS - UNDER/OVER PLAYER POINTS, ASSISTS AND REBOUNDS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1090	2024-01-07 18:00:00
	12055122	SADDIQ BEY - UNDER/OVER PLAYER POINTS, ASSISTS AND REBOUNDS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1090	2024-01-07 18:00:00
	12055122	MURRAY DEJOUNTE - UNDER/OVER PLAYER POINTS, ASSISTS AND REBOUNDS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1090	2024-01-07 18:00:00
	12055122	PAOLO BANCHERO - UNDER/OVER PLAYER POINTS, ASSISTS AND REBOUNDS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1090	2024-01-07 18:00:00
	12055133	RUDY GOBERT - UNDER/OVER PLAYER POINTS, ASSISTS AND REBOUNDS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1090	2024-01-07 19:30:00
	12055133	KYLE ANDERSON - UNDER/OVER PLAYER POINTS, ASSISTS AND REBOUNDS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1090	2024-01-07 19:30:00
	12055133	NAZ REID - UNDER/OVER PLAYER POINTS, ASSISTS AND REBOUNDS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1090	2024-01-07 19:30:00
	12055133	ANTHONY EDWARDS - UNDER/OVER PLAYER POINTS, ASSISTS AND REBOUNDS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1090	2024-01-07 19:30:00
	12055133	LUKA DONCIC - UNDER/OVER PLAYER POINTS, ASSISTS AND REBOUNDS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1090	2024-01-07 19:30:00
	12055133	NICKEIL ALEXANDER-WALKER - UNDER/OVER PLAYER POINTS, ASSISTS AND REBOUNDS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1090	2024-01-07 19:30:00
	12055133	MIKE CONLEY JR. - UNDER/OVER PLAYER POINTS, ASSISTS AND REBOUNDS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1090	2024-01-07 19:30:00
	12055133	KARL-ANTHONY TOWNS JR. - UNDER/OVER PLAYER POINTS, ASSISTS AND REBOUNDS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1090	2024-01-07 19:30:00
	12055133	JADEN MCDANIELS - UNDER/OVER PLAYER POINTS, ASSISTS AND REBOUNDS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1090	2024-01-07 19:30:00
	12055132	DEVIN BOOKER - UNDER/OVER PLAYER POINTS, ASSISTS AND REBOUNDS (Phoenix Suns vs Memphis Grizzlies) (Phoenix Suns vs Memphis Grizzlies)	Player Prop	GAME - TOTAL	No	1090	2024-01-07 20:00:00
	12055132	JA MORANT - UNDER/OVER PLAYER POINTS, ASSISTS AND REBOUNDS (Phoenix Suns vs Memphis Grizzlies) (Phoenix Suns vs Memphis Grizzlies)	Player Prop	GAME - TOTAL	No	1090	2024-01-07 20:00:00
	12055141	MICHAEL PORTER JR. - UNDER/OVER PLAYER POINTS, ASSISTS AND REBOUNDS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1090	2024-01-07 20:00:00
	12055141	BOJAN BOGDANOVIC - UNDER/OVER PLAYER POINTS, ASSISTS AND REBOUNDS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1090	2024-01-07 20:00:00
	12055141	AARON GORDON - UNDER/OVER PLAYER POINTS, ASSISTS AND REBOUNDS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1090	2024-01-07 20:00:00
	12055141	CALDWELL POPE KENTAVIOUS - UNDER/OVER PLAYER POINTS, ASSISTS AND REBOUNDS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1090	2024-01-07 20:00:00
	12055141	JALEN DUREN - UNDER/OVER PLAYER POINTS, ASSISTS AND REBOUNDS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1090	2024-01-07 20:00:00
	12055141	JAMAL MURRAY - UNDER/OVER PLAYER POINTS, ASSISTS AND REBOUNDS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1090	2024-01-07 20:00:00
	12055141	NIKOLA JOKIC - UNDER/OVER PLAYER POINTS, ASSISTS AND REBOUNDS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1090	2024-01-07 20:00:00
	12055141	CADE CUNNINGHAM - UNDER/OVER PLAYER POINTS, ASSISTS AND REBOUNDS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1090	2024-01-07 20:00:00
	12055140	BRANDIN PODZIEMSKI - UNDER/OVER PLAYER POINTS, ASSISTS AND REBOUNDS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1090	2024-01-07 20:30:00
	12055140	IMMANUEL QUICKLEY - UNDER/OVER PLAYER POINTS, ASSISTS AND REBOUNDS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1090	2024-01-07 20:30:00
	12055140	JAKOB POELTL - UNDER/OVER PLAYER POINTS, ASSISTS AND REBOUNDS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1090	2024-01-07 20:30:00
	12055140	SCOTTIE BARNES - UNDER/OVER PLAYER POINTS, ASSISTS AND REBOUNDS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1090	2024-01-07 20:30:00
	12055140	PASCAL SIAKAM - UNDER/OVER PLAYER POINTS, ASSISTS AND REBOUNDS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1090	2024-01-07 20:30:00
	12055140	STEPHEN CURRY - UNDER/OVER PLAYER POINTS, ASSISTS AND REBOUNDS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1090	2024-01-07 20:30:00
	12055140	JONATHAN KUMINGA - UNDER/OVER PLAYER POINTS, ASSISTS AND REBOUNDS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1090	2024-01-07 20:30:00
	12055140	KLAY THOMPSON - UNDER/OVER PLAYER POINTS, ASSISTS AND REBOUNDS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1090	2024-01-07 20:30:00
	12055140	RJ BARRETT JR. - UNDER/OVER PLAYER POINTS, ASSISTS AND REBOUNDS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1090	2024-01-07 20:30:00
	12055115	TERANCE MANN - UNDER/OVER PLAYER POINTS, ASSISTS AND REBOUNDS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1090	2024-01-07 21:30:00
	12055115	JAMES HARDEN - UNDER/OVER PLAYER POINTS, ASSISTS AND REBOUNDS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1090	2024-01-07 21:30:00
	12055115	TAUREAN PRINCE - UNDER/OVER PLAYER POINTS, ASSISTS AND REBOUNDS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1090	2024-01-07 21:30:00
	12055115	IVICA ZUBAC - UNDER/OVER PLAYER POINTS, ASSISTS AND REBOUNDS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1090	2024-01-07 21:30:00
	12055115	LEBRON JAMES - UNDER/OVER PLAYER POINTS, ASSISTS AND REBOUNDS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1090	2024-01-07 21:30:00
	12055115	KAWHI LEONARD - UNDER/OVER PLAYER POINTS, ASSISTS AND REBOUNDS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1090	2024-01-07 21:30:00
	12055115	ANTHONY DAVIS JR. - UNDER/OVER PLAYER POINTS, ASSISTS AND REBOUNDS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1090	2024-01-07 21:30:00
	12055115	PAUL GEORGE - UNDER/OVER PLAYER POINTS, ASSISTS AND REBOUNDS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1090	2024-01-07 21:30:00
	12055116	DONOVAN MITCHELL - UNDER/OVER PLAYER STEALS AND BLOCKS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1089	2024-01-07 13:00:00
	12055116	TRE JONES - UNDER/OVER PLAYER STEALS AND BLOCKS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1089	2024-01-07 13:00:00
	12055116	MAX STRUS - UNDER/OVER PLAYER STEALS AND BLOCKS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1089	2024-01-07 13:00:00
	12055116	MALAKI BRANHAM - UNDER/OVER PLAYER STEALS AND BLOCKS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1089	2024-01-07 13:00:00
	12055116	JARRETT ALLEN - UNDER/OVER PLAYER STEALS AND BLOCKS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1089	2024-01-07 13:00:00
	12055116	ISAAC OKORO - UNDER/OVER PLAYER STEALS AND BLOCKS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1089	2024-01-07 13:00:00
	12055116	DEAN WADE - UNDER/OVER PLAYER STEALS AND BLOCKS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1089	2024-01-07 13:00:00
	12055116	GEORGES NIANG - UNDER/OVER PLAYER STEALS AND BLOCKS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1089	2024-01-07 13:00:00
	12055116	WEMBANYAMA VICTOR - UNDER/OVER PLAYER STEALS AND BLOCKS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1089	2024-01-07 13:00:00
	12055116	SAM MERRILL - UNDER/OVER PLAYER STEALS AND BLOCKS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1089	2024-01-07 13:00:00
	12055116	DEVIN VASSELL - UNDER/OVER PLAYER STEALS AND BLOCKS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1089	2024-01-07 13:00:00
	12055116	CARIS LEVERT - UNDER/OVER PLAYER STEALS AND BLOCKS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1089	2024-01-07 13:00:00
	12055116	JULIAN CHAMPAGNIE - UNDER/OVER PLAYER STEALS AND BLOCKS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1089	2024-01-07 13:00:00
	12055116	JEREMY SOCHAN - UNDER/OVER PLAYER STEALS AND BLOCKS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1089	2024-01-07 13:00:00
	12055116	KELDON JOHNSON - UNDER/OVER PLAYER STEALS AND BLOCKS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1089	2024-01-07 13:00:00
	12055117	CAMERON JOHNSON - UNDER/OVER PLAYER STEALS AND BLOCKS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1089	2024-01-07 15:00:00
	12055117	DENNIS SMITH JR. - UNDER/OVER PLAYER STEALS AND BLOCKS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1089	2024-01-07 15:00:00
	12055117	NICOLAS CLAXTON - UNDER/OVER PLAYER STEALS AND BLOCKS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1089	2024-01-07 15:00:00
	12055117	CAMERON THOMAS - UNDER/OVER PLAYER STEALS AND BLOCKS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1089	2024-01-07 15:00:00
	12055117	ANFERNEE SIMONS - UNDER/OVER PLAYER STEALS AND BLOCKS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1089	2024-01-07 15:00:00
	12055117	GRANT JERAMI - UNDER/OVER PLAYER STEALS AND BLOCKS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1089	2024-01-07 15:00:00
	12055117	MIKAL BRIDGES - UNDER/OVER PLAYER STEALS AND BLOCKS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1089	2024-01-07 15:00:00
	12055117	ROYCE O'NEALE - UNDER/OVER PLAYER STEALS AND BLOCKS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1089	2024-01-07 15:00:00
	12055117	DORIAN FINNEY SMITH - UNDER/OVER PLAYER STEALS AND BLOCKS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1089	2024-01-07 15:00:00
	12055117	DAY'RON SHARPE - UNDER/OVER PLAYER STEALS AND BLOCKS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1089	2024-01-07 15:00:00
	12055117	SPENCER DINWIDDIE - UNDER/OVER PLAYER STEALS AND BLOCKS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1089	2024-01-07 15:00:00
	12055121	DOMANTAS SABONIS - UNDER/OVER PLAYER STEALS AND BLOCKS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1089	2024-01-07 18:00:00
	12055121	HARRISON BARNES - UNDER/OVER PLAYER STEALS AND BLOCKS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1089	2024-01-07 18:00:00
	12055121	MALIK MONK - UNDER/OVER PLAYER STEALS AND BLOCKS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1089	2024-01-07 18:00:00
	12055121	CHRISTIAN JAMES MCCOLLUM - UNDER/OVER PLAYER STEALS AND BLOCKS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1089	2024-01-07 18:00:00
	12055121	ZION WILLIAMSON - UNDER/OVER PLAYER STEALS AND BLOCKS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1089	2024-01-07 18:00:00
	12055121	HERBERT JONES - UNDER/OVER PLAYER STEALS AND BLOCKS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1089	2024-01-07 18:00:00
	12055121	KEEGAN MURRAY - UNDER/OVER PLAYER STEALS AND BLOCKS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1089	2024-01-07 18:00:00
	12055121	BRANDON INGRAM - UNDER/OVER PLAYER STEALS AND BLOCKS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1089	2024-01-07 18:00:00
	12055121	DE'AARON FOX - UNDER/OVER PLAYER STEALS AND BLOCKS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1089	2024-01-07 18:00:00
	12055122	ONYEKA OKONGWU - UNDER/OVER PLAYER STEALS AND BLOCKS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1089	2024-01-07 18:00:00
	12055122	MURRAY DEJOUNTE - UNDER/OVER PLAYER STEALS AND BLOCKS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1089	2024-01-07 18:00:00
	12055122	JALEN JOHNSON - UNDER/OVER PLAYER STEALS AND BLOCKS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1089	2024-01-07 18:00:00
	12055122	BOGDAN BOGDANOVIC - UNDER/OVER PLAYER STEALS AND BLOCKS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1089	2024-01-07 18:00:00
	12055122	CLINT CAPELA - UNDER/OVER PLAYER STEALS AND BLOCKS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1089	2024-01-07 18:00:00
	12055122	SADDIQ BEY - UNDER/OVER PLAYER STEALS AND BLOCKS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1089	2024-01-07 18:00:00
	12055122	TRAE YOUNG - UNDER/OVER PLAYER STEALS AND BLOCKS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1089	2024-01-07 18:00:00
	12055122	JALEN SUGGS - UNDER/OVER PLAYER STEALS AND BLOCKS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1089	2024-01-07 18:00:00
	12055122	PAOLO BANCHERO - UNDER/OVER PLAYER STEALS AND BLOCKS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1089	2024-01-07 18:00:00
	12055133	RUDY GOBERT - UNDER/OVER PLAYER STEALS AND BLOCKS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1089	2024-01-07 19:30:00
	12055133	NAZ REID - UNDER/OVER PLAYER STEALS AND BLOCKS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1089	2024-01-07 19:30:00
	12055133	JADEN MCDANIELS - UNDER/OVER PLAYER STEALS AND BLOCKS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1089	2024-01-07 19:30:00
	12055133	KYLE ANDERSON - UNDER/OVER PLAYER STEALS AND BLOCKS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1089	2024-01-07 19:30:00
	12055133	NICKEIL ALEXANDER-WALKER - UNDER/OVER PLAYER STEALS AND BLOCKS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1089	2024-01-07 19:30:00
	12055133	MIKE CONLEY JR. - UNDER/OVER PLAYER STEALS AND BLOCKS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1089	2024-01-07 19:30:00
	12055133	LUKA DONCIC - UNDER/OVER PLAYER STEALS AND BLOCKS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1089	2024-01-07 19:30:00
	12055133	KARL-ANTHONY TOWNS JR. - UNDER/OVER PLAYER STEALS AND BLOCKS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1089	2024-01-07 19:30:00
	12055133	ANTHONY EDWARDS - UNDER/OVER PLAYER STEALS AND BLOCKS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1089	2024-01-07 19:30:00
	12055132	JA MORANT - UNDER/OVER PLAYER STEALS AND BLOCKS (Phoenix Suns vs Memphis Grizzlies) (Phoenix Suns vs Memphis Grizzlies)	Player Prop	GAME - TOTAL	No	1089	2024-01-07 20:00:00
	12055132	DEVIN BOOKER - UNDER/OVER PLAYER STEALS AND BLOCKS (Phoenix Suns vs Memphis Grizzlies) (Phoenix Suns vs Memphis Grizzlies)	Player Prop	GAME - TOTAL	No	1089	2024-01-07 20:00:00
	12055141	CALDWELL POPE KENTAVIOUS - UNDER/OVER PLAYER STEALS AND BLOCKS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1089	2024-01-07 20:00:00
	12055141	CADE CUNNINGHAM - UNDER/OVER PLAYER STEALS AND BLOCKS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1089	2024-01-07 20:00:00
	12055141	NIKOLA JOKIC - UNDER/OVER PLAYER STEALS AND BLOCKS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1089	2024-01-07 20:00:00
	12055141	AARON GORDON - UNDER/OVER PLAYER STEALS AND BLOCKS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1089	2024-01-07 20:00:00
	12055141	MICHAEL PORTER JR. - UNDER/OVER PLAYER STEALS AND BLOCKS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1089	2024-01-07 20:00:00
	12055141	BOJAN BOGDANOVIC - UNDER/OVER PLAYER STEALS AND BLOCKS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1089	2024-01-07 20:00:00
	12055141	JAMAL MURRAY - UNDER/OVER PLAYER STEALS AND BLOCKS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1089	2024-01-07 20:00:00
	12055141	JALEN DUREN - UNDER/OVER PLAYER STEALS AND BLOCKS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1089	2024-01-07 20:00:00
	12055140	JAKOB POELTL - UNDER/OVER PLAYER STEALS AND BLOCKS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1089	2024-01-07 20:30:00
	12055140	STEPHEN CURRY - UNDER/OVER PLAYER STEALS AND BLOCKS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1089	2024-01-07 20:30:00
	12055140	BRANDIN PODZIEMSKI - UNDER/OVER PLAYER STEALS AND BLOCKS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1089	2024-01-07 20:30:00
	12055140	IMMANUEL QUICKLEY - UNDER/OVER PLAYER STEALS AND BLOCKS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1089	2024-01-07 20:30:00
	12055140	KLAY THOMPSON - UNDER/OVER PLAYER STEALS AND BLOCKS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1089	2024-01-07 20:30:00
	12055140	PASCAL SIAKAM - UNDER/OVER PLAYER STEALS AND BLOCKS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1089	2024-01-07 20:30:00
	12055140	RJ BARRETT JR. - UNDER/OVER PLAYER STEALS AND BLOCKS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1089	2024-01-07 20:30:00
	12055140	SCOTTIE BARNES - UNDER/OVER PLAYER STEALS AND BLOCKS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1089	2024-01-07 20:30:00
	12055140	JONATHAN KUMINGA - UNDER/OVER PLAYER STEALS AND BLOCKS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1089	2024-01-07 20:30:00
	12055115	TAUREAN PRINCE - UNDER/OVER PLAYER STEALS AND BLOCKS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1089	2024-01-07 21:30:00
	12055115	IVICA ZUBAC - UNDER/OVER PLAYER STEALS AND BLOCKS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1089	2024-01-07 21:30:00
	12055115	KAWHI LEONARD - UNDER/OVER PLAYER STEALS AND BLOCKS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1089	2024-01-07 21:30:00
	12055115	ANTHONY DAVIS JR. - UNDER/OVER PLAYER STEALS AND BLOCKS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1089	2024-01-07 21:30:00
	12055115	PAUL GEORGE - UNDER/OVER PLAYER STEALS AND BLOCKS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1089	2024-01-07 21:30:00
	12055115	JAMES HARDEN - UNDER/OVER PLAYER STEALS AND BLOCKS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1089	2024-01-07 21:30:00
	12055115	LEBRON JAMES - UNDER/OVER PLAYER STEALS AND BLOCKS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1089	2024-01-07 21:30:00
	12055115	TERANCE MANN - UNDER/OVER PLAYER STEALS AND BLOCKS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1089	2024-01-07 21:30:00
	12055116	DONOVAN MITCHELL - UNDER/OVER PLAYER 3 POINTS MADE (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1075	2024-01-07 13:00:00
	12055116	JEREMY SOCHAN - UNDER/OVER PLAYER 3 POINTS MADE (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1075	2024-01-07 13:00:00
	12055116	GEORGES NIANG - UNDER/OVER PLAYER 3 POINTS MADE (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1075	2024-01-07 13:00:00
	12055116	KELDON JOHNSON - UNDER/OVER PLAYER 3 POINTS MADE (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1075	2024-01-07 13:00:00
	12055116	MAX STRUS - UNDER/OVER PLAYER 3 POINTS MADE (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1075	2024-01-07 13:00:00
	12055116	DEAN WADE - UNDER/OVER PLAYER 3 POINTS MADE (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1075	2024-01-07 13:00:00
	12055116	TRE JONES - UNDER/OVER PLAYER 3 POINTS MADE (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1075	2024-01-07 13:00:00
	12055116	CARIS LEVERT - UNDER/OVER PLAYER 3 POINTS MADE (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1075	2024-01-07 13:00:00
	12055116	WEMBANYAMA VICTOR - UNDER/OVER PLAYER 3 POINTS MADE (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1075	2024-01-07 13:00:00
	12055116	DEVIN VASSELL - UNDER/OVER PLAYER 3 POINTS MADE (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1075	2024-01-07 13:00:00
	12055116	SAM MERRILL - UNDER/OVER PLAYER 3 POINTS MADE (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1075	2024-01-07 13:00:00
	12055116	ISAAC OKORO - UNDER/OVER PLAYER 3 POINTS MADE (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1075	2024-01-07 13:00:00
	12055117	ANFERNEE SIMONS - UNDER/OVER PLAYER 3 POINTS MADE (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1075	2024-01-07 15:00:00
	12055117	DENNIS SMITH JR. - UNDER/OVER PLAYER 3 POINTS MADE (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1075	2024-01-07 15:00:00
	12055117	MIKAL BRIDGES - UNDER/OVER PLAYER 3 POINTS MADE (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1075	2024-01-07 15:00:00
	12055117	DORIAN FINNEY SMITH - UNDER/OVER PLAYER 3 POINTS MADE (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1075	2024-01-07 15:00:00
	12055117	CAMERON JOHNSON - UNDER/OVER PLAYER 3 POINTS MADE (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1075	2024-01-07 15:00:00
	12055117	CAMERON THOMAS - UNDER/OVER PLAYER 3 POINTS MADE (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1075	2024-01-07 15:00:00
	12055117	SPENCER DINWIDDIE - UNDER/OVER PLAYER 3 POINTS MADE (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1075	2024-01-07 15:00:00
	12055117	GRANT JERAMI - UNDER/OVER PLAYER 3 POINTS MADE (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1075	2024-01-07 15:00:00
	12055117	ROYCE O'NEALE - UNDER/OVER PLAYER 3 POINTS MADE (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1075	2024-01-07 15:00:00
	12055121	DE'AARON FOX - UNDER/OVER PLAYER 3 POINTS MADE (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1075	2024-01-07 18:00:00
	12055121	CHRISTIAN JAMES MCCOLLUM - UNDER/OVER PLAYER 3 POINTS MADE (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1075	2024-01-07 18:00:00
	12055121	HARRISON BARNES - UNDER/OVER PLAYER 3 POINTS MADE (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1075	2024-01-07 18:00:00
	12055121	DOMANTAS SABONIS - UNDER/OVER PLAYER 3 POINTS MADE (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1075	2024-01-07 18:00:00
	12055121	KEEGAN MURRAY - UNDER/OVER PLAYER 3 POINTS MADE (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1075	2024-01-07 18:00:00
	12055121	HERBERT JONES - UNDER/OVER PLAYER 3 POINTS MADE (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1075	2024-01-07 18:00:00
	12055121	MALIK MONK - UNDER/OVER PLAYER 3 POINTS MADE (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1075	2024-01-07 18:00:00
	12055121	BRANDON INGRAM - UNDER/OVER PLAYER 3 POINTS MADE (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1075	2024-01-07 18:00:00
	12055122	PAOLO BANCHERO - UNDER/OVER PLAYER 3 POINTS MADE (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1075	2024-01-07 18:00:00
	12055122	JALEN SUGGS - UNDER/OVER PLAYER 3 POINTS MADE (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1075	2024-01-07 18:00:00
	12055122	JALEN JOHNSON - UNDER/OVER PLAYER 3 POINTS MADE (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1075	2024-01-07 18:00:00
	12055122	SADDIQ BEY - UNDER/OVER PLAYER 3 POINTS MADE (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1075	2024-01-07 18:00:00
	12055122	BOGDAN BOGDANOVIC - UNDER/OVER PLAYER 3 POINTS MADE (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1075	2024-01-07 18:00:00
	12055122	MURRAY DEJOUNTE - UNDER/OVER PLAYER 3 POINTS MADE (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1075	2024-01-07 18:00:00
	12055122	TRAE YOUNG - UNDER/OVER PLAYER 3 POINTS MADE (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1075	2024-01-07 18:00:00
	12055133	MIKE CONLEY JR. - UNDER/OVER PLAYER 3 POINTS MADE (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1075	2024-01-07 19:30:00
	12055133	NICKEIL ALEXANDER-WALKER - UNDER/OVER PLAYER 3 POINTS MADE (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1075	2024-01-07 19:30:00
	12055133	LUKA DONCIC - UNDER/OVER PLAYER 3 POINTS MADE (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1075	2024-01-07 19:30:00
	12055133	JADEN MCDANIELS - UNDER/OVER PLAYER 3 POINTS MADE (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1075	2024-01-07 19:30:00
	12055133	NAZ REID - UNDER/OVER PLAYER 3 POINTS MADE (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1075	2024-01-07 19:30:00
	12055133	KARL-ANTHONY TOWNS JR. - UNDER/OVER PLAYER 3 POINTS MADE (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1075	2024-01-07 19:30:00
	12055133	ANTHONY EDWARDS - UNDER/OVER PLAYER 3 POINTS MADE (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1075	2024-01-07 19:30:00
	12055132	DEVIN BOOKER - UNDER/OVER PLAYER 3 POINTS MADE (Phoenix Suns vs Memphis Grizzlies) (Phoenix Suns vs Memphis Grizzlies)	Player Prop	GAME - TOTAL	No	1075	2024-01-07 20:00:00
	12055132	JA MORANT - UNDER/OVER PLAYER 3 POINTS MADE (Phoenix Suns vs Memphis Grizzlies) (Phoenix Suns vs Memphis Grizzlies)	Player Prop	GAME - TOTAL	No	1075	2024-01-07 20:00:00
	12055141	CADE CUNNINGHAM - UNDER/OVER PLAYER 3 POINTS MADE (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1075	2024-01-07 20:00:00
	12055141	BOJAN BOGDANOVIC - UNDER/OVER PLAYER 3 POINTS MADE (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1075	2024-01-07 20:00:00
	12055141	MICHAEL PORTER JR. - UNDER/OVER PLAYER 3 POINTS MADE (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1075	2024-01-07 20:00:00
	12055141	JAMAL MURRAY - UNDER/OVER PLAYER 3 POINTS MADE (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1075	2024-01-07 20:00:00
	12055141	AARON GORDON - UNDER/OVER PLAYER 3 POINTS MADE (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1075	2024-01-07 20:00:00
	12055141	NIKOLA JOKIC - UNDER/OVER PLAYER 3 POINTS MADE (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1075	2024-01-07 20:00:00
	12055141	CALDWELL POPE KENTAVIOUS - UNDER/OVER PLAYER 3 POINTS MADE (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1075	2024-01-07 20:00:00
	12055140	STEPHEN CURRY - UNDER/OVER PLAYER 3 POINTS MADE (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1075	2024-01-07 20:30:00
	12055140	JONATHAN KUMINGA - UNDER/OVER PLAYER 3 POINTS MADE (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1075	2024-01-07 20:30:00
	12055140	KLAY THOMPSON - UNDER/OVER PLAYER 3 POINTS MADE (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1075	2024-01-07 20:30:00
	12055140	IMMANUEL QUICKLEY - UNDER/OVER PLAYER 3 POINTS MADE (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1075	2024-01-07 20:30:00
	12055140	BRANDIN PODZIEMSKI - UNDER/OVER PLAYER 3 POINTS MADE (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1075	2024-01-07 20:30:00
	12055140	RJ BARRETT JR. - UNDER/OVER PLAYER 3 POINTS MADE (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1075	2024-01-07 20:30:00
	12055140	SCOTTIE BARNES - UNDER/OVER PLAYER 3 POINTS MADE (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1075	2024-01-07 20:30:00
	12055140	PASCAL SIAKAM - UNDER/OVER PLAYER 3 POINTS MADE (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1075	2024-01-07 20:30:00
	12055115	ANTHONY DAVIS JR. - UNDER/OVER PLAYER 3 POINTS MADE (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1075	2024-01-07 21:30:00
	12055115	JAMES HARDEN - UNDER/OVER PLAYER 3 POINTS MADE (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1075	2024-01-07 21:30:00
	12055115	KAWHI LEONARD - UNDER/OVER PLAYER 3 POINTS MADE (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1075	2024-01-07 21:30:00
	12055115	LEBRON JAMES - UNDER/OVER PLAYER 3 POINTS MADE (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1075	2024-01-07 21:30:00
	12055115	TERANCE MANN - UNDER/OVER PLAYER 3 POINTS MADE (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1075	2024-01-07 21:30:00
	12055115	TAUREAN PRINCE - UNDER/OVER PLAYER 3 POINTS MADE (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1075	2024-01-07 21:30:00
	12055115	PAUL GEORGE - UNDER/OVER PLAYER 3 POINTS MADE (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1075	2024-01-07 21:30:00
	12055116	GEORGES NIANG - UNDER/OVER PLAYER TURNOVERS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1074	2024-01-07 13:00:00
	12055116	DONOVAN MITCHELL - UNDER/OVER PLAYER TURNOVERS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1074	2024-01-07 13:00:00
	12055116	SAM MERRILL - UNDER/OVER PLAYER TURNOVERS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1074	2024-01-07 13:00:00
	12055116	JEREMY SOCHAN - UNDER/OVER PLAYER TURNOVERS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1074	2024-01-07 13:00:00
	12055116	WEMBANYAMA VICTOR - UNDER/OVER PLAYER TURNOVERS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1074	2024-01-07 13:00:00
	12055116	KELDON JOHNSON - UNDER/OVER PLAYER TURNOVERS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1074	2024-01-07 13:00:00
	12055116	MAX STRUS - UNDER/OVER PLAYER TURNOVERS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1074	2024-01-07 13:00:00
	12055116	CARIS LEVERT - UNDER/OVER PLAYER TURNOVERS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1074	2024-01-07 13:00:00
	12055116	JARRETT ALLEN - UNDER/OVER PLAYER TURNOVERS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1074	2024-01-07 13:00:00
	12055116	DEAN WADE - UNDER/OVER PLAYER TURNOVERS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1074	2024-01-07 13:00:00
	12055116	ISAAC OKORO - UNDER/OVER PLAYER TURNOVERS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1074	2024-01-07 13:00:00
	12055116	DEVIN VASSELL - UNDER/OVER PLAYER TURNOVERS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1074	2024-01-07 13:00:00
	12055116	TRE JONES - UNDER/OVER PLAYER TURNOVERS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1074	2024-01-07 13:00:00
	12055116	JULIAN CHAMPAGNIE - UNDER/OVER PLAYER TURNOVERS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1074	2024-01-07 13:00:00
	12055117	GRANT JERAMI - UNDER/OVER PLAYER TURNOVERS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1074	2024-01-07 15:00:00
	12055117	DAY'RON SHARPE - UNDER/OVER PLAYER TURNOVERS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1074	2024-01-07 15:00:00
	12055117	CAMERON THOMAS - UNDER/OVER PLAYER TURNOVERS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1074	2024-01-07 15:00:00
	12055117	DENNIS SMITH JR. - UNDER/OVER PLAYER TURNOVERS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1074	2024-01-07 15:00:00
	12055117	CAMERON JOHNSON - UNDER/OVER PLAYER TURNOVERS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1074	2024-01-07 15:00:00
	12055117	NICOLAS CLAXTON - UNDER/OVER PLAYER TURNOVERS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1074	2024-01-07 15:00:00
	12055117	SPENCER DINWIDDIE - UNDER/OVER PLAYER TURNOVERS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1074	2024-01-07 15:00:00
	12055117	DORIAN FINNEY SMITH - UNDER/OVER PLAYER TURNOVERS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1074	2024-01-07 15:00:00
	12055117	MIKAL BRIDGES - UNDER/OVER PLAYER TURNOVERS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1074	2024-01-07 15:00:00
	12055117	ANFERNEE SIMONS - UNDER/OVER PLAYER TURNOVERS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1074	2024-01-07 15:00:00
	12055117	ROYCE O'NEALE - UNDER/OVER PLAYER TURNOVERS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1074	2024-01-07 15:00:00
	12055121	KEEGAN MURRAY - UNDER/OVER PLAYER TURNOVERS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1074	2024-01-07 18:00:00
	12055121	DE'AARON FOX - UNDER/OVER PLAYER TURNOVERS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1074	2024-01-07 18:00:00
	12055121	CHRISTIAN JAMES MCCOLLUM - UNDER/OVER PLAYER TURNOVERS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1074	2024-01-07 18:00:00
	12055121	ZION WILLIAMSON - UNDER/OVER PLAYER TURNOVERS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1074	2024-01-07 18:00:00
	12055121	MALIK MONK - UNDER/OVER PLAYER TURNOVERS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1074	2024-01-07 18:00:00
	12055121	HERBERT JONES - UNDER/OVER PLAYER TURNOVERS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1074	2024-01-07 18:00:00
	12055121	BRANDON INGRAM - UNDER/OVER PLAYER TURNOVERS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1074	2024-01-07 18:00:00
	12055121	DOMANTAS SABONIS - UNDER/OVER PLAYER TURNOVERS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1074	2024-01-07 18:00:00
	12055121	HARRISON BARNES - UNDER/OVER PLAYER TURNOVERS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1074	2024-01-07 18:00:00
	12055122	CLINT CAPELA - UNDER/OVER PLAYER TURNOVERS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1074	2024-01-07 18:00:00
	12055122	BOGDAN BOGDANOVIC - UNDER/OVER PLAYER TURNOVERS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1074	2024-01-07 18:00:00
	12055122	SADDIQ BEY - UNDER/OVER PLAYER TURNOVERS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1074	2024-01-07 18:00:00
	12055122	JALEN JOHNSON - UNDER/OVER PLAYER TURNOVERS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1074	2024-01-07 18:00:00
	12055122	JALEN SUGGS - UNDER/OVER PLAYER TURNOVERS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1074	2024-01-07 18:00:00
	12055122	ONYEKA OKONGWU - UNDER/OVER PLAYER TURNOVERS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1074	2024-01-07 18:00:00
	12055122	TRAE YOUNG - UNDER/OVER PLAYER TURNOVERS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1074	2024-01-07 18:00:00
	12055122	PAOLO BANCHERO - UNDER/OVER PLAYER TURNOVERS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1074	2024-01-07 18:00:00
	12055122	MURRAY DEJOUNTE - UNDER/OVER PLAYER TURNOVERS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1074	2024-01-07 18:00:00
	12055133	NAZ REID - UNDER/OVER PLAYER TURNOVERS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1074	2024-01-07 19:30:00
	12055133	LUKA DONCIC - UNDER/OVER PLAYER TURNOVERS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1074	2024-01-07 19:30:00
	12055133	KYLE ANDERSON - UNDER/OVER PLAYER TURNOVERS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1074	2024-01-07 19:30:00
	12055133	JADEN MCDANIELS - UNDER/OVER PLAYER TURNOVERS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1074	2024-01-07 19:30:00
	12055133	RUDY GOBERT - UNDER/OVER PLAYER TURNOVERS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1074	2024-01-07 19:30:00
	12055133	MIKE CONLEY JR. - UNDER/OVER PLAYER TURNOVERS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1074	2024-01-07 19:30:00
	12055133	KARL-ANTHONY TOWNS JR. - UNDER/OVER PLAYER TURNOVERS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1074	2024-01-07 19:30:00
	12055133	NICKEIL ALEXANDER-WALKER - UNDER/OVER PLAYER TURNOVERS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1074	2024-01-07 19:30:00
	12055133	ANTHONY EDWARDS - UNDER/OVER PLAYER TURNOVERS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1074	2024-01-07 19:30:00
	12055132	DEVIN BOOKER - UNDER/OVER PLAYER TURNOVERS (Phoenix Suns vs Memphis Grizzlies) (Phoenix Suns vs Memphis Grizzlies)	Player Prop	GAME - TOTAL	No	1074	2024-01-07 20:00:00
	12055132	JA MORANT - UNDER/OVER PLAYER TURNOVERS (Phoenix Suns vs Memphis Grizzlies) (Phoenix Suns vs Memphis Grizzlies)	Player Prop	GAME - TOTAL	No	1074	2024-01-07 20:00:00
	12055141	NIKOLA JOKIC - UNDER/OVER PLAYER TURNOVERS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1074	2024-01-07 20:00:00
	12055141	MICHAEL PORTER JR. - UNDER/OVER PLAYER TURNOVERS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1074	2024-01-07 20:00:00
	12055141	CADE CUNNINGHAM - UNDER/OVER PLAYER TURNOVERS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1074	2024-01-07 20:00:00
	12055141	AARON GORDON - UNDER/OVER PLAYER TURNOVERS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1074	2024-01-07 20:00:00
	12055141	JALEN DUREN - UNDER/OVER PLAYER TURNOVERS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1074	2024-01-07 20:00:00
	12055141	BOJAN BOGDANOVIC - UNDER/OVER PLAYER TURNOVERS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1074	2024-01-07 20:00:00
	12055141	JAMAL MURRAY - UNDER/OVER PLAYER TURNOVERS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1074	2024-01-07 20:00:00
	12055141	CALDWELL POPE KENTAVIOUS - UNDER/OVER PLAYER TURNOVERS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1074	2024-01-07 20:00:00
	12055140	BRANDIN PODZIEMSKI - UNDER/OVER PLAYER TURNOVERS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1074	2024-01-07 20:30:00
	12055140	PASCAL SIAKAM - UNDER/OVER PLAYER TURNOVERS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1074	2024-01-07 20:30:00
	12055140	JAKOB POELTL - UNDER/OVER PLAYER TURNOVERS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1074	2024-01-07 20:30:00
	12055140	JONATHAN KUMINGA - UNDER/OVER PLAYER TURNOVERS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1074	2024-01-07 20:30:00
	12055140	IMMANUEL QUICKLEY - UNDER/OVER PLAYER TURNOVERS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1074	2024-01-07 20:30:00
	12055140	STEPHEN CURRY - UNDER/OVER PLAYER TURNOVERS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1074	2024-01-07 20:30:00
	12055140	SCOTTIE BARNES - UNDER/OVER PLAYER TURNOVERS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1074	2024-01-07 20:30:00
	12055140	RJ BARRETT JR. - UNDER/OVER PLAYER TURNOVERS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1074	2024-01-07 20:30:00
	12055140	KLAY THOMPSON - UNDER/OVER PLAYER TURNOVERS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1074	2024-01-07 20:30:00
	12055115	KAWHI LEONARD - UNDER/OVER PLAYER TURNOVERS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1074	2024-01-07 21:30:00
	12055115	TERANCE MANN - UNDER/OVER PLAYER TURNOVERS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1074	2024-01-07 21:30:00
	12055115	PAUL GEORGE - UNDER/OVER PLAYER TURNOVERS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1074	2024-01-07 21:30:00
	12055115	JAMES HARDEN - UNDER/OVER PLAYER TURNOVERS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1074	2024-01-07 21:30:00
	12055115	ANTHONY DAVIS JR. - UNDER/OVER PLAYER TURNOVERS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1074	2024-01-07 21:30:00
	12055115	LEBRON JAMES - UNDER/OVER PLAYER TURNOVERS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1074	2024-01-07 21:30:00
	12055115	IVICA ZUBAC - UNDER/OVER PLAYER TURNOVERS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1074	2024-01-07 21:30:00
	12055115	TAUREAN PRINCE - UNDER/OVER PLAYER TURNOVERS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1074	2024-01-07 21:30:00
	12055116	GEORGES NIANG - UNDER/OVER PLAYER STEALS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1073	2024-01-07 13:00:00
	12055116	JARRETT ALLEN - UNDER/OVER PLAYER STEALS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1073	2024-01-07 13:00:00
	12055116	MAX STRUS - UNDER/OVER PLAYER STEALS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1073	2024-01-07 13:00:00
	12055116	DONOVAN MITCHELL - UNDER/OVER PLAYER STEALS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1073	2024-01-07 13:00:00
	12055116	SAM MERRILL - UNDER/OVER PLAYER STEALS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1073	2024-01-07 13:00:00
	12055116	KELDON JOHNSON - UNDER/OVER PLAYER STEALS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1073	2024-01-07 13:00:00
	12055116	CARIS LEVERT - UNDER/OVER PLAYER STEALS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1073	2024-01-07 13:00:00
	12055116	TRE JONES - UNDER/OVER PLAYER STEALS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1073	2024-01-07 13:00:00
	12055116	WEMBANYAMA VICTOR - UNDER/OVER PLAYER STEALS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1073	2024-01-07 13:00:00
	12055116	MALAKI BRANHAM - UNDER/OVER PLAYER STEALS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1073	2024-01-07 13:00:00
	12055116	JULIAN CHAMPAGNIE - UNDER/OVER PLAYER STEALS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1073	2024-01-07 13:00:00
	12055116	DEAN WADE - UNDER/OVER PLAYER STEALS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1073	2024-01-07 13:00:00
	12055116	JEREMY SOCHAN - UNDER/OVER PLAYER STEALS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1073	2024-01-07 13:00:00
	12055116	ISAAC OKORO - UNDER/OVER PLAYER STEALS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1073	2024-01-07 13:00:00
	12055116	DEVIN VASSELL - UNDER/OVER PLAYER STEALS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1073	2024-01-07 13:00:00
	12055117	MIKAL BRIDGES - UNDER/OVER PLAYER STEALS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1073	2024-01-07 15:00:00
	12055117	DAY'RON SHARPE - UNDER/OVER PLAYER STEALS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1073	2024-01-07 15:00:00
	12055117	SPENCER DINWIDDIE - UNDER/OVER PLAYER STEALS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1073	2024-01-07 15:00:00
	12055117	DENNIS SMITH JR. - UNDER/OVER PLAYER STEALS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1073	2024-01-07 15:00:00
	12055117	GRANT JERAMI - UNDER/OVER PLAYER STEALS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1073	2024-01-07 15:00:00
	12055117	ANFERNEE SIMONS - UNDER/OVER PLAYER STEALS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1073	2024-01-07 15:00:00
	12055117	CAMERON THOMAS - UNDER/OVER PLAYER STEALS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1073	2024-01-07 15:00:00
	12055117	CAMERON JOHNSON - UNDER/OVER PLAYER STEALS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1073	2024-01-07 15:00:00
	12055117	NICOLAS CLAXTON - UNDER/OVER PLAYER STEALS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1073	2024-01-07 15:00:00
	12055117	DORIAN FINNEY SMITH - UNDER/OVER PLAYER STEALS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1073	2024-01-07 15:00:00
	12055117	ROYCE O'NEALE - UNDER/OVER PLAYER STEALS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1073	2024-01-07 15:00:00
	12055121	ZION WILLIAMSON - UNDER/OVER PLAYER STEALS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1073	2024-01-07 18:00:00
	12055121	HARRISON BARNES - UNDER/OVER PLAYER STEALS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1073	2024-01-07 18:00:00
	12055121	HERBERT JONES - UNDER/OVER PLAYER STEALS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1073	2024-01-07 18:00:00
	12055121	CHRISTIAN JAMES MCCOLLUM - UNDER/OVER PLAYER STEALS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1073	2024-01-07 18:00:00
	12055121	KEEGAN MURRAY - UNDER/OVER PLAYER STEALS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1073	2024-01-07 18:00:00
	12055121	BRANDON INGRAM - UNDER/OVER PLAYER STEALS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1073	2024-01-07 18:00:00
	12055121	DOMANTAS SABONIS - UNDER/OVER PLAYER STEALS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1073	2024-01-07 18:00:00
	12055121	MALIK MONK - UNDER/OVER PLAYER STEALS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1073	2024-01-07 18:00:00
	12055121	DE'AARON FOX - UNDER/OVER PLAYER STEALS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1073	2024-01-07 18:00:00
	12055122	MURRAY DEJOUNTE - UNDER/OVER PLAYER STEALS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1073	2024-01-07 18:00:00
	12055122	CLINT CAPELA - UNDER/OVER PLAYER STEALS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1073	2024-01-07 18:00:00
	12055122	PAOLO BANCHERO - UNDER/OVER PLAYER STEALS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1073	2024-01-07 18:00:00
	12055122	JALEN JOHNSON - UNDER/OVER PLAYER STEALS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1073	2024-01-07 18:00:00
	12055122	JALEN SUGGS - UNDER/OVER PLAYER STEALS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1073	2024-01-07 18:00:00
	12055122	TRAE YOUNG - UNDER/OVER PLAYER STEALS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1073	2024-01-07 18:00:00
	12055122	ONYEKA OKONGWU - UNDER/OVER PLAYER STEALS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1073	2024-01-07 18:00:00
	12055122	SADDIQ BEY - UNDER/OVER PLAYER STEALS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1073	2024-01-07 18:00:00
	12055122	BOGDAN BOGDANOVIC - UNDER/OVER PLAYER STEALS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1073	2024-01-07 18:00:00
	12055133	ANTHONY EDWARDS - UNDER/OVER PLAYER STEALS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1073	2024-01-07 19:30:00
	12055133	RUDY GOBERT - UNDER/OVER PLAYER STEALS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1073	2024-01-07 19:30:00
	12055133	MIKE CONLEY JR. - UNDER/OVER PLAYER STEALS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1073	2024-01-07 19:30:00
	12055133	JADEN MCDANIELS - UNDER/OVER PLAYER STEALS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1073	2024-01-07 19:30:00
	12055133	NICKEIL ALEXANDER-WALKER - UNDER/OVER PLAYER STEALS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1073	2024-01-07 19:30:00
	12055133	KYLE ANDERSON - UNDER/OVER PLAYER STEALS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1073	2024-01-07 19:30:00
	12055133	LUKA DONCIC - UNDER/OVER PLAYER STEALS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1073	2024-01-07 19:30:00
	12055133	NAZ REID - UNDER/OVER PLAYER STEALS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1073	2024-01-07 19:30:00
	12055133	KARL-ANTHONY TOWNS JR. - UNDER/OVER PLAYER STEALS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1073	2024-01-07 19:30:00
	12055132	JA MORANT - UNDER/OVER PLAYER STEALS (Phoenix Suns vs Memphis Grizzlies) (Phoenix Suns vs Memphis Grizzlies)	Player Prop	GAME - TOTAL	No	1073	2024-01-07 20:00:00
	12055132	DEVIN BOOKER - UNDER/OVER PLAYER STEALS (Phoenix Suns vs Memphis Grizzlies) (Phoenix Suns vs Memphis Grizzlies)	Player Prop	GAME - TOTAL	No	1073	2024-01-07 20:00:00
	12055141	AARON GORDON - UNDER/OVER PLAYER STEALS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1073	2024-01-07 20:00:00
	12055141	CADE CUNNINGHAM - UNDER/OVER PLAYER STEALS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1073	2024-01-07 20:00:00
	12055141	JALEN DUREN - UNDER/OVER PLAYER STEALS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1073	2024-01-07 20:00:00
	12055141	MICHAEL PORTER JR. - UNDER/OVER PLAYER STEALS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1073	2024-01-07 20:00:00
	12055141	BOJAN BOGDANOVIC - UNDER/OVER PLAYER STEALS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1073	2024-01-07 20:00:00
	12055141	JAMAL MURRAY - UNDER/OVER PLAYER STEALS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1073	2024-01-07 20:00:00
	12055141	CALDWELL POPE KENTAVIOUS - UNDER/OVER PLAYER STEALS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1073	2024-01-07 20:00:00
	12055141	NIKOLA JOKIC - UNDER/OVER PLAYER STEALS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1073	2024-01-07 20:00:00
	12055140	KLAY THOMPSON - UNDER/OVER PLAYER STEALS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1073	2024-01-07 20:30:00
	12055140	SCOTTIE BARNES - UNDER/OVER PLAYER STEALS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1073	2024-01-07 20:30:00
	12055140	PASCAL SIAKAM - UNDER/OVER PLAYER STEALS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1073	2024-01-07 20:30:00
	12055140	RJ BARRETT JR. - UNDER/OVER PLAYER STEALS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1073	2024-01-07 20:30:00
	12055140	JAKOB POELTL - UNDER/OVER PLAYER STEALS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1073	2024-01-07 20:30:00
	12055140	STEPHEN CURRY - UNDER/OVER PLAYER STEALS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1073	2024-01-07 20:30:00
	12055140	BRANDIN PODZIEMSKI - UNDER/OVER PLAYER STEALS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1073	2024-01-07 20:30:00
	12055140	JONATHAN KUMINGA - UNDER/OVER PLAYER STEALS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1073	2024-01-07 20:30:00
	12055140	IMMANUEL QUICKLEY - UNDER/OVER PLAYER STEALS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1073	2024-01-07 20:30:00
	12055115	TERANCE MANN - UNDER/OVER PLAYER STEALS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1073	2024-01-07 21:30:00
	12055115	IVICA ZUBAC - UNDER/OVER PLAYER STEALS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1073	2024-01-07 21:30:00
	12055115	JAMES HARDEN - UNDER/OVER PLAYER STEALS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1073	2024-01-07 21:30:00
	12055115	LEBRON JAMES - UNDER/OVER PLAYER STEALS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1073	2024-01-07 21:30:00
	12055115	KAWHI LEONARD - UNDER/OVER PLAYER STEALS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1073	2024-01-07 21:30:00
	12055115	TAUREAN PRINCE - UNDER/OVER PLAYER STEALS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1073	2024-01-07 21:30:00
	12055115	ANTHONY DAVIS JR. - UNDER/OVER PLAYER STEALS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1073	2024-01-07 21:30:00
	12055115	PAUL GEORGE - UNDER/OVER PLAYER STEALS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1073	2024-01-07 21:30:00
	12055116	DEAN WADE - UNDER/OVER PLAYER REBOUNDS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1072	2024-01-07 13:00:00
	12055116	DEVIN VASSELL - UNDER/OVER PLAYER REBOUNDS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1072	2024-01-07 13:00:00
	12055116	CARIS LEVERT - UNDER/OVER PLAYER REBOUNDS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1072	2024-01-07 13:00:00
	12055116	JARRETT ALLEN - UNDER/OVER PLAYER REBOUNDS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1072	2024-01-07 13:00:00
	12055116	TRE JONES - UNDER/OVER PLAYER REBOUNDS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1072	2024-01-07 13:00:00
	12055116	WEMBANYAMA VICTOR - UNDER/OVER PLAYER REBOUNDS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1072	2024-01-07 13:00:00
	12055116	DONOVAN MITCHELL - UNDER/OVER PLAYER REBOUNDS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1072	2024-01-07 13:00:00
	12055116	JULIAN CHAMPAGNIE - UNDER/OVER PLAYER REBOUNDS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1072	2024-01-07 13:00:00
	12055116	MAX STRUS - UNDER/OVER PLAYER REBOUNDS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1072	2024-01-07 13:00:00
	12055116	KELDON JOHNSON - UNDER/OVER PLAYER REBOUNDS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1072	2024-01-07 13:00:00
	12055116	JEREMY SOCHAN - UNDER/OVER PLAYER REBOUNDS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1072	2024-01-07 13:00:00
	12055116	GEORGES NIANG - UNDER/OVER PLAYER REBOUNDS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1072	2024-01-07 13:00:00
	12055116	SAM MERRILL - UNDER/OVER PLAYER REBOUNDS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1072	2024-01-07 13:00:00
	12055116	ISAAC OKORO - UNDER/OVER PLAYER REBOUNDS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1072	2024-01-07 13:00:00
	12055116	MALAKI BRANHAM - UNDER/OVER PLAYER REBOUNDS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1072	2024-01-07 13:00:00
	12055117	MIKAL BRIDGES - UNDER/OVER PLAYER REBOUNDS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1072	2024-01-07 15:00:00
	12055117	ANFERNEE SIMONS - UNDER/OVER PLAYER REBOUNDS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1072	2024-01-07 15:00:00
	12055117	CAMERON THOMAS - UNDER/OVER PLAYER REBOUNDS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1072	2024-01-07 15:00:00
	12055117	CAMERON JOHNSON - UNDER/OVER PLAYER REBOUNDS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1072	2024-01-07 15:00:00
	12055117	ROYCE O'NEALE - UNDER/OVER PLAYER REBOUNDS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1072	2024-01-07 15:00:00
	12055117	DORIAN FINNEY SMITH - UNDER/OVER PLAYER REBOUNDS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1072	2024-01-07 15:00:00
	12055117	NICOLAS CLAXTON - UNDER/OVER PLAYER REBOUNDS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1072	2024-01-07 15:00:00
	12055117	GRANT JERAMI - UNDER/OVER PLAYER REBOUNDS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1072	2024-01-07 15:00:00
	12055117	DENNIS SMITH JR. - UNDER/OVER PLAYER REBOUNDS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1072	2024-01-07 15:00:00
	12055117	SPENCER DINWIDDIE - UNDER/OVER PLAYER REBOUNDS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1072	2024-01-07 15:00:00
	12055117	DAY'RON SHARPE - UNDER/OVER PLAYER REBOUNDS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1072	2024-01-07 15:00:00
	12055121	DE'AARON FOX - UNDER/OVER PLAYER REBOUNDS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1072	2024-01-07 18:00:00
	12055121	HERBERT JONES - UNDER/OVER PLAYER REBOUNDS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1072	2024-01-07 18:00:00
	12055121	ZION WILLIAMSON - UNDER/OVER PLAYER REBOUNDS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1072	2024-01-07 18:00:00
	12055121	CHRISTIAN JAMES MCCOLLUM - UNDER/OVER PLAYER REBOUNDS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1072	2024-01-07 18:00:00
	12055121	HARRISON BARNES - UNDER/OVER PLAYER REBOUNDS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1072	2024-01-07 18:00:00
	12055121	MALIK MONK - UNDER/OVER PLAYER REBOUNDS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1072	2024-01-07 18:00:00
	12055121	DOMANTAS SABONIS - UNDER/OVER PLAYER REBOUNDS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1072	2024-01-07 18:00:00
	12055121	KEEGAN MURRAY - UNDER/OVER PLAYER REBOUNDS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1072	2024-01-07 18:00:00
	12055121	BRANDON INGRAM - UNDER/OVER PLAYER REBOUNDS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1072	2024-01-07 18:00:00
	12055122	MURRAY DEJOUNTE - UNDER/OVER PLAYER REBOUNDS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1072	2024-01-07 18:00:00
	12055122	JALEN JOHNSON - UNDER/OVER PLAYER REBOUNDS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1072	2024-01-07 18:00:00
	12055122	CLINT CAPELA - UNDER/OVER PLAYER REBOUNDS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1072	2024-01-07 18:00:00
	12055122	JALEN SUGGS - UNDER/OVER PLAYER REBOUNDS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1072	2024-01-07 18:00:00
	12055122	PAOLO BANCHERO - UNDER/OVER PLAYER REBOUNDS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1072	2024-01-07 18:00:00
	12055122	SADDIQ BEY - UNDER/OVER PLAYER REBOUNDS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1072	2024-01-07 18:00:00
	12055122	BOGDAN BOGDANOVIC - UNDER/OVER PLAYER REBOUNDS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1072	2024-01-07 18:00:00
	12055122	TRAE YOUNG - UNDER/OVER PLAYER REBOUNDS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1072	2024-01-07 18:00:00
	12055122	ONYEKA OKONGWU - UNDER/OVER PLAYER REBOUNDS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1072	2024-01-07 18:00:00
	12055133	MIKE CONLEY JR. - UNDER/OVER PLAYER REBOUNDS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1072	2024-01-07 19:30:00
	12055133	LUKA DONCIC - UNDER/OVER PLAYER REBOUNDS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1072	2024-01-07 19:30:00
	12055133	NAZ REID - UNDER/OVER PLAYER REBOUNDS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1072	2024-01-07 19:30:00
	12055133	RUDY GOBERT - UNDER/OVER PLAYER REBOUNDS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1072	2024-01-07 19:30:00
	12055133	NICKEIL ALEXANDER-WALKER - UNDER/OVER PLAYER REBOUNDS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1072	2024-01-07 19:30:00
	12055133	ANTHONY EDWARDS - UNDER/OVER PLAYER REBOUNDS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1072	2024-01-07 19:30:00
	12055133	JADEN MCDANIELS - UNDER/OVER PLAYER REBOUNDS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1072	2024-01-07 19:30:00
	12055133	KARL-ANTHONY TOWNS JR. - UNDER/OVER PLAYER REBOUNDS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1072	2024-01-07 19:30:00
	12055133	KYLE ANDERSON - UNDER/OVER PLAYER REBOUNDS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1072	2024-01-07 19:30:00
	12055132	DEVIN BOOKER - UNDER/OVER PLAYER REBOUNDS (Phoenix Suns vs Memphis Grizzlies) (Phoenix Suns vs Memphis Grizzlies)	Player Prop	GAME - TOTAL	No	1072	2024-01-07 20:00:00
	12055132	JA MORANT - UNDER/OVER PLAYER REBOUNDS (Phoenix Suns vs Memphis Grizzlies) (Phoenix Suns vs Memphis Grizzlies)	Player Prop	GAME - TOTAL	No	1072	2024-01-07 20:00:00
	12055141	JALEN DUREN - UNDER/OVER PLAYER REBOUNDS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1072	2024-01-07 20:00:00
	12055141	JAMAL MURRAY - UNDER/OVER PLAYER REBOUNDS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1072	2024-01-07 20:00:00
	12055141	AARON GORDON - UNDER/OVER PLAYER REBOUNDS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1072	2024-01-07 20:00:00
	12055141	NIKOLA JOKIC - UNDER/OVER PLAYER REBOUNDS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1072	2024-01-07 20:00:00
	12055141	CALDWELL POPE KENTAVIOUS - UNDER/OVER PLAYER REBOUNDS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1072	2024-01-07 20:00:00
	12055141	CADE CUNNINGHAM - UNDER/OVER PLAYER REBOUNDS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1072	2024-01-07 20:00:00
	12055141	BOJAN BOGDANOVIC - UNDER/OVER PLAYER REBOUNDS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1072	2024-01-07 20:00:00
	12055141	MICHAEL PORTER JR. - UNDER/OVER PLAYER REBOUNDS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1072	2024-01-07 20:00:00
	12055140	STEPHEN CURRY - UNDER/OVER PLAYER REBOUNDS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1072	2024-01-07 20:30:00
	12055140	JONATHAN KUMINGA - UNDER/OVER PLAYER REBOUNDS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1072	2024-01-07 20:30:00
	12055140	JAKOB POELTL - UNDER/OVER PLAYER REBOUNDS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1072	2024-01-07 20:30:00
	12055140	RJ BARRETT JR. - UNDER/OVER PLAYER REBOUNDS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1072	2024-01-07 20:30:00
	12055140	KLAY THOMPSON - UNDER/OVER PLAYER REBOUNDS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1072	2024-01-07 20:30:00
	12055140	IMMANUEL QUICKLEY - UNDER/OVER PLAYER REBOUNDS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1072	2024-01-07 20:30:00
	12055140	SCOTTIE BARNES - UNDER/OVER PLAYER REBOUNDS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1072	2024-01-07 20:30:00
	12055140	PASCAL SIAKAM - UNDER/OVER PLAYER REBOUNDS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1072	2024-01-07 20:30:00
	12055140	BRANDIN PODZIEMSKI - UNDER/OVER PLAYER REBOUNDS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1072	2024-01-07 20:30:00
	12055115	JAMES HARDEN - UNDER/OVER PLAYER REBOUNDS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1072	2024-01-07 21:30:00
	12055115	LEBRON JAMES - UNDER/OVER PLAYER REBOUNDS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1072	2024-01-07 21:30:00
	12055115	KAWHI LEONARD - UNDER/OVER PLAYER REBOUNDS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1072	2024-01-07 21:30:00
	12055115	PAUL GEORGE - UNDER/OVER PLAYER REBOUNDS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1072	2024-01-07 21:30:00
	12055115	TAUREAN PRINCE - UNDER/OVER PLAYER REBOUNDS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1072	2024-01-07 21:30:00
	12055115	ANTHONY DAVIS JR. - UNDER/OVER PLAYER REBOUNDS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1072	2024-01-07 21:30:00
	12055115	TERANCE MANN - UNDER/OVER PLAYER REBOUNDS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1072	2024-01-07 21:30:00
	12055115	IVICA ZUBAC - UNDER/OVER PLAYER REBOUNDS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1072	2024-01-07 21:30:00
	12055116	KELDON JOHNSON - UNDER/OVER PLAYER ASSISTS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1071	2024-01-07 13:00:00
	12055116	CARIS LEVERT - UNDER/OVER PLAYER ASSISTS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1071	2024-01-07 13:00:00
	12055116	WEMBANYAMA VICTOR - UNDER/OVER PLAYER ASSISTS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1071	2024-01-07 13:00:00
	12055116	JARRETT ALLEN - UNDER/OVER PLAYER ASSISTS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1071	2024-01-07 13:00:00
	12055116	MAX STRUS - UNDER/OVER PLAYER ASSISTS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1071	2024-01-07 13:00:00
	12055116	GEORGES NIANG - UNDER/OVER PLAYER ASSISTS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1071	2024-01-07 13:00:00
	12055116	DONOVAN MITCHELL - UNDER/OVER PLAYER ASSISTS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1071	2024-01-07 13:00:00
	12055116	SAM MERRILL - UNDER/OVER PLAYER ASSISTS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1071	2024-01-07 13:00:00
	12055116	ISAAC OKORO - UNDER/OVER PLAYER ASSISTS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1071	2024-01-07 13:00:00
	12055116	TRE JONES - UNDER/OVER PLAYER ASSISTS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1071	2024-01-07 13:00:00
	12055116	DEVIN VASSELL - UNDER/OVER PLAYER ASSISTS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1071	2024-01-07 13:00:00
	12055116	JEREMY SOCHAN - UNDER/OVER PLAYER ASSISTS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1071	2024-01-07 13:00:00
	12055116	DEAN WADE - UNDER/OVER PLAYER ASSISTS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1071	2024-01-07 13:00:00
	12055117	CAMERON JOHNSON - UNDER/OVER PLAYER ASSISTS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1071	2024-01-07 15:00:00
	12055117	CAMERON THOMAS - UNDER/OVER PLAYER ASSISTS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1071	2024-01-07 15:00:00
	12055117	SPENCER DINWIDDIE - UNDER/OVER PLAYER ASSISTS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1071	2024-01-07 15:00:00
	12055117	ROYCE O'NEALE - UNDER/OVER PLAYER ASSISTS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1071	2024-01-07 15:00:00
	12055117	DENNIS SMITH JR. - UNDER/OVER PLAYER ASSISTS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1071	2024-01-07 15:00:00
	12055117	DORIAN FINNEY SMITH - UNDER/OVER PLAYER ASSISTS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1071	2024-01-07 15:00:00
	12055117	NICOLAS CLAXTON - UNDER/OVER PLAYER ASSISTS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1071	2024-01-07 15:00:00
	12055117	MIKAL BRIDGES - UNDER/OVER PLAYER ASSISTS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1071	2024-01-07 15:00:00
	12055117	ANFERNEE SIMONS - UNDER/OVER PLAYER ASSISTS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1071	2024-01-07 15:00:00
	12055117	DAY'RON SHARPE - UNDER/OVER PLAYER ASSISTS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1071	2024-01-07 15:00:00
	12055117	GRANT JERAMI - UNDER/OVER PLAYER ASSISTS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1071	2024-01-07 15:00:00
	12055121	DE'AARON FOX - UNDER/OVER PLAYER ASSISTS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1071	2024-01-07 18:00:00
	12055121	BRANDON INGRAM - UNDER/OVER PLAYER ASSISTS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1071	2024-01-07 18:00:00
	12055121	DOMANTAS SABONIS - UNDER/OVER PLAYER ASSISTS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1071	2024-01-07 18:00:00
	12055121	MALIK MONK - UNDER/OVER PLAYER ASSISTS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1071	2024-01-07 18:00:00
	12055121	HERBERT JONES - UNDER/OVER PLAYER ASSISTS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1071	2024-01-07 18:00:00
	12055121	CHRISTIAN JAMES MCCOLLUM - UNDER/OVER PLAYER ASSISTS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1071	2024-01-07 18:00:00
	12055121	KEEGAN MURRAY - UNDER/OVER PLAYER ASSISTS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1071	2024-01-07 18:00:00
	12055121	HARRISON BARNES - UNDER/OVER PLAYER ASSISTS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1071	2024-01-07 18:00:00
	12055121	ZION WILLIAMSON - UNDER/OVER PLAYER ASSISTS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1071	2024-01-07 18:00:00
	12055122	JALEN JOHNSON - UNDER/OVER PLAYER ASSISTS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1071	2024-01-07 18:00:00
	12055122	SADDIQ BEY - UNDER/OVER PLAYER ASSISTS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1071	2024-01-07 18:00:00
	12055122	PAOLO BANCHERO - UNDER/OVER PLAYER ASSISTS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1071	2024-01-07 18:00:00
	12055122	BOGDAN BOGDANOVIC - UNDER/OVER PLAYER ASSISTS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1071	2024-01-07 18:00:00
	12055122	ONYEKA OKONGWU - UNDER/OVER PLAYER ASSISTS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1071	2024-01-07 18:00:00
	12055122	MURRAY DEJOUNTE - UNDER/OVER PLAYER ASSISTS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1071	2024-01-07 18:00:00
	12055122	JALEN SUGGS - UNDER/OVER PLAYER ASSISTS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1071	2024-01-07 18:00:00
	12055122	CLINT CAPELA - UNDER/OVER PLAYER ASSISTS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1071	2024-01-07 18:00:00
	12055122	TRAE YOUNG - UNDER/OVER PLAYER ASSISTS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1071	2024-01-07 18:00:00
	12055133	ANTHONY EDWARDS - UNDER/OVER PLAYER ASSISTS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1071	2024-01-07 19:30:00
	12055133	JADEN MCDANIELS - UNDER/OVER PLAYER ASSISTS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1071	2024-01-07 19:30:00
	12055133	NICKEIL ALEXANDER-WALKER - UNDER/OVER PLAYER ASSISTS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1071	2024-01-07 19:30:00
	12055133	KYLE ANDERSON - UNDER/OVER PLAYER ASSISTS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1071	2024-01-07 19:30:00
	12055133	NAZ REID - UNDER/OVER PLAYER ASSISTS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1071	2024-01-07 19:30:00
	12055133	LUKA DONCIC - UNDER/OVER PLAYER ASSISTS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1071	2024-01-07 19:30:00
	12055133	MIKE CONLEY JR. - UNDER/OVER PLAYER ASSISTS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1071	2024-01-07 19:30:00
	12055133	RUDY GOBERT - UNDER/OVER PLAYER ASSISTS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1071	2024-01-07 19:30:00
	12055133	KARL-ANTHONY TOWNS JR. - UNDER/OVER PLAYER ASSISTS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1071	2024-01-07 19:30:00
	12055132	DEVIN BOOKER - UNDER/OVER PLAYER ASSISTS (Phoenix Suns vs Memphis Grizzlies) (Phoenix Suns vs Memphis Grizzlies)	Player Prop	GAME - TOTAL	No	1071	2024-01-07 20:00:00
	12055132	JA MORANT - UNDER/OVER PLAYER ASSISTS (Phoenix Suns vs Memphis Grizzlies) (Phoenix Suns vs Memphis Grizzlies)	Player Prop	GAME - TOTAL	No	1071	2024-01-07 20:00:00
	12055141	BOJAN BOGDANOVIC - UNDER/OVER PLAYER ASSISTS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1071	2024-01-07 20:00:00
	12055141	NIKOLA JOKIC - UNDER/OVER PLAYER ASSISTS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1071	2024-01-07 20:00:00
	12055141	CADE CUNNINGHAM - UNDER/OVER PLAYER ASSISTS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1071	2024-01-07 20:00:00
	12055141	AARON GORDON - UNDER/OVER PLAYER ASSISTS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1071	2024-01-07 20:00:00
	12055141	MICHAEL PORTER JR. - UNDER/OVER PLAYER ASSISTS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1071	2024-01-07 20:00:00
	12055141	JAMAL MURRAY - UNDER/OVER PLAYER ASSISTS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1071	2024-01-07 20:00:00
	12055141	JALEN DUREN - UNDER/OVER PLAYER ASSISTS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1071	2024-01-07 20:00:00
	12055141	CALDWELL POPE KENTAVIOUS - UNDER/OVER PLAYER ASSISTS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1071	2024-01-07 20:00:00
	12055140	KLAY THOMPSON - UNDER/OVER PLAYER ASSISTS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1071	2024-01-07 20:30:00
	12055140	STEPHEN CURRY - UNDER/OVER PLAYER ASSISTS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1071	2024-01-07 20:30:00
	12055140	BRANDIN PODZIEMSKI - UNDER/OVER PLAYER ASSISTS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1071	2024-01-07 20:30:00
	12055140	PASCAL SIAKAM - UNDER/OVER PLAYER ASSISTS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1071	2024-01-07 20:30:00
	12055140	SCOTTIE BARNES - UNDER/OVER PLAYER ASSISTS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1071	2024-01-07 20:30:00
	12055140	JONATHAN KUMINGA - UNDER/OVER PLAYER ASSISTS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1071	2024-01-07 20:30:00
	12055140	IMMANUEL QUICKLEY - UNDER/OVER PLAYER ASSISTS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1071	2024-01-07 20:30:00
	12055140	RJ BARRETT JR. - UNDER/OVER PLAYER ASSISTS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1071	2024-01-07 20:30:00
	12055140	JAKOB POELTL - UNDER/OVER PLAYER ASSISTS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1071	2024-01-07 20:30:00
	12055115	LEBRON JAMES - UNDER/OVER PLAYER ASSISTS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1071	2024-01-07 21:30:00
	12055115	JAMES HARDEN - UNDER/OVER PLAYER ASSISTS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1071	2024-01-07 21:30:00
	12055115	TERANCE MANN - UNDER/OVER PLAYER ASSISTS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1071	2024-01-07 21:30:00
	12055115	IVICA ZUBAC - UNDER/OVER PLAYER ASSISTS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1071	2024-01-07 21:30:00
	12055115	PAUL GEORGE - UNDER/OVER PLAYER ASSISTS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1071	2024-01-07 21:30:00
	12055115	TAUREAN PRINCE - UNDER/OVER PLAYER ASSISTS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1071	2024-01-07 21:30:00
	12055115	ANTHONY DAVIS JR. - UNDER/OVER PLAYER ASSISTS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1071	2024-01-07 21:30:00
	12055115	KAWHI LEONARD - UNDER/OVER PLAYER ASSISTS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1071	2024-01-07 21:30:00
	12055116	JULIAN CHAMPAGNIE - UNDER/OVER PLAYER BLOCKS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1070	2024-01-07 13:00:00
	12055116	KELDON JOHNSON - UNDER/OVER PLAYER BLOCKS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1070	2024-01-07 13:00:00
	12055116	TRE JONES - UNDER/OVER PLAYER BLOCKS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1070	2024-01-07 13:00:00
	12055116	DONOVAN MITCHELL - UNDER/OVER PLAYER BLOCKS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1070	2024-01-07 13:00:00
	12055116	GEORGES NIANG - UNDER/OVER PLAYER BLOCKS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1070	2024-01-07 13:00:00
	12055116	JEREMY SOCHAN - UNDER/OVER PLAYER BLOCKS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1070	2024-01-07 13:00:00
	12055116	SAM MERRILL - UNDER/OVER PLAYER BLOCKS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1070	2024-01-07 13:00:00
	12055116	WEMBANYAMA VICTOR - UNDER/OVER PLAYER BLOCKS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1070	2024-01-07 13:00:00
	12055116	MAX STRUS - UNDER/OVER PLAYER BLOCKS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1070	2024-01-07 13:00:00
	12055116	JARRETT ALLEN - UNDER/OVER PLAYER BLOCKS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1070	2024-01-07 13:00:00
	12055116	DEAN WADE - UNDER/OVER PLAYER BLOCKS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1070	2024-01-07 13:00:00
	12055116	ISAAC OKORO - UNDER/OVER PLAYER BLOCKS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1070	2024-01-07 13:00:00
	12055116	DEVIN VASSELL - UNDER/OVER PLAYER BLOCKS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1070	2024-01-07 13:00:00
	12055116	CARIS LEVERT - UNDER/OVER PLAYER BLOCKS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1070	2024-01-07 13:00:00
	12055117	DAY'RON SHARPE - UNDER/OVER PLAYER BLOCKS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1070	2024-01-07 15:00:00
	12055117	MIKAL BRIDGES - UNDER/OVER PLAYER BLOCKS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1070	2024-01-07 15:00:00
	12055117	NICOLAS CLAXTON - UNDER/OVER PLAYER BLOCKS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1070	2024-01-07 15:00:00
	12055117	DORIAN FINNEY SMITH - UNDER/OVER PLAYER BLOCKS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1070	2024-01-07 15:00:00
	12055117	SPENCER DINWIDDIE - UNDER/OVER PLAYER BLOCKS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1070	2024-01-07 15:00:00
	12055117	ROYCE O'NEALE - UNDER/OVER PLAYER BLOCKS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1070	2024-01-07 15:00:00
	12055117	ANFERNEE SIMONS - UNDER/OVER PLAYER BLOCKS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1070	2024-01-07 15:00:00
	12055117	CAMERON JOHNSON - UNDER/OVER PLAYER BLOCKS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1070	2024-01-07 15:00:00
	12055117	GRANT JERAMI - UNDER/OVER PLAYER BLOCKS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1070	2024-01-07 15:00:00
	12055117	CAMERON THOMAS - UNDER/OVER PLAYER BLOCKS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1070	2024-01-07 15:00:00
	12055117	DENNIS SMITH JR. - UNDER/OVER PLAYER BLOCKS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1070	2024-01-07 15:00:00
	12055121	MALIK MONK - UNDER/OVER PLAYER BLOCKS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1070	2024-01-07 18:00:00
	12055121	HARRISON BARNES - UNDER/OVER PLAYER BLOCKS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1070	2024-01-07 18:00:00
	12055121	ZION WILLIAMSON - UNDER/OVER PLAYER BLOCKS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1070	2024-01-07 18:00:00
	12055121	DE'AARON FOX - UNDER/OVER PLAYER BLOCKS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1070	2024-01-07 18:00:00
	12055121	BRANDON INGRAM - UNDER/OVER PLAYER BLOCKS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1070	2024-01-07 18:00:00
	12055121	KEEGAN MURRAY - UNDER/OVER PLAYER BLOCKS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1070	2024-01-07 18:00:00
	12055121	CHRISTIAN JAMES MCCOLLUM - UNDER/OVER PLAYER BLOCKS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1070	2024-01-07 18:00:00
	12055121	DOMANTAS SABONIS - UNDER/OVER PLAYER BLOCKS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1070	2024-01-07 18:00:00
	12055121	HERBERT JONES - UNDER/OVER PLAYER BLOCKS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1070	2024-01-07 18:00:00
	12055122	PAOLO BANCHERO - UNDER/OVER PLAYER BLOCKS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1070	2024-01-07 18:00:00
	12055122	BOGDAN BOGDANOVIC - UNDER/OVER PLAYER BLOCKS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1070	2024-01-07 18:00:00
	12055122	CLINT CAPELA - UNDER/OVER PLAYER BLOCKS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1070	2024-01-07 18:00:00
	12055122	JALEN JOHNSON - UNDER/OVER PLAYER BLOCKS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1070	2024-01-07 18:00:00
	12055122	TRAE YOUNG - UNDER/OVER PLAYER BLOCKS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1070	2024-01-07 18:00:00
	12055122	MURRAY DEJOUNTE - UNDER/OVER PLAYER BLOCKS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1070	2024-01-07 18:00:00
	12055122	JALEN SUGGS - UNDER/OVER PLAYER BLOCKS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1070	2024-01-07 18:00:00
	12055122	SADDIQ BEY - UNDER/OVER PLAYER BLOCKS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1070	2024-01-07 18:00:00
	12055122	ONYEKA OKONGWU - UNDER/OVER PLAYER BLOCKS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1070	2024-01-07 18:00:00
	12055133	LUKA DONCIC - UNDER/OVER PLAYER BLOCKS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1070	2024-01-07 19:30:00
	12055133	RUDY GOBERT - UNDER/OVER PLAYER BLOCKS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1070	2024-01-07 19:30:00
	12055133	MIKE CONLEY JR. - UNDER/OVER PLAYER BLOCKS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1070	2024-01-07 19:30:00
	12055133	JADEN MCDANIELS - UNDER/OVER PLAYER BLOCKS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1070	2024-01-07 19:30:00
	12055133	KYLE ANDERSON - UNDER/OVER PLAYER BLOCKS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1070	2024-01-07 19:30:00
	12055133	NAZ REID - UNDER/OVER PLAYER BLOCKS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1070	2024-01-07 19:30:00
	12055133	ANTHONY EDWARDS - UNDER/OVER PLAYER BLOCKS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1070	2024-01-07 19:30:00
	12055133	NICKEIL ALEXANDER-WALKER - UNDER/OVER PLAYER BLOCKS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1070	2024-01-07 19:30:00
	12055133	KARL-ANTHONY TOWNS JR. - UNDER/OVER PLAYER BLOCKS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1070	2024-01-07 19:30:00
	12055132	JA MORANT - UNDER/OVER PLAYER BLOCKS (Phoenix Suns vs Memphis Grizzlies) (Phoenix Suns vs Memphis Grizzlies)	Player Prop	GAME - TOTAL	No	1070	2024-01-07 20:00:00
	12055132	DEVIN BOOKER - UNDER/OVER PLAYER BLOCKS (Phoenix Suns vs Memphis Grizzlies) (Phoenix Suns vs Memphis Grizzlies)	Player Prop	GAME - TOTAL	No	1070	2024-01-07 20:00:00
	12055141	BOJAN BOGDANOVIC - UNDER/OVER PLAYER BLOCKS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1070	2024-01-07 20:00:00
	12055141	NIKOLA JOKIC - UNDER/OVER PLAYER BLOCKS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1070	2024-01-07 20:00:00
	12055141	AARON GORDON - UNDER/OVER PLAYER BLOCKS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1070	2024-01-07 20:00:00
	12055141	JALEN DUREN - UNDER/OVER PLAYER BLOCKS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1070	2024-01-07 20:00:00
	12055141	JAMAL MURRAY - UNDER/OVER PLAYER BLOCKS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1070	2024-01-07 20:00:00
	12055141	CADE CUNNINGHAM - UNDER/OVER PLAYER BLOCKS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1070	2024-01-07 20:00:00
	12055141	CALDWELL POPE KENTAVIOUS - UNDER/OVER PLAYER BLOCKS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1070	2024-01-07 20:00:00
	12055141	MICHAEL PORTER JR. - UNDER/OVER PLAYER BLOCKS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1070	2024-01-07 20:00:00
	12055140	RJ BARRETT JR. - UNDER/OVER PLAYER BLOCKS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1070	2024-01-07 20:30:00
	12055140	STEPHEN CURRY - UNDER/OVER PLAYER BLOCKS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1070	2024-01-07 20:30:00
	12055140	JAKOB POELTL - UNDER/OVER PLAYER BLOCKS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1070	2024-01-07 20:30:00
	12055140	KLAY THOMPSON - UNDER/OVER PLAYER BLOCKS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1070	2024-01-07 20:30:00
	12055140	IMMANUEL QUICKLEY - UNDER/OVER PLAYER BLOCKS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1070	2024-01-07 20:30:00
	12055140	PASCAL SIAKAM - UNDER/OVER PLAYER BLOCKS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1070	2024-01-07 20:30:00
	12055140	SCOTTIE BARNES - UNDER/OVER PLAYER BLOCKS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1070	2024-01-07 20:30:00
	12055140	JONATHAN KUMINGA - UNDER/OVER PLAYER BLOCKS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1070	2024-01-07 20:30:00
	12055140	BRANDIN PODZIEMSKI - UNDER/OVER PLAYER BLOCKS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1070	2024-01-07 20:30:00
	12055115	ANTHONY DAVIS JR. - UNDER/OVER PLAYER BLOCKS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1070	2024-01-07 21:30:00
	12055115	IVICA ZUBAC - UNDER/OVER PLAYER BLOCKS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1070	2024-01-07 21:30:00
	12055115	JAMES HARDEN - UNDER/OVER PLAYER BLOCKS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1070	2024-01-07 21:30:00
	12055115	PAUL GEORGE - UNDER/OVER PLAYER BLOCKS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1070	2024-01-07 21:30:00
	12055115	TAUREAN PRINCE - UNDER/OVER PLAYER BLOCKS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1070	2024-01-07 21:30:00
	12055115	TERANCE MANN - UNDER/OVER PLAYER BLOCKS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1070	2024-01-07 21:30:00
	12055115	KAWHI LEONARD - UNDER/OVER PLAYER BLOCKS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1070	2024-01-07 21:30:00
	12055115	LEBRON JAMES - UNDER/OVER PLAYER BLOCKS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1070	2024-01-07 21:30:00
	12055116	TRE JONES - UNDER/OVER PLAYER POINTS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1069	2024-01-07 13:00:00
	12055116	DONOVAN MITCHELL - UNDER/OVER PLAYER POINTS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1069	2024-01-07 13:00:00
	12055116	DEVIN VASSELL - UNDER/OVER PLAYER POINTS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1069	2024-01-07 13:00:00
	12055116	GEORGES NIANG - UNDER/OVER PLAYER POINTS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1069	2024-01-07 13:00:00
	12055116	JEREMY SOCHAN - UNDER/OVER PLAYER POINTS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1069	2024-01-07 13:00:00
	12055116	ISAAC OKORO - UNDER/OVER PLAYER POINTS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1069	2024-01-07 13:00:00
	12055116	JARRETT ALLEN - UNDER/OVER PLAYER POINTS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1069	2024-01-07 13:00:00
	12055116	WEMBANYAMA VICTOR - UNDER/OVER PLAYER POINTS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1069	2024-01-07 13:00:00
	12055116	DEAN WADE - UNDER/OVER PLAYER POINTS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1069	2024-01-07 13:00:00
	12055116	CARIS LEVERT - UNDER/OVER PLAYER POINTS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1069	2024-01-07 13:00:00
	12055116	MAX STRUS - UNDER/OVER PLAYER POINTS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1069	2024-01-07 13:00:00
	12055116	MALAKI BRANHAM - UNDER/OVER PLAYER POINTS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1069	2024-01-07 13:00:00
	12055116	KELDON JOHNSON - UNDER/OVER PLAYER POINTS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1069	2024-01-07 13:00:00
	12055116	JULIAN CHAMPAGNIE - UNDER/OVER PLAYER POINTS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1069	2024-01-07 13:00:00
	12055116	SAM MERRILL - UNDER/OVER PLAYER POINTS (Cleveland Cavaliers vs San Antonio Spurs) (Cleveland Cavaliers vs San Antonio Spurs)	Player Prop	GAME - TOTAL	No	1069	2024-01-07 13:00:00
	12055117	NICOLAS CLAXTON - UNDER/OVER PLAYER POINTS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1069	2024-01-07 15:00:00
	12055117	ROYCE O'NEALE - UNDER/OVER PLAYER POINTS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1069	2024-01-07 15:00:00
	12055117	CAMERON JOHNSON - UNDER/OVER PLAYER POINTS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1069	2024-01-07 15:00:00
	12055117	ANFERNEE SIMONS - UNDER/OVER PLAYER POINTS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1069	2024-01-07 15:00:00
	12055117	GRANT JERAMI - UNDER/OVER PLAYER POINTS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1069	2024-01-07 15:00:00
	12055117	DORIAN FINNEY SMITH - UNDER/OVER PLAYER POINTS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1069	2024-01-07 15:00:00
	12055117	SPENCER DINWIDDIE - UNDER/OVER PLAYER POINTS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1069	2024-01-07 15:00:00
	12055117	DAY'RON SHARPE - UNDER/OVER PLAYER POINTS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1069	2024-01-07 15:00:00
	12055117	CAMERON THOMAS - UNDER/OVER PLAYER POINTS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1069	2024-01-07 15:00:00
	12055117	MIKAL BRIDGES - UNDER/OVER PLAYER POINTS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1069	2024-01-07 15:00:00
	12055117	DENNIS SMITH JR. - UNDER/OVER PLAYER POINTS (Brooklyn Nets vs Portland Trail Blazers) (Brooklyn Nets vs Portland Trail Blazers)	Player Prop	GAME - TOTAL	No	1069	2024-01-07 15:00:00
	12055121	ZION WILLIAMSON - UNDER/OVER PLAYER POINTS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1069	2024-01-07 18:00:00
	12055121	MALIK MONK - UNDER/OVER PLAYER POINTS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1069	2024-01-07 18:00:00
	12055121	BRANDON INGRAM - UNDER/OVER PLAYER POINTS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1069	2024-01-07 18:00:00
	12055121	KEEGAN MURRAY - UNDER/OVER PLAYER POINTS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1069	2024-01-07 18:00:00
	12055121	CHRISTIAN JAMES MCCOLLUM - UNDER/OVER PLAYER POINTS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1069	2024-01-07 18:00:00
	12055121	DOMANTAS SABONIS - UNDER/OVER PLAYER POINTS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1069	2024-01-07 18:00:00
	12055121	HARRISON BARNES - UNDER/OVER PLAYER POINTS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1069	2024-01-07 18:00:00
	12055121	HERBERT JONES - UNDER/OVER PLAYER POINTS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1069	2024-01-07 18:00:00
	12055121	DE'AARON FOX - UNDER/OVER PLAYER POINTS (Sacramento Kings vs New Orleans Pelicans) (Sacramento Kings vs New Orleans Pelicans)	Player Prop	GAME - TOTAL	No	1069	2024-01-07 18:00:00
	12055122	PAOLO BANCHERO - UNDER/OVER PLAYER POINTS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1069	2024-01-07 18:00:00
	12055122	SADDIQ BEY - UNDER/OVER PLAYER POINTS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1069	2024-01-07 18:00:00
	12055122	CLINT CAPELA - UNDER/OVER PLAYER POINTS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1069	2024-01-07 18:00:00
	12055122	TRAE YOUNG - UNDER/OVER PLAYER POINTS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1069	2024-01-07 18:00:00
	12055122	BOGDAN BOGDANOVIC - UNDER/OVER PLAYER POINTS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1069	2024-01-07 18:00:00
	12055122	JALEN SUGGS - UNDER/OVER PLAYER POINTS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1069	2024-01-07 18:00:00
	12055122	ONYEKA OKONGWU - UNDER/OVER PLAYER POINTS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1069	2024-01-07 18:00:00
	12055122	JALEN JOHNSON - UNDER/OVER PLAYER POINTS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1069	2024-01-07 18:00:00
	12055122	MURRAY DEJOUNTE - UNDER/OVER PLAYER POINTS (Orlando Magic vs Atlanta Hawks) (Orlando Magic vs Atlanta Hawks)	Player Prop	GAME - TOTAL	No	1069	2024-01-07 18:00:00
	12055133	JADEN MCDANIELS - UNDER/OVER PLAYER POINTS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1069	2024-01-07 19:30:00
	12055133	MIKE CONLEY JR. - UNDER/OVER PLAYER POINTS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1069	2024-01-07 19:30:00
	12055133	ANTHONY EDWARDS - UNDER/OVER PLAYER POINTS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1069	2024-01-07 19:30:00
	12055133	NAZ REID - UNDER/OVER PLAYER POINTS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1069	2024-01-07 19:30:00
	12055133	NICKEIL ALEXANDER-WALKER - UNDER/OVER PLAYER POINTS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1069	2024-01-07 19:30:00
	12055133	KARL-ANTHONY TOWNS JR. - UNDER/OVER PLAYER POINTS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1069	2024-01-07 19:30:00
	12055133	RUDY GOBERT - UNDER/OVER PLAYER POINTS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1069	2024-01-07 19:30:00
	12055133	KYLE ANDERSON - UNDER/OVER PLAYER POINTS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1069	2024-01-07 19:30:00
	12055133	LUKA DONCIC - UNDER/OVER PLAYER POINTS (Dallas Mavericks vs Minnesota Timberwolves) (Dallas Mavericks vs Minnesota Timberwolves)	Player Prop	GAME - TOTAL	No	1069	2024-01-07 19:30:00
	12055132	JA MORANT - UNDER/OVER PLAYER POINTS (Phoenix Suns vs Memphis Grizzlies) (Phoenix Suns vs Memphis Grizzlies)	Player Prop	GAME - TOTAL	No	1069	2024-01-07 20:00:00
	12055132	DEVIN BOOKER - UNDER/OVER PLAYER POINTS (Phoenix Suns vs Memphis Grizzlies) (Phoenix Suns vs Memphis Grizzlies)	Player Prop	GAME - TOTAL	No	1069	2024-01-07 20:00:00
	12055141	CADE CUNNINGHAM - UNDER/OVER PLAYER POINTS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1069	2024-01-07 20:00:00
	12055141	NIKOLA JOKIC - UNDER/OVER PLAYER POINTS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1069	2024-01-07 20:00:00
	12055141	AARON GORDON - UNDER/OVER PLAYER POINTS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1069	2024-01-07 20:00:00
	12055141	MICHAEL PORTER JR. - UNDER/OVER PLAYER POINTS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1069	2024-01-07 20:00:00
	12055141	JAMAL MURRAY - UNDER/OVER PLAYER POINTS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1069	2024-01-07 20:00:00
	12055141	JALEN DUREN - UNDER/OVER PLAYER POINTS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1069	2024-01-07 20:00:00
	12055141	BOJAN BOGDANOVIC - UNDER/OVER PLAYER POINTS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1069	2024-01-07 20:00:00
	12055141	CALDWELL POPE KENTAVIOUS - UNDER/OVER PLAYER POINTS (Denver Nuggets vs Detroit Pistons) (Denver Nuggets vs Detroit Pistons)	Player Prop	GAME - TOTAL	No	1069	2024-01-07 20:00:00
	12055140	BRANDIN PODZIEMSKI - UNDER/OVER PLAYER POINTS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1069	2024-01-07 20:30:00
	12055140	KLAY THOMPSON - UNDER/OVER PLAYER POINTS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1069	2024-01-07 20:30:00
	12055140	IMMANUEL QUICKLEY - UNDER/OVER PLAYER POINTS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1069	2024-01-07 20:30:00
	12055140	JAKOB POELTL - UNDER/OVER PLAYER POINTS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1069	2024-01-07 20:30:00
	12055140	SCOTTIE BARNES - UNDER/OVER PLAYER POINTS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1069	2024-01-07 20:30:00
	12055140	STEPHEN CURRY - UNDER/OVER PLAYER POINTS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1069	2024-01-07 20:30:00
	12055140	JONATHAN KUMINGA - UNDER/OVER PLAYER POINTS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1069	2024-01-07 20:30:00
	12055140	RJ BARRETT JR. - UNDER/OVER PLAYER POINTS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1069	2024-01-07 20:30:00
	12055140	PASCAL SIAKAM - UNDER/OVER PLAYER POINTS (Golden State Warriors vs Toronto Raptors) (Golden State Warriors vs Toronto Raptors)	Player Prop	GAME - TOTAL	No	1069	2024-01-07 20:30:00
	12055115	IVICA ZUBAC - UNDER/OVER PLAYER POINTS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1069	2024-01-07 21:30:00
	12055115	TERANCE MANN - UNDER/OVER PLAYER POINTS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1069	2024-01-07 21:30:00
	12055115	TAUREAN PRINCE - UNDER/OVER PLAYER POINTS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1069	2024-01-07 21:30:00
	12055115	PAUL GEORGE - UNDER/OVER PLAYER POINTS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1069	2024-01-07 21:30:00
	12055115	LEBRON JAMES - UNDER/OVER PLAYER POINTS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1069	2024-01-07 21:30:00
	12055115	JAMES HARDEN - UNDER/OVER PLAYER POINTS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1069	2024-01-07 21:30:00
	12055115	KAWHI LEONARD - UNDER/OVER PLAYER POINTS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1069	2024-01-07 21:30:00
	12055115	ANTHONY DAVIS JR. - UNDER/OVER PLAYER POINTS (L.A. Lakers vs Los Angeles Clippers) (L.A. Lakers vs Los Angeles Clippers)	Player Prop	GAME - TOTAL	No	1069	2024-01-07 21:30:00




"""


games_count, prop_types, total_props_per_type = extract_data(text)

print(f"Number of games: {games_count}")
print(f"Types of props: {prop_types}")

print("\nTotal number of props for each type:")
for prop_type, count in total_props_per_type.items():
    print(f"{prop_type}: {count}")