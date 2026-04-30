# 🎾 Game Analytics — Unlocking Tennis Data with SportRadar API

> An end-to-end data engineering and analytics project that extracts live tennis data from the SportRadar API, processes it through a centralized pipeline, and surfaces insights through an interactive multi-page Streamlit dashboard.

---
## 📌 Live Demo: [Tennis_Data_Analysis_Dashboard](https://tennisdataanalytics.streamlit.app/)

## 📌 Project Overview

This project implements a complete data analytics stack for tennis performance data:

| Phase | Title | Status |
|-------|-------|--------|
| 1 | **Data Engineering** — API Extraction & CSV Export | ✅ Complete |
| 2 | **Core Logic** — Centralized Data Cleaning & ML Prediction | ✅ Complete |
| 3 | **Interactive Dashboard** — 7-Page Analytics Suite | ✅ Complete |

**Data Source:** [SportRadar Tennis API v3](https://developer.sportradar.com/tennis/reference/tennis-v3)  
**Tech Stack:** Python · Pandas · Scikit-Learn · Plotly · Streamlit

---

## 📂 Project Structure

```
Game_Analytics/
│
├── api/
│   └── Tennis_Data_Pipeline.ipynb   # API extraction & initial cleaning
│
├── app/
│   ├── app.py                       # Main router for the Streamlit app
│   ├── components/                  # UI components (Navbar, Filters)
│   ├── my_pages/                    # Individual dashboard pages
│   │   ├── home.py                  # Executive Dashboard
│   │   ├── competitors.py           # Player Deep Dive
│   │   ├── country.py               # Global Analytics
│   │   ├── leaderboard.py           # Rankings Table
│   │   ├── simulation.py            # Tournament Analytics
│   │   ├── predictor.py             # ML Match Predictor
│   │   └── insights.py              # Business Insights & Recommendations
│   └── utils/
│       ├── data_loader.py           # Centralized caching & preprocessing
│       └── prediction.py            # ML Model training & logic
│
├── data/
│   ├── raw_data/                    # Raw JSON API responses
│   └── processed_data/              # Cleaned CSV files used by the app
│
├── database/                        # SQL Schema & Analysis Scripts
│   ├── schema.sql
│   ├── data_import.sql
│   └── analysis_queries.sql
│
├── requirements.txt                 # Project dependencies
└── README.md
```

---

## ⚙️ Workflow Explanation

### 1. Data Pipeline (`api/`)
The `Tennis_Data_Pipeline.ipynb` notebook handles the extraction of live data from SportRadar. It flattens nested JSON responses into relational formats and exports them as CSVs to `data/processed_data/`.

### 2. Centralized Data Loading (`app/utils/data_loader.py`)
To ensure consistency across the dashboard, a centralized data loader handles:
- **Type Casting:** Ensuring ranks and points are numeric.
- **Deduplication:** Keeping only the most recent/best rank for each competitor.
- **Caching:** Using `@st.cache_data` to ensure fast page loads without redundant disk I/O.

### 3. ML Prediction Engine (`app/utils/prediction.py`)
The app features a Logistic Regression model that predicts match outcomes based on:
- Point differentials
- Rank positions
- Recent movement/trends
- Experience (competitions played)

---

## 📊 Dashboard Features

The dashboard is organized into six specialized views:

1. **🏠 Home**: Executive overview with high-level KPIs (Total Players, Avg Points) and top 10 rankings.
2. **👤 Players**: Individual player search with point capacity gauges and movement indicators.
3. **🌍 Country**: Geographic analysis of tennis strength and player distribution.
4. **🏆 Leaderboard**: A fully sortable and filterable table of all ranked players.
5. **📉 Simulation**: Breakdown of tournament hierarchies (Categories -> Tournaments -> Events).
6. **🤖 Predictor**: A "What-If" tool using ML and Monte Carlo simulations (500+ iterations) to predict winners between any two players.
7. **📈 Insights**: Strategic business analysis providing stakeholders with recommendations on market growth, sponsorship, and tournament strategy.

---

## 🔧 Fixes & Optimizations

- **Deterministic Simulations**: Fixed an issue where visualizations showed different measurements on every refresh by implementing fixed random seeds (`np.random.seed(42)`) in the ML model and simulation logic.
- **Improved Performance**: Consolidated data processing into a single utility, reducing memory footprint and ensuring data integrity across pages.
- **UI Consistency**: Removed redundant page configurations to prevent Streamlit rendering errors.

---

## 🚀 Getting Started

### Installation
```bash
pip install -r requirements.txt
```

### Running the App
```bash
streamlit run app/app.py
```

---

## 🏗️ Architecture

```
SportRadar API ──► JSON ──► Pandas (Pipeline) ──► CSV
                                             │
                                             ▼
                                     Data Loader (Utils)
                                             │
                                     ┌───────┴───────┐
                                     ▼               ▼
                               ML Predictor    Plotly Charts
                                     └───────┬───────┘
                                             ▼
                                     Streamlit Dashboard
```
