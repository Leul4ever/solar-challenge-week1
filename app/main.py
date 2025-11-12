import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats
from urllib.error import URLError

# Page configuration
st.set_page_config(
    page_title="Solar Energy Analytics Dashboard",
    page_icon="☀️",
    layout="wide"
)

# Title
st.title("☀️ Solar Energy Analytics Dashboard")
st.markdown("Advanced analysis and comparison of solar energy metrics across countries")

# Sidebar for controls
st.sidebar.header("🔧 Analytics Mode")

# Country selection
st.sidebar.subheader("Select Countries")
countries = ["Benin", "Togo", "Sierra Leone"]
selected_countries = st.sidebar.multiselect(
    "Choose countries to compare:",
    countries,
    default=countries
)

# Metric selection
st.sidebar.subheader("Select Metrics")
metrics = ["GHI", "DNI", "DHI", "Tamb", "WS"]
selected_metrics = st.sidebar.multiselect(
    "Choose metrics to analyze:",
    metrics,
    default=["GHI", "DNI"]
)

# Remote data configuration
DEFAULT_REMOTE_FILE_MAP = {
    "Benin": "https://drive.google.com/uc?export=download&id=11yvYlYcIDuCSBot7buK-Xn568eH4ZrkP",
    "Togo": "https://drive.google.com/uc?export=download&id=1RdQu-1O1Ar3D5_Ce02GSbfQ3LaaoI0iB",
    "Sierra Leone": "https://drive.google.com/uc?export=download&id=1mnsM0smG7mBZNuNOe_exxTtgIgYSdGHx",
}
try:
    secret_file_map = st.secrets["DATA_FILES"]  # type: ignore[index]
except Exception:
    secret_file_map = None

try:
    secret_base_url = st.secrets["DATA_BASE_URL"]  # type: ignore[index]
except Exception:
    secret_base_url = ""

REMOTE_FILE_MAP = secret_file_map or DEFAULT_REMOTE_FILE_MAP
REMOTE_BASE_URL = secret_base_url.rstrip("/") if secret_base_url else ""

# Data loading function (prefers uploaded data)
def load_data(country):
    """Load cleaned data for selected country"""
    file_name = f"{country.lower().replace(' ', '_')}_clean.csv"
    remote_url = REMOTE_FILE_MAP.get(country)
    if not remote_url and REMOTE_BASE_URL:
        remote_url = f"{REMOTE_BASE_URL}/{file_name}"

    if remote_url:
        try:
            df_remote = pd.read_csv(remote_url)
            return df_remote
        except URLError as e:
            st.warning(f"⚠️ Could not download `{remote_url}` for {country}: {e.reason}")
        except Exception as e:
            st.warning(f"⚠️ Unable to load remote data for {country}: {e}")

    file_path = f"data/{file_name}"
    
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        st.error(f"❌ Data file not found: {file_path}. Upload a CSV in the sidebar.")
        return None

