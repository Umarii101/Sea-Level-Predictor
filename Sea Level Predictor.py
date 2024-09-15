#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Load the data
df = pd.read_csv('epa-sea-level.csv')

# Create scatter plot
plt.figure(figsize=(14, 7))
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Data', color='blue')

# Fit line to entire dataset
slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
plt.plot(df['Year'], slope * df['Year'] + intercept, color='red', label='Fit Line (1880-2050)')

# Extend the line to 2050
years_extended = pd.Series(range(df['Year'].min(), 2051))
plt.plot(years_extended, slope * years_extended + intercept, color='red', linestyle='--')

# Fit line to data from year 2000 onward
df_recent = df[df['Year'] >= 2000]
slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
plt.plot(df_recent['Year'], slope_recent * df_recent['Year'] + intercept_recent, color='green', label='Fit Line (2000-2050)')

# Extend the line to 2050
plt.plot(years_extended, slope_recent * years_extended + intercept_recent, color='green', linestyle='--')

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')
plt.legend()

# Save the figure
plt.savefig('sea_level_rise.png')

# Show the plot
plt.show()

