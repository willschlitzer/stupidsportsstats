"""My first project in finding trends in unrelated data, in this case the relationship between
Matt Ryan's passing yards and the time since the most recent full moon."""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# File of Matt Ryan's game data from 2017 season
file = "2017_season_ryan.csv"

# Imports the data, removes any NaN values, and sets the week as the index
df = pd.read_csv(file, parse_dates=True, index_col='WK').dropna(how='all')

# Creates arrays of both pandas series
x_values = np.array(df['MoonDiff'])
y_values = np.array(df['PassYds'])

#Sets the style for the plot
plt.style.use('ggplot')
# Plots the data
plt.scatter(x_values, y_values)
# Adds axis and chart titles
plt.xlabel('Days since most recent Full Moon')
plt.ylabel('Passing Yards')
plt.title('Is Matt Ryan a werewolf?')

# Saves the plot
plt.savefig('mattryanwerewolf.png')
# Shows the plot
plt.show()
