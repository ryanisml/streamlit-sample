import datetime
import streamlit as st
from st_pages import add_page_title
import pandas as pd
from _mylibs import *
import sqlalchemy as sal
from sqlalchemy import text

add_page_title(layout="wide")

st.write("SQL Data")

connection_string = st.secrets["db_connection_string"]
connection_url = sal.create_engine(connection_string)
conn = connection_url.connect()

def generateChart(series, start_date, end_date):
    query_chart1 = text("SELECT category, SUM(" + series + ") as "+series+" FROM products where created_at >= '" + start_date.strftime("%Y-%m-%d") + "' and created_at <= '" + end_date.strftime("%Y-%m-%d") + "' GROUP BY category")
    data_chart1 = pd.read_sql_query(query_chart1, conn)
    if(data_chart1.empty == False):
        chart1 = pd.DataFrame(data_chart1)
        st.write("Bar Chart by Category")
        st.bar_chart(data=chart1, use_container_width=True, x='category', y=series, color="#8ecae6")

@st.cache_data(ttl=300)
def filterData(category, series, start_date, end_date):
    # Add your filtering logic here
    query = "SELECT * FROM products where created_at >= '" + start_date.strftime("%Y-%m-%d") + "' and created_at <= '" + end_date.strftime("%Y-%m-%d") + "'"
    if(category != 'ALL'):
        query += " and category = '" + category + "'"
    data = pd.read_sql_query(text(query), conn)
    if(data.empty == False):
        st.dataframe(data, use_container_width=True)
        st.markdown("<center><h5>SUM DATA " + series + " FROM " + start_date.strftime("%Y-%m-%d") + " TO " + end_date.strftime("%Y-%m-%d") + "</h5></center>", unsafe_allow_html=True)
        generateChart(series, start_date, end_date)
    else:
        st.error("Data not found")
    pass

@st.cache_data(ttl=300)
def runQuery(query):
    sqlText = text(query)
    data = pd.read_sql_query(sqlText, conn)
    return data

category = runQuery("SELECT DISTINCT category FROM products")
new_category = loopFetchData(category['category'])
series = ["STOCK", "PRICE"]
with st.expander("Filter Data", expanded=True):
    value_category = st.selectbox("Category", new_category)
    value_series = st.selectbox("Series", series)
    timeday = datetime.datetime.now()
    temp_prev_month = timeday.month - 1
    # next_year = today.year + 1
    first_day = datetime.date(timeday.year, 1, 1)

    today = datetime.date(timeday.year, timeday.month, timeday.day)
    previouse_month = datetime.date(timeday.year, temp_prev_month, timeday.day)
    d = st.date_input(
        "Select date range",
        (previouse_month, today),
        first_day,
        today,
        format="YYYY/MM/DD",
    )

    if(st.button('Filter Data')):
        if((d[1]-d[0]).days > 31):
            st.error("Date range cannot more than 1 month")
        else:
            filterData(value_category, value_series, d[0], d[1])