import matplotlib.pyplot as plt
import seaborn as sea
import pandas as pa
import streamlit as st


def bowler_most_dot_balls(dataframe):
    print(dataframe)


def bowler_most_wickets_taken(dataframe):
    print(dataframe)


def wickets_taken_per_season(dataframe):
    print(dataframe)


def player_most_runs_scored(dataframe):
    print(dataframe)


def player_faced_more_balls(dataframe):
    print(dataframe)


def most_wickets_taken_venue(dataframe):
    print(dataframe)


def player_of_the_match(dataframe):
    df = dataframe[["Player of Match"]]
    df = df["Player of Match"].value_counts()
    df = df.head(10)
    fig, ax = plt.subplots()
    sea.barplot(x=df.index, y=df, palette="YlOrBr", saturation=1)
    ax.set_title("Player of the Match")
    ax.set_xlabel("Players")
    ax.set_ylabel("Total")
    st.pyplot(fig)
    return df


def runs_scored_by_players_per_ball(dataframe):
    df = dataframe[["Runs Scored"]]
    runs_names_list = ["Dot", "1 Run", "2 Run", "3 Run", "4 Run", "6 Run"]
    runs_0 = 0
    runs_1 = 0
    runs_2 = 0
    runs_3 = 0
    runs_4 = 0
    runs_6 = 0
    for runs in df["Runs Scored"]:
        if runs == 0:
            runs_0 += 1
        elif runs == 1:
            runs_1 += 1
        elif runs == 2:
            runs_2 += 1
        elif runs == 3:
            runs_3 += 1
        elif runs == 4:
            runs_4 += 1
        elif runs == 6:
            runs_6 += 1
    runs_count_list = [runs_0, runs_1, runs_2, runs_3, runs_4, runs_6]
    fig, ax = plt.subplots()
    sea.barplot(x=runs_names_list, y=runs_count_list, palette="YlOrBr", saturation=1)
    ax.set_title("")
    ax.set_xlabel("")
    ax.set_ylabel("")
    st.pyplot(fig)
    return runs_names_list, runs_count_list


def player_zero_runs(dataframe):
    df = dataframe[["Runs Scored", "Striker"]]
    players = []
    runs = []
    players_zero_run = []
    for run, player in zip(df["Runs Scored"], df["Striker"]):
        runs.append(run)
        players.append(player)
    for score in range(0, len(players)):
        if runs[score] == 0:
            players_zero_run.append(players[score])
    df = pa.DataFrame(data=players_zero_run, columns=["Players"]).reset_index()
    df = df["Players"].value_counts()
    df = df.head(10)
    fig, ax = plt.subplots()
    sea.barplot(x=df.index, y=df, palette="YlOrBr", saturation=1)
    ax.set_title("Player with maximum count of dot balls")
    ax.set_xlabel("Player")
    ax.set_ylabel("Count")
    st.pyplot(fig)
    return df


def player_one_runs(dataframe):
    df = dataframe[["Runs Scored", "Striker"]]
    players = []
    runs = []
    players_one_run = []
    for run, player in zip(df["Runs Scored"], df["Striker"]):
        runs.append(run)
        players.append(player)
    for score in range(0, len(players)):
        if runs[score] == 1:
            players_one_run.append(players[score])
    df = pa.DataFrame(data=players_one_run, columns=["Players"]).reset_index()
    df = df["Players"].value_counts()
    df = df.head(10)
    fig, ax = plt.subplots()
    sea.barplot(x=df.index, y=df, palette="coolwarm", saturation=1)
    ax.set_title("Player with maximum count of 1 runs")
    ax.set_xlabel("Player")
    ax.set_ylabel("Count")
    st.pyplot(fig)
    return df


def player_two_runs(dataframe):
    df = dataframe[["Runs Scored", "Striker"]]
    players = []
    runs = []
    players_two_run = []
    for run, player in zip(df["Runs Scored"], df["Striker"]):
        runs.append(run)
        players.append(player)
    for score in range(0, len(players)):
        if runs[score] == 2:
            players_two_run.append(players[score])
    df = pa.DataFrame(data=players_two_run, columns=["Players"]).reset_index()
    df = df["Players"].value_counts()
    df = df.head(10)
    fig, ax = plt.subplots()
    sea.barplot(x=df.index, y=df, palette="Spectral", saturation=1)
    ax.set_title("Player with maximum count of 2 runs")
    ax.set_xlabel("Player")
    ax.set_ylabel("Count")
    st.pyplot(fig)
    return df


def player_three_runs(dataframe):
    df = dataframe[["Runs Scored", "Striker"]]
    players = []
    runs = []
    players_three_run = []
    for run, player in zip(df["Runs Scored"], df["Striker"]):
        runs.append(run)
        players.append(player)
    for score in range(0, len(players)):
        if runs[score] == 3:
            players_three_run.append(players[score])
    df = pa.DataFrame(data=players_three_run, columns=["Players"]).reset_index()
    df = df["Players"].value_counts()
    df = df.head(10)
    fig, ax = plt.subplots()
    sea.barplot(x=df.index, y=df, palette="vlag", saturation=1)
    ax.set_title("Player with maximum count of 3 runs")
    ax.set_xlabel("Player")
    ax.set_ylabel("Count")
    st.pyplot(fig)
    return df


def player_four_runs(dataframe):
    df = dataframe[["Runs Scored", "Striker"]]
    players = []
    runs = []
    players_four_run = []
    for run, player in zip(df["Runs Scored"], df["Striker"]):
        runs.append(run)
        players.append(player)
    for score in range(0, len(players)):
        if runs[score] == 4:
            players_four_run.append(players[score])
    df = pa.DataFrame(data=players_four_run, columns=["Players"]).reset_index()
    df = df["Players"].value_counts()
    df = df.head(10)
    fig, ax = plt.subplots()
    sea.barplot(x=df.index, y=df, saturation=1)
    ax.set_title("Player with maximum count of 4 runs")
    ax.set_xlabel("Player")
    ax.set_ylabel("Count")
    st.pyplot(fig)
    return df


def player_six_runs(dataframe):
    df = dataframe[["Runs Scored", "Striker"]]
    players = []
    runs = []
    players_six_run = []
    for run, player in zip(df["Runs Scored"], df["Striker"]):
        runs.append(run)
        players.append(player)
    for score in range(0, len(players)):
        if runs[score] == 6:
            players_six_run.append(players[score])
    df = pa.DataFrame(data=players_six_run, columns=["Players"]).reset_index()
    df = df["Players"].value_counts()
    df = df.head(10)
    fig, ax = plt.subplots()
    sea.barplot(x=df.index, y=df, palette="vlag", saturation=1)
    ax.set_title("Player with maximum count of 6 runs")
    ax.set_xlabel("Player")
    ax.set_ylabel("Count")
    st.pyplot(fig)
    return df
