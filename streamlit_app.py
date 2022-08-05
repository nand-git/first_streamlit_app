import streamlit as sl
import requests as req
import pandas as pd
import snowflake.connector
from urllib.error import URLError

sl.title("Breakfast Menu")
sl.header("Fruit bowl")

fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
fruit_list = fruit_list.set_index('Fruit')
fruit_selected = sl.multiselect("Pick some fruits: ", list(fruit_list.index),['Banana','Apple'])
fruit_to_show = fruit_list.loc[fruit_selected]
sl.dataframe(fruit_to_show)

sl.header("Fruit Advice")
def get_fuit_data(fruit_name):
  fruit_res=req.get("https://fruityvice.com/api/fruit/" + fruit_name)
  #sl.text(fruit_res.json())
  fruit_norm = pd.json_normalize(fruit_res.json())
  return fruit_norm

try:
  fruit_choice=sl.text_input("Choose fruit: ")
  if not fruit_choice:
    sl.error("Please choose a fruit!")
  else:
    fun_res=get_fuit_data(fruit_choice)
    sl.dataframe(fun_res)
except URLError as e:
  sl.error()

#sl.stop()

my_cnx = snowflake.connector.connect(**sl.secrets["snowflake"])
my_cur = my_cnx.cursor()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("select * from PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST")
my_data_row = my_cur.fetchall()
#sl.text("Hello from Snowflake:")
sl.header("Fruit list: ")
sl.dataframe(my_data_row)
