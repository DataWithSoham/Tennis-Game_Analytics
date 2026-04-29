import streamlit as st
from components.navbar import render_navbar
from my_pages import home, competitors, country, leaderboard, simulation, predictor

st.set_page_config(
    page_title="Game Analytics: Tennis Data with SportRadar API",
    page_icon="🎾",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------- NAVBAR ----------------
page = render_navbar()

# ---------------- ROUTING ----------------
if page == "Home":
    home.show()

elif page == "Players":
    competitors.show()

elif page == "Country":
    country.show()

elif page == "Leaderboard":
    leaderboard.show()

elif page == "Simulation":
    simulation.show()

elif page == "Predictor":
    predictor.show()
