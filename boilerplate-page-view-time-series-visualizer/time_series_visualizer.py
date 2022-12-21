import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=['date'])

# Clean data
df = df[(df['value'] <= df['value'].quantile(0.975)) & (df['value'] >= df['value'].quantile(0.025))]


def draw_line_plot():
    # Draw line plot
    fig = plt.figure(figsize=(16,5))
    plt.plot(df, color='red')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    ticks = ['2016-07-01','2017-01-01','2017-07-01','2018-01-01','2018-07-01','2019-01-01','2019-07-01','2020-01-01']
    lticks = ['2016-07','2017-01','2017-07','2018-01','2018-07','2019-01','2019-07','2020-01']
    plt.xticks(ticks=ticks, labels=lticks)

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['Year'] = df_bar.index.year
    df_bar['Months'] = df_bar.index.month_name()
    df_bar = df_bar.groupby(['Year','Months'], sort=False)['value'].mean().reset_index()

    # Draw bar plot
    fig = plt.figure(layout='constrained')
    months_order = ['January','February','March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    sns.barplot(data=df_bar, x='Year', y='value', hue='Months', hue_order=months_order, palette='tab10')
    plt.xlabel('Years')
    plt.xticks(rotation=90)
    plt.ylabel('Average Page Views')




    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig = plt.figure(figsize=(15,5))
    plt.subplot(121)
    sns.boxplot(data=df_box, x='year', y='value')
    plt.xlabel('Year')
    plt.ylabel('Page Views')
    plt.title('Year-wise Box Plot (Trend)')
    plt.subplot(122)
    months_order = ['Jan','Feb','Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    sns.boxplot(data=df_box, x='month', y='value', order=months_order)
    plt.xlabel('Month')
    plt.ylabel('Page Views')
    plt.title('Month-wise Box Plot (Seasonality)')
    


    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
