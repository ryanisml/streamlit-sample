import time
import streamlit as st
from st_pages import Page, Section, hide_pages, add_page_title, show_pages
import extra_streamlit_components as stx

# st.title("Login Page :door:")
# add_page_title(layout="wide")

@st.cache_resource(hash_funcs={"_thread.RLock": lambda _: None}, experimental_allow_widgets=True)
def get_manager():
    return stx.CookieManager()

st.set_page_config(page_title="Login Page", layout="wide", page_icon=":door:", menu_items=None)

st.title("Login Page :door:")
st.divider()
cookie_manager = get_manager()
cookie_manager.get_all()

st.toast('You can refresh all page using R', icon='📢')
time.sleep(.10)

def checkResponse(username, password):
    if username == "admin" or password == "admin":
        cookie_manager.set("user_logged_in", {"id":"19693", "name": "Ryan Ismail", "roles": "admin", "position": "Specialist Application Systems"})
        return True
    else:
        st.error("Username or password is invalid.")
        return False
    pass
        
def checkPassword():
    def validateData(username, password):
        if username == "" or password == "":
            st.error("Please fill username and password first.")
            return False
        checkResponse(username, password)
    if cookie_manager.get(cookie="user_logged_in") != None:
        return True
    username = st.text_input("Username")
    password = st.text_input("Password", type="password", key="password")
    st.button("Login", on_click=validateData, args=(username, password))
    return False

if not checkPassword():
    # show_pages([Page("main.py", "Login Page", ":door:")])
    # hide_pages(["Dashboard", "Loader", "Hauler", "Log Data", "Location", "Logout"])
    # st.markdown("""<style>[data-testid="stSidebar"] {display: none} [data-testid="collapsedControl"] { display: none }</style>""", unsafe_allow_html=True)
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