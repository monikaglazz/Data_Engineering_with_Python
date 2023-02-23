import pandas as pd
import numpy as np

# 1

pit_list = [['PIT', 'NL', 2012, 651, 674, 79, 162, 0], ['PIT', 'NL', 2011, 610, 712, 72, 162, 0], ['PIT', 'NL',
                                                                                                   2010, 587, 866, 57, 162, 0], ['PIT', 'NL', 2009, 636, 768, 62, 161, 0], ['PIT', 'NL', 2008, 735, 884, 67, 162, 0]]
col = ['Team', 'League', 'Year', 'RS', 'RA', 'W', 'G', 'Playoffs']
pit_df = pd.DataFrame(pit_list, columns=col)

# Iterate over pit_df and print each index variable and then each row
for i, row in pit_df.iterrows():
    print(i)
    print(row)
    print(type(row))

# Print the row and type of each row
for row_tuple in pit_df.iterrows():
    print(row_tuple)
    print(type(row_tuple))

# 2


def calc_run_diff(runs_scored, runs_allowed):
    run_diff = runs_scored - runs_allowed
    return run_diff


giants_list = [['SFG', 'NL', 2012, 718, 649, 94, 162, 1],
               ['SFG', 'NL', 2011, 570, 578, 86, 162, 0],
               ['SFG', 'NL', 2010, 697, 583, 92, 162, 1],
               ['SFG', 'NL', 2009, 657, 611, 88, 162, 0],
               ['SFG', 'NL', 2008, 640, 759, 72, 162, 0]]

giants_df = pd.DataFrame(giants_list, columns=col)

# Create an empty list to store run differentials
run_diffs = []

# Write a for loop and collect runs allowed and runs scored for each row
for i, row in giants_df.iterrows():
    runs_scored = row['RS']
    runs_allowed = row['RA']

    # Use the provided function to calculate run_diff for each row
    run_diff = calc_run_diff(runs_scored, runs_allowed)

    # Append each run differential to the output list
    run_diffs.append(run_diff)

giants_df['RD'] = run_diffs
print(giants_df)

# 3

rangers_list = [['TEX', 'AL', 2012, 808, 707, 93, 162, 1],
                ['TEX', 'AL', 2011, 855, 677, 96, 162, 1],
                ['TEX', 'AL', 2010, 787, 687, 90, 162, 1],
                ['TEX', 'AL', 2009, 784, 740, 87, 162, 0],
                ['TEX', 'AL', 2008, 901, 967, 79, 162, 0],
                ['TEX', 'AL', 2007, 816, 844, 75, 162, 0],
                ['TEX', 'AL', 2006, 835, 784, 80, 162, 0],
                ['TEX', 'AL', 2005, 865, 858, 79, 162, 0],
                ['TEX', 'AL', 2004, 860, 794, 89, 162, 0],
                ['TEX', 'AL', 2003, 826, 969, 71, 162, 0],
                ['TEX', 'AL', 2002, 843, 882, 72, 162, 0],
                ['TEX', 'AL', 2001, 890, 968, 73, 162, 0],
                ['TEX', 'AL', 2000, 848, 974, 71, 162, 0],
                ['TEX', 'AL', 1999, 945, 859, 95, 162, 1],
                ['TEX', 'AL', 1998, 940, 871, 88, 162, 1],
                ['TEX', 'AL', 1997, 807, 823, 77, 162, 0],
                ['TEX', 'AL', 1996, 928, 799, 90, 163, 1],
                ['TEX', 'AL', 1993, 835, 751, 86, 162, 0],
                ['TEX', 'AL', 1992, 682, 753, 77, 162, 0],
                ['TEX', 'AL', 1991, 829, 814, 85, 162, 0],
                ['TEX', 'AL', 1990, 676, 696, 83, 162, 0],
                ['TEX', 'AL', 1989, 695, 714, 83, 162, 0],
                ['TEX', 'AL', 1988, 637, 735, 70, 161, 0],
                ['TEX', 'AL', 1987, 823, 849, 75, 162, 0],
                ['TEX', 'AL', 1986, 771, 743, 87, 162, 0],
                ['TEX', 'AL', 1985, 617, 785, 62, 161, 0],
                ['TEX', 'AL', 1984, 656, 714, 69, 161, 0],
                ['TEX', 'AL', 1983, 639, 609, 77, 163, 0],
                ['TEX', 'AL', 1982, 590, 749, 64, 162, 0],
                ['TEX', 'AL', 1980, 756, 752, 76, 163, 0],
                ['TEX', 'AL', 1979, 750, 698, 83, 162, 0],
                ['TEX', 'AL', 1978, 692, 632, 87, 162, 0],
                ['TEX', 'AL', 1977, 767, 657, 94, 162, 0],
                ['TEX', 'AL', 1976, 616, 652, 76, 162, 0],
                ['TEX', 'AL', 1975, 714, 733, 79, 162, 0],
                ['TEX', 'AL', 1974, 690, 698, 83, 161, 0],
                ['TEX', 'AL', 1973, 619, 844, 57, 162, 0]]

