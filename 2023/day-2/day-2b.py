
# part 2 - in progress
# For each game, find the minimum set of cubes that must have been present. 
# What is the sum of the power of these sets?

# The power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together.
import re

puzzle_input = open("puzzle-input.txt", "r")

organized_games = {}

total_power_sum = 0
game_number = 0

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

# For each game in organized games:
#     For each round in game:
#       For each color in the round:
#         Update all colors to the max val in that round

for game_num in organized_games:
    min_red = 0
    min_green = 0
    min_blue = 0

    for game in organized_games[game_num]:
        for color in game:
            if color == "red" and game[color] > min_red:
                min_red = game[color]
            if color == "green" and game[color] > min_green:
                min_green = game[color]
            if color == "blue" and game[color] > min_blue:
                min_blue = game[color]

    total_power_sum += min_red * min_blue * min_green

print(total_power_sum)

puzzle_input.close()