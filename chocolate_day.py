import streamlit as st
import time
import random

# ---------------- READ FROM URL ----------------
params = st.query_params
GF_NAME = params.get("gf", "My Sweetheart ❤️")
YOUR_NAME = params.get("me", "Someone Who Loves You")

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="🍫 Happy Chocolate Day",
    page_icon="🍫",
    layout="centered"
)

# ---------------- CSS ----------------
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #6f1d1b, #bb9457);
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
    color: #3a2d28;
}
.choco {
    font-size: 38px;
    text-align: center;
    animation: pop 1.5s infinite;
}
@keyframes pop {
    0% {transform: scale(1);}
    50% {transform: scale(1.15);}
    100% {transform: scale(1);}
}
.footer {
    text-align: center;
    font-size: 14px;
    color: #5a4a42;
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
    st.markdown(
        "<h1 style='text-align:center;color:#5a1a01;'>Happy Chocolate Day 🍫</h1>",
        unsafe_allow_html=True
    )
    st.markdown("<div class='choco'>🍫 🍩 🍪</div>", unsafe_allow_html=True)

    intro = f"""
    {GF_NAME},<br><br>
    Today isn’t just about chocolates.<br><br>
    It’s about sweetness,<br>
    warmth,<br>
    and those little cravings<br>
    that make life better 😌
    """

    type_text(intro)

    if st.button("🍬 Continue"):
        st.session_state.step = 2
        st.rerun()

# ---------------- STEP 2 ----------------
elif st.session_state.step == 2:
    story = f"""
    Some chocolates are dark.<br>
    Some are soft.<br>
    Some are crazy sweet.<br><br>
    But the best ones?<br>
    They leave you smiling<br>
    long after they melt ❤️
    """

    type_text(story)

    if st.button("🍫 Tell me more"):
        st.session_state.step = 3
        st.rerun()

# ---------------- STEP 3 ----------------
elif st.session_state.step == 3:
    reveal = f"""
    {GF_NAME},<br><br>
    You’re my favorite kind of sweetness.<br><br>
    Not too much.<br>
    Not too little.<br><br>
    Just… perfect 😌🍫
    """

    type_text(reveal)

    if st.button("🎁 One last thing"):
        st.session_state.step = 4
        st.rerun()

# ---------------- FINAL STEP ----------------
elif st.session_state.step == 4:
    st.balloons()

    final = f"""
    So today,<br>
    I’m sending you chocolates 🍫<br>
    mixed with a little love,<br>
    a lot of care,<br>
    and endless smiles 💕<br><br>
    Happy Chocolate Day,<br>
    {GF_NAME}.<br><br>
    — {YOUR_NAME}
    """

    type_text(final, speed=0.045)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🍫 I want chocolates"):
            st.success("Order placed in my heart 😄❤️")
            st.snow()

    with col2:
        if st.button("🤎 I want YOU"):
            st.success("Best choice ever 😌🍫")
            st.balloons()

# ---------------- DECOR ----------------
treats = " ".join(random.choice(["🍫", "🍪", "🍩", "🍬", "🤎"]) for _ in range(12))
st.markdown(f"<div style='text-align:center;font-size:26px'>{treats}</div>", unsafe_allow_html=True)

st.markdown(
    "<div class='footer'>Because life is sweeter with you 🍫❤️</div>",
    unsafe_allow_html=True
)
