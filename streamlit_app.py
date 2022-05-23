import streamlit
import pandas

# Unicode ref: https://unicode.org/emoji/charts/emoji-list.html#1f4aa

streamlit.title("My parents new insect grub")
streamlit.header("grub grub menu")
streamlit.text("\N{beetle} Omega 3 beetle muffin")
streamlit.text("\N{cricket}  Skinny cricket fries")
streamlit.text("\N{cockroach}  Cockroach crisps")

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list.set_index('Fruit')
streamlit.multiselect("Pick something from the list", list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)
