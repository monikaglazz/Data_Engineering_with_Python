from collections import Counter
from itertools import combinations
import numpy as np

# 1

names = ['Abomasnow', 'Abra', 'Absol', 'Accelgor', 'Aerodactyl', 'Aggron', 'Aipom', 'Alakazam', 'Alomomola',
         'Altaria', 'Amaura', 'Ambipom', 'Amoonguss', 'Ampharos', 'Anorith', 'Arbok', 'Arcanine', 'Arceus',
         'Archen', 'Archeops', 'Ariados', 'Armaldo', 'Aromatisse', 'Aron', 'Articuno', 'Audino', 'Aurorus',
         'Avalugg', 'Axew', 'Azelf', 'Azumarill', 'Azurill', 'Bagon', 'Baltoy', 'Banette', 'Barbaracle',
         'Barboach', 'Basculin', 'Bastiodon', 'Bayleef', 'Beartic', 'Beautifly', 'Beedrill', 'Beheeyem',
         'Beldum', 'Bellossom', 'Bellsprout', 'Bergmite']
primary_types = ['Grass', 'Psychic', 'Dark', 'Bug', 'Rock', 'Steel', 'Normal', 'Psychic', 'Water', 'Dragon',
                 'Rock', 'Normal', 'Grass', 'Electric', 'Rock', 'Poison', 'Fire', 'Normal', 'Rock', 'Rock',
                 'Bug', 'Rock', 'Fairy', 'Steel', 'Ice', 'Normal', 'Rock', 'Ice', 'Dragon', 'Psychic',
                 'Water', 'Normal', 'Dragon', 'Ground', 'Ghost', 'Rock', 'Water', 'Water', 'Rock', 'Grass',
                 'Ice', 'Bug', 'Bug', 'Psychic', 'Steel', 'Grass', 'Grass', 'Ice']
secondary_types = ['Ice', 'nan', 'nan', 'nan', 'Flying', 'Rock', 'nan', 'nan', 'nan', 'Flying',
                   'Ice', 'nan', 'Poison', 'nan', 'Bug', 'nan', 'nan', 'nan', 'Flying', 'Flying',
                   'Poison', 'Bug', 'nan', 'Rock', 'Flying', 'nan', 'Ice', 'nan', 'nan', 'nan',
                   'Fairy', 'Fairy', 'nan', 'Psychic', 'nan', 'Water', 'Ground', 'nan', 'Steel', 'nan',
                    'nan', 'Flying', 'Poison', 'nan', 'Psychic', 'nan', 'Poison', 'nan']


# Combine names and primary_types
names_type1 = [*zip(names, primary_types)]

print(*names_type1[:5], sep='\n')

# Combine all three lists together
names_types = [*zip(names, primary_types, secondary_types)]

print(*names_types[:5], sep='\n')

# Combine five items from names and three items from primary_types
differing_lengths = [*zip(names[:5], primary_types[:3])]

print(*differing_lengths, sep='\n')

# 2

generations = [1, 1, 1, 5, 3, 5, 1, 6, 1, 6, 5, 5, 4, 6, 3, 4, 2, 5, 2, 5, 4, 1,
               1, 2, 6, 5, 5, 6, 6, 1, 4, 5, 6, 2, 6, 1, 3, 2, 4, 1, 5, 3, 5, 5, 1, 5, 5, 5]

# Collect the count of primary types
type_count = Counter(primary_types)
print(type_count, '\n')

# Collect the count of generations
gen_count = Counter(generations)
print(gen_count, '\n')

# Use list comprehension to get each Pokémon's starting letter
starting_letters = [name[0] for name in names]

# Collect the count of Pokémon for each starting_letter
starting_letters_count = Counter(starting_letters)
print(starting_letters_count)

# 3

pokemon = ['Geodude', 'Cubone', 'Lickitung', 'Persian', 'Diglett']

# Create a combination object with pairs of Pokémon
combos_obj = combinations(pokemon, 2)
print(type(combos_obj), '\n')

# Convert combos_obj to a list by unpacking
combos_2 = [*combos_obj]
print(combos_2, '\n')

# Collect all possible combinations of 4 Pokémon directly into a list
combos_4 = [*combinations(pokemon, 4)]
print(combos_4)

# 4

ash_pokedex = ['Pikachu', 'Bulbasaur', 'Koffing', 'Spearow',
               'Vulpix', 'Wigglytuff', 'Zubat', 'Rattata', 'Psyduck', 'Squirtle']

misty_pokedex = ['Krabby', 'Horsea', 'Slowbro', 'Tentacool',
                 'Vaporeon', 'Magikarp', 'Poliwag', 'Starmie', 'Psyduck', 'Squirtle']

# Convert both lists to sets
ash_set = set(ash_pokedex)
misty_set = set(misty_pokedex)

# Find the Pokémon that exist in both sets
both = ash_set.intersection(misty_set)
print(both)

