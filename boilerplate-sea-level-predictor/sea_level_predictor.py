import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
  # Read data from file
  df = pd.read_csv('epa-sea-level.csv')

  # Create scatter plot
  plt.scatter(df['Year'],df['CSIRO Adjusted Sea Level'] )

  # Create first line of best fit
  lob1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
  x = np.arange(df['Year'][0], 2051)
  plt.plot(x,lob1.intercept + lob1.slope*x)

  # Create second line of best fit
  df2 = df[df['Year'] > 1999]
  lob2 = linregress(df2['Year'], df2['CSIRO Adjusted Sea Level'])
  x2 = np.arange(2000, 2051) 
  plt.plot(x2,lob2.intercept + lob2.slope*x2)

  # Add labels and title
  plt.xlabel('Year')
  plt.ylabel('Sea Level (inches)')
  plt.title('Rise in Sea Level')

  
  # Save plot and return data for testing (DO NOT MODIFY)
  plt.savefig('sea_level_plot.png')
  return plt.gca()