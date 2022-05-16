import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
  # Read data from file
  df = pd.read_csv("epa-sea-level.csv")
  
  x = df['Year']
  y = df['CSIRO Adjusted Sea Level']
  
  # Create scatter plot
  fig, ax = plt.subplots()
  plt.scatter(x, y)
  
  # Create first line of best fit
  result1 = linregress(x, y)
  x1 = pd.Series(i for i in range(df['Year'].min(), 2051))
  y1 = result1.intercept + result1.slope * x1
  
  plt.plot(x1, y1, 'g')

  # Create second line of best fit
  df_new = df.loc[df["Year"] >= 2000]
  
  x2 = df_new['Year']
  y2 = df_new['CSIRO Adjusted Sea Level']  
  result2 = linregress(x2, y2)
  x3 = pd.Series(i for i in range(2000, 2051))
  y3 = result2.intercept + result2.slope * x3

  plt.plot(x3, y3, 'r' )
  # Add labels and title
  
  
  ax.set_title('Rise in Sea Level')
  ax.set_xlabel('Year')
  ax.set_ylabel('Sea Level (inches)') 
  
  # Save plot and return data for testing (DO NOT MODIFY)
   
  plt.savefig('sea_level_plot.png')
  return plt.gca()