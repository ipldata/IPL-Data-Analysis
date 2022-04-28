import streamlit as st
import run_rate
import ipl_winner_predictor


def main():
    st.title("IPL Prediction")

    run_rate.run_rate()

    st.subheader("Winner Predictor")
    columns = st.columns(2)
    with columns[0]:
        predict = ipl_winner_predictor.winner_predictor()
    with columns[1]:
        st.dataframe(predict)
