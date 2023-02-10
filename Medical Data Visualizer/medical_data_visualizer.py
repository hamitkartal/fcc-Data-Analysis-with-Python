import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
df['bmi'] = df['weight'] / (df['height']*df['height']/10000)
df['overweight'] = df['bmi'].apply(lambda x: 1 if x > 25 else 0)
df.drop('bmi', axis=1, inplace=True)
df['overweight'].astype(np.int8)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = df_cat.groupby(['cardio', 'variable'])['value'].value_counts().reset_index(name='total')
    

    # Draw the catplot with 'sns.catplot()'
    sns.catplot(data=df_cat, x='variable', y='total', hue='value', kind='bar', col='cardio')


    # Get the figure for the output
    fig = sns.catplot(data=df_cat, x='variable', y='total', hue='value', kind='bar', col='cardio')


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df.drop(df[df['ap_lo'] > df['ap_hi']].index)
    df_heat.drop(df_heat[(df_heat['height'] < df_heat['height'].quantile(0.025)) & (df_heat['height'] > df_heat['height'].quantile(0.975))].index, inplace=True)
    df_heat.drop(df_heat[(df_heat['weight'] < df_heat['weight'].quantile(0.025)) & (df_heat['weight'] > df_heat['weight'].quantile(0.975))].index, inplace=True)
  
    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr))



    # Set up the matplot  lib figure
    fig, ax = plt.subplots(figsize=(12,8))

    # Draw the heatmap with 'sns.heatmap()'
    ax = sns.heatmap(corr, annot=True, mask=mask, linewidth=1, fmt=".1f", ax=ax, cbar=True, square=True)

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
