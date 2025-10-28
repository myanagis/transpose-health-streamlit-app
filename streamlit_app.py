# Import python packages
import streamlit as st


# Define the pages
scriptpro_tables = st.Page("widgets/scriptpro_tables.py", title="ScriptPro Tables")
epic_mappings = st.Page("widgets/epic_mappings.py", title="Epic Mappings")

# Set up navigation
pg = st.navigation(
    {       "Tools": [scriptpro_tables, epic_mappings]
    }
)
pg.run()
