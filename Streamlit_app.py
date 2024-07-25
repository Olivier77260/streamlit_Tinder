import streamlit as st

create_page = st.Page("page1.py", title="Create entry 1")
delete_page = st.Page("page2.py", title="Delete entry")

pg = st.navigation([create_page, delete_page])
st.set_page_config(page_title="Data manager")
pg.run()
