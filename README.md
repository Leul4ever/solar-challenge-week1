## 📊 Streamlit Dashboard

An interactive web dashboard for visualizing and comparing solar energy data across countries.

### Features
- **Country Selection**: Multi-select widget to choose countries for comparison
- **Irradiance Distribution**: Boxplots showing GHI/GHT distribution across selected countries
- **Top Regions Table**: Display of highest-performing regions
- **Country Metrics**: Key statistics for each selected country

### Local Development
```bash
# Install dependencies
pip install -r requirements.txt

# Run the dashboard
streamlit run app/main.py
solar-challenge-week1/
├── app/
│   ├── __init__.py
│   ├── main.py          # Main Streamlit application
│   └── utils.py         # Utility functions
├── data/                # Data files (git-ignored)
├── notebooks/           # Jupyter notebooks for EDA
└── requirements.txt     # Python dependencies