# Find the Pokémon that Ash has and Misty does not have
ash_only = ash_set.difference(misty_set)
print(ash_only)

# Find the Pokémon that are in only one set (not both)
unique_to_set = ash_set.symmetric_difference(misty_set)
print(unique_to_set)


# 5

brock_pokedex = ['Onix', 'Geodude', 'Zubat', 'Golem', 'Vulpix',
                 'Tauros', 'Kabutops', 'Omastar', 'Machop', 'Dugtrio']

# Convert Brock's Pokédex to a set
brock_pokedex_set = set(brock_pokedex)
print(brock_pokedex_set)

# Check if Psyduck is in Ash's list and Brock's set
print('Psyduck' in ash_pokedex)
print('Psyduck' in brock_pokedex_set)

# Check if Machop is in Ash's list and Brock's set
print('Machop' in ash_pokedex)
print('Machop' in brock_pokedex_set)

"""
%timeit 'Psyduck' in ash_pokedex
212 ns +- 49.6 ns per loop (mean +- std. dev. of 7 runs, 10000000 loops each)

%timeit 'Psyduck' in brock_pokedex_set
38.4 ns +- 6.49 ns per loop (mean +- std. dev. of 7 runs, 10000000 loops each)

%timeit 'Machop' in ash_pokedex
169 ns +- 5.76 ns per loop (mean +- std. dev. of 7 runs, 10000000 loops each)

%timeit 'Machop' in brock_pokedex_set
34.7 ns +- 4.24 ns per loop (mean +- std. dev. of 7 runs, 10000000 loops each)

"""


# 6

def find_unique_items(data):
    uniques = []

    for item in data:
        if item not in uniques:
            uniques.append(item)

    return uniques


# Use find_unique_items() to collect unique Pokémon names
uniq_names_func = find_unique_items(names)
print(len(uniq_names_func))

# Convert the names list to a set to collect unique Pokémon names
uniq_names_set = set(names)
print(len(uniq_names_set))

# Check that both unique collections are equivalent
print(sorted(uniq_names_func) == sorted(uniq_names_set))

# Use the best approach to collect unique primary types and generations
uniq_types = set(primary_types)
uniq_gens = set(generations)
print(uniq_types, uniq_gens, sep='\n')

"""
%timeit find_unique_items(names)
2.33 ms +- 286 us per loop (mean +- std. dev. of 7 runs, 100 loops each)

%timeit  set(names)
8.98 us +- 366 ns per loop (mean +- std. dev. of 7 runs, 100000 loops each)

"""

# 7

gen1_gen2_name_lengths_loop = []

for name, gen in zip(names, generations):
    if gen < 3:
        name_length = len(name)
        poke_tuple = (name, name_length)
        gen1_gen2_name_lengths_loop.append(poke_tuple)

# Collect Pokémon that belong to generation 1 or generation 2
gen1_gen2_pokemon = [name for name, gen in zip(names, generations) if gen < 3]

# Create a map object that stores the name lengths
name_lengths_map = map(len, gen1_gen2_pokemon)

# Combine gen1_gen2_pokemon and name_lengths_map into a list
gen1_gen2_name_lengths = [*zip(gen1_gen2_pokemon, name_lengths_map)]

print(gen1_gen2_name_lengths_loop[:5])
print(gen1_gen2_name_lengths[:5])


# 8

#  Each column represents an individual Pokémon stat (HP, Attack, Defense, Special Attack, Special Defense, and Speed respectively)
stats = np.array([[90,  92,  75,  92,  85,  60],
                  [25,  20,  15, 105,  55,  90],
                  [65, 130,  60,  75,  60,  75],
                  [80,  70,  40, 100,  60, 145],
                  [80, 105,  65,  60,  75, 130],
                  [70, 110, 180,  60,  60,  50],
                  [55,  70,  55,  40,  55,  85],
                  [55,  50,  45, 135,  95, 120],
                  [165,  75,  80,  40,  45,  65],
                  [75,  70,  90,  70, 105,  80],
                  [77,  59,  50,  67,  63,  46],
                  [75, 100,  66,  60,  66, 115],
                  [114,  85,  70,  85,  80,  30],
                  [90,  75,  85, 115,  90,  55],
                  [45,  95,  50,  40,  50,  75],
                  [60,  85,  69,  65,  79,  80],
                  [90, 110,  80, 100,  80,  95],
                  [120, 120, 120, 120, 120, 120],
                  [55, 112,  45,  74,  45,  70],
                  [75, 140,  65, 112,  65, 110],
                  [70,  90,  70,  60,  60,  40],
                  [75, 125, 100,  70,  80,  45],
                  [101,  72,  72,  99,  89,  29],
                  [50,  70, 100,  40,  40,  30],
                  [90,  85, 100,  95, 125,  85],
                  [103,  60,  86,  60,  86,  50],
                  [123,  77,  72,  99,  92,  58],
                  [95, 117, 184,  44,  46,  28],
                  [46,  87,  60,  30,  40,  57],
                  [75, 125,  70, 125,  70, 115],
                  [100,  50,  80,  60,  80,  50],
                  [50,  20,  40,  20,  40,  20],
                  [45,  75,  60,  40,  30,  50],
                  [40,  40,  55,  40,  70,  55],
                  [64, 115,  65,  83,  63,  65],
                  [72, 105, 115,  54,  86,  68],
                  [50,  48,  43,  46,  41,  60],
                  [70,  92,  65,  80,  55,  98],
                  [60,  52, 168,  47, 138,  30],
                  [60,  62,  80,  63,  80,  60],
                  [95, 110,  80,  70,  80,  50],
                  [60,  70,  50, 100,  50,  65],
                  [65,  90,  40,  45,  80,  75],
                  [75,  75,  75, 125,  95,  40],
                  [40,  55,  80,  35,  60,  30],
                  [75,  80,  95,  90, 100,  50],
                  [50,  75,  35,  70,  30,  40],
                  [55,  69,  85,  32,  35,  28],
                  [79,  85,  60,  55,  60,  71]])


