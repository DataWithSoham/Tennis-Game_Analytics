import streamlit as st
import pandas as pd
import plotly.express as px
from utils.data_loader import load_full_data, load_competition_data

def show():
    st.title("📈 Strategic Business Insights")
    st.caption("Data-Driven Recommendations for Stakeholders")

    df = load_full_data()
    categories, competitions = load_competition_data()

    if df.empty:
        st.error("Data not available for analysis.")
        return

    # ---------------------------------------------------------
    # TOP SECTION: EXECUTIVE SUMMARY
    # ---------------------------------------------------------
    st.markdown("""
    <div style="background-color:#1e2130; padding:20px; border-radius:10px; border-left:5px solid #00d4ff; margin-bottom:20px;">
        <h3 style="margin-top:0;">Executive Summary</h3>
        <p>This report synthesizes current tennis performance data to identify growth opportunities, market dominance, and strategic pathways for sponsorship and talent development.</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        # Insight 1: Market Concentration
        st.subheader("🌍 Market Concentration")
        country_share = df['country'].value_counts(normalize=True).head(5) * 100
        fig_share = px.pie(
            values=country_share.values,
            names=country_share.index,
            title="Top 5 Countries Player Share (%)",
            hole=0.4,
            template="plotly_dark",
            color_discrete_sequence=px.colors.sequential.Teal
        )
        st.plotly_chart(fig_share, use_container_width=True)
        
        st.info(f"**Dominance:** {country_share.index[0]} leads with {country_share.iloc[0]:.1f}% of the professional player base.")

    with col2:
        # Insight 2: Performance Efficiency
        st.subheader("⚡ Performance Efficiency")
        # Avg points per player by country
        efficiency = df.groupby('country').agg({
            'points': 'mean',
            'competitor_id': 'count'
        }).rename(columns={'competitor_id': 'player_count'})
        
        # Filter for countries with at least 5 players to avoid outliers
        efficiency = efficiency[efficiency['player_count'] >= 5].sort_values('points', ascending=False).head(10)
        
        fig_eff = px.bar(
            efficiency,
            x=efficiency.index,
            y='points',
            title="Avg Points per Player (Min. 5 Players)",
            template="plotly_dark",
            color='points',
            color_continuous_scale="Viridis"
        )
        st.plotly_chart(fig_eff, use_container_width=True)
        
        st.success(f"**High Yield:** {efficiency.index[0]} shows the highest average performance per athlete.")

    st.divider()

    # ---------------------------------------------------------
    # MIDDLE SECTION: GROWTH OPPORTUNITIES
    # ---------------------------------------------------------
    st.header("🚀 Growth Opportunities")
    
    c1, c2, c3 = st.columns(3)
    
    # 1. Underserved Markets
    with c1:
        st.markdown("### 🏺 Emerging Markets")
        st.write("Countries with high performance growth but low current player volume.")
        # Logic: Low player count but high average movement
        growth = df.groupby('country').agg({
            'movement': 'mean',
            'competitor_id': 'count'
        })
        emerging = growth[(growth['competitor_id'] < 10) & (growth['movement'] > 0)].sort_values('movement', ascending=False).head(3)
        for country in emerging.index:
            st.write(f"- **{country}**: +{emerging.loc[country, 'movement']:.1f} avg rank jump")

    # 2. Tournament Saturation
    with c2:
        st.markdown("### 🎾 Event Portfolio")
        type_dist = competitions['type'].value_counts()
        st.write(f"The circuit is currently **{ (type_dist.get('singles', 0)/len(competitions)*100):.1f}% Singles** dominated.")
        st.write("Recommendation: Increase investment in Doubles and Mixed formats to diversify audience engagement.")

    # 3. Sponsorship Targets
    with c3:
        st.markdown("### 💰 Sponsorship Targets")
        top_risers = df.sort_values('movement', ascending=False).head(3)
        st.write("Top 'Fastest Risers' this week:")
        for _, row in top_risers.iterrows():
            st.write(f"- **{row['name']}** ({row['country']})")

    st.divider()

    # ---------------------------------------------------------
    # BOTTOM SECTION: STRATEGIC RECOMMENDATIONS
    # ---------------------------------------------------------
    st.header("🎯 Strategic Recommendations")
    
    st.markdown("""
    1. **Regional Diversification**: While Europe remains the stronghold, data shows high 'movement' trends in emerging regions. Allocating scouting resources to these areas could yield high ROI.
    2. **Performance-Based Tiering**: Implement tiered sponsorship models based on the 'Points Capacity' metric visualized in the Player Deep Dive.
    3. **Tournament Scheduling**: Align event promotion with the geographic distribution of 'Top 100' players to maximize local viewership and ticket sales.
    4. **Digital Engagement**: Leverage the 'Match Predictor' logic for fan engagement platforms, as predictive analytics are a key driver for younger demographics.
    """)

    st.caption("Generated by Game Analytics Insight Engine")