rangers_df = pd.DataFrame(rangers_list, columns=col)

# Loop over the DataFrame and print each row's Index, Year and Wins (W)
for row in rangers_df.itertuples():
    i = row.Index
    year = row.Year
    wins = row.W

    # Check if rangers made Playoffs (1 means yes; 0 means no)
    if row.Playoffs == 1:
        print(i, year, wins)

# 4

yankees_list = [['NYY', 'AL', 2012, 804, 668, 95, 162, 1],
                ['NYY', 'AL', 2011, 867, 657, 97, 162, 1],
                ['NYY', 'AL', 2010, 859, 693, 95, 162, 1],
                ['NYY', 'AL', 2009, 915, 753, 103, 162, 1],
                ['NYY', 'AL', 2008, 789, 727, 89, 162, 0],
                ['NYY', 'AL', 2007, 968, 777, 94, 162, 1],
                ['NYY', 'AL', 2006, 930, 767, 97, 162, 1],
                ['NYY', 'AL', 2005, 886, 789, 95, 162, 1],
                ['NYY', 'AL', 2004, 897, 808, 101, 162, 1],
                ['NYY', 'AL', 2003, 877, 716, 101, 163, 1],
                ['NYY', 'AL', 2002, 897, 697, 103, 161, 1],
                ['NYY', 'AL', 2001, 804, 713, 95, 161, 1],
                ['NYY', 'AL', 2000, 871, 814, 87, 161, 1],
                ['NYY', 'AL', 1999, 900, 731, 98, 162, 1],
                ['NYY', 'AL', 1998, 965, 656, 114, 162, 1],
                ['NYY', 'AL', 1997, 891, 688, 96, 162, 1],
                ['NYY', 'AL', 1996, 871, 787, 92, 162, 1],
                ['NYY', 'AL', 1993, 821, 761, 88, 162, 0],
                ['NYY', 'AL', 1992, 733, 746, 76, 162, 0],
                ['NYY', 'AL', 1991, 674, 777, 71, 162, 0],
                ['NYY', 'AL', 1990, 603, 749, 67, 162, 0],
                ['NYY', 'AL', 1989, 698, 792, 74, 161, 0],
                ['NYY', 'AL', 1988, 772, 748, 85, 161, 0],
                ['NYY', 'AL', 1987, 788, 758, 89, 162, 0],
                ['NYY', 'AL', 1986, 797, 738, 90, 162, 0],
                ['NYY', 'AL', 1985, 839, 660, 97, 161, 0],
                ['NYY', 'AL', 1984, 758, 679, 87, 162, 0],
                ['NYY', 'AL', 1983, 770, 703, 91, 162, 0],
                ['NYY', 'AL', 1982, 709, 716, 79, 162, 0],
                ['NYY', 'AL', 1980, 820, 662, 103, 162, 1],
                ['NYY', 'AL', 1979, 734, 672, 89, 160, 0],
                ['NYY', 'AL', 1978, 735, 582, 100, 163, 1],
                ['NYY', 'AL', 1977, 831, 651, 100, 162, 1],
                ['NYY', 'AL', 1976, 730, 575, 97, 159, 1],
                ['NYY', 'AL', 1975, 681, 588, 83, 160, 0],
                ['NYY', 'AL', 1974, 671, 623, 89, 162, 0],
                ['NYY', 'AL', 1973, 641, 610, 80, 162, 0],
                ['NYY', 'AL', 1971, 648, 641, 81, 162, 0],
                ['NYY', 'AL', 1970, 680, 612, 93, 163, 0],
                ['NYY', 'AL', 1969, 562, 587, 80, 162, 0],
                ['NYY', 'AL', 1968, 536, 531, 83, 164, 0],
                ['NYY', 'AL', 1967, 522, 621, 72, 163, 0],
                ['NYY', 'AL', 1966, 611, 612, 70, 160, 0],
                ['NYY', 'AL', 1965, 611, 604, 77, 162, 0],
                ['NYY', 'AL', 1964, 730, 577, 99, 164, 1],
                ['NYY', 'AL', 1963, 714, 547, 104, 161, 1],
                ['NYY', 'AL', 1962, 817, 680, 96, 162, 1]]

yankees_df = pd.DataFrame(yankees_list, columns=col)

