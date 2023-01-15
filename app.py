import streamlit as st
import pandas as pd
import plotly.express as px

st.title('India Census Data')
df = pd.read_csv('df.csv')
list_of_state = list(sorted((df['State']).unique()))
list_of_state.insert(0, 'Overall India')
st.sidebar.subheader('State')
selected_state = st.sidebar.selectbox('Select State', list_of_state)
st.sidebar.subheader('Primary Parameter')
primary = st.sidebar.selectbox('Select Primary Field', df.columns[5:])
st.sidebar.subheader('Secondary Parameter')
secondary = st.sidebar.selectbox('Select Secondary Field', df.columns[5:])
btn = st.sidebar.button('Plot Graph')
st.text('size represents primary parameter')
st.text('color represents secondary parameter')

if btn:
    if selected_state == 'Overall India':
        fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude",
                                zoom=4,size=primary,color=secondary,size_max=10,width=600,height=700,
                                mapbox_style="carto-positron",hover_name='District')
        st.plotly_chart(fig,use_container_width=True)

    else:
        df_state = df[df['State'] == selected_state]
        fig = px.scatter_mapbox(df_state, lat="Latitude", lon="Longitude",
                                zoom=5, size=primary, color=secondary, size_max=10, width=600, height=700,
                                mapbox_style="carto-positron", hover_name='District')
        st.plotly_chart(fig, use_container_width=True)



