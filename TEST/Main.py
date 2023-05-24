import re

data = '''
Alabama 2023 Regular Season Wins
FRI 25TH AUG 8:00PM
Over 10.5
+135
Under 10.5
−155
Arizona 2023 Regular Season Wins
FRI 25TH AUG 8:01PM
Over 5
−110
Under 5
−110
Arizona State 2023 Regular Season Wins
FRI 25TH AUG 8:02PM
Over 5
+120
Under 5
−140
'''

lines = data.strip().split('\n')
results = []

for i in range(0, len(lines), 6):
    team = lines[i]
    date = lines[i + 1]

    over_value = re.findall(r'[\d.]+', lines[i + 2])[0]
    over_odds = int(lines[i + 3].replace('−', '-'))

    under_value = re.findall(r'[\d.]+', lines[i + 4])[0]
    under_odds = int(lines[i + 5].replace('−', '-'))

    result = {
        'team': team,
        'date': date,
        'over_unders': {
            'Over': {
                float(over_value),
                over_odds
            },
            'Under': {
                float(under_value),
                under_odds
            }
        }
    }
    results.append(result)

    # Print the collected data
for result in results:
    print('Team:', result['team'])
    print('Over:', result['over_unders']['Over'])
    print('Under:', result['over_unders']['Under'])
