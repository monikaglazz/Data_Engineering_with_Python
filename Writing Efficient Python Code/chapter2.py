import numpy as np
# 1

# Create a list of integers (0-50) using list comprehension
nums_list_comp = [num for num in range(51)]
print(nums_list_comp)

# Create a list of integers (0-50) by unpacking range
nums_unpack = [*range(51)]
print(nums_unpack)


"""
%timeit nums_list_comp = [num for num in range(51)]
3.69 us +- 776 ns per loop (mean +- std. dev. of 7 runs, 100000 loops each)

%timeit -o nums_unpack = [*range(51)]
802 ns +- 196 ns per loop (mean +- std. dev. of 7 runs, 1000000 loops each)
"""

# 2

# Create a list using the formal name
formal_list = list()
print(formal_list)

# Create a list using the literal syntax
literal_list = []
print(literal_list)

# Print out the type of formal_list
print(type(formal_list))

# Print out the type of literal_list
print(type(literal_list))


"""
%timeit formal_list = list()
85.5 ns +- 12 ns per loop (mean +- std. dev. of 7 runs, 10000000 loops each)

%timeit literal_list = []
28.4 ns +- 3.24 ns per loop (mean +- std. dev. of 7 runs, 10000000 loops each)

"""

# 3

"""

%%timeit
hero_wts_lbs = []
for wt in wts:
    hero_wts_lbs.append(wt * 2.20462)
1.1 ms +- 72.3 us per loop (mean +- std. dev. of 7 runs, 1000 loops each)

%%timeit
wts_np = np.array(wts)
hero_wts_lbs_np = wts_np * 2.20462
21.7 us +- 939 ns per loop (mean +- std. dev. of 7 runs, 10000 loops each)
"""

# 4


def convert_units(heroes, heights, weights):

    new_hts = [ht * 0.39370 for ht in heights]
    new_wts = [wt * 2.20462 for wt in weights]

    hero_data = {}

    for i, hero in enumerate(heroes):
        hero_data[hero] = (new_hts[i], new_wts[i])

    return hero_data


heroes = ['A-Bomb', 'Abe Sapien', 'Abin Sur', 'Abomination', 'Absorbing Man', 'Adam Strange', 'Agent 13', 'Agent Bob', 'Agent Zero',
          'Air-Walker', 'Ajax', 'Alan Scott', 'Alfred Pennyworth', 'Alien', 'Amazo', 'Ammo', 'Angel', 'Angel Dust', 'Angel Salvadore',
          'Animal Man', 'Annihilus', 'Ant-Man', 'Ant-Man II', 'Anti-Venom', 'Apocalypse', 'Aqualad', 'Aquaman', 'Arachne', 'Archangel',
          'Arclight', 'Ardina', 'Ares', 'Ariel', 'Armor', 'Atlas', 'Atom', 'Atom Girl', 'Atom II', 'Aurora', 'Azazel', 'Bane', 'Banshee',
          'Bantam', 'Batgirl', 'Batgirl IV', 'Batgirl VI', 'Batman', 'Batman II']

hts = np.array([203.,  191.,  185.,  203.,  193.,  185., 173.,  178.,  191.,  188.,  193.,  180.,
                178.,  244.,  257.,  188.,  183.,  165.,  163.,  183.,  180.,  211.,  183.,  229.,
                213.,  178.,  185.,  175.,  183.,  173.,  193.,  185.,  165.,  163.,  183.,  178.,
                168.,  183.,  180.,  183.,  203.,  183.,  165.,  170.,  165.,  168.,  188.,  178.,
                ])

wts = np.array([441.,  65.,  90., 441., 122.,  88.,  61.,  81., 104., 108.,  90.,  90.,  72., 169.,
                173., 101.,  68.,  57.,  54.,  83.,  90., 122.,  86., 358., 135., 106., 146., 63.,
                68.,  57.,  98., 270.,  59.,  50., 101., 68., 54., 81., 63., 67., 180., 77.,
                54.,  57., 52.,  61.,  95., 79.,
                ])


"""
pip install line_profiler

%load_ext line_profiler
%lprun -f convert_units convert_units(heroes, hts, wts)

Timer unit: 1e-06 s

Total time: 0.002053 s
File: <ipython-input-1-2ae8c0194a47>
Function: convert_units at line 1

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     1                                           def convert_units(heroes, heights, weights):
     2                                           
     3         1        339.0    339.0     16.5      new_hts = [ht * 0.39370  for ht in heights]
     4         1        304.0    304.0     14.8      new_wts = [wt * 2.20462  for wt in weights]
     5                                           
     6         1          1.0      1.0      0.0      hero_data = {}
     7                                           
     8       481        698.0      1.5     34.0      for i,hero in enumerate(heroes):
     9       480        710.0      1.5     34.6          hero_data[hero] = (new_hts[i], new_wts[i])
    10                                                   
    11         1          1.0      1.0      0.0      return hero_data
"""

