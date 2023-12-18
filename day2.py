
from collections import Counter


def parse_turns(turns):
    colors = ['red', 'green', 'blue']
    max_colors = {color: 0 for color in colors}
    turns = turns.replace(';', ',')
    for cube in turns.split(','):
        cube = cube.strip()
        for color in colors:
            if color in cube:
                n_cubes = int(cube.split(' ')[0])
                if n_cubes > max_colors[color]:
                    max_colors[color] = n_cubes
    
    power = 1
    for val in max_colors.values():
        power *= val
    return (max_colors, power)


file = open("input2.txt", "r")
lines = file.readlines()

for line in lines:
    print(line)

games = {int(line.split(':')[0].replace('Game ', '')): line.split(':')[1].replace('\n', '') for line in lines}

game_sum = 0
game_sum_2 = 0
for id_game, game in games.items():
    print(id_game, game)
    max_colors, power = parse_turns(game)
    game_sum_2 += power
    if (max_colors["red"] <= 12) and (max_colors["green"] <= 13) and (max_colors["blue"] <= 14):
        print(f"{id_game} nailed it!")
        game_sum += id_game

print(game_sum)
print(game_sum_2)


turns = "12 green, 5 red, 9 blue; 3 blue, 3 green, 2 red; 5 green, 2 blue; 5 green, 7 red, 10 blue; 7 red, 10 blue, 10 green"
turns = turns.replace(';', ',')
lst = turns.split(',')

{cube.split(' ')[1]: 0 for cube in turns.split(',')}

target = "12 red cubes, 13 green cubes, and 14 blue"
