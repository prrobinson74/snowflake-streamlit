import streamlit
import pandas
import requests
import snowflake.connector

# Unicode ref: https://unicode.org/emoji/charts/emoji-list.html#1f4aa

streamlit.title("My parents new insect grub")
streamlit.header("grub grub favourites")
streamlit.text("\N{beetle} Omega 3 beetle muffin")
streamlit.text("\N{cricket}  Skinny cricket fries")
streamlit.text("\N{cockroach}  Cockroach crisps")

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected = streamlit.multiselect("Pick something:", list(my_fruit_list.index),
                                            ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

fruit_choice = streamlit.text_input("What fruit would you like information about?", "kiwi")
streamlit.write("The user entered", fruit_choice)

fr_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
fr_normalised = pandas.json_normalize(fr_response.json())
streamlit.dataframe(fr_normalised)

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)
