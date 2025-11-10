import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Page configuration
st.set_page_config(
    page_title="Solar Energy Dashboard",
    page_icon="☀️",
    layout="wide"
)

# Title
st.title("☀️ Solar Energy Dashboard")
st.markdown("Compare solar energy metrics across countries")

# Sidebar for country selection
st.sidebar.header("Country Selection")
countries = ["Benin", "Togo", "Sierra Leone"]
selected_countries = st.sidebar.multiselect(
    "Select Countries to Compare",
    countries,
    default=["Benin"]
)

# Data loading function
@st.cache_data
def load_data(country):
    """Load cleaned data for selected country"""
    file_name = f"{country.lower().replace(' ', '_')}_clean.csv"
    file_path = f"data/{file_name}"
    
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        st.error(f"❌ Data file not found: {file_path}")
        st.info(f"💡 Make sure '{file_name}' exists in the 'data' folder")
        return None

# Main content area
if selected_countries:
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.header("📊 Solar Irradiance Distribution")
        
        # Check for different possible column names
        irradiance_data = []
        labels = []
        irradiance_col = None
        
        for country in selected_countries:
            df = load_data(country)
            if df is not None:
                # Look for irradiance columns (GHI or GHT)
                if 'GHI' in df.columns:
                    irradiance_col = 'GHI'
                elif 'GHT' in df.columns:
                    irradiance_col = 'GHT'
                
                if irradiance_col and irradiance_col in df.columns:
                    irradiance_data.append(df[irradiance_col].dropna())
                    labels.append(country)
        
        if irradiance_data and irradiance_col:
            # Create boxplot
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.boxplot(irradiance_data, labels=labels)
            ax.set_ylabel(f'{irradiance_col} (W/m²)')
            ax.set_title(f'{irradiance_col} Distribution by Country')
            ax.grid(True, alpha=0.3)
            st.pyplot(fig)
            
            # Show which column is being used
            st.info(f"📊 Displaying {irradiance_col} data")
        else:
            st.warning("No irradiance data columns found (looking for GHI or GHT)")
    
    with col2:
        st.header("🏆 Top Regions")
        
        # Display top regions table for first selected country
        if selected_countries:
            df = load_data(selected_countries[0])
            if df is not None:
                # Look for region/location columns
                region_cols = [col for col in df.columns 
                              if any(keyword in col.lower() 
                                    for keyword in ['region', 'location', 'site', 'station'])]
                
                # Determine which irradiance column to use
                irradiance_col = None
                if 'GHI' in df.columns:
                    irradiance_col = 'GHI'
                elif 'GHT' in df.columns:
                    irradiance_col = 'GHT'
                
                if region_cols and irradiance_col:
                    region_col = region_cols[0]
                    top_regions = (df.groupby(region_col)[irradiance_col]
                                  .mean()
                                  .sort_values(ascending=False)
                                  .head(10)
                                  .reset_index())
                    top_regions.columns = ['Region', f'Average {irradiance_col} (W/m²)']
                    st.dataframe(top_regions, use_container_width=True)
                else:
                    # Sample data if no region column found
                    sample_data = {
                        'Region': [f'Region {chr(65+i)}' for i in range(5)],
                        'Average GHI (W/m²)': [485.2, 467.8, 452.3, 438.9, 425.1]
                    }
                    st.dataframe(pd.DataFrame(sample_data), use_container_width=True)
                    st.info("💡 Sample data shown - add region columns to your CSV for actual regional analysis")
    
    # Additional metrics section
    st.header("📈 Country Metrics")
    
    metrics_cols = st.columns(len(selected_countries))
    
    for idx, country in enumerate(selected_countries):
        df = load_data(country)
        if df is not None:
            with metrics_cols[idx]:
                st.subheader(country)
                
                # Determine which irradiance column to use
                irradiance_col = None
                if 'GHI' in df.columns:
                    irradiance_col = 'GHI'
                elif 'GHT' in df.columns:
                    irradiance_col = 'GHT'
                
                if irradiance_col and irradiance_col in df.columns:
                    irradiance = df[irradiance_col]
                    st.metric(f"Average {irradiance_col}", f"{irradiance.mean():.1f} W/m²")
                    st.metric(f"Max {irradiance_col}", f"{irradiance.max():.1f} W/m²")
                    st.metric("Data Points", len(irradiance))
                else:
                    st.metric("Data Points", len(df))
                    st.warning(f"No {irradiance_col} data found")

else:
    st.info("👈 Please select at least one country from the sidebar to begin")

# Data information section
st.header("ℹ️ Data Information")
st.markdown("""
**Available Countries:**
- **Benin**: benin_clean.csv
- **Togo**: togo_clean.csv  
- **Sierra Leone**: sierra_leone_clean.csv

**Note:** The app automatically detects whether your data uses 'GHI' or 'GHT' column names for irradiance data.
""")

# Footer with instructions
st.markdown("---")
st.markdown("**Usage Instructions:**")
st.markdown("""
1. **Select countries** from the sidebar to compare
2. **View irradiance distributions** in the boxplot
3. **Explore top regions** performance
4. **Compare metrics** across selected countries
""")

st.markdown("**Development Info:**")
st.markdown("""
- Built with Streamlit
- Uses matplotlib and seaborn for visualizations
- Reads data from CSV files in the `data/` folder
- Supports both GHI and GHT column names
""")