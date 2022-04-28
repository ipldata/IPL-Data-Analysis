import requests as req
import bs4


def live_score():
    live_score_url = "https://www.cricbuzz.com/cricket-match/live-scores"
    code = 115
    response = req.get(live_score_url)
    data_in_html = bs4.BeautifulSoup(response.content, 'html5lib')

    data = []
    for d in data_in_html.findAll('div'):
        data.append(d.text)

    live_score_data = data[code]
    print(live_score_data)
    header = (live_score_data.split(",")[0]).lstrip(" ")
    team_1 = (header.split("vs")[0]).rstrip(" ")
    team_2 = (header.split("vs")[1]).lstrip(" ")
    match_number = ((live_score_data.split(",")[1]).split("th")[0]).lstrip(" ")
    venue = ((live_score_data.split(",")[2]).split(":")[2]).lstrip(" ")
    date = ((live_score_data.split(",")[3]).split(":")[1]).lstrip(" ")
    time = (live_score_data.split(",")[4]).split("PM")[0]
    toss_winner = ((live_score_data.split("Toss:")[1]).split("Recent")[0]).rstrip(" ").lstrip(" ")
    team_score = ((((live_score_data.split(",")[4]).split("("))[0]).rstrip(" ")).split(" ")
    team_score = team_score[len(team_score) - 2:]
    batting_team = team_score[0]
    score = team_score[1]
    balls = ((((live_score_data.split(",")[4]).split("("))[1]).split(")")[0])
    run_rate = ((live_score_data.split(",")[4]).split(":")[2]).split(" ")[0]

    print(team_1)
    print(team_2)
    print(match_number)
    print(venue)
    print(date)
    print(time)
    print(toss_winner)
    print(batting_team)
    print(score)
    print(balls)
    print(run_rate)
    return team_1, team_2, match_number, venue, date, time, toss_winner, batting_team, score, balls, run_rate
