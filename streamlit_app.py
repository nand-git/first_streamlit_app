import streamlit as sl
import pandas as pd

sl.title("Breakfast Menu")
sl.header("Fruit bowl")

fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
fruit_list = fruit_list.set_index('Fruit')
fruit_selected = sl.multiselect("Pick some fruits: ", list(fruit_list.index),['Banana','Apple'])
fruit_to_show = fruit_list.loc[fruit_selected]
sl.dataframe(fruit_to_show)