# 5


def convert_units_broadcast(heroes, heights, weights):

    # Array broadcasting instead of list comprehension
    new_hts = heights * 0.39370
    new_wts = weights * 2.20462

    hero_data = {}

    for i, hero in enumerate(heroes):
        hero_data[hero] = (new_hts[i], new_wts[i])

    return hero_data


"""
%load_ext line_profiler
%lprun -f convert_units_broadcast convert_units_broadcast(heroes, hts, wts)

Timer unit: 1e-06 s

Total time: 0.001159 s
File: <ipython-input-1-84e44a6b12f5>
Function: convert_units_broadcast at line 1

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     1                                           def convert_units_broadcast(heroes, heights, weights):
     2                                           
     3                                               # Array broadcasting instead of list comprehension
     4         1         86.0     86.0      7.4      new_hts = heights * 0.39370
     5         1          6.0      6.0      0.5      new_wts = weights * 2.20462
     6                                           
     7         1          0.0      0.0      0.0      hero_data = {}
     8                                           
     9       481        447.0      0.9     38.6      for i,hero in enumerate(heroes):
    10       480        619.0      1.3     53.4          hero_data[hero] = (new_hts[i], new_wts[i])
    11                                                   
    12         1          1.0      1.0      0.1      return hero_data

"""

# 6


def calc_bmi_lists(sample_indices, hts, wts):

    # Gather sample heights and weights as lists
    s_hts = [hts[i] for i in sample_indices]
    s_wts = [wts[i] for i in sample_indices]

    # Convert heights from cm to m and square with list comprehension
    s_hts_m_sqr = [(ht / 100) ** 2 for ht in s_hts]

    # Calculate BMIs as a list with list comprehension
    bmis = [s_wts[i] / s_hts_m_sqr[i] for i in range(len(sample_indices))]

    return bmis


"""
from bmi_lists import calc_bmi_lists

%load_ext memory_profiler

%mprun -f calc_bmi_lists calc_bmi_lists(sample_indices, hts, wts)

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     1     89.1 MiB     89.1 MiB           1   def calc_bmi_lists(sample_indices, hts, wts):
     2                                         
     3                                             # Gather sample heights and weights as lists
     4     89.9 MiB      0.8 MiB       25003       s_hts = [hts[i] for i in sample_indices]
     5     90.6 MiB      0.8 MiB       25003       s_wts = [wts[i] for i in sample_indices]
     6                                         
     7                                             # Convert heights from cm to m and square with list comprehension
     8     91.6 MiB      1.0 MiB       25003       s_hts_m_sqr = [(ht / 100) ** 2 for ht in s_hts]
     9                                         
    10                                             # Calculate BMIs as a list with list comprehension
    11     92.4 MiB      0.8 MiB       25003       bmis = [s_wts[i] / s_hts_m_sqr[i] for i in range(len(sample_indices))]
    12                                         
    13     92.4 MiB      0.0 MiB           1       return bmis
"""

# 7


def calc_bmi_arrays(sample_indices, hts, wts):

    # Gather sample heights and weights as arrays
    s_hts = hts[sample_indices]
    s_wts = wts[sample_indices]

    # Convert heights from cm to m and square with broadcasting
    s_hts_m_sqr = (s_hts / 100) ** 2

    # Calculate BMIs as an array using broadcasting
    bmis = s_wts / s_hts_m_sqr

    return bmis


"""
from bmi_arrays import calc_bmi_arrays

%load_ext memory_profiler

%mprun -f calc_bmi_arrays calc_bmi_arrays(sample_indices, hts, wts)


Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     1    113.9 MiB    113.9 MiB           1   def calc_bmi_arrays(sample_indices, hts, wts):
     2                                         
     3                                             # Gather sample heights and weights as arrays
     4    113.9 MiB      0.0 MiB           1       s_hts = hts[sample_indices]
     5    113.9 MiB      0.0 MiB           1       s_wts = wts[sample_indices]
     6                                         
     7                                             # Convert heights from cm to m and square with broadcasting
     8    113.9 MiB      0.0 MiB           1       s_hts_m_sqr = (s_hts / 100) ** 2
     9                                         
    10                                             # Calculate BMIs as an array using broadcasting
    11    113.9 MiB      0.0 MiB           1       bmis = s_wts / s_hts_m_sqr
    12                                         
    13    113.9 MiB      0.0 MiB           1       return bmis
"""

# 8


def get_publisher_heroes(heroes, publishers, desired_publisher):

    desired_heroes = []

    for i, pub in enumerate(publishers):
        if pub == desired_publisher:
            desired_heroes.append(heroes[i])

    return desired_heroes


