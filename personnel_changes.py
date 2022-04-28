import streamlit as st
import pandas as pa
import numpy as npy


def main():
    st.title("Personnel Changes")

    personnel_changes_page_markdown = open("PERSONNEL_CHANGES/WebsiteStyles/personnel_changes_style.css", "r").read()
    st.markdown(f"<style>{personnel_changes_page_markdown}</style>", unsafe_allow_html=True)

    st.write("Every season IPL witnesses Personnel changes. New franchises are added and some old franchises are "
             "left. Each franchise depending on the availability of funds and opinions given by their respective "
             "managers and experts performs pre-auctions. Personnel changes table gives information about team "
             "players, retained/ released players, staff changes, sold players and so on.")
    st.write("On this page you can view the personnel changes of all the franchises of year 2021 and 2022")
    st.subheader("")

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

    with st.expander("Personnel Changes Summary", expanded=True):
        st.write("This section of the page contains a tabular summary of personnel changes for all franchises in the "
                 "years 2021 and 2022.")

        dataframe = pa.read_csv(f"PERSONNEL_CHANGES/WebsiteDatasets/IPL 2021-2022 PCS Data.csv")
        dataframe = dataframe.drop(['ID'], axis=1)
        dataframe.index = npy.arange(1, len(dataframe) + 1)
        table = dataframe
        seasons = ["Select", 2022, 2021]

        columns = st.columns([3, 5, 2])
        with columns[0]:
            pcs_choice = st.selectbox("Select the Season", seasons, key="pcs")
        with columns[2]:
            st.subheader("")
            st.subheader("")
            st.write("(Amount in ₹ lakhs)")

        if pcs_choice == "Select":
            streamlit_table(table.style.set_properties(**table_style))
        else:
            table = table.loc[table["Season"] == pcs_choice]
            table.index = npy.arange(1, len(table) + 1)
            streamlit_table(table.style.set_properties(**table_style))

        csv = convert_dataframe_to_csv(dataframe)
        download_csv_button(csv, "IPL 2021-2022 PCS Data.csv", "Download Personnel Changes Summary Data")

    st.write("You can also view a comprehensive information of Pre-Auction, Auction and Support Staff. We have also "
             "provided a detailed summary of Pre-Auction and Auction Changes in separate sections")

    select_box_choices = ["Pre Auction", "Auction", "Support Staff"]
    choice = st.selectbox("Select a section to view in detail", select_box_choices)

    if choice == "Pre Auction":
        st.subheader("Pre Auction")
        st.write("In every season a Pre-auction is conducted to maintain a level playing field for all the teams. All "
                 "the existing franchises are allowed upto four player retentions. Retention/released of "
                 "players is done in pre-auction. Pre-auction details of all the teams are presented below.")

        with st.expander("Pre Auction Summary", expanded=True):
            st.write("This section of the page contains a tabular summary of Pre-Auction changes for all franchises "
                     "in the years 2021 and 2022")

            dataframe = pa.read_csv(f"PERSONNEL_CHANGES/WebsiteDatasets/IPL 2021-2022 PAS Data.csv")
            dataframe = dataframe.drop(['ID'], axis=1)
            dataframe.index = npy.arange(1, len(dataframe) + 1)
            table = dataframe
            seasons = ["Select", 2022, 2021]

            columns = st.columns([3, 5, 2])
            with columns[0]:
                pas_choice = st.selectbox("Select the Season", seasons, key="pas")
            with columns[2]:
                st.subheader("")
                st.subheader("")
                st.write("(Amount in ₹ lakhs)")

            if pas_choice == "Select":
                streamlit_table(table.style.set_properties(**table_style))
            else:
                table = table.loc[table["Season"] == pas_choice]
                table.index = npy.arange(1, len(table) + 1)
                streamlit_table(table.style.set_properties(**table_style))

            csv = convert_dataframe_to_csv(dataframe)
            download_csv_button(csv, "IPL 2021-2022 PAS Data.csv", "Download Pre Auction Summary data")

        with st.expander("Retained Players", expanded=False):
            st.write("This section of the page contains retained players list with their franchise and salary for the "
                     "year 2021 and 2022")

            dataframe = pa.read_csv(f"PERSONNEL_CHANGES/WebsiteDatasets/IPL 2021-2022 PART Data.csv")
            dataframe = dataframe.drop(['ID'], axis=1)
            dataframe.index = npy.arange(1, len(dataframe) + 1)
            table = dataframe
            seasons = ["Select", 2022, 2021]

            columns = st.columns([3, 5, 2])
            with columns[0]:
                part_choice = st.selectbox("Select the Season", seasons, key="part")
            with columns[2]:
                st.subheader("")
                st.subheader("")
                st.write("(Amount in ₹ lakhs)")

            if part_choice == "Select":
                streamlit_table(table.style.set_properties(**table_style))
            else:
                table = table.loc[table["Season"] == part_choice]
                table.index = npy.arange(1, len(table) + 1)
                streamlit_table(table.style.set_properties(**table_style))

            csv = convert_dataframe_to_csv(dataframe)
            download_csv_button(csv, "IPL 2021-2022 PART Data.csv", "Download Retained Players data")

        with st.expander("Released Players", expanded=False):
            st.write("This section of the page contains released players list with their franchise and salary for the "
                     "year 2021 and 2022")

            dataframe = pa.read_csv(f"PERSONNEL_CHANGES/WebsiteDatasets/IPL 2021-2022 PARL Data.csv")
            dataframe = dataframe.drop(['ID'], axis=1)
            dataframe.index = npy.arange(1, len(dataframe) + 1)
            table = dataframe
            seasons = ["Select", 2022, 2021]

            columns = st.columns([3, 5, 2])
            with columns[0]:
                parl_choice = st.selectbox("Select the Season", seasons, key="parl")
            with columns[2]:
                st.subheader("")
                st.subheader("")
                st.write("(Amount in ₹ lakhs)")

            if parl_choice == "Select":
                streamlit_table(table.style.set_properties(**table_style))
            else:
                table = table.loc[table["Season"] == parl_choice]
                table.index = npy.arange(1, len(table) + 1)
                streamlit_table(table.style.set_properties(**table_style))

            csv = convert_dataframe_to_csv(dataframe)
            download_csv_button(csv, "IPL 2021-2022 PARL Data.csv", "Download Released Players data")

    elif choice == "Auction":
        st.subheader("Auction")
        st.write("Released/new players in pre-auction are auctioned and are open for all the franchises. Franchises "
                 "with the help of expert opinion participates in the auction and buys the players. So players "
                 "previously played for one franchise may play for another franchise in different seasons. All the "
                 "information regarding the auction of the players, their price at present and price earlier is "
                 "presented below.")

        with st.expander("Auction Summary", expanded=True):
            st.write("This section of the page contains a tabular summary of Auction changes for all franchises "
                     "in the years 2021 and 2022")

            dataframe = pa.read_csv(f"PERSONNEL_CHANGES/WebsiteDatasets/IPL 2021-2022 AS Data.csv")
            dataframe = dataframe.drop(['ID'], axis=1)
            dataframe.index = npy.arange(1, len(dataframe) + 1)
            table = dataframe
            seasons = [2022, 2021]
            seasons.insert(0, "Select")

            columns = st.columns([3, 5, 2])
            with columns[0]:
                as_choice = st.selectbox("Select the Season", seasons, key="as")
            with columns[2]:
                st.subheader("")
                st.subheader("")
                st.write("(Amount in ₹ lakhs)")

            if as_choice == "Select":
                streamlit_table(table.style.set_properties(**table_style))
            else:
                table = table.loc[table["Season"] == as_choice]
                table.index = npy.arange(1, len(table) + 1)
                streamlit_table(table.style.set_properties(**table_style))

            csv = convert_dataframe_to_csv(dataframe)
            download_csv_button(csv, "IPL 2021-2022 AS Data.csv", "Download Auction Summary data")

        with st.expander("Sold Players", expanded=False):
            st.write("This section of the page contains Sold players list with their franchise and salary for the "
                     "year 2021 and 2022")

            dataframe = pa.read_csv(f"PERSONNEL_CHANGES/WebsiteDatasets/IPL 2021-2022 ASP Data.csv")
            dataframe = dataframe.drop(['ID'], axis=1)
            dataframe.index = npy.arange(1, len(dataframe) + 1)
            table = dataframe
            seasons = ["Select", 2022, 2021]

            columns = st.columns([3, 5, 2])
            with columns[0]:
                asp_choice = st.selectbox("Select the Season", seasons, key="asp")
            with columns[2]:
                st.subheader("")
                st.subheader("")
                st.write("(Amount in ₹ lakhs)")

            if asp_choice == "Select":
                streamlit_table(table.style.set_properties(**table_style))
            else:
                table = table.loc[table["Season"] == asp_choice]
                table.index = npy.arange(1, len(table) + 1)
                streamlit_table(table.style.set_properties(**table_style))

            csv = convert_dataframe_to_csv(dataframe)
            download_csv_button(csv, "IPL 2021-2022 ASP Data.csv", "Download Sold Players data")

        with st.expander("Unsold Players", expanded=False):
            st.write("This section of the page contains Unsold players list with their franchise and salary for the "
                     "year 2021 and 2022")

            dataframe = pa.read_csv(f"PERSONNEL_CHANGES/WebsiteDatasets/IPL 2021-2022 AUSP Data.csv")
            dataframe = dataframe.drop(['ID'], axis=1)
            dataframe.index = npy.arange(1, len(dataframe) + 1)
            table = dataframe
            seasons = ["Select", 2022, 2021]

            columns = st.columns([3, 5, 2])
            with columns[0]:
                ausp_choice = st.selectbox("Select the Season", seasons, key="ausp")
            with columns[2]:
                st.subheader("")
                st.subheader("")
                st.write("(Amount in ₹ lakhs)")

            if ausp_choice == "Select":
                streamlit_table(table.style.set_properties(**table_style))
            else:
                table = table.loc[table["Season"] == ausp_choice]
                table.index = npy.arange(1, len(table) + 1)
                streamlit_table(table.style.set_properties(**table_style))

            csv = convert_dataframe_to_csv(dataframe)
            download_csv_button(csv, "IPL 2021-2022 AUSP Data.csv", "Download Unsold Players data")

    elif choice == "Support Staff":
        st.subheader("Support Staff")
        st.write("Apart from players, Franchises also do certain changes in Staff such as managers, coaches, "
                 "physiotherapists, and other managerial staff. Of all the staff coaches garner more interest among "
                 "IPL followers. Selection of Coaches also is observed with heightened interest among IPL fans. The "
                 "information about staff changes in every team is presented below.")

        with st.expander("Staff Changes", expanded=True):
            st.write("This section of the page contains Staff Changes list with their franchise and Role for the year "
                     "2021 and 2022")

            dataframe = pa.read_csv(f"PERSONNEL_CHANGES/WebsiteDatasets/IPL 2021-2022 SS Data.csv")
            dataframe = dataframe.drop(['ID'], axis=1)
            dataframe.index = npy.arange(1, len(dataframe) + 1)
            table = dataframe
            seasons = ["Select", 2022, 2021]

            columns = st.columns([3, 5, 2])
            with columns[0]:
                ss_choice = st.selectbox("Select the Season", seasons, key="ss")
            with columns[2]:
                st.subheader("")
                st.subheader("")
                st.write("(Amount in ₹ lakhs)")

            if ss_choice == "Select":
                streamlit_table(table.style.set_properties(**table_style))
            else:
                table = table.loc[table["Season"] == ss_choice]
                table.index = npy.arange(1, len(table) + 1)
                streamlit_table(table.style.set_properties(**table_style))

            csv = convert_dataframe_to_csv(dataframe)
            download_csv_button(csv, "IPL 2021-2022 SS Data.csv", "Download Staff Changes data")
