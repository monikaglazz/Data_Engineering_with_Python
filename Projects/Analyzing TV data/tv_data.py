# Import pandas
import seaborn as sns
from matplotlib import pyplot as plt
import pandas as pd

# Load the CSV data into DataFrames
super_bowls = pd.read_csv("datasets/super_bowls.csv")
tv = pd.read_csv("datasets/tv.csv")
halftime_musicians = pd.read_csv("datasets/halftime_musicians.csv")

# Display the first five rows of each DataFrame
print(super_bowls.head())
print(tv.head())
print(halftime_musicians.head())


# ## 2. Taking note of dataset issues

# Summary of the TV data to inspect
tv.info()

# Summary of the halftime musician data to inspect
halftime_musicians.info()


# ## 3. Combined points distribution

# Import matplotlib and set plotting style
plt.style.use("seaborn")

# Plot a histogram of combined points
plt.hist(super_bowls["combined_pts"], bins=10)
plt.xlabel("Combined Points")
plt.ylabel("Number of Super Bowls")
plt.show()

# Display the Super Bowls with the highest and lowest combined scores
print(super_bowls[super_bowls["combined_pts"] > 70])
print(super_bowls[super_bowls["combined_pts"] < 25])


# ## 4. Point difference distribution

# Plot a histogram of point differences
plt.hist(super_bowls.difference_pts)
plt.xlabel("Point Difference")
plt.ylabel("Number of Super Bowls")
plt.show()

# Display the closest game(s) and biggest blowouts
print(super_bowls[super_bowls["difference_pts"] == 1])
print(super_bowls[super_bowls["difference_pts"] >= 35])


# ## 5. Do blowouts translate to lost viewers?

# Join game and TV data, filtering out SB I because it was split over two
# networks
games_tv = pd.merge(tv[tv["super_bowl"] > 1], super_bowls, on="super_bowl")

# Import seaborn

# Create a scatter plot with a linear regression model fit
sns.regplot(x=games_tv["difference_pts"], y=games_tv["share_household"],
            data=games_tv)


# ## 6. Viewership and the ad industry over time

# Create a figure with 3x1 subplot and activate the top subplot
plt.subplot(3, 1, 1)
plt.plot(tv.super_bowl, tv.avg_us_viewers, color="#648FFF")
plt.title("Average Number of US Viewers")

# Activate the middle subplot
plt.subplot(3, 1, 2)
plt.plot(tv.super_bowl, tv.rating_household, color="#DC267F")
plt.title("Household Rating")

# Activate the bottom subplot
plt.subplot(3, 1, 3)
plt.plot(tv.super_bowl, tv.ad_cost, color="#FFB000")
plt.title("Ad Cost")
plt.xlabel("SUPER BOWL")

# Improve the spacing between subplots
plt.tight_layout()


# ## 7. Halftime shows weren't always this great

# Display all halftime musicians for Super Bowls up to and including
# Super Bowl XXVII
halftime_musicians[halftime_musicians["super_bowl"] <= 27]


# ## 8. Who has the most halftime show appearances?

# Count halftime show appearances for each musician and sort them from most to
# least
halftime_appearances = (
    halftime_musicians.groupby("musician").count()["super_bowl"].reset_index()
)
halftime_appearances = halftime_appearances.sort_values("super_bowl",
                                                        ascending=False)

# Display musicians with more than one halftime show appearance
halftime_appearances[halftime_appearances["super_bowl"] > 1]


# ## 9. Who performed the most songs in a halftime show?

# Filter out most marching bands
no_bands = halftime_musicians[~halftime_musicians.musician.str.contains("Marching")]
no_bands = no_bands[~no_bands.musician.str.contains("Spirit")]

# Plot a histogram of number of songs per performance
most_songs = int(max(no_bands["num_songs"].values))
plt.hist(no_bands.num_songs.dropna(), bins=most_songs)
plt.xlabel("Number of Songs Per Halftime Show Performance")
plt.ylabel("Number of Musicians")
plt.show()

# Sort the non-band musicians by number of songs per appearance...
no_bands = no_bands.sort_values("num_songs", ascending=False)
# ...and display the top 15
print(no_bands.head(15))


# ## 10. Conclusion

# 2018-2019 conference champions
patriots = "New England Patriots"
rams = "Los Angeles Rams"

# Who will win Super Bowl LIII?
super_bowl_LIII_winner = rams
print("The winner of Super Bowl LIII will be the", super_bowl_LIII_winner)
