import streamlit as st
import time
import random

# ---------------- READ FROM URL ----------------
params = st.query_params
GF_NAME = params.get("gf", "My Love ❤️")
YOUR_NAME = params.get("me", "Someone Special")

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="💍 Propose Day",
    page_icon="❤️",
    layout="centered"
)

# ---------------- CSS ----------------
st.markdown("""
<style>
body {
    background: linear-gradient(120deg, #ff758c, #ff7eb3);
}
.main {
    background: rgba(255,255,255,0.92);
    border-radius: 24px;
    padding: 40px;
}
.story {
    font-size: 20px;
    text-align: center;
    line-height: 1.9;
}
.heart {
    font-size: 36px;
    text-align: center;
    animation: beat 1.4s infinite;
}
@keyframes beat {
    0% {transform: scale(1);}
    25% {transform: scale(1.2);}
    50% {transform: scale(1);}
    75% {transform: scale(1.2);}
}
.footer {
    text-align: center;
    font-size: 14px;
    color: gray;
}
</style>
""", unsafe_allow_html=True)

# ---------------- SESSION STATE ----------------
if "step" not in st.session_state:
    st.session_state.step = 1

def type_text(text, speed=0.035):
    box = st.empty()
    out = ""
    for ch in text:
        out += ch
        box.markdown(f"<div class='story'>{out}</div>", unsafe_allow_html=True)
        time.sleep(speed)

# ---------------- STEP 1 ----------------
if st.session_state.step == 1:
    st.markdown("<h1 style='text-align:center;color:#ff2e63;'>Happy Propose Day 💍</h1>", unsafe_allow_html=True)
    st.markdown("<div class='heart'>❤️ 💖 ❤️</div>", unsafe_allow_html=True)

    intro = f"""
    {GF_NAME},<br><br>
    This isn’t random.<br>
    This isn’t accidental.<br><br>
    Some feelings deserve
    more than just words…
    """

    type_text(intro)

    if st.button("✨ Continue"):
        st.session_state.step = 2
        st.rerun()

# ---------------- STEP 2 ----------------
elif st.session_state.step == 2:
    story = f"""
    Somewhere between the conversations,<br>
    the laughs,<br>
    and the quiet moments…<br><br>
    you became important to me ❤️
    """

    type_text(story)

    if st.button("💫 There’s more"):
        st.session_state.step = 3
        st.rerun()

# ---------------- STEP 3 ----------------
elif st.session_state.step == 3:
    suspense = f"""
    {GF_NAME},<br><br>
    I don’t want perfect.<br>
    I just want *you* —<br>
    exactly the way you are 😌
    """

    type_text(suspense)

    if st.button("💍 Open my heart"):
        st.session_state.step = 4
        st.rerun()

# ---------------- FINAL STEP ----------------
elif st.session_state.step == 4:
    st.balloons()

    proposal = f"""
    {GF_NAME}, ❤️<br><br>
    Will you be mine?<br><br>
    Not just for today,<br>
    but for all the days that follow.<br><br>
    — {YOUR_NAME}
    """

    type_text(proposal, speed=0.05)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Yes ❤️"):
            st.success("This is my favorite answer 🥹💖")
            st.snow()
    with col2:
        if st.button("Obviously 😍"):
            st.success("Forever unlocked 💍✨")
            st.balloons()

# ---------------- DECOR ----------------
hearts = " ".join(random.choice(["❤️", "💖", "💕", "💘"]) for _ in range(10))
st.markdown(f"<div style='text-align:center;font-size:26px'>{hearts}</div>", unsafe_allow_html=True)
st.markdown("<div class='footer'>Made specially, not generically ❤️</div>", unsafe_allow_html=True)
