# Import python packages
import streamlit as st


# Define the pages
scriptpro_tables = st.Page("widgets/scriptpro_tables.py", title="ScriptPro Tables")

# Set up navigation
pg = st.navigation(
    {       "Tools": [scriptpro_tables]
    }
)
pg.run()
