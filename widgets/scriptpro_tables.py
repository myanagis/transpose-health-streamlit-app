import streamlit as st
import pandas as pd
from pathlib import Path

# Read Excel file


# Get current script directory
current_dir = Path(__file__).parent
file_path = current_dir.parent / "data" / "scriptpro_tables_and_columns_uk.xlsx"

# Read the table
sp_tables_df = pd.read_excel(file_path)

#####################

# Display
st.title("ScriptPro Tables")

# Filters
col1, col2 = st.columns(2)
with col1:
    table_filter = st.text_input("Filter by table name:")

with col2:
    column_filter = st.text_input("Filter by column name:")

# Filtering logic
filtered_df = sp_tables_df
if table_filter:
    filtered_df = filtered_df[filtered_df['table_name'].str.contains(table_filter, case=False, na=False)]
if column_filter:
    filtered_df = filtered_df[filtered_df['column_name'].str.contains(column_filter, case=False, na=False)]

# Display
st.dataframe(filtered_df)
