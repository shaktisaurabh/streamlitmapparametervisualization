import numpy as np 
import plotly.express as px 
import streamlit as st 
import pandas as pd 
# st.set_page_config(layout='wide')
df=pd.read_csv(r"C:\Users\LENOVO\Downloads\plotlyproject.csv") 
# print(df.head()) 
st.set_page_config(layout='wide')
st.sidebar.title("India's data vizualization") 
am=list(df['State'].unique())
am.insert(0,'All states')
selected_state=st.sidebar.selectbox("Select a state",am)
primary=st.sidebar.selectbox("Select the first parameter",sorted(df.columns[5:]))
secondary=st.sidebar.selectbox("Select the second parameter",sorted(df.columns[5:])) 
plot=st.sidebar.button('Plot graph') 
if plot:
    if selected_state=='All states':
        st.text('Size represent primary parameter')
        st.text('Color represents secondary parameter')
        fig=px.scatter_mapbox(df,lat='Latitude',lon='Longitude',size=primary,zoom=4,size_max=35,color=secondary,
                          mapbox_style="carto-positron",width=1200,height=700,hover_name='District') 
        st.plotly_chart(fig) 
    else:
        st.text('Size represent primary parameter')
        st.text('Color represents secondary parameter')
        state_df=df[df['State']==selected_state]
        fig=px.scatter_mapbox(state_df,lat='Latitude',lon='Longitude',size=primary,zoom=6,size_max=36,color=secondary,
                              mapbox_style="carto-positron",width=1200,height=700,hover_name='District') 
        st.plotly_chart(fig)