import pandas as pd
import streamlit as st

def load_country_data(country_name):
    """
    Load cleaned data for a specific country
    """
    file_name = f"{country_name.lower().replace(' ', '_')}_clean.csv"
    file_path = f"data/{file_name}"
    
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        st.error(f"Data file not found: {file_path}")
        return None

def calculate_ghi_stats(df):
    """
    Calculate basic statistics for GHI data
    """
    if 'GHI' not in df.columns:
        return None
    
    stats = {
        'mean': df['GHI'].mean(),
        'max': df['GHI'].max(),
        'min': df['GHI'].min(),
        'std': df['GHI'].std()
    }
    return stats