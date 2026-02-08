import streamlit as st

# --------------------------------------------------
# Page config
# --------------------------------------------------
st.set_page_config(
    page_title="Happy Rose Day 🌹",
    page_icon="🌹",
    layout="centered"
)

name = st.query_params.get("name")


# --------------------------------------------------
# Global Styles & Animations
# --------------------------------------------------
def load_styles():
    st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #ffdde1, #ee9ca7);
    }

    /* Card */
    .card {
        background: white;
        padding: 32px;
        border-radius: 20px;
        text-align: center;
        box-shadow: 0 10px 25px rgba(0,0,0,0.15);
        animation: fadeIn 1.5s ease-in-out;
    }

    /* Text */
    .title {
        font-size: 36px;
        color: #e91e63;
        font-weight: 700;
        margin-bottom: 10px;
    }
    .text {
        font-size: 20px;
        color: #444;
        line-height: 1.6;
    }
    .footer {
        margin-top: 20px;
        font-size: 15px;
        color: #888;
    }

    /* Photo */
    .photo-container {
        display: flex;
        justify-content: center;
        margin-bottom: 20px;
    }
    .photo {
        width: 220px;
        height: 220px;
        border-radius: 50%;
        object-fit: cover;
        border: 6px solid #e91e63;
        animation: pulse 3s infinite;
    }

    /* Floating elements */
    .floating {
        position: fixed;
        bottom: -50px;
        font-size: 28px;
        opacity: 0.8;
        animation: floatUp linear infinite;
        pointer-events: none;
    }
    img {
        border-radius: 50%;
        border: 6px solid #e91e63;
        animation: pulse 3s infinite;
    }


    /* Animations */
    @keyframes floatUp {
        0% { transform: translateY(0); opacity: 1; }
        100% { transform: translateY(-110vh); opacity: 0; }
    }

    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    </style>

    <!-- Floating roses & hearts -->
    <div class="floating" style="left:10%; animation-duration:9s;">🌹</div>
    <div class="floating" style="left:30%; animation-duration:11s;">❤️</div>
    <div class="floating" style="left:50%; animation-duration:10s;">🌹</div>
    <div class="floating" style="left:70%; animation-duration:12s;">❤️</div>
    <div class="floating" style="left:90%; animation-duration:13s;">🌹</div>
    """, unsafe_allow_html=True)


# --------------------------------------------------
# UI Sections
# --------------------------------------------------
def show_wish(name):
    st.markdown('<div class="card">', unsafe_allow_html=True)

    # IMAGE (correct way)
    st.image(
        "assets/faguniya1.jpeg",
        width=220,
        caption=None
    )

    st.markdown(f"""
        <div class="title">Happy Rose Day 🌹</div>

        <div class="text">
            Dear <b>{name}</b>,<br><br>
            Like a rose, you add beauty,  
            love and happiness to my life.<br><br>
            I’m grateful for you — today and always ❤️
        </div>

        <div class="footer">
            — Made with love 💖
        </div>
    </div>
    """, unsafe_allow_html=True)



def show_creator():
    st.markdown("## 🌹 Create Your Rose Day Wish")
    gf_name = st.text_input("Enter her name 💖")

    if gf_name:
        base_url = "https://your-streamlit-app-url"
        link = f"{base_url}?name={gf_name.replace(' ', '%20')}"
        st.success("✨ Your link is ready")
        st.code(link)


# --------------------------------------------------
# App Execution
# --------------------------------------------------
load_styles()

if name:
    show_wish(name)
else:
    show_creator()
