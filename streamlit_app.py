import streamlit
import pandas

streamlit.title('Hello World')

streamlit.header('🥣 Hello World')

streamlit.text('🥗 Hello World')

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
streamlit.dataframe(my_fruit_list)
