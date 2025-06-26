import streamlit as st
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "product_moderation"))
sys.path.append(os.path.join(os.path.dirname(__file__), "content_moderation"))

from product_moderation.product_description_app import product_description
from content_moderation.content_moderation_app import content_moderation
from Main import main


st.set_page_config(layout="wide", page_title="Image Background")

st.sidebar.success("Select a a tool below.")

page_names_to_funcs = {
    "Home": main,
    "Product Description": product_description,
    "Content Moderation": content_moderation,
}

demo_name = st.sidebar.selectbox("Choose a demo", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()