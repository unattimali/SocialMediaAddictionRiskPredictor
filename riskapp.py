import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import random

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
["🏠 Dashboard", "🔍 Predictor", "📊 Analysis", "🎬 Awareness"])


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


def get_recommendation(risk):
    if risk == "High":
        return [
            "📵 Limit social media to less than 2 hours/day",
            "😴 Maintain 7-8 hours of sleep",
            "🚫 Avoid phone before bedtime",
            "📊 Use app timers or blockers"
        ]
    elif risk == "Medium":
        return [
            "⏳ Reduce screen time gradually",
            "📚 Focus on productive tasks",
            "🌙 Avoid late-night scrolling"
        ]
    else:
        return [
            "✅ Maintain your current routine",
            "💪 Keep a balanced lifestyle",
            "📈 Continue productive habits"
        ]


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
        elif risk == "Medium":
            st.warning("⚠️ Medium Risk")
        else:
            st.success("✅ Low Risk")

        # 🔥 RECOMMENDATIONS
        st.subheader("💡 Personalized Suggestions")
        tips = get_recommendation(risk)

        for tip in tips:
            st.write(tip)

        st.markdown(f"### 🔥 {random.choice(quotes)}")


elif page == "📊 Analysis":

    st.header("📊 Your Data Analysis")

    try:
        df = pd.read_csv("data.csv")

        st.dataframe(df)

        st.subheader("Usage vs Risk")

        fig, ax = plt.subplots(figsize=(8,5))  
        sns.barplot(x="Risk", y="Usage", data=df, ax=ax)
        st.pyplot(fig)

        st.subheader("Sleep vs Score")

        fig2, ax2 = plt.subplots(figsize=(8,5)) 
        sns.scatterplot(x="Sleep", y="Score", data=df, ax=ax2)
        st.pyplot(fig2)

    except:
        st.warning("No data found. Please add data first.")


elif page == "🎬 Awareness":

    st.header("Why You Should Reduce Social Media")

    st.video("https://youtu.be/QugooaNRnsk")

    st.markdown("💡 Tips:")
    st.write("- Turn off notifications")
    st.write("- Use app timers")
    st.write("- Sleep on time")