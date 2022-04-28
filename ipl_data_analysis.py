import streamlit as st
import base64
import home
import about_ipl
import ipl_stats
import ipl_prediction
import points_table
import personnel_changes
import feedback


def image_to_bytes(image_path):
    image_file = open(image_path, "rb")
    image_bytes = image_file.read()
    encoded_image = base64.b64encode(image_bytes).decode()
    return encoded_image


def main():
    st.set_page_config(
        page_title="IPL Data Analysis",
        page_icon=f"data:image/png;"
                  f"base64,{image_to_bytes('HOME/WebsiteImages/page_icon.png')}",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    home_page_markdown = open("HOME/WebsiteStyles/home_style.css", "r").read()
    st.markdown(f"<style>{home_page_markdown}</style>", unsafe_allow_html=True)

    st.sidebar.title("IPL Data Analysis")
    sidebar_image = f'<img src="data:image/png;base64,{image_to_bytes("HOME/WebsiteImages/page_logo.png")}"' \
                    f' class="image_sidebar">'
    st.sidebar.markdown(sidebar_image, unsafe_allow_html=True)
    st.sidebar.subheader("")

    pages_list = ["Home", "About IPL", "IPL Stats", "IPL Prediction", "Points Table", "Personnel Changes", "Feedback"]
    page = st.sidebar.radio("GO TO", pages_list)

    if page == "Home":
        home.main()
    elif page == "About IPL":
        about_ipl.main()
    elif page == "IPL Stats":
        ipl_stats.main()
    elif page == "IPL Prediction":
        ipl_prediction.main()
    elif page == "Points Table":
        points_table.main()
    elif page == "Personnel Changes":
        personnel_changes.main()
    elif page == "Feedback":
        feedback.main()

    st.sidebar.title("Thank You for visiting our Web app")
    st.sidebar.subheader("")
    st.sidebar.write("Please take a few minutes from your busy schedule and provide us your feedback.")
    st.sidebar.write("Your feedback is valuable to us. It helps us to improve our Web analysis app")


if __name__ == "__main__":
    main()
