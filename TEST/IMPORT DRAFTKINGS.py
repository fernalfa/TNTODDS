import requests
from bs4 import BeautifulSoup

url = "https://sportsbook.draftkings.com/leagues/baseball/mlb?category=game-parlays"

# Send a GET request to the URL
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find the container that holds the data you want to extract
container = soup.find('div', class_='sportsbook-table__body')

# Extract specific information from the container
parlay_items = container.find_all('div', class_='sportsbook-event')

# Iterate over the parlay items and extract relevant details
for parlay in parlay_items:
    title = parlay.find('div', class_='sportsbook-event-accordion__title')
    teams = title.find_all('span', class_='sportsbook-event-accordion__title-participant')
    team1 = teams[0].text.strip()
    team2 = teams[1].text.strip()

    odds = parlay.find_all('span', class_='sportsbook-outcome-cell__line')
    team1_odds = odds[0].text.strip()
    team2_odds = odds[1].text.strip()

    print(f"Teams: {team1} vs {team2}")
    print(f"Odds: {team1_odds} vs {team2_odds}")
    print("---------------------")
