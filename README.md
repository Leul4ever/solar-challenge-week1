Solar Challenge - W0 (🌞 Solar Site Data Analysis & Region Ranking)
This repository contains a complete data pipeline and EDA framework to clean, explore, and compare solar sensor datasets from multiple West African countries. The goal is to enable data-driven region ranking for solar farm expansion decisions.

🧭 Project Structuresolar-challenge-week1/

solar-challenge-week1/
├── .github/
├── app/                           # Streamlit Dashboard
│   ├── __init__.py
│   ├── main.py                    # Main analytics dashboard
│   └── utils.py                   # Utility functions
├── dashboard_screenshots/         # Dashboard visuals
├── notebooks/                     # Jupyter Notebooks for EDA
│   ├── benin_eda.ipynb
│   ├── togo_eda.ipynb
│   ├── sierra_leone_eda.ipynb
│   └── compare_countries.ipynb
├── data/                          # Cleaned datasets (gitignored)
│   ├── benin_clean.csv
│   ├── togo_clean.csv
│   └── sierra_leone_clean.csv
├── scripts/                       # Utility scripts
├── tests/
├── .gitignore
├── requirements.txt               # Python dependencies
└── README.md                      # This file


📌 Project Objectives
Main Goal: Profile, clean, and explore solar datasets from Benin, Togo, and Sierra Leone to support data-driven region ranking for solar development.

✅ Completed Tasks
Task 1: Project Setup & Environment
☑️ Set up GitHub repository with clear folder structure

☑️ Define modular code layout (app/, notebooks/, data/)

☑️ Add .gitignore to exclude local artifacts

☑️ Create comprehensive requirements.txt

☑️ Implement Git workflow with feature branches and PRs

Task 2: Data Profiling, Cleaning & EDA
☑️ Data Profiling: Summary statistics and null checks for each country

☑️ Data Cleaning: Outlier detection using z-score method, negative value handling

☑️ EDA Implementation: Comprehensive analysis for each country dataset

☑️ Output Generation: Cleaned datasets (*_clean.csv) for all countries

Task 3: Cross-Country Comparison
☑️ Boxplot Visualizations: GHI distribution across countries

☑️ Statistical Summary Tables: Mean, median, std for key metrics

☑️ ANOVA Testing: Statistical significance testing for GHI differences

☑️ Performance Ranking: Country comparison based on solar metrics

Bonus: Interactive Dashboard
☑️ Streamlit App: Multi-feature analytics dashboard

☑️ Interactive Widgets: Country selection, metric comparison

☑️ Statistical Tests: ANOVA and Kruskal-Wallis implementations

☑️ Professional UI: Clean layout with comprehensive analytics

🚀 Quick Start
# 1. Clone & setup
git clone https://github.com/Leul4ever/solar-challenge-week1.git
cd solar-challenge-week1

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run dashboard
streamlit run app/main.py

🤝 Development Workflow
Git Strategy
# Feature development
git checkout -b feature-branch
git add .
git commit -m "feat: descriptive message"
git push origin feature-branch

# Create PR and merge after review
🔬 Analytical Approach
Data Processing
Outlier detection using z-score (threshold: 3)

Negative value correction for night-time irradiance

Statistical validation across all metrics

Visualization & Testing
Boxplot comparisons of GHI across countries

ANOVA tests confirming significant differences

Performance rankings based on solar metrics

📊 Live Dashboard Features

✅ Multi-country selection (Benin, Togo, Sierra Leone)

✅ Metric comparison (GHI, DNI, DHI, Temperature, Wind Speed)

✅ Statistical testing with real-time results

✅ Performance rankings and summary tables


🎯 Business Impact
This analysis provides data-driven insights for:

Solar farm location selection

Investment prioritization across regions

Resource allocation based on solar potential
📞 Repository Info
GitHub: https://github.com/Leul4ever/solar-challenge-week1
Main Branch: Production-ready with all features
Status: ✅ Complete & Deployed