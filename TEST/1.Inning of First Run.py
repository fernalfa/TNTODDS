import re

def get_input_data():
    with open("../0.INFO", "r") as f:
        data = f.read()
        input_data = []
        for line in data.split("\n"):
            if line:
                match = re.match(r"^(.*)\s+-\s+(.*)$", line)
                if match:
                    game = {
                        "Team": match.group(1),
                        "Inning of First Run": match.group(2),
                    }
                    input_data.append(game)
    return input_data

def get_inning_of_first_run(input_data):
    inning_of_first_run = {}
    for game in input_data:
        inning_of_first_run[game["Team"]] = game["Inning of First Run"]
    return inning_of_first_run

def get_inning_of_last_run(input_data):
    inning_of_last_run = {}
    for game in input_data:
        inning_of_last_run[game["Team"]] = game["Inning of Last Run"]
    return inning_of_last_run

if __name__ == "__main__":
    input_data = get_input_data()
    inning_of_first_run = get_inning_of_first_run(input_data)
    inning_of_last_run = get_inning_of_last_run(input_data)
    print(inning_of_first_run)
    print(inning_of_last_run)