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

def get_fruit_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("select * from PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST")
    return my_cur.fetchall()

if sl.button('Get Fruit load list'):
  my_cnx = snowflake.connector.connect(**sl.secrets["snowflake"])
  my_data_rows=get_fruit_list()
  sl.header("Fruit list: ")
  sl.dataframe(my_data_rows)
  
add_my_fruit=sl.text_input("What fruit to add?")

def insert_fruit(new_fruit):
  with my_cnx.cursor() as my_cur:
    my_cur.execute("insert into PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST values('" + new_fruit + "')")
    return new_fruit+" added!"
  
if sl.button("Add a fruit to list"):
  my_cnx = snowflake.connector.connect(**sl.secrets["snowflake"])
  fruit_sf_res=insert_fruit(add_my_fruit)
  sl.text(fruit_sf_res)
