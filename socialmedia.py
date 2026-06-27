import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import random
import os


st.set_page_config(page_title="Social Media Risk Predictor", layout="wide")


st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

html, body {
    font-family: 'Poppins', sans-serif;
    background: #0f172a;
    color: white;
}

.card {
    background: rgba(255,255,255,0.05);
    padding: 20px;
    border-radius: 15px;
    margin: 10px 0;
}

h1,h2,h3 {
    color: #38bdf8;
}

.stButton>button {
    background: #38bdf8;
    color: black;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)


page = st.sidebar.radio("📱 Menu",
["🏠 Dashboard", "📝 Tracker", "🔍 Predictor", "📊 Analysis", "🎬 Awareness"])


quotes = [
    "Your life is bigger than your screen.",
    "Control your phone or it controls you.",
    "Discipline > Dopamine.",
    "Real life > Reel life."
]


def calculate_score(usage, sleep, productivity):
    score = usage*2 + (10-sleep)*1.5 + (10-productivity)

    if score > 25:
        risk = "High"
    elif score > 15:
        risk = "Medium"
    else:
        risk = "Low"

    return score, risk


if page == "🏠 Dashboard":

    st.title("📱 Social Media Risk Predictor App")

    st.markdown("""
    <div class="card">
    Track, analyze, and reduce your social media addiction using real data.
    </div>
    """, unsafe_allow_html=True)

    st.subheader("📲 Popular Social Media Platforms")

    col1, col2, col3, col4, col5, col6 = st.columns(6)

    with col1:
        st.image("https://cdn-icons-png.flaticon.com/512/733/733585.png", width=60)
        st.caption("WhatsApp")

    with col2:
        st.image("https://cdn-icons-png.flaticon.com/512/2111/2111463.png", width=60)
        st.caption("Instagram")

    with col3:
        st.image("https://cdn-icons-png.flaticon.com/512/1384/1384060.png", width=60)
        st.caption("YouTube")

    with col4:
        st.image("https://cdn-icons-png.flaticon.com/512/733/733579.png", width=60)
        st.caption("Twitter")

    with col5:
        st.image("https://cdn-icons-png.flaticon.com/512/733/733547.png", width=60)
        st.caption("Facebook")

    with col6:
        st.image("https://cdn-icons-png.flaticon.com/512/2111/2111646.png", width=60)
        st.caption("Snapchat")

    st.markdown("---")

    st.subheader("💡 Daily Motivation")
    st.markdown(f"### *{random.choice(quotes)}*")


elif page == "📝 Tracker":

    st.header("Enter Your Daily Data")

    usage = st.slider("📱 Usage (hrs)", 0.0, 15.0, 5.0)
    sleep = st.slider("😴 Sleep (hrs)", 0.0, 12.0, 7.0)
    productivity = st.slider("⚡ Productivity Level", 1, 10, 5)

    if st.button("Save Data"):

        score, risk = calculate_score(usage, sleep, productivity)

        new_data = pd.DataFrame([[usage, sleep, productivity, score, risk]],
                                columns=["Usage", "Sleep", "Productivity", "Score", "Risk"])

        file_exists = os.path.isfile("data.csv")

        new_data.to_csv("data.csv", mode='a', header=not file_exists, index=False)

        st.success("✅ Data Saved Successfully!")


elif page == "🔍 Predictor":

    st.header("Addiction Prediction")

    usage = st.slider("Usage (hrs)", 0.0, 15.0, 5.0)
    sleep = st.slider("Sleep (hrs)", 0.0, 12.0, 7.0)
    productivity = st.slider("Productivity", 1, 10, 5)

    if st.button("Analyze"):

        score, risk = calculate_score(usage, sleep, productivity)

        st.subheader(f"Score: {round(score,2)}")
        st.progress(min(int(score*3),100))

        if risk == "High":
            st.error("🚨 High Addiction Risk")
            st.write("Reduce usage and improve sleep immediately.")
        elif risk == "Medium":
            st.warning("⚠️ Medium Risk")
            st.write("Try to balance your daily routine.")
        else:
            st.success("✅ Low Risk")
            st.write("Good job! Keep it up.")


elif page == "📊 Analysis":

    st.header("📊 Your Data Analysis")

    if os.path.exists("data.csv"):

        df = pd.read_csv("data.csv")

        st.dataframe(df)

        st.subheader("Usage vs Risk")
        fig, ax = plt.subplots()
        sns.barplot(x="Risk", y="Usage", data=df, ax=ax)
        st.pyplot(fig)

        st.subheader("Sleep vs Score")
        fig2, ax2 = plt.subplots()
        sns.scatterplot(x="Sleep", y="Score", data=df, ax=ax2)
        st.pyplot(fig2)

    else:
        st.warning("No data found. Please add data first.")


elif page == "🎬 Awareness":

    st.header("Why You Should Reduce Social Media")

    st.video("https://youtu.be/QugooaNRnsk")

    st.markdown("💡 Tips:")
    st.write("- Turn off notifications")
    st.write("- Use app timers")
    st.write("- Sleep on time")