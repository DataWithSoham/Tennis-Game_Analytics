import streamlit as st
import pandas as pd

@st.cache_data
def load_full_data():
    """
    Loads and merges rankings and competitors data.
    """
    try:
        competitors = pd.read_csv("data/processed_data/competitors.csv")
        rankings = pd.read_csv("data/processed_data/rankings.csv")

        df = pd.merge(rankings, competitors, on="competitor_id")

        # Standard Cleaning
        df["rank_position"] = pd.to_numeric(df["rank_position"], errors="coerce")
        df["points"] = pd.to_numeric(df["points"], errors="coerce")
        df["movement"] = pd.to_numeric(df["movement"], errors="coerce").fillna(0)
        df["competitions_played"] = pd.to_numeric(df["competitions_played"], errors="coerce").fillna(0)

        df = df.dropna(subset=["rank_position", "points"])

        # Deduplicate to keep the best rank for each player
        df = df.sort_values("rank_position").drop_duplicates(
            subset=["competitor_id"], keep="first"
        )
        
        return df
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame()

@st.cache_data
def load_competition_data():
    """
    Loads competition and category data.
    """
    try:
        competitions = pd.read_csv("data/processed_data/competitions.csv")
        categories = pd.read_csv("data/processed_data/categories.csv")

        competitions["parent_id"] = competitions["parent_id"].fillna("ROOT")
        competitions["type"] = competitions["type"].fillna("unknown")
        competitions["gender"] = competitions["gender"].fillna("unknown")

        competitions = competitions.merge(
            categories[["category_id", "category_name"]],
            on="category_id",
            how="left"
        )

        return categories, competitions
    except Exception as e:
        st.error(f"Error loading competition data: {e}")
        return pd.DataFrame(), pd.DataFrame()
