import streamlit as st
import pandas as pa
import numpy as npy


def main():
    st.title("Points Table")

    points_table_page_markdown = open("ABOUT_IPL/WebsiteStyles/about_ipl_style.css", "r").read()
    st.markdown(f"<style>{points_table_page_markdown}</style>", unsafe_allow_html=True)

    st.write("This page of the web app is the most viewed page as it gives the performance of teams in a "
             "particular year as well as in cumulative years. The points table helps the viewer in "
             "assessing the team and also helps in predicting the future of the team in coming games and "
             "seasons. The information provided is from the season 2008 to 2021.")

    st.write("The points table gives information about the team’s performance in particular season. The table has "
             "information about the team’s standing, games played, won matches, lost matches, tied matches, N/R, "
             "Net run rate, average runs scored for and against the rival teams, and total points scored in that "
             "particular season.")

    def download_csv_button(download_data, file_name, label_txt):
        st.download_button(
            label=f"{label_txt} as CSV",
            data=download_data,
            file_name=f'{file_name}',
            mime='text/csv',
        )

    def streamlit_table(dataframe_styled):
        st.dataframe(dataframe_styled)

    @st.cache
    def convert_dataframe_to_csv(df):
        return df.to_csv().encode('utf-8')

    table_style = {
        'color': '',
        'font-size': '',
        'background-color': '',
        'text-align': ''
    }

    years = [2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
    years.reverse()
    dataframe = pa.read_csv(f"POINTS_TABLE/WebsiteDatasets/IPL 2008-2021 Points Table Data.csv")

    choice = st.selectbox("Select a season to view the Standing of teams in IPL", years)
    st.subheader("")
    if choice == 2022:
        table = pa.read_csv("POINTS_TABLE/WebsiteDatasets/live_data.csv")
        table = table[["Rank", "Team", "Played", "Won", "Lost", "N/R", "Tied", "NET RR", "Points"]]
        streamlit_table(table.style.set_properties(**table_style))
        csv = convert_dataframe_to_csv(table)
        download_csv_button(csv, f"IPL {choice} Points Table Data.csv", f"Download {choice} Points Table Data")
    else:
        table = dataframe.loc[dataframe["Season"] == choice]
        table.index = npy.arange(1, len(table) + 1)
        table.drop(["ID"], axis=1)
        streamlit_table(table.style.set_properties(**table_style))
        csv = convert_dataframe_to_csv(table)
        download_csv_button(csv, f"IPL {choice} Points Table Data.csv", f"Download {choice} Points Table Data")
