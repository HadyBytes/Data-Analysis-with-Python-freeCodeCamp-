import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=True, index_col='date')

# Clean data
df = df[(df['value'] < df['value'].quantile(0.975)) & (df['value'] > df['value'].quantile(0.025))]

renaming = { 
    1 : "January",
    2 : "February",
    3 : "March",
    4 : "April",
    5 : "May",
    6 : "June",
    7 : "July",
    8 : "August",
    9 : "September",
    10 : "October",
    11 : "November",
    12 : "December"
}

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(1, 1, figsize=(15, 5))
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")
    ax.plot(df, color='r')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = None

    # Draw bar plot
    grouped = df.groupby([(df.index.year), (df.index.month)]).mean()
    grouped.index.names = ['Years', 'Months']
    fig, ax = plt.subplots(1, 1)
    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")
    grouped.unstack().droplevel(0, axis=1).rename(columns=renaming).plot.bar(ax=ax)

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    months = dict((v[0:3],k) for k,v in renaming.items())
    df_box.sort_values('month', inplace=True, key=lambda x: x.map(months))
        
    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(1, 2, figsize=(15,5))
    sns.boxplot(df_box, x='year', y='value', hue='year', 
            legend=False, ax=axes[0], palette='bright',
            flierprops={"marker": "d", 'markersize' : 3})
    sns.boxplot(df_box, x='month', y='value', hue='month',
            legend=False, ax=axes[1],
            flierprops={"marker": "d", 'markersize' : 3})
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[1].set_ylabel('Page Views')
    axes[1].set_xlabel('Month')
    axes[1].set_title('Month-wise Box Plot (Seasonality)')



    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
