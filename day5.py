

file = open("input5.txt", "r")
lines = file.readlines()

seeds = []
fert_map = {
    'seed-to-soil': [],
    'soil-to-fertilizer': [],
    'fertilizer-to-water': [],
    'water-to-light': [],
    'light-to-temperature': [],
    'temperature-to-humidity': [],
    'humidity-to-location': []
}

current_map = ''

for line in lines:
    line = line.replace('\n', '')
    if line.strip() == '':
        current_map = ''
        continue

    if 'seeds' in line:
        seeds = [int(i) for i in line.split(':')[1].strip().split(' ')]
        continue

    skip = False
    for m in fert_map.keys():
        if m in line:
            current_map = m
            skip = True
            break

    if skip:
        continue
    line = [int(i) for i in line.strip().split(' ')]
    fert_map[current_map].append(line)

print(fert_map)


dest_map = {}
for k in fert_map.keys():
    print(k)
    init_range = [i for i in range(4300000000)]
    for vals in fert_map[k]:
        dest_start = vals[0]
        source_start = vals[1]
        range_length = vals[2]
        source_range = [i for i in range(source_start, source_start + range_length)]
        dest_range = [i for i in range(dest_start, dest_start + range_length)]

        for idx in range(len(source_range)):
            init_range[source_range[idx]] = dest_range[idx]
    
    dest_map[k] = {i: init_range[i] for i in range(len(init_range))}

results = []
for seed in seeds:
    s = dest_map['seed-to-soil'][seed]
    f = dest_map['soil-to-fertilizer'][s]
    w = dest_map['fertilizer-to-water'][f]
    l = dest_map['water-to-light'][w]
    t = dest_map['light-to-temperature'][l]
    h = dest_map['temperature-to-humidity'][t]
    res = dest_map['humidity-to-location'][h]
    print(seed, res)
    results.append(res)

print(min(results))
