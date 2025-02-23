import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    # Create scatter plot
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    fig, ax = plt.subplots(1,1)
    ax.scatter(x, y)

    # Create first line of best fit
    res = linregress(x, y)
    yrs_prog = pd.Series(np.arange(df['Year'].iloc[-1]+1, 2051))
    x_proj = pd.concat([df['Year'], yrs_prog])
    ax.plot(x_proj, res.intercept + res.slope*x_proj, 'g')

    # Create second line of best fit
    x2 = df['Year'][df['Year']>=2000]
    y2 = df['CSIRO Adjusted Sea Level'][df['Year']>=2000]
    res2 = linregress(x2, y2)
    ax.plot(x_proj[x_proj>=2000], res2.intercept + res2.slope*x_proj[x_proj>=2000], 'r')

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()