import streamlit as st


def run_rate():
    st.subheader("Run rate calculator")
    columns = st.columns([5, 2, 3])
    with columns[0]:
        st.write("Example for overs input in below inout field")
        st.dataframe(data=[["1.1", "1.2", "1.3", "1.4", "1.5", "1.6"], ["1.16", "1.33", "1.50", "1.67", "1.83", "2"]])
        innings = st.text_input(label="Enter 1st or 2nd innings", max_chars=3)
        if innings == "1st":
            overs = st.number_input(label="Enter the numbers of overs completed", max_value=20)
            if overs > 0:
                score = st.number_input(label="Enter the score scored till now", min_value=0)
                if score > 0:
                    rate = float(score / overs)
                    current_run_rate = int(score + (rate * abs(overs - 20)))
                    run_rate_8 = int(score + (8 * abs(overs - 20)))
                    run_rate_10 = int(score + (10 * abs(overs - 20)))
                    run_rate_12 = int(score + (12 * abs(overs - 20)))

                    with columns[2]:
                        if innings == "1st":
                            st.title(" ")
                            st.metric("Current run rate", rate)
                            st.metric("Current run rate per over score", current_run_rate)
                            st.metric("8 runs per over", run_rate_8)
                            st.metric("10 runs per over", run_rate_10)
                            st.metric("12 runs per over", run_rate_12)
                else:
                    st.write("Enter the score scored")
            else:
                st.write("Enter the overs completed")
        elif innings == "2nd":
            required_score = st.number_input(label="Enter the total score in 1st Innings", min_value=0)
            if required_score > 0:
                overs = st.number_input(label="Enter the overs completed", max_value=20, min_value=0)
                if overs == 0:
                    required_rate = float(required_score / 20)
                    with columns[2]:
                        if innings == "2nd" and overs == 0:
                            st.title(" ")
                            st.title(" ")
                            st.title(" ")
                            st.title(" ")
                            st.metric("Required run rate", required_rate)
                else:
                    score = st.number_input(label="Enter the score scored till now", min_value=0)
                    if score > 0:
                        current_run_rate = float(score / overs)
                        required_run_rate = float((required_score - score) / abs(overs - 20))
                        with columns[2]:
                            if innings == "2nd" and overs != 0:
                                st.title(" ")
                                st.title(" ")
                                st.title(" ")
                                st.title(" ")
                                st.metric("Current run rate", current_run_rate)
                                st.metric("Required run rate", required_run_rate)
        else:
            st.write("Enter the valid input (1st / 2nd)")
