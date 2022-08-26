"""
Haosen Li
Elliot Liu
This file contains functions for data visualization.
"""
import matplotlib.pyplot as plt
import seaborn as sns
import data_parser as dp


def daily_stock(df, month, year):
    """
    Takes a monthly Pandas DataFrame representation of
    daily stock frequency. Plots a grouped bar plot representing
    the most frequently discussed stock followed by their date within
    the given month and year.
    """
    int_month = dp.convert_month(month)
    df = df[(df['month'] == int_month) & (df['year'] == year)]
    sns.catplot(
        data=df, kind='bar', x='day', y='mention frequency',
        hue='most mentioned stock', dodge=False
    )
    plt.title("Most Mentioned Stock Daily for the Month of "
              + month[0].upper() + month[1:])
    plt.savefig('daily_stock.png', bbox_inches='tight')


def subreddit_activity(df, month):
    """
    Takes in a Pandas DataFrame containing information on Reddit
    Submissions, and a month as an int. Plots a line plot
    illustrating the subreddit activity over a given month.
    """
    int_month = dp.convert_month(month)
    mask = df['month'] == int_month
    comments = df[mask].groupby('day', as_index=False)['comments'].sum()
    sns.relplot(data=comments, x='day', y='comments', kind='line')
    plt.title(f'Subreddit activity in {month}')
    plt.xticks(range(1, 32, 2))
    plt.ylabel('Comment Amount')
    plt.xlabel('Day')
    plt.fill_between(x=comments['day'], y1=comments['comments'], alpha=0.5)
    plt.savefig('plot_subreddit_activity.png', bbox_inches='tight')