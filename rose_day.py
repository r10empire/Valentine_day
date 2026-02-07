import streamlit as st

# Page config
st.set_page_config(
    page_title="Happy Rose Day 🌹",
    page_icon="🌹",
    layout="centered"
)

# Get name from URL
name = st.query_params.get("name")



# CSS Styling
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #ffdde1, #ee9ca7);
}
.card {
    background-color: white;
    padding: 30px;
    border-radius: 20px;
    text-align: center;
    box-shadow: 0px 10px 25px rgba(0,0,0,0.15);
}
.rose {
    font-size: 60px;
}
.title {
    font-size: 36px;
    color: #e91e63;
    font-weight: bold;
}
.text {
    font-size: 20px;
    color: #444;
}
.footer {
    margin-top: 20px;
    font-size: 16px;
    color: #888;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
/* Falling roses container */
.rose-container {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    overflow: hidden;
    z-index: 999;
}

/* Individual rose */
.rose {
    position: absolute;
    top: -10%;
    font-size: 30px;
    animation-name: fall;
    animation-timing-function: linear;
    animation-iteration-count: infinite;
}

/* Falling animation */
@keyframes fall {
    0% {
        transform: translateY(0) rotate(0deg);
        opacity: 1;
    }
    100% {
        transform: translateY(110vh) rotate(360deg);
        opacity: 0;
    }
}
</style>

<div class="rose-container">
    <div class="rose" style="left:10%; animation-duration:10s;">🌹</div>
    <div class="rose" style="left:25%; animation-duration:12s; font-size:24px;">🌹</div>
    <div class="rose" style="left:40%; animation-duration:9s;">🌹</div>
    <div class="rose" style="left:55%; animation-duration:14s; font-size:35px;">🌹</div>
    <div class="rose" style="left:70%; animation-duration:11s;">🌹</div>
    <div class="rose" style="left:85%; animation-duration:13s; font-size:28px;">🌹</div>
</div>
""", unsafe_allow_html=True)


# If name exists → show wish
if name:
    st.markdown(f"""
    <div class="card">
        <div class="rose">🌹</div>
        <div class="title">Happy Rose Day</div>
        <br>
        <div class="text">
            Dear <b>{name}</b>,<br><br>
            Like a rose, you bring beauty, love,  
            and happiness into my life.<br><br>
            Thank you for being my forever ❤️
        </div>
        <div class="footer">
            — From someone who loves you endlessly 💕
        </div>
    </div>
    """, unsafe_allow_html=True)

else:
    # Creator page
    st.markdown("## 🌹 Create Your Rose Day Wish")

    gf_name = st.text_input("Enter your girlfriend's name 💖")

    if gf_name:
        base_url = "https://your-streamlit-app-url"
        wish_link = f"{base_url}?name={gf_name.replace(' ', '%20')}"

        st.success("✨ Your Rose Day link is ready!")
        st.code(wish_link, language="text")

        st.markdown("📩 **Send this link to her and make her smile** 😊")
