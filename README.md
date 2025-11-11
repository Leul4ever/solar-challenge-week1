Solar Challenge — Week 1
Solar Resource Analytics, Validation, and Interactive Reporting

Overview
This repository provides a complete, reproducible workflow to evaluate solar resource potential across West African regions (Benin, Togo, Sierra Leone). It includes data quality checks, cleaning, exploratory data analysis (EDA), statistical validation, and an interactive Streamlit dashboard for rapid comparison and insight generation.

Key capabilities
- Data ingestion, validation, and cleaning for sensor datasets (GHI, DNI, DHI, temperature, wind speed).
- Exploratory analytics and visualization for each country.
- Cross-country comparison with statistical testing (ANOVA, Kruskal–Wallis).
- Interactive dashboard for stakeholders to explore findings and rankings.

Project structure

```
solar-challenge-week1/
├── app/                     # Streamlit dashboard
│   ├── main.py              # UI/controls and high-level orchestration
│   └── utils.py             # Data loading, preprocessing, shared utilities
├── data/                    # Input and cleaned CSV datasets
├── dashboard_screenshots/   # Dashboard images for README/docs
├── notebooks/               # Country EDA and comparison notebooks
│   ├── benin_eda.ipynb
│   ├── togo_eda.ipynb
│   ├── sierra_leone_eda.ipynb
│   └── compare_countries.ipynb
├── scripts/                 # Optional CLI/utilities (future automation)
├── src/                     # Reserved for library-style modules (future growth)
├── tests/                   # Test suite scaffolding
├── requirements.txt         # Python dependencies
└── README.md
```

Data
- Primary inputs: Cleaned or raw site-level CSVs in `data/` (e.g., `benin_clean.csv`, `togo_clean.csv`, `sierra_leone_clean.csv`).
- Expected core columns: irradiance metrics (GHI, DNI, DHI), temperature, wind speed, timestamp.
- Data quality steps include null audits, negative-value handling, outlier screening (z-score), and nighttime irradiance normalization.

Environment setup (Windows/PowerShell)

```bash
# 1) Clone
git clone https://github.com/Leul4ever/solar-challenge-week1.git
cd solar-challenge-week1

# 2) Create and activate virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1

# 3) Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
```

Running the dashboard

```bash
streamlit run app/main.py
```

Open your browser to `http://localhost:8501`.

Working with notebooks
- Notebooks in `notebooks/` document EDA per country and cross-country comparison.
- Ensure the virtual environment kernel is selected in your Jupyter environment for consistent dependencies.

Analytical methodology (summary)
- Profiling and cleaning: null checks, negative/physically invalid values, outlier detection (z-score, default threshold 3σ).
- Visualization: distributions, time series, correlations, boxplots, country comparisons.
- Statistical validation: ANOVA and non-parametric Kruskal–Wallis tests to confirm differences in solar resource distributions.

Dashboard features (high level)
- Country selection and multi-metric analysis (GHI, DNI, DHI, temperature, wind speed).
- Real-time statistical summaries and comparison views.
- Figures and summary tables for quick decision support.

Coding standards and linting
To ensure consistency and readability across the codebase, adopt the following tooling and conventions.

- Formatter: Black
- Import sorter: isort
- Linting: Flake8 (or Ruff as a drop-in faster alternative, if preferred)
- Docstrings: NumPy-style docstrings for functions, classes, and modules

Install optional dev tools:

```bash
pip install black isort flake8
# or
pip install ruff
```

Recommended commands (run at repo root):

```bash
# Format code
black app scripts tests
isort app scripts tests

# Lint code
flake8 app scripts tests
# or, with Ruff
ruff check app scripts tests
```

Docstring and module-level documentation
- Each public function/class should include a NumPy-style docstring describing purpose, parameters, returns, and raises.
- Each module (e.g., `app/utils.py`) should begin with a brief module-level overview (what the module provides, key assumptions, and any invariants).

Example (NumPy-style):

```python
def compute_daily_ghi_stats(df: pd.DataFrame) -> pd.DataFrame:
    \"\"\"Compute daily summary statistics for GHI.

    Parameters
    ----------
    df : pd.DataFrame
        Input data containing at least a 'timestamp' column and 'GHI' in W/m^2.

    Returns
    -------
    pd.DataFrame
        DataFrame indexed by date with columns for mean, median, std.
    \"\"\"
    # implementation
```

Testing
- Add unit tests under `tests/` for reusable utilities in `app/utils.py` and any new modules under `src/`.
- Suggested stack: `pytest` with simple fixtures for small tabular test data.

```bash
pip install pytest
pytest -q
```

Deployment
- The app is Streamlit-ready and can be deployed to Streamlit Community Cloud.
- Ensure `requirements.txt` is up to date; set the app entry point to `app/main.py`.

Screenshots
Representative screenshots are stored under `dashboard_screenshots/` (e.g., `GHI.png`, `DNI.png`, `Tamb.png`). These illustrate core views of the dashboard and analytical outputs.

Contributing
- Use feature branches and conventional commits (e.g., `feat:`, `fix:`, `docs:`).
- Open a pull request with a concise summary and screenshots where applicable.
- Keep PRs focused and small for easier review.

Troubleshooting
- Streamlit fails to start: verify the virtual environment is activated and dependencies installed.
- Encoding or path issues on Windows: prefer raw strings or `pathlib.Path`, and avoid non-ASCII filenames.
- Data not loading: confirm expected columns exist and that CSVs are placed under `data/`.

License
If this work is public, specify your license (e.g., MIT). If internal, omit or state “All rights reserved.”

Acknowledgements
This work evaluates open solar resource datasets across West African regions and is intended to support data-driven siting and planning decisions.