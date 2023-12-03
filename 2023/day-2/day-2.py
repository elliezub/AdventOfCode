#Determine which games would have been possible if the bag had been loaded with only 
# 12 red cubes, 
# 13 green cubes, 
# and 14 blue cubes. 
# What is the sum of the IDs of those games?
import re

puzzle_input = open("puzzle-input.txt", "r")

organized_games = {}

possible_games_sum = 0
game_number = 0
max_red = 12
max_green = 13
max_blue = 14

for line in puzzle_input:
    game_number += 1
    individual_rounds = []
    rounds_data = line.strip().split(';')

    for round_data in rounds_data:
        round_dict = {}
        # get the color/count pairs for each round
        pairs = re.findall(r'(\d+)\s*(red|green|blue)', round_data)
          
        # add color/count pairs to round dict
        for count, color in pairs:
            round_dict[color] = int(count)
        
        individual_rounds.append(round_dict)

    organized_games[game_number] = individual_rounds # add colors and counts here

for game_num in organized_games:
    for game in organized_games[game_num]:
        game_possible = True
        
        for color in game:
            if (color == "red" and game[color] > max_red) or \
               (color == "green" and game[color] > max_green) or \
               (color == 'blue' and game[color] > max_blue):
                game_possible = False
                break 

        if not game_possible:
            break

    if game_possible == True:
        possible_games_sum += game_num
    
print(possible_games_sum)

puzzle_input.close()