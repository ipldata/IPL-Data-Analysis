import pandas as pa
import streamlit as st
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from xgboost import XGBClassifier


def winner_predictor():
    train_data = pa.read_csv('IPL_PREDICTION/WebsiteDatasets/IPL 2008-2021 Matches Data.csv')
    train_data.isnull().sum()
    train_data['City'].fillna('Abu Dhabi', inplace=True)
    train_data['Match Winner'].fillna('Draw', inplace=True)

    train_data.replace(
        {
            "Mumbai Indians": "MI", "Delhi Capitals": "DC", "Sunrisers Hyderabad": "SRH", "Rajasthan Royals": "RR",
            "Kolkata Knight Riders": "KKR", "Punjab Kings": "PBKS",
            "Chennai Super Kings": "CSK", "Royal Challengers Bangalore": "RCB",
            "Kochi Tuskers Kerala": "KTK", "Rising Pune Supergiants": "RPS",
            "Gujarat Lions": "GL", "Pune Warriors India": "PW", "QUALIFIER1": "Q1", "QUALIFIER2": "Q2"
        }, inplace=True)
    encode = {
        'Team1': {
            'KKR': 1, 'CSK': 2, 'RR': 3, 'MI': 4, 'SRH': 5, 'PBKS': 6, 'RCB': 7, 'DC': 8, 'KTK': 9, 'RPS': 10, 'GL': 11,
            'PW': 12, 'Q2': 0, 'Q1': 0},
        'Team2': {
            'KKR': 1, 'CSK': 2, 'RR': 3, 'MI': 4, 'SRH': 5, 'PBKS': 6, 'RCB': 7, 'DC': 8, 'KTK': 9, 'RPS': 10, 'GL': 11,
            'PW': 12, 'Q2': 0, 'Q1': 0},
        'Toss Winner': {
            'KKR': 1, 'CSK': 2, 'RR': 3, 'MI': 4, 'SRH': 5, 'PBKS': 6, 'RCB': 7, 'DC': 8, 'KTK': 9, 'RPS': 10, 'GL': 11,
            'PW': 12, 'Q2': 0, 'Q1': 0},
        'Match Winner': {
            'KKR': 1, 'CSK': 2, 'RR': 3, 'MI': 4, 'SRH': 5, 'PBKS': 6, 'RCB': 7, 'DC': 8, 'KTK': 9, 'RPS': 10, 'GL': 11,
            'PW': 12, 'Draw': 13, 'Q2': 0, 'Q1': 0}
    }

    train_data.replace(encode, inplace=True)
    dic_val = encode["Match Winner"]
    train = train_data[['Team1', 'Team2', 'City', 'Toss Decision', 'Toss Winner', 'Venue', 'Match Winner']]
    df = pa.DataFrame(train)
    var_mod = ['City', 'Toss Decision', 'Venue']
    le = LabelEncoder()
    for i in var_mod:
        df[i] = le.fit_transform(df[i])

    x = df[['Team1', 'Team2', 'Venue']]
    y = df[['Match Winner']]
    y = y.astype('int')
    sc = StandardScaler()
    x = sc.fit_transform(x)
    logistic_model = LogisticRegression()
    logistic_model.fit(x, y)
    st.write("Logistic Regression accuracy: ", (logistic_model.score(x, y)) * 100)
    random_model = RandomForestClassifier()
    random_model.fit(x, y)
    st.write("Random Forest accuracy: ", (random_model.score(x, y)) * 100)
    xgb_model = XGBClassifier(n_estimators=390, learning_rate=0.1)
    xgb_model.fit(x, y)
    st.write("XGB accuracy: ", (xgb_model.score(x, y)) * 100)
    knn_model = KNeighborsClassifier()
    knn_model.fit(x, y)
    st.write("KNeighbor Classifier accuracy", (knn_model.score(x, y)) * 100)
    nb_model = GaussianNB()
    nb_model.fit(x, y)
    st.write("Gaussion Navie Bayis accuracy: ", (nb_model.score(x, y)) * 100)
    decision_model = DecisionTreeClassifier()
    decision_model.fit(x, y)
    st.write("Decision Tree Classifier accuracy: ", (decision_model.score(x, y)) * 100)
    svm_model = SVC()
    svm_model.fit(x, y)
    st.write("SVM accuracy: ", (svm_model.score(x, y)) * 100)

    test_data = pa.read_csv('IPL_PREDICTION/WebsiteDatasets/IPL 2022 MS Data.csv')
    encode = {
        'Team1': {'KKR': 1, 'CSK': 2, 'RR': 3, 'MI': 4, 'SRH': 5, 'PBKS': 6, 'RCB': 7, 'DC': 8, 'KTK': 9, 'RPS': 10,
                  'GL': 11, 'PW': 12},
        'Team2': {'KKR': 1, 'CSK': 2, 'RR': 3, 'MI': 4, 'SRH': 5, 'PBKS': 6, 'RCB': 7, 'DC': 8, 'KTK': 9, 'RPS': 10,
                  'GL': 11, 'PW': 12}
    }

    test_data.replace(encode, inplace=True)
    var_mod = ['Venue']
    le = LabelEncoder()
    for i in var_mod:
        test_data[i] = le.fit_transform(test_data[i])

    test_x = test_data[['Team1', 'Team2', 'Venue']]
    test_x = sc.fit_transform(test_x)
    y_predict = random_model.predict(test_x)
    new_list = []
    for i in y_predict:
        new_list.append(list(dic_val.keys())[list(dic_val.values()).index(i)])
    test_data['Match Winner'] = new_list
    test_data['Venue'] = le.inverse_transform(test_data['Venue'])
    for i in range(60):
        test_data['Team1'][i] = (list(dic_val.keys())[list(dic_val.values()).index(test_data['Team1'][i])])
        test_data['Team2'][i] = (list(dic_val.keys())[list(dic_val.values()).index(test_data['Team2'][i])])
    test_data.loc[test_data["Match Winner"] == test_data["Team1"], "Winner Team"] = 1
    test_data.loc[test_data["Match Winner"] != test_data["Team1"], "Winner Team"] = 2
    test_data['Win by Number'] = test_data['Winner Team'].astype(int)
    test_data = test_data.head(50)
    test_data = test_data[["Team1", "Team2", "Match Winner"]]
    test_data = test_data.astype(str)
    return test_data
