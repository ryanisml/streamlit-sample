import streamlit as st
from st_pages import Page, add_page_title, show_pages
import extra_streamlit_components as stx

def get_manager():
    return stx.CookieManager()

cookie_manager = get_manager()
cookie_manager.get_all()
user_logged_in = cookie_manager.get(cookie="user_logged_in")

add_page_title(layout="wide")

if user_logged_in is not None:
    st.write("Hello, " + user_logged_in["id"] + " - " + user_logged_in["name"] + "!")
    st.write("Your position is " + user_logged_in["position"] + "!")
    st.warning("Do you really, wanna logout from this apps?")