import streamlit as st
import pymongo


def main():
    st.title("Feedback Form")
    with st.form(key="feedback_form"):
        answer1 = st.text_input("1) Name", placeholder="Enter your Name")
        answer2 = st.text_input("2) Age (optional)", placeholder="Enter your Age")
        answer3 = st.text_input("3) Email (optional)", placeholder="Enter your email ID")
        answer4 = st.text_input("4) Does our IPL Analysis meet with your expectations? (optional)")
        answer5 = st.radio("5) Does the prediction meet with the real time data/scores?", ("Yes", "Maybe", "No"))
        answer6 = st.radio("6) Did you find our analysis useful?", ("Yes", "Maybe", "No"))
        answer7 = st.text_input("7) Did we reach your expectations? (optional)", placeholder="Enter the reason")
        answer8 = st.radio("8) Did you find our website useful?", ("Yes", "Maybe", "No"))
        answer9 = st.slider("9) How would you rate our website?", min_value=1, max_value=5, value=3)
        answer10 = st.text_area("10) Share your suggestions to improve our website?",
                                placeholder="Enter any comments")

        submit = st.form_submit_button(label="Submit this form")
        if submit:
            if answer1:
                if answer4:
                    if answer5:
                        st.success("Your Responses are recorded, Thank you for visiting our website")
                        connection = pymongo.MongoClient(st.secrets["mongodb"]["url"])
                        database = connection.get_database("FEEDBACK_DATABASE")
                        table = database.FEEDBACK_COLLECTION

                        response_data = {
                            "S_No": (table.count_documents({}) + 1),
                            "Question1": answer1,
                            "Question2": answer2,
                            "Question3": answer3,
                            "Question4": answer4,
                            "Question5": answer5,
                            "Question6": answer6,
                            "Question7": answer7,
                            "Question8": answer8,
                            "Question9": answer9,
                            "Question10": answer10
                        }
                        table.insert_one(response_data)
            else:
                st.warning("Please Enter Your Name")
