import streamlit as sl
import pandas as pd

sl.title("Breakfast Menu")

fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
sl.dataframe(fruit_list)
