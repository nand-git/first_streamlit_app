import streamlit as sl
import requests as req
import pandas as pd
import snowflake.connector as conn

sl.title("Breakfast Menu")
sl.header("Fruit bowl")

fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
fruit_list = fruit_list.set_index('Fruit')
fruit_selected = sl.multiselect("Pick some fruits: ", list(fruit_list.index),['Banana','Apple'])
fruit_to_show = fruit_list.loc[fruit_selected]
sl.dataframe(fruit_to_show)

sl.header("Fruit Advice")
fruit_choice=sl.text_input("Choose fruit: ","kiwi")
fruit_res=req.get("https://fruityvice.com/api/fruit/" + fruit_choice)
#sl.text(fruit_res.json())
fruit_norm = pd.json_normalize(fruit_res.json())
sl.dataframe(fruit_norm)
