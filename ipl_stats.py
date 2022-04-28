import streamlit as st
import pandas as pa
import toss_analysis_graphs as tag
import player_analysis_graphs as pag
import franchise_analysis_graphs as fag


def main():
    st.title("IPL Stats")

    st.write("Exploratory Data Analysis (EDA) is an approach to analyzing datasets to summarize their main "
             "characteristics, often with visual methods. EDA is used for seeing what the data can tell us before the "
             "modeling task.")
    st.write("With IPL Data we can analyse ball by ball, matches, points table, etc.. The analysed data is depicted "
             "in the form infographs and dataframes")

    data_ball = pa.read_csv("IPL_PREDICTION/WebsiteDatasets/IPL 2008-2021 Ball by Ball Data.csv")
    data_match = pa.read_csv("IPL_STATS/WebsiteDatasets/IPL 2008-2021 Matches Data.csv")
    data_points = pa.read_csv("IPL_STATS/WebsiteDatasets/IPL 2008-2021 Points Table Data.csv")

    choice = st.selectbox(
        "Select your required analysis", ('Toss Analysis', 'Player Analysis', 'Franchise Analysis')
    )

    if choice == "Toss Analysis":
        st.subheader("Toss Analysis")
        st.write('A "Toss" plays a very crucial role in the outcome of a match. Captain of each team chooses either '
                 'to field or to bat and this decision depends on ground, whether, pitch, time. Therefore, '
                 'winning toss sometimes wins the match. Toss Analysis gives the captain, viewer to predict the '
                 'winner of the match.')
        st.write("From 2008 to 2021, number of tosses held are 876 out of which 337 times toss winning captains "
                 "choose to bat first and 538 times they choose to field. The second graph gives number of times toss "
                 "winner winning th match likewise losing the match")

        data_toss = data_match[["Season", "City", "Toss Decision", "Toss Winner", "Match Winner"]]

        columns = st.columns(2)
        with columns[0]:
            tag.total_toss_count(data_toss)
        with columns[1]:
            tag.total_toss_wins(data_toss)

        st.title("")
        st.write("Below graphs gives the total count of toss won per season along with bat and field")

        columns = st.columns(2)
        with columns[0]:
            st.title("")
            st.subheader("")
            sea_no_choice = tag.season_without_choice(data_toss)
        with columns[1]:
            st.title("")
            st.subheader("")
            tag.season_with_choice(data_toss)

        st.table(sea_no_choice)
        st.write("Below graphs gives the total count of toss won by each teem per season and there choice to bat or "
                 "field")

        columns = st.columns(2)
        with columns[0]:
            team_no_choice = tag.team_without_choice(data_toss)
        with columns[1]:
            tag.team_with_choice(data_toss)

        st.table(team_no_choice)

        columns = st.columns(2)
        with columns[0]:
            city_bat = tag.cities_bat_percentage(data_toss)
            city_field = tag.cities_field_percentage(data_toss)
        with columns[1]:
            st.subheader("")
            st.dataframe(city_bat)
            st.subheader("")
            st.dataframe(city_field)
    elif choice == "Player Analysis":
        st.subheader("Player Analysis")
        st.write('In player analysis, a viewer can get information about the player who as won "Player of Match", '
                 'and the batsmen whose score has dot balls, 1, 2, ,3 ,4, 6 runs')
        df_ball = data_ball[["Season", "Runs Scored", "Ball", "Striker", "Player Dismissed"]]
        df_match = data_match[["Season", "Player of Match", "Match Winner"]]

        columns = st.columns(2)
        with columns[0]:
            player_match_df = pag.player_of_the_match(df_match)
            zero_df = pag.player_zero_runs(df_ball)
            one_df = pag.player_one_runs(df_ball)
            two_df = pag.player_two_runs(df_ball)
            three_df = pag.player_three_runs(df_ball)
            four_df = pag.player_four_runs(df_ball)
            six_df = pag.player_six_runs(df_ball)
        with columns[1]:
            st.dataframe(player_match_df)
            st.dataframe(zero_df)
            st.dataframe(one_df)
            st.dataframe(two_df)
            st.dataframe(three_df)
            st.dataframe(four_df)
            st.dataframe(six_df)
    elif choice == "Franchise Analysis":
        st.subheader("Franchise Analysis")
        st.write("Below graphs give analysis of team performance. The team that as entered playoffs maximum time, "
                 "most runs scored, most wickets taken, most wins, most boundaries scored")
        df_ball = data_ball[
            ["Season", "Runs Scored", "Ball", "Striker", "Player Dismissed", "Batting Team", "Bowling Team",
             "Wicket Type"]]
        df_match = data_match[["Season", "Player of Match", "Match Winner"]]
        df_points = data_points

        columns = st.columns(2)
        with columns[0]:
            team_qualified = fag.team_qualified_for_playoffs_count(df_points)
            boundaries = fag.team_most_boundaries(df_ball)
            wins = fag.team_most_wins(df_match)
            runs = fag.team_most_runs(df_ball)
            wickets = fag.team_most_wickets(df_ball)
        with columns[1]:
            st.dataframe(team_qualified)
            st.dataframe(boundaries)
            st.dataframe(wins)
            st.dataframe(runs)
            st.dataframe(wickets)
