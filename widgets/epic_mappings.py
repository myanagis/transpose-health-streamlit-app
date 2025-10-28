import streamlit as st
import pandas as pd
from pathlib import Path
import polars as pl

# Read Excel file


# Get current script directory
current_dir = Path(__file__).parent
file_path = current_dir.parent / "data" / "hl7_map_new_streamlit.xlsx"

# Read the table
map_df_raw = pl.read_excel(file_path)

#####################

# Display
st.title("Epic Mapping")
st.write("Below is the mapping of pharmacy data into Epic via the HL7 interface.")

# Selection
how_to_sort = st.segmented_control("Sort by...", ["Grouping", "Segment"], default="Grouping")

st.divider()

if how_to_sort == "Segment":
    sort_key = "segment"
    # We have an order that we want to display these in
    segment_order = ["MSH", "PID", "ORC", "RXE", "TQ1", "NTE", "RXR", "DG1", "ZWA"]

    for seg in segment_order:
        subdf = (map_df_raw.filter(pl.col("segment").eq(seg))
                           .sort(["segment_index", "repeat_number", "field_number"])
        )
        st.subheader(seg)
        st.dataframe(subdf)

# Sort by "Grouping"
else:
    for key, subdf in map_df_raw.group_by("grouping", maintain_order=True):
        display_key = key[0] # key is a tuple, and will display as:  ('key',)
        st.subheader(f"{display_key}")
        st.dataframe(subdf)
        


