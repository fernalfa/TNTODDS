import requests
from bs4 import BeautifulSoup

url = 'https://sportsbook.fanduel.com/navigation/nba?tab=player-doubles'

# Realizar la solicitud HTTP GET a la página web
response = requests.get(url)

# Imprimir el HTML obtenido
print(response.text)

# Crear el objeto BeautifulSoup con el HTML obtenido
soup = BeautifulSoup(response.text, 'html.parser')

# Encontrar la tabla de jugadores
table = soup.find('table', {'class': 'table--sportsbook'})

# Encontrar todas las filas de la tabla
rows = table.find_all('tr')

# Iterar sobre cada fila y extraer el nombre del jugador y las probabilidades de dobles
for row in rows:
    # Encontrar el nombre del jugador
    name_div = row.find('div', {'class': 'name'})
    name = name_div.text.strip()

    # Encontrar las probabilidades de dobles
    odds_div = row.find('div', {'class': 'bet'})
    odds = odds_div.text.strip()

    # Imprimir los resultados
    print(f'Jugador: {name}, Probabilidades de dobles: {odds}')