run_diffs = []

# Loop over the DataFrame and calculate each row's run differential
for row in yankees_df.itertuples():

    runs_scored = row.RS
    runs_allowed = row.RA

    run_diff = calc_run_diff(runs_scored, runs_allowed)

    run_diffs.append(run_diff)

# Append new column
yankees_df["RD"] = run_diffs
print(yankees_df)

# 5


def text_playoffs(num_playoffs):
    if num_playoffs == 1:
        return 'Yes'
    else:
        return 'No'


rays_list = [[697, 577, 90, 0],
             [707, 614, 91, 1],
             [802, 649, 96, 1],
             [803, 754, 84, 0],
             [774, 671, 97, 1]]

rays_df = pd.DataFrame(rays_list, index=[2012, 2011, 2010, 2009, 2008], columns=[
                       'RS', 'RA', 'W', 'Playoffs'])

# Gather sum of all columns
stat_totals = rays_df.apply(sum, axis=0)
print(stat_totals)

# Gather total runs scored in all games per year
total_runs_scored = rays_df[['RS', 'RA']].apply(sum, axis=1)
print(total_runs_scored)

# Convert numeric playoffs to text by applying text_playoffs()
textual_playoffs = rays_df.apply(
    lambda row: text_playoffs(row['Playoffs']), axis=1)
print(textual_playoffs)

# 6

dbacks_list = [['ARI', 'NL', 2012, 734, 688, 81, 162, 0],
               ['ARI', 'NL', 2011, 731, 662, 94, 162, 1],
               ['ARI', 'NL', 2010, 713, 836, 65, 162, 0],
               ['ARI', 'NL', 2009, 720, 782, 70, 162, 0],
               ['ARI', 'NL', 2008, 720, 706, 82, 162, 0],
               ['ARI', 'NL', 2007, 712, 732, 90, 162, 1],
               ['ARI', 'NL', 2006, 773, 788, 76, 162, 0],
               ['ARI', 'NL', 2005, 696, 856, 77, 162, 0],
               ['ARI', 'NL', 2004, 615, 899, 51, 162, 0],
               ['ARI', 'NL', 2003, 717, 685, 84, 162, 0],
               ['ARI', 'NL', 2002, 819, 674, 98, 162, 1],
               ['ARI', 'NL', 2001, 818, 677, 92, 162, 1],
               ['ARI', 'NL', 2000, 792, 754, 85, 162, 0],
               ['ARI', 'NL', 1999, 908, 676, 100, 162, 1],
               ['ARI', 'NL', 1998, 665, 812, 65, 162, 0]]

dbacks_df = pd.DataFrame(dbacks_list, columns=col)


def calc_win_perc(wins, games_played):
    win_perc = wins / games_played
    return np.round(win_perc, 2)


# Display the first five rows of the DataFrame
print(dbacks_df.head())

# Create a win percentage Series
win_percs = dbacks_df.apply(
    lambda row: calc_win_perc(row['W'], row['G']), axis=1)
print(win_percs, '\n')

# Append a new column to dbacks_df
dbacks_df['WP'] = win_percs
print(dbacks_df, '\n')

# Display dbacks_df where WP is greater than 0.50
print(dbacks_df[dbacks_df['WP'] >= 0.50])

# 7

baseball_stats = pd.read_csv('baseball_stats.csv')
baseball_df = baseball_stats.loc[[
    'Team', 'League', 'Year', 'RS', 'RA', 'W', 'G', 'Playoffs']]

# Use the W array and G array to calculate win percentages
win_percs_np = calc_win_perc(baseball_df['W'].values, baseball_df['G'].values)

# Append a new column to baseball_df that stores all win percentages
baseball_df['WP'] = win_percs_np

print(baseball_df.head())

# 8


def predict_win_perc(RS, RA):
    prediction = RS ** 2 / (RS ** 2 + RA ** 2)
    return np.round(prediction, 2)


win_perc_preds_loop = []

# Use a loop and .itertuples() to collect each row's predicted win percentage
for row in baseball_df.itertuples():
    runs_scored = row.RS
    runs_allowed = row.RA
    win_perc_pred = predict_win_perc(runs_scored, runs_allowed)
    win_perc_preds_loop.append(win_perc_pred)

# Apply predict_win_perc to each row of the DataFrame
win_perc_preds_apply = baseball_df.apply(
    lambda row: predict_win_perc(row['RS'], row['RA']), axis=1)

# Calculate the win percentage predictions using NumPy arrays
win_perc_preds_np = predict_win_perc(
    baseball_df['RS'].values, baseball_df['RA'].values)
baseball_df['WP_preds'] = win_perc_preds_np
print(baseball_df.head())