# Main content
if selected_countries and selected_metrics:
    
    # Load data for all selected countries
    country_data = {}
    available_metrics = set()
    
    for country in selected_countries:
        df = load_data(country)
        if df is not None:
            country_data[country] = df
            # Find which of the selected metrics are available
            for metric in selected_metrics:
                if metric in df.columns:
                    available_metrics.add(metric)
    
    if not available_metrics:
        st.error("❌ None of the selected metrics are available in the data")
        st.stop()
    
    # Convert back to list for ordering
    available_metrics = [m for m in selected_metrics if m in available_metrics]
    
    # Two main columns
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.header("📊 Country Comparison")
        
        # Distribution plots for each selected metric
        for metric in available_metrics:
            st.subheader(f"{metric} Distribution")
            
            fig, ax = plt.subplots(figsize=(10, 6))
            plot_data = []
            labels = []
            
            for country in selected_countries:
                if country in country_data and metric in country_data[country].columns:
                    data = country_data[country][metric].dropna()
                    if len(data) > 0:
                        plot_data.append(data)
                        labels.append(country)
            
            if plot_data:
                # Create boxplot
                box_plot = ax.boxplot(plot_data, labels=labels, patch_artist=True)
                
                # Add colors to boxes
                colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7']
                for patch, color in zip(box_plot['boxes'], colors):
                    patch.set_facecolor(color)
                
                ax.set_ylabel(f'{metric} Value')
                ax.set_title(f'{metric} Distribution by Country')
                ax.grid(True, alpha=0.3)
                plt.xticks(rotation=45)
                
                st.pyplot(fig)
            else:
                st.warning(f"No {metric} data available for selected countries")
    
    with col2:
        st.header("🏆 Performance Rankings")
        
        # Create performance comparison table
        performance_data = []
        for country in selected_countries:
            if country in country_data:
                country_stats = {'Country': country}
                for metric in available_metrics:
                    if metric in country_data[country].columns:
                        data = country_data[country][metric].dropna()
                        if len(data) > 0:
                            country_stats[f'{metric} Mean'] = f"{data.mean():.2f}"
                            country_stats[f'{metric} Max'] = f"{data.max():.2f}"
                performance_data.append(country_stats)
        
        if performance_data:
            performance_df = pd.DataFrame(performance_data)
            st.dataframe(performance_df, use_container_width=True)
    
    # Summary Statistics Section
    st.header("📈 Summary Statistics")
    
    for metric in available_metrics:
        st.subheader(f"{metric} Statistical Summary")
        
        stats_data = []
        for country in selected_countries:
            if country in country_data and metric in country_data[country].columns:
                data = country_data[country][metric].dropna()
                if len(data) > 0:
                    stats_row = {
                        'Country': country,
                        'count': len(data),
                        'mean': f"{data.mean():.2f}",
                        'std': f"{data.std():.2f}",
                        'min': f"{data.min():.2f}",
                        '25%': f"{np.percentile(data, 25):.2f}",
                        '50%': f"{np.percentile(data, 50):.2f}",
                        '75%': f"{np.percentile(data, 75):.2f}",
                        'max': f"{data.max():.2f}"
                    }
                    stats_data.append(stats_row)
        
        if stats_data:
            stats_df = pd.DataFrame(stats_data)
            st.dataframe(stats_df, use_container_width=True)
        else:
            st.warning(f"No {metric} data available for statistical analysis")
    
    # Statistical Tests Section
    st.header("🔬 Statistical Tests")
    
    col_test1, col_test2 = st.columns(2)
    
    with col_test1:
        st.subheader("ANOVA Test")
        
        for metric in available_metrics:
            test_data = []
            for country in selected_countries:
                if country in country_data and metric in country_data[country].columns:
                    data = country_data[country][metric].dropna()
                    if len(data) > 0:
                        test_data.append(data)
            
            if len(test_data) >= 2:
                try:
                    # Perform ANOVA
                    f_stat, p_value = stats.f_oneway(*test_data)
                    
                    st.write(f"**{metric} ANOVA Results:**")
                    st.write(f"F-statistic: {f_stat:.4f}")
                    st.write(f"p-value: {p_value:.4f}")
                    
                    # Interpretation
                    if p_value < 0.05:
                        st.success("✅ Significant differences exist between countries (p < 0.05)")
                    else:
                        st.info("ℹ️ No significant differences between countries (p ≥ 0.05)")
                    
                    st.markdown("---")
                    
                except Exception as e:
                    st.error(f"Error performing ANOVA for {metric}: {str(e)}")
    
    with col_test2:
        st.subheader("Kruskal-Wallis Test")
        
        for metric in available_metrics:
            test_data = []
            for country in selected_countries:
                if country in country_data and metric in country_data[country].columns:
                    data = country_data[country][metric].dropna()
                    if len(data) > 0:
                        test_data.append(data)
            
            if len(test_data) >= 2:
                try:
                    # Perform Kruskal-Wallis test
                    h_stat, p_value = stats.kruskal(*test_data)
                    
                    st.write(f"**{metric} Kruskal-Wallis Results:**")
                    st.write(f"H-statistic: {h_stat:.4f}")
                    st.write(f"p-value: {p_value:.4f}")
                    
                    # Interpretation
                    if p_value < 0.05:
                        st.success("✅ Significant differences exist between countries (p < 0.05)")
                    else:
                        st.info("ℹ️ No significant differences between countries (p ≥ 0.05)")
                    
                    st.markdown("---")
                    
                except Exception as e:
                    st.error(f"Error performing Kruskal-Wallis test for {metric}: {str(e)}")
    
    # Interpretation Guide
    st.info("""
    **📋 Interpretation Guide:**
    - **p < 0.05**: Significant differences exist between countries
    - **p ≥ 0.05**: No significant differences between countries
    """)

else:
    st.info("👈 Please select at least one country and one metric from the sidebar to begin analysis")

# Data Quality Information
st.header("ℹ️ Data Quality & Information")

col_info1, col_info2 = st.columns(2)

with col_info1:
    st.subheader("Available Countries & Files")
    for country in countries:
        st.write(f"• **{country}**: `{country.lower().replace(' ', '_')}_clean.csv`")

with col_info2:
    st.subheader("Metric Definitions")
    metric_definitions = {
        "GHI": "Global Horizontal Irradiance - Total solar radiation received",
        "DNI": "Direct Normal Irradiance - Direct solar radiation",
        "DHI": "Diffuse Horizontal Irradiance - Scattered solar radiation",
        "Tamb": "Ambient Temperature",
        "WS": "Wind Speed"
    }
    
    for metric, definition in metric_definitions.items():
        if metric in metrics:
            st.write(f"• **{metric}**: {definition}")

# Footer
st.markdown("---")
st.markdown("""
**🔧 Features:**
- Multi-country comparison with statistical testing
- Interactive metric selection
- Comprehensive statistical summaries
- Data quality indicators
- Professional analytics interface
""")