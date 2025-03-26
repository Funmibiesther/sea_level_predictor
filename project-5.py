import pandas as pd
df = pd.read_csv('epa-sea-level.csv')

import matplotlib.pyplot as plt
#scatter plot
plt.scatter(df['Year'],df['CSIRO Adjusted Sea Level'])

from scipy.stats import linregress
 # get slope and intercept
slope, intercept = linregress(df['Year'],df['CSIRO Adjusted Sea Level'])[:2]

years = pd.Series(range(1880,2051))
 #line of best fit
plt.plot(years.values, slope*years.values + intercept, label= 'First line of best fit')

 #new line of best fit
df2 = df[df['Year']>=2000]
slope2, intercept2 = linregress(df2['Year'],df2['CSIRO Adjusted Sea Level'])[:2]
year2 = pd.Series(range(2000,2051))

# label of title, x and y axis
plt.plot(year2)

plt.title('Rise in Sea Level')
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')

