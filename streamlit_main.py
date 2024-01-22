import time
import streamlit as st
from st_pages import Page, Section, hide_pages, show_pages
import extra_streamlit_components as stx
import requests
import json

# st.title("Login Page :door:")
# add_page_title(layout="wide")

@st.cache_resource(hash_funcs={"_thread.RLock": lambda _: None}, experimental_allow_widgets=True)
def get_manager():
    return stx.CookieManager()

st.set_page_config(page_title="Login Page", page_icon="images/logo.png", layout="wide", menu_items=None)

st.title("Login Page - STREAMLIT :door:")
st.divider()
cookie_manager = get_manager()
cookie_manager.get_all()

st.toast('You can refresh all page using R', icon='📢')
time.sleep(.10)

def checkResponse(email, password):
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    data = '{"email": "'+email+'", "password": "'+password+'"}'
    try:
        response = requests.post(st.secrets.auth_url, headers=headers, json=json.loads(data))
        if 'token' in response.json():
            cookie_manager.set("user_logged_in", response.json())
            return True
        else:
            st.error(response.json()["message"])
            return False
        return False
    except requests.exceptions.RequestException as e:
        st.exception(e)
        return False
    pass
        
def checkPassword():
    def validateData(email, password):
        if email == "" or password == "":
            st.error("Please fill email and password first.")
            return False
        checkResponse(email, password)
    if cookie_manager.get(cookie="user_logged_in") != None:
        return True
    email = st.text_input("email")
    password = st.text_input("Password", type="password", key="password")
    st.button("Login", on_click=validateData, args=(email, password))
    return False

if not checkPassword():
    st.stop()

if cookie_manager.get(cookie="user_logged_in") != None:
    st.markdown("""<style>[data-testid="stSidebar"] {display: block} [data-testid="collapsedControl"] { display: block }</style>""", unsafe_allow_html=True)
    show_pages(
        [
            Page("menu/dashboard.py", "Dashboard", "💼"),
            Section(name="Menu 1", icon=":apple:"),
            Page("menu/get-data-api.py", "Get Data API", "🦏"),
            Page("menu/get-data-db.py", "Get Data DB", "🐙"),
            Page("menu/locations.py", "Location", "📌", in_section=False),
            Page("menu/logout.py", "Logout", ":no_entry_sign:", in_section=False)
        ]
    )
    hide_pages(["Login Page"])
    st.rerun()
else:
    checkPassword()