# Create a total stats array
total_stats_np = stats.sum(axis=1)

# Create an average stats array
avg_stats_np = stats.mean(axis=1)

# Combine names, total_stats_np, and avg_stats_np into a list
poke_list_np = [*zip(names, total_stats_np, avg_stats_np)]

top_3 = sorted(poke_list_np, key=lambda x: x[1], reverse=True)[:3]
print('3 strongest Pokémon:\n{}'.format(top_3))

# 9

"""
for gen,count in gen_counts.items():
    total_count = len(generations)
    gen_percent = round(count / total_count * 100, 2)
    print(
      'generation {}: count = {:3} percentage = {}'
      .format(gen, count, gen_percent)
    )
"""

# Collect the count of each generation
gen_counts = Counter(generations)

# Improve for loop by moving one calculation above the loop
total_count = len(generations)

for gen, count in gen_counts.items():
    gen_percent = round(count / total_count * 100, 2)
    print('generation {}: count = {:3} percentage = {}'
          .format(gen, count, gen_percent))

# 10

pokemon_types = ['Bug', 'Dark', 'Dragon', 'Electric', 'Fairy', 'Fighting', 'Fire', 'Flying',
                 'Ghost', 'Grass', 'Ground', 'Ice', 'Normal', 'Poison', 'Psychic', 'Rock', 'Steel', 'Water']

"""
enumerated_pairs = []

for i,pair in enumerate(possible_pairs, 1):
    enumerated_pair_tuple = (i,) + pair
    enumerated_pair_list = list(enumerated_pair_tuple)
    enumerated_pairs.append(enumerated_pair_list)
    
"""

# Collect all possible pairs using combinations()
possible_pairs = [*combinations(pokemon_types, 2)]

# Create an empty list called enumerated_tuples
enumerated_tuples = []

# Append each enumerated_pair_tuple to the empty list above
for i, pair in enumerate(possible_pairs, 1):
    enumerated_pair_tuple = (i,) + pair
    enumerated_tuples.append(enumerated_pair_tuple)

# Convert all tuples in enumerated_tuples to a list
enumerated_pairs = [*map(list, enumerated_tuples)]
print(enumerated_pairs)


# 11

# Each Pokémon's corresponding Health Points
hps = np.array([80.,  60., 131.,  62.,  71., 109.,  45.,  53.,  73.,  60.,  37.,
                63.,  59.,  84.,  25.,  50.,  98., 116.,  29.,  85.,  43.,  46.,
                46.,  57.,  94.,  87.,  70.,  59.,  68.,  65.,  89.,  52.,  68.,
                66.,  67.,  75.,  73., 103.,  66., 109.,  60.,  56.,  71.,  77.,
                75., 102.,  98.,  81.,  60.])

"""
The below code was written to calculate the HP z-score for each Pokémon and gather the Pokémon with the highest HPs based on their z-scores:

poke_zscores = []

for name,hp in zip(names, hps):
    hp_avg = hps.mean()
    hp_std = hps.std()
    z_score = (hp - hp_avg)/hp_std
    poke_zscores.append((name, hp, z_score))
highest_hp_pokemon = []

for name,hp,zscore in poke_zscores:
    if zscore > 2:
        highest_hp_pokemon.append((name, hp, zscore))

"""

# Calculate the total HP avg and total HP standard deviation
hp_avg = hps.mean()
hp_std = hps.std()

# Use NumPy to eliminate the previous for loop
z_scores = (hps - hp_avg)/hp_std

# Combine names, hps, and z_scores
poke_zscores2 = [*zip(names, hps, z_scores)]
print(*poke_zscores2[:3], sep='\n')

# Use list comprehension with the same logic as the highest_hp_pokemon code block
highest_hp_pokemon2 = [(name, hps, zscore)
                       for name, hps, zscore in poke_zscores2 if zscore > 2]
print(*highest_hp_pokemon2, sep='\n')
