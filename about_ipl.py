import pandas as pa
import streamlit as st
import ipl_data_analysis


def main():
    st.title("About IPL")

    about_ipl_page_markdown = open("ABOUT_IPL/WebsiteStyles/about_ipl_style.css", "r").read()
    st.markdown(f"<style>{about_ipl_page_markdown}</style>", unsafe_allow_html=True)

    st.write("The Indian Premier League (IPL)  is a Twenty-20 cricket tournament league started by Board of Control "
             "for Cricket in India (BCCI) in 2008. The tournament was established to promote cricket in India and "
             "thereby nurture young and talented players. IPL is an annual event where teams representing different "
             "Indian cities compete against each other. IPL is now a giant remunerative cricket venture where teams "
             "are selected using an auction.")
    st.write("IPL can rightly be credited as a game-changer for the sport in the country. Undoubtedly, "
             "IPL is the biggest cricketing league in the world. The league’s fan following is not only limited to "
             "India but all across the world. The tournament is nothing less than a festival for cricket fans. The "
             "league is a perfect balance of glamour, glitz, and sports. This tournament is the most viewed "
             "cricketing league in the world. The IPL has transformed the game at a global level.")

    st.image(f"data:image/png;"
             f"base64,{ipl_data_analysis.image_to_bytes('ABOUT_IPL/WebsiteImages/first_image.png')}")

    st.subheader("IPL Sponsors from 2008-2022")
    columns = st.columns(2)
    with columns[0]:
        sponsors = pa.read_csv("ABOUT_IPL/WebsiteDatasets/sponsors_dataset.csv")
        st.dataframe(data=sponsors)
    with columns[1]:
        st.subheader("")
        st.image(f"data:image/png;"
                 f"base64,{ipl_data_analysis.image_to_bytes('ABOUT_IPL/WebsiteImages/second_image.png')}")

    st.subheader("Team's Performance")
    st.write("Out of the thirteen teams that have played in the Indian Premier League since its inception, "
             "one team has won the competition five times, one team has won the competition four times, one team has "
             "won the competition twice and three other teams have won it once. Mumbai Indians are the most "
             "successful team in the league’s history in terms of the number of titles won. The Chennai Super Kings "
             "have won 4 titles, the Kolkata Knight Riders have won two titles, and the other three teams who have "
             "won the tournament are the Deccan Chargers, Rajasthan Royals, and Sunrisers Hyderabad. The current "
             "champions are the Chennai Super Kings who defeated the Kolkata Knight Riders in the final of 2021 "
             "season securing their fourth title.")
    st.subheader("")
    st.image(f"data:image/png;"
             f"base64,{ipl_data_analysis.image_to_bytes('ABOUT_IPL/WebsiteImages/third_image.png')}")

    st.subheader("IPL 2022 Teams and Squads")
    st.write("For only the second time in the IPL and the first time in 11 years, a total of 10 teams will compete "
             "for the ultimate glory. Joining Mumbai Indians, Chennai Super Kings, Royal Challengers Bangalore, "
             "Kolkata Knight Riders, Rajasthan Royals, Sunrisers Hyderabad, Delhi Capitals and Punjab Kings, "
             "are debutants Lucknow Super Giants and Gujarat Titans, led by KL Rahul and Hardik Pandya respectively.")

    st.subheader("Complete List of All IPL Team Owners 2022")
    owners = pa.read_csv("ABOUT_IPL/WebsiteDatasets/owners_dataset.csv")
    st.dataframe(data=owners)

    st.subheader("IPL 2022 Teams and Brand Value")
    columns = st.columns(2)
    with columns[0]:
        brand = pa.read_csv("ABOUT_IPL/WebsiteDatasets/brand_dataset.csv")
        st.dataframe(data=brand)
    with columns[1]:
        st.subheader("")
        st.subheader("")
        st.image(f"data:image/png;"
                 f"base64,{ipl_data_analysis.image_to_bytes('ABOUT_IPL/WebsiteImages/fourth_image.png')}")

    st.subheader("List of IPL awards")
    st.write("Arguably the IPL is the best cricket league in the world. The best league sure does award some honors "
             "to players/teams in each aspect. The tournament honors the best players at the end of each season with "
             "various awards. The awards available in IPL are The Orange Cap, The Purple Cap, Most Valuable Player, "
             "Maximum six award, Emerging player of the tournament, and Fair Play award. Let’s take a brief look at "
             "each of the types of awards in IPL in this article.")

    st.subheader("Individual Awards")
    st.write("Orange Cap – The wonderful-looking Orange Cap is awarded to the highest run-scorer of the season and "
             "was introduced back on 25th April a week after the start of the season. While the tournament runs, "
             "the batsman with most runs wears the cap while fielding and batting. The most run-scorer of the "
             "tournament gets it on the final day permanently.")
    st.image(f"data:image/png;"
             f"base64,{ipl_data_analysis.image_to_bytes('ABOUT_IPL/WebsiteImages/orange_cap.png')}")
    st.write("Purple Cap – The elegant-looking Purple Cap is awarded to the highest wicket-taker of the season of the "
             "tournament’s end. It was introduced on 13th May 2008. The leading wicket-taker wears the cap while "
             "fielding while the leading wicket-taker of the season wins the cap on the final day.")
    st.image(f"data:image/png;"
             f"base64,{ipl_data_analysis.image_to_bytes('ABOUT_IPL/WebsiteImages/purple_cap.png')}")
    st.write("Most Valuable Player – Basically, the best player of the tournament gets the Most Valuable Ward. Before "
             "2012 the award was called “Man of the tournament.” But changed its name the following season to “Most "
             "Valuable Player of the Tournament.")
    st.write("Maximum Six Award – Batsman hitting the most six in a season gets the Maximum Six Award.")
    st.write("Emerging Player of the Tournament – The Emerging Player of the tournament is given to the best young "
             "player of the season and has the potential of becoming a future star.")
    st.write("The other awards that are given at individual level are Power player of the season, Game changer of the "
             "Season, Super Striker of the Season, Player of the Series, Power player of the Season, Perfect catch of "
             "the season")
    st.subheader("Team Awards")
    st.write("Fair Play Awards – IPL awards the Fair Play Award to a team. After the completion of each match, "
             "the two on-field umpires along with the third umpire allots points to each team on the basis of their "
             "performance to hold the spirit of the game.")
    st.image(f"data:image/png;"
             f"base64,{ipl_data_analysis.image_to_bytes('ABOUT_IPL/WebsiteImages/last_image.png')}")
    st.subheader("Little Known facts of IPL")
    st.write("- Only two Indians to have won Most valuable Player - Sachin Tendulkar, Virat Kholi")
    st.write("- Cost of one ball in IPL 2018 – The broad casting rights of IPL 2018 were sold for a whopping Rs "
             "16347.5 "
             "making 1 ball cost approximately Rs. 21 lakh")
    st.write("- No no-ball for 386 overs - Piyush Chawla is one of the most underrated spinners of Indian cricket "
             "history. However, the leg-spinner holds one of the most astounding records. During his time with Delhi "
             "Daredevils, he did not bowl a single no-ball for 386 overs. For eight years, he had bowled in the most "
             "disciplined way one can imagine.")
    st.write("- Only Two overseas players have played more than 100 matches for a single team – Kieron Polard and AB "
             "de "
             "Villiers are the only two players who have played over 100 matches for one team")
    st.write("- Virat Kohli has been part of three double century partnerships – 204 with Chris Gayle, 215 with de "
             "Villiers, 229 with A B de Villiers")
    st.write("- RCB hold the record for the highest and lowest total in IPL history – 263 and 49")
