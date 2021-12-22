import streamlit as st

# Custom imports 
from multipage import MultiPage
from pages import base_page# import your pages here

# Create an instance of the app 
app = MultiPage()

apptitle = 'Dashboard Base'
st.set_page_config(page_title=apptitle, page_icon="🦈", layout='wide')

# Add all your applications (pages) here
app.add_page("Page 1", base_page.app)
app.add_page("Page 2", base_page.app)

# The main app
app.run()