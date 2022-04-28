import matplotlib.pyplot as plt
import seaborn as sea
import pandas as pa
import streamlit as st


def team_most_wickets(dataframe):
    dataframe = dataframe[["Bowling Team", "Wicket Type"]]
    teams = []
    wickets = []
    wicket_type = []
    for team, wicket in zip(dataframe["Bowling Team"], dataframe["Wicket Type"]):
        teams.append(team)
        wickets.append(wicket)
    for score in range(0, len(teams)):
        if wickets[score] == "caught" or wickets[score] == "hit wicket" or wickets[score] == "stumped" or\
                wickets[score] == "lbw" or wickets[score] == "bowled" or wickets[score] == "run out":
            wicket_type.append(teams[score])
    df = pa.DataFrame(data=wicket_type, columns=["Bowling Team"]).reset_index()
    df = df["Bowling Team"].value_counts()
    fig, ax = plt.subplots()
    fig.set_size_inches(30, 10)
    sea.barplot(x=df.index, y=df, palette="flare", saturation=1)
    ax.set_title("Team taken most wickets", fontsize="xx-large")
    ax.set_xlabel("Teams", fontsize="xx-large")
    ax.set_ylabel("Wickets", fontsize="xx-large")
    st.pyplot(fig)
    return df


def team_most_runs(dataframe):
    dataframe = dataframe[["Batting Team", "Runs Scored"]]
    teams = []
    runs = []
    teams_runs = []
    for run, team in zip(dataframe["Runs Scored"], dataframe["Batting Team"]):
        runs.append(run)
        teams.append(team)
    for score in range(0, len(teams)):
        if runs[score] > 0:
            teams_runs.append(teams[score])
    df = pa.DataFrame(data=teams_runs, columns=["Batting Team"]).reset_index()
    df = df["Batting Team"].value_counts()
    fig, ax = plt.subplots()
    fig.set_size_inches(30, 10)
    sea.barplot(x=df.index, y=df, palette="crest", saturation=1)
    ax.set_title("Team scored most runs", fontsize="xx-large")
    ax.set_xlabel("Teams", fontsize="xx-large")
    ax.set_ylabel("Runs Scored", fontsize="xx-large")
    st.pyplot(fig)
    return df


def team_most_wins(dataframe):
    df = dataframe["Match Winner"].value_counts()
    fig, ax = plt.subplots()
    sea.barplot(y=df.index, x=df, saturation=1, palette="magma")
    ax.set_title("Total wins by each Team")
    ax.set_xlabel("Total")
    ax.set_ylabel("Teams")
    st.pyplot(fig)
    return df


def team_most_boundaries(dataframe):
    dataframe = dataframe[["Batting Team", "Runs Scored"]]
    teams = []
    runs = []
    teams_runs = []
    for run, team in zip(dataframe["Runs Scored"], dataframe["Batting Team"]):
        runs.append(run)
        teams.append(team)
    for score in range(0, len(teams)):
        if runs[score] == 4 or runs[score] == 6:
            teams_runs.append(teams[score])
    df = pa.DataFrame(data=teams_runs, columns=["Batting Team"]).reset_index()
    df = df["Batting Team"].value_counts()
    fig, ax = plt.subplots()
    fig.set_size_inches(30, 10)
    sea.barplot(x=df.index, y=df, palette="viridis", saturation=1)
    ax.set_title("Total Boundaries scored by teams", fontsize="xx-large")
    ax.set_xlabel("Teams", fontsize="xx-large")
    ax.set_ylabel("Boundaries", fontsize="xx-large")
    st.pyplot(fig)
    return df


def team_qualified_for_playoffs_count(dataframe):
    df_1 = dataframe.loc[dataframe['Rank'] == 1].reset_index()[["Franchise"]]
    df_2 = dataframe.loc[dataframe['Rank'] == 2].reset_index()[["Franchise"]]
    df_3 = dataframe.loc[dataframe['Rank'] == 3].reset_index()[["Franchise"]]
    df_4 = dataframe.loc[dataframe['Rank'] == 4].reset_index()[["Franchise"]]
    df = pa.DataFrame(columns=["Franchise"])
    df = pa.concat([df, df_1, df_2, df_3, df_4]).reset_index()[["Franchise"]]
    df = df['Franchise'].value_counts()
    fig, ax = plt.subplots()
    fig.set_size_inches(10, 5)
    sea.barplot(y=df.index, x=df, orient='h', palette="cubehelix", saturation=1)
    ax.set_title("Number of teams qualified for playoffs", fontsize="xx-large")
    ax.set_xlabel("Total", fontsize="xx-large")
    ax.set_ylabel("Teams", fontsize="xx-large")
    st.pyplot(fig)
    return df
