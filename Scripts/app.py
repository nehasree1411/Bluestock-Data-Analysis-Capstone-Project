import streamlit as st
import pandas as pd
import plotly.express as px

nav=pd.read_csv(r"D:\BlueStock_Project\Data\Processed\02_nav_history_cleaned.csv")

st.title('Mutual Fund Dashboard')

fig=px.line(nav,x='date',y='nav',title='NAV Trend')
st.plotly_chart(fig)

st.metric('Latest NAV',round(nav['nav'].iloc[-1],2))