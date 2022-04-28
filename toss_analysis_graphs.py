import matplotlib.pyplot as plt
import seaborn as sea
import pandas as pa
import streamlit as st


def total_toss_count(dataframe):
    df = dataframe['Toss Decision'].value_counts()
    fig, ax = plt.subplots()
    sea.countplot(x=df, hue=df, palette="rocket", saturation=1)
    ax.set_title("Total Toss Count (2008-2021)")
    ax.set_xlabel("Toss Decision")
    ax.set_ylabel("Total count")
    st.pyplot(fig)
    return df


def total_toss_wins(dataframe):
    toss_winner = dataframe['Toss Winner']
    winner = dataframe['Match Winner']

    won = {'Toss Winner Wins Match': 0, 'Toss Winner Loses Match': 0}
    for i in range(len(dataframe)):
        if toss_winner[i] == winner[i]:
            won['Toss Winner Wins Match'] += 1
        else:
            won['Toss Winner Loses Match'] += 1

    df = won
    li, li1 = [], []
    for x, y in df.items():
        li.append(x)
        li1.append(y)
    fig, ax = plt.subplots()
    sea.barplot(x=li1, y=li, palette="mako", saturation=1)
    ax.set_title("Toss Winner Wins/Loss Match")
    ax.set_xlabel("Count")
    st.pyplot(fig)
    return df


def season_without_choice(dataframe):
    df_total_toss_per_season = dataframe[['Season', 'Toss Decision']]
    df_total_toss_per_season_encoder = pa.get_dummies(df_total_toss_per_season['Toss Decision'])
    df_total_toss_per_season = pa.concat([df_total_toss_per_season_encoder, df_total_toss_per_season['Season']],
                                         axis=1)
    df_total_toss_per_season = df_total_toss_per_season.groupby(['Season']).sum().reset_index()
    df_total_toss_per_season['Total'] = df_total_toss_per_season.bat + df_total_toss_per_season.field
    df = df_total_toss_per_season

    fig, ax = plt.subplots()
    sea.barplot(x='Season', y='Total', data=df, palette="tab10", saturation=1)
    ax.set_title("Total Toss Decisions in each season")
    ax.set_xlabel("Seasons")
    ax.set_ylabel("Total")
    st.pyplot(fig)
    return df


def season_with_choice(dataframe):
    df = dataframe[['Season', 'Toss Decision']]
    fig, ax = plt.subplots()
    sea.countplot(x='Season', hue='Toss Decision', data=df, palette="YlOrBr", saturation=1)
    ax.set_title("Total Toss Decision in each Season (bat/field)")
    ax.set_xlabel("Seasons")
    ax.set_ylabel("Total")
    st.pyplot(fig)
    return df


def team_without_choice(dataframe):
    df = dataframe['Toss Winner'].value_counts()
    fig, ax = plt.subplots()
    sea.barplot(y=df.index, x=df, orient='h', palette="Set2", saturation=1)
    ax.set_title("Total Toss won by each Team")
    ax.set_xlabel("Total")
    ax.set_ylabel("Teams")
    st.pyplot(fig)
    return df


def team_with_choice(dataframe):
    df = dataframe[['Toss Decision', 'Toss Winner']]
    fig, ax = plt.subplots()
    sea.countplot(y="Toss Winner", data=df, hue="Toss Decision", palette="Paired")
    ax.set_title("Total Toss won by each Team (bat/field)")
    ax.set_xlabel("Total")
    ax.set_ylabel("Teams")
    st.pyplot(fig)
    return df


def cities_bat_percentage(dataframe):
    df_cities_percentage = dataframe[['City', 'Toss Decision']]
    df_cities_percentage_encoder = pa.get_dummies(df_cities_percentage['Toss Decision'])
    df_cities_percentage = pa.concat([df_cities_percentage_encoder, df_cities_percentage['City']], axis=1)
    df_cities_percentage = df_cities_percentage.groupby(['City']).sum().reset_index()
    df_cities_percentage['Total'] = df_cities_percentage.bat + df_cities_percentage.field
    df_cities_percentage['Bat Percent'] = (df_cities_percentage.bat / df_cities_percentage.Total) * 100
    df_cities_percentage['Field Percent'] = (df_cities_percentage.field / df_cities_percentage.Total) * 100

    df = df_cities_percentage
    df = df.sort_values(['Bat Percent'], ascending=False).reset_index()
    df = df[df['City'] != 'Port Elizabeth']
    df = df[df['City'] != 'East London']
    df = df.head(10)
    fig, ax = plt.subplots()
    ax.bar(df['City'], df['Bat Percent'], color='yellow')
    ax.bar(df['City'], df['Field Percent'], color='red')
    ax.set_title("Cities with most bat percentage")
    ax.set_xlabel("Cities")
    ax.set_ylabel("Count")
    st.pyplot(fig)
    df = df.drop(["index"], axis=1)
    return df


def cities_field_percentage(dataframe):
    df_cities_percentage = dataframe[['City', 'Toss Decision']]
    df_cities_percentage_encoder = pa.get_dummies(df_cities_percentage['Toss Decision'])
    df_cities_percentage = pa.concat([df_cities_percentage_encoder, df_cities_percentage['City']], axis=1)
    df_cities_percentage = df_cities_percentage.groupby(['City']).sum().reset_index()
    df_cities_percentage['Total'] = df_cities_percentage.bat + df_cities_percentage.field
    df_cities_percentage['Bat Percent'] = (df_cities_percentage.bat / df_cities_percentage.Total) * 100
    df_cities_percentage['Field Percent'] = (df_cities_percentage.field / df_cities_percentage.Total) * 100

    df = df_cities_percentage
    df = df.sort_values(['Field Percent'], ascending=False).reset_index()
    df = df[df['City'] != 'Kanpur']
    df = df.head(10)
    fig, ax = plt.subplots()
    ax.bar(df['City'], df['Field Percent'], color='red')
    ax.bar(df['City'], df['Bat Percent'], color='green')
    ax.set_title("Cities with most field percentage")
    ax.set_xlabel("Cities")
    ax.set_ylabel("Count")
    st.pyplot(fig)
    df = df.drop(["index"], axis=1)
    return df
