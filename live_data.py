import requests as req
import bs4
import pandas as pa


def web_scraping_data():
    points_table_url = "https://www.news18.com/cricketnext/ipl-2022/points-table.html"
    response = req.get(points_table_url)
    data_in_html = bs4.BeautifulSoup(response.content, 'html5lib')

    points_table_data = []
    for data in data_in_html.findAll('td'):
        points_table_data.append(data.text)
    points_table_data = [points_table_data[i:i + 9] for i in range(0, len(points_table_data), 9)]

    dataframe = pa.DataFrame(data=points_table_data,
                             columns=["Rank", "Team", "Played", "Won", "Lost", "N/R", "Tied", "NET RR", "Points"])
    dataframe.to_csv("POINTS_TABLE/WebsiteDatasets/live_data.csv")
    return dataframe