def get_publisher_heroes_np(heroes, publishers, desired_publisher):

    heroes_np = np.array(heroes)
    pubs_np = np.array(publishers)

    desired_heroes = heroes_np[pubs_np == desired_publisher]

    return desired_heroes


publishers = ['Marvel Comics', 'Dark Horse Comics', 'DC Comics', 'Marvel Comics', 'Marvel Comics', 'DC Comics', 'Marvel Comics', 'Marvel Comics',
              'Marvel Comics', 'Marvel Comics', 'Marvel Comics', 'DC Comics', 'DC Comics', 'Dark Horse Comics', 'DC Comics', 'Marvel Comics',
              'Marvel Comics', 'Marvel Comics', 'Marvel Comics', 'DC Comics', 'Marvel Comics', 'Marvel Comics', 'Marvel Comics', 'Marvel Comics',
              'Marvel Comics', 'DC Comics', 'DC Comics', 'Marvel Comics', 'Marvel Comics', 'Marvel Comics', 'Marvel Comics', 'Marvel Comics',
              'Marvel Comics', 'Marvel Comics', 'Marvel Comics', 'DC Comics', 'DC Comics', 'DC Comics', 'Marvel Comics', 'Marvel Comics',
              'DC Comics', 'Marvel Comics', 'Marvel Comics', 'DC Comics', 'DC Comics', 'DC Comics', 'DC Comics', 'DC Comics']


# Use get_publisher_heroes() to gather Star Wars heroes
star_wars_heroes = get_publisher_heroes(heroes, publishers, 'George Lucas')

print(star_wars_heroes)
print(type(star_wars_heroes))

# Use get_publisher_heroes_np() to gather Star Wars heroes
star_wars_heroes_np = get_publisher_heroes_np(
    heroes, publishers, 'George Lucas')

print(star_wars_heroes_np)
print(type(star_wars_heroes_np))

"""
%load_ext line_profiler

%lprun -f get_publisher_heroes get_publisher_heroes(heroes, publishers, 'George Lucas')

Timer unit: 1e-06 s

Total time: 0.00037 s
File: <ipython-input-1-5a6bc05c1c55>
Function: get_publisher_heroes at line 1

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     1                                           def get_publisher_heroes(heroes, publishers, desired_publisher):
     2                                           
     3         1          2.0      2.0      0.5      desired_heroes = []
     4                                           
     5       481        176.0      0.4     47.6      for i,pub in enumerate(publishers):
     6       480        176.0      0.4     47.6          if pub == desired_publisher:
     7         4         16.0      4.0      4.3              desired_heroes.append(heroes[i])
     8                                           
     9         1          0.0      0.0      0.0      return desired_heroes


     
%lprun -f get_publisher_heroes_np get_publisher_heroes_np(heroes, publishers, 'George Lucas')

Timer unit: 1e-06 s

Total time: 0.000262 s
File: <ipython-input-1-5a6bc05c1c55>
Function: get_publisher_heroes_np at line 12

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    12                                           def get_publisher_heroes_np(heroes, publishers, desired_publisher):
    13                                           
    14         1        180.0    180.0     68.7      heroes_np = np.array(heroes)
    15         1         56.0     56.0     21.4      pubs_np = np.array(publishers)
    16                                           
    17         1         25.0     25.0      9.5      desired_heroes = heroes_np[pubs_np == desired_publisher]
    18                                           
    19         1          1.0      1.0      0.4      return desired_heroes


    
from hero_funcs import get_publisher_heroes
%load_ext memory_profiler
%mprun -f get_publisher_heroes get_publisher_heroes(heroes, publishers, 'George Lucas')
    
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     4    114.4 MiB    114.4 MiB           1   def get_publisher_heroes(heroes, publishers, desired_publisher):
     5                                         
     6    114.4 MiB      0.0 MiB           1       desired_heroes = []
     7                                         
     8    114.4 MiB      0.0 MiB         481       for i,pub in enumerate(publishers):
     9    114.4 MiB      0.0 MiB         480           if pub == desired_publisher:
    10    114.4 MiB      0.0 MiB           4               desired_heroes.append(heroes[i])
    11                                         
    12    114.4 MiB      0.0 MiB           1       return desired_heroes
    
    
from hero_funcs  import get_publisher_heroes_np
%mprun -f get_publisher_heroes_np get_publisher_heroes_np(heroes, publishers, 'George Lucas')

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    15    114.4 MiB    114.4 MiB           1   def get_publisher_heroes_np(heroes, publishers, desired_publisher):
    16                                         
    17    114.4 MiB      0.0 MiB           1       heroes_np = np.array(heroes)
    18    114.4 MiB      0.0 MiB           1       pubs_np = np.array(publishers)
    19                                         
    20    114.4 MiB      0.0 MiB           1       desired_heroes = heroes_np[pubs_np == desired_publisher]
    21                                         
    22    114.4 MiB      0.0 MiB           1       return desired_heroes
"""
