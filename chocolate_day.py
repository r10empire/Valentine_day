import streamlit as st
import time
import random

def chocolate_rain(choco="🍫", count=18, key="rain"):
    rain_html = ""
    for i in range(count):
        left = random.randint(0, 95)
        delay = round(random.uniform(0, 1.5), 2)
        duration = round(random.uniform(2.5, 4), 2)

        rain_html += f"""
        <span style="
            position: fixed;
            top: -10%;
            left: {left}%;
            font-size: 28px;
            animation: fall_{key} {duration}s linear {delay}s infinite;
        ">
            {choco}
        </span>
        """

    st.markdown(
        f"""
        <div class="choco-rain-container">
            {rain_html}
        </div>

        <style>
        @keyframes fall_{key} {{
            0% {{ transform: translateY(-10vh); opacity: 0; }}
            10% {{ opacity: 1; }}
            100% {{ transform: translateY(110vh); opacity: 1; }}
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


def chocolate_pop(choco="🍫", key="pop"):
    burst = " ".join([choco for _ in range(7)])
    st.markdown(
        f"""
        <div style="
            text-align:center;
            font-size:42px;
            animation: pop_{key} 0.9s ease-out;
        ">
            {burst}
        </div>

        <style>
        @keyframes pop_{key} {{
            0% {{ transform: scale(0.4); opacity: 0; }}
            60% {{ transform: scale(1.3); opacity: 1; }}
            100% {{ transform: scale(1); opacity: 1; }}
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

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
.choco-rain {
    text-align: center;
    font-size: 28px;
    opacity: 0.85;
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
    chocolate_rain("🍫", key="step1")
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
    chocolate_pop("🍫", key="step1")
    type_text(intro)


    if st.button("🍬 Continue"):
        st.session_state.step = 2
        st.rerun()

# ---------------- STEP 2 ----------------
elif st.session_state.step == 2:
    chocolate_rain("🍩", key="step2")
    story = f"""
    Some chocolates are dark.<br>
    Some are soft.<br>
    Some are crazy sweet.<br><br>
    But the best ones?<br>
    They leave you smiling<br>
    long after they melt ❤️
    """

    chocolate_pop("🍩", key="step2")
    type_text(story)


    if st.button("🍫 Tell me more"):
        st.session_state.step = 3
        st.rerun()

# ---------------- STEP 3 ----------------
elif st.session_state.step == 3:
    chocolate_rain("🍪", key="step3")
    reveal = f"""
    {GF_NAME},<br><br>
    You’re my favorite kind of sweetness.<br><br>
    Not too much.<br>
    Not too little.<br><br>
    Just… perfect 😌🍫
    """
    chocolate_pop("🍪", key="step3")
    type_text(reveal)


    if st.button("🎁 One last thing"):
        st.session_state.step = 4
        st.rerun()

# ---------------- FINAL STEP ----------------
elif st.session_state.step == 4:
    mix = random.choice(["🍫", "🍩", "🍪", "🍬", "🤎"])
    chocolate_rain(mix, key="final")
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
    
    chocolate_pop(mix, key="final")
    type_text(final, speed=0.045)


    col1, col2 = st.columns(2)
    with col1:
        if st.button("🍫 I want chocolates"):
            st.success("Order placed in my heart 😄❤️")
            st.snow()

    with col2:
        if st.button("🤎 I want YOU"):
            st.success("Best choice ever 😌🍫")

# ---------------- DECOR ----------------
treats = " ".join(random.choice(["🍫", "🍪", "🍩", "🍬", "🤎"]) for _ in range(12))
st.markdown(f"<div style='text-align:center;font-size:26px'>{treats}</div>", unsafe_allow_html=True)

st.markdown(
    "<div class='footer'>Because life is sweeter with you 🍫❤️</div>",
    unsafe_allow_html=True
